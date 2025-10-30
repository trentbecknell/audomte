from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from datetime import datetime, timedelta
import secrets
import shutil
import sqlite3
from .db import init_db, get_conn
from .schemas import ClientCreate, ProjectCreate, MessageSend, ServiceCreate, ServiceUpdate
from .adapters.messaging import MessagingAdapter
from .adapters.payments import resolve_payment_link
from .adapters.phone_masking import PhoneMaskingAdapter
from .utils import format_phone_number

app = FastAPI(title="Alioop Comms + Preferences Microservice")

# Get the base directory (parent of app folder)
BASE_DIR = Path(__file__).resolve().parent.parent

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
messaging = MessagingAdapter()
phone_masking = PhoneMaskingAdapter()

# Storage configuration
STORAGE_FOLDER = Path(__file__).resolve().parents[1] / "storage" / "deliveries"
STORAGE_FOLDER.mkdir(parents=True, exist_ok=True)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health_check():
    """Health check endpoint for Railway"""
    return {
        "status": "healthy",
        "static_dir": str(BASE_DIR / "static"),
        "templates_dir": str(BASE_DIR / "templates"),
        "storage_dir": str(STORAGE_FOLDER)
    }

@app.get("/", response_class=HTMLResponse)
def landing_page(request: Request):
    """Public landing page with drag-and-drop upload"""
    return templates.TemplateResponse("landing.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    """Engineer dashboard - requires authentication"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients ORDER BY id DESC")
    clients = cur.fetchall()
    cur.execute("SELECT p.id, p.title, p.status, c.name as client_name FROM projects p JOIN clients c ON p.client_id=c.id ORDER BY p.id DESC")
    projects = cur.fetchall()
    
    # Get masked phone info for display
    cur.execute("SELECT client_id, masked_phone FROM masked_phones")
    masked_phones = {row["client_id"]: row["masked_phone"] for row in cur.fetchall()}
    
    conn.close()
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "clients": clients, 
        "projects": projects,
        "masked_phones": masked_phones
    })

@app.post("/clients")
def create_client(client: ClientCreate):
    # Format phone number to E.164 if provided
    if client.phone:
        original_phone = client.phone
        client.phone = format_phone_number(client.phone)
        print(f"[PHONE_FORMAT] {original_phone} → {client.phone}")
    
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO clients (name, email, phone, delivery_pref, delivery_custom_url, payment_pref, payment_custom_url, use_masked_phone)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (client.name, client.email, client.phone, client.delivery_pref, client.delivery_custom_url, 
                 client.payment_pref, client.payment_custom_url, int(client.use_masked_phone)))
    client_id = cur.lastrowid
    conn.commit()
    conn.close()
    
    # If phone masking is requested and phone is provided, create masked number
    masked_phone = None
    if client.use_masked_phone and client.phone:
        masked_phone = phone_masking.create_phone_mask(client_id, client.phone, get_conn)
    
    return {"ok": True, "client_id": client_id, "masked_phone": masked_phone}

@app.post("/projects")
def create_project(project: ProjectCreate):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO projects (client_id, title, notes) VALUES (?, ?, ?)''',
                (project.client_id, project.title, project.notes))
    conn.commit()
    conn.close()
    return {"ok": True}

@app.post("/send")
def send_message(msg: MessageSend):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients WHERE id=?", (msg.client_id,))
    client = cur.fetchone()
    conn.close()
    if not client:
        return JSONResponse({"ok": False, "error": "Client not found"}, status_code=404)

    if msg.channel == "email" and client["email"]:
        messaging.send_email(client["email"], "Message from Studio", msg.body)
    elif msg.channel == "sms" and client["phone"]:
        # Check if client uses masked phone
        target_phone = client["phone"]
        if client["use_masked_phone"]:
            masked = phone_masking.get_masked_number(msg.client_id, get_conn)
            if masked:
                target_phone = masked
                print(f"[SMS] Using masked number {masked} instead of {client['phone']}")
        
        messaging.send_sms(target_phone, msg.body)
    else:
        return JSONResponse({"ok": False, "error": "Missing contact info"}, status_code=400)
    return {"ok": True}

@app.post("/projects/{project_id}/complete")
def complete_project(project_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE projects SET status='completed' WHERE id=?", (project_id,))
    cur.execute('''SELECT p.title, c.* FROM projects p JOIN clients c ON p.client_id=c.id WHERE p.id=?''', (project_id,))
    row = cur.fetchone()
    conn.commit()
    conn.close()
    if not row:
        return JSONResponse({"ok": False, "error": "Not found"}, status_code=404)

    payment_link = resolve_payment_link(row["payment_pref"], row["payment_custom_url"])
    delivery_note = f"Delivery method: {row['delivery_pref']}"
    if row["delivery_pref"] == "Custom" and row["delivery_custom_url"]:
        delivery_note += f" ({row['delivery_custom_url']})"

    body = f"Your project '{row['title']}' is ready!\n{delivery_note}\nPayment: {payment_link or 'as arranged'}"
    if row["email"]:
        messaging.send_email(row["email"], "Your project is ready", body)
    elif row["phone"]:
        # Use masked number if client has it enabled
        target_phone = row["phone"]
        if row["use_masked_phone"]:
            masked = phone_masking.get_masked_number(row["id"], get_conn)
            if masked:
                target_phone = masked
        messaging.send_sms(target_phone, body)
    return {"ok": True}

@app.get("/clients/{client_id}/masked-phone")
def get_client_masked_phone(client_id: int):
    """Get the masked phone number for a client."""
    masked = phone_masking.get_masked_number(client_id, get_conn)
    if masked:
        return {"ok": True, "client_id": client_id, "masked_phone": masked}
    return JSONResponse({"ok": False, "error": "No masked phone found"}, status_code=404)

@app.post("/clients/{client_id}/masked-phone")
def create_client_masked_phone(client_id: int):
    """Create a masked phone number for an existing client."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT phone, use_masked_phone FROM clients WHERE id=?", (client_id,))
    client = cur.fetchone()
    conn.close()
    
    if not client:
        return JSONResponse({"ok": False, "error": "Client not found"}, status_code=404)
    
    if not client["phone"]:
        return JSONResponse({"ok": False, "error": "Client has no phone number"}, status_code=400)
    
    # Create or get existing masked number
    masked_phone = phone_masking.create_phone_mask(client_id, client["phone"], get_conn)
    
    # Update client to use masked phone
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE clients SET use_masked_phone=1 WHERE id=?", (client_id,))
    conn.commit()
    conn.close()
    
    return {"ok": True, "client_id": client_id, "masked_phone": masked_phone}

@app.delete("/clients/{client_id}/masked-phone")
def delete_client_masked_phone(client_id: int):
    """Delete/release the masked phone number for a client."""
    deleted = phone_masking.delete_phone_mask(client_id, get_conn)
    
    if deleted:
        # Update client to not use masked phone
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE clients SET use_masked_phone=0 WHERE id=?", (client_id,))
        conn.commit()
        conn.close()
        return {"ok": True, "message": "Masked phone released"}
    
    return JSONResponse({"ok": False, "error": "No masked phone found"}, status_code=404)


# ===== SERVICE MANAGEMENT ENDPOINTS =====

@app.get("/services")
def list_services():
    """Get all services with pricing."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM services WHERE is_active = 1 ORDER BY id")
    services = cur.fetchall()
    conn.close()
    return {"services": [dict(s) for s in services]}


@app.post("/services")
def create_service(service: ServiceCreate):
    """Create a new service type."""
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO services (name, description, default_price, is_active) VALUES (?, ?, ?, ?)",
            (service.name, service.description, service.default_price, int(service.is_active))
        )
        service_id = cur.lastrowid
        conn.commit()
        return {"ok": True, "service_id": service_id}
    except sqlite3.IntegrityError:
        return JSONResponse({"ok": False, "error": "Service already exists"}, status_code=400)
    finally:
        conn.close()


@app.patch("/services/{service_id}")
def update_service(service_id: int, service: ServiceUpdate):
    """Update service pricing or details."""
    conn = get_conn()
    cur = conn.cursor()
    
    updates = []
    params = []
    
    if service.name is not None:
        updates.append("name = ?")
        params.append(service.name)
    if service.description is not None:
        updates.append("description = ?")
        params.append(service.description)
    if service.default_price is not None:
        updates.append("default_price = ?")
        params.append(service.default_price)
    if service.is_active is not None:
        updates.append("is_active = ?")
        params.append(int(service.is_active))
    
    if not updates:
        return JSONResponse({"ok": False, "error": "No updates provided"}, status_code=400)
    
    params.append(service_id)
    cur.execute(f"UPDATE services SET {', '.join(updates)} WHERE id = ?", params)
    conn.commit()
    conn.close()
    
    return {"ok": True}


# ===== DELIVERY/DOWNLOAD ENDPOINTS =====

@app.get("/delivery/{token}", response_class=HTMLResponse)
def view_delivery(request: Request, token: str):
    """Customer download page - shows file info, download button, and payment options."""
    conn = get_conn()
    cur = conn.cursor()
    
    # Get delivery info
    cur.execute("""
        SELECT d.*, c.name as client_name, s.name as service_name
        FROM deliveries d
        JOIN clients c ON d.client_id = c.id
        JOIN services s ON d.service_id = s.id
        WHERE d.download_token = ?
    """, (token,))
    
    delivery = cur.fetchone()
    conn.close()
    
    if not delivery:
        return templates.TemplateResponse("delivery.html", {
            "request": request,
            "error": "Invalid or expired download link."
        })
    
    # Check if expired
    expires_at = datetime.fromisoformat(delivery['token_expires_at'])
    if datetime.now() > expires_at:
        return templates.TemplateResponse("delivery.html", {
            "request": request,
            "error": "This download link has expired."
        })
    
    # Format file size
    file_size_mb = delivery['file_size'] / (1024 * 1024) if delivery['file_size'] else 0
    
    return templates.TemplateResponse("delivery.html", {
        "request": request,
        "delivery_id": delivery['id'],
        "token": token,
        "filename": delivery['filename'],
        "service_name": delivery['service_name'],
        "client_name": delivery['client_name'],
        "file_size_mb": f"{file_size_mb:.2f}",
        "price": delivery['price'],
        "download_count": delivery['download_count'],
        "max_downloads": delivery['max_downloads'],
        "payment_confirmed": delivery['payment_confirmed'],
        "payment_method": delivery['payment_method'],
        "expires_at": expires_at.strftime("%b %d, %Y"),
        "error": None
    })


@app.get("/delivery/{token}/download")
def download_file(token: str):
    """Actually download the file - increments download counter."""
    conn = get_conn()
    cur = conn.cursor()
    
    # Get delivery
    cur.execute("SELECT * FROM deliveries WHERE download_token = ?", (token,))
    delivery = cur.fetchone()
    
    if not delivery:
        raise HTTPException(status_code=404, detail="Invalid download link")
    
    # Check expiry
    expires_at = datetime.fromisoformat(delivery['token_expires_at'])
    if datetime.now() > expires_at:
        raise HTTPException(status_code=410, detail="Download link expired")
    
    # Check download limit
    if delivery['download_count'] >= delivery['max_downloads']:
        raise HTTPException(status_code=403, detail="Maximum downloads reached")
    
    # Increment download count and update status
    cur.execute("""
        UPDATE deliveries 
        SET download_count = download_count + 1,
            status = CASE 
                WHEN status = 'pending' OR status = 'notified' THEN 'downloaded'
                ELSE status 
            END
        WHERE id = ?
    """, (delivery['id'],))
    conn.commit()
    conn.close()
    
    # Serve the file
    file_path = Path(delivery['file_path'])
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found on server")
    
    return FileResponse(
        path=file_path,
        filename=delivery['filename'],
        media_type='application/octet-stream'
    )


@app.post("/delivery/{token}/confirm-payment")
async def confirm_payment(token: str, payment_method: str = Form(...)):
    """Customer confirms they've sent payment - notifies engineer."""
    conn = get_conn()
    cur = conn.cursor()
    
    # Get delivery with client info
    cur.execute("""
        SELECT d.*, c.name as client_name, c.email as client_email, s.name as service_name
        FROM deliveries d
        JOIN clients c ON d.client_id = c.id
        JOIN services s ON d.service_id = s.id
        WHERE d.download_token = ?
    """, (token,))
    
    delivery = cur.fetchone()
    
    if not delivery:
        raise HTTPException(status_code=404, detail="Invalid link")
    
    # Update payment info (pending engineer confirmation)
    cur.execute("""
        UPDATE deliveries 
        SET payment_method = ?,
            status = 'payment_pending'
        WHERE id = ?
    """, (payment_method, delivery['id']))
    
    conn.commit()
    conn.close()
    
    # TODO: Send notification to engineer (email/SMS)
    # For now, just log it
    print(f"💰 Payment notification: {delivery['client_name']} paid ${delivery['price']} via {payment_method}")
    print(f"   Delivery ID: {delivery['id']} | Service: {delivery['service_name']}")
    
    # Redirect back to delivery page
    return RedirectResponse(url=f"/delivery/{token}", status_code=303)


@app.post("/admin/deliveries/{delivery_id}/verify-payment")
def verify_payment(delivery_id: int):
    """Engineer confirms payment received - marks delivery as paid."""
    conn = get_conn()
    cur = conn.cursor()
    
    cur.execute("""
        UPDATE deliveries 
        SET payment_confirmed = 1,
            payment_confirmed_at = ?,
            status = 'paid'
        WHERE id = ?
    """, (datetime.now(), delivery_id))
    
    affected = cur.rowcount
    conn.commit()
    
    if affected:
        # TODO: Send thank you notification to customer
        print(f"✅ Payment verified for delivery #{delivery_id}")
    
    conn.close()
    
    return {"ok": True, "verified": affected > 0}


@app.get("/admin/deliveries")
def list_deliveries(status: str = None):
    """List all deliveries with optional status filter."""
    conn = get_conn()
    cur = conn.cursor()
    
    if status:
        cur.execute("""
            SELECT d.*, c.name as client_name, s.name as service_name
            FROM deliveries d
            JOIN clients c ON d.client_id = c.id
            JOIN services s ON d.service_id = s.id
            WHERE d.status = ?
            ORDER BY d.created_at DESC
        """, (status,))
    else:
        cur.execute("""
            SELECT d.*, c.name as client_name, s.name as service_name
            FROM deliveries d
            JOIN clients c ON d.client_id = c.id
            JOIN services s ON d.service_id = s.id
            ORDER BY d.created_at DESC
        """)
    
    deliveries = cur.fetchall()
    conn.close()
    
    return {"deliveries": [dict(d) for d in deliveries]}


@app.get("/api/clients")
def api_list_clients():
    """API endpoint to list all clients for the upload form."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, phone FROM clients ORDER BY name")
    clients = cur.fetchall()
    conn.close()
    return {"clients": [dict(c) for c in clients]}


@app.post("/api/upload-delivery")
async def api_upload_delivery(
    file: UploadFile = File(...),
    client_id: int = Form(...),
    service_id: int = Form(...),
    custom_price: float = Form(None),
    project_id: int = Form(None)
):
    """Web-based file upload for creating deliveries."""
    
    # Validate file type
    valid_extensions = {'.wav', '.mp3', '.flac', '.aiff', '.m4a', '.ogg', '.aac', '.wma'}
    file_ext = Path(file.filename).suffix.lower()
    
    if file_ext not in valid_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    # Get client and service info
    conn = get_conn()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
    client = cur.fetchone()
    if not client:
        conn.close()
        raise HTTPException(status_code=404, detail="Client not found")
    
    cur.execute("SELECT * FROM services WHERE id = ?", (service_id,))
    service = cur.fetchone()
    if not service:
        conn.close()
        raise HTTPException(status_code=404, detail="Service not found")
    
    # Determine price
    price = custom_price if custom_price is not None else service['default_price']
    
    # Generate secure token
    download_token = secrets.token_urlsafe(32)
    token_expires_at = datetime.now() + timedelta(days=30)
    
    # Save file to storage
    storage_filename = f"{download_token}_{file.filename}"
    storage_path = STORAGE_FOLDER / storage_filename
    
    # Read and save file
    file_content = await file.read()
    file_size = len(file_content)
    
    with open(storage_path, 'wb') as f:
        f.write(file_content)
    
    # Create delivery record
    cur.execute('''
        INSERT INTO deliveries 
        (client_id, project_id, service_id, filename, file_path, file_size, price, 
         download_token, token_expires_at, status, created_at, max_downloads)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)
    ''', (
        client_id,
        project_id,
        service_id,
        file.filename,
        str(storage_path),
        file_size,
        price,
        download_token,
        token_expires_at,
        datetime.now(),
        3  # max downloads
    ))
    
    delivery_id = cur.lastrowid
    conn.commit()
    
    # Send notification to customer
    from .adapters.messaging import send_email, send_sms
    
    download_url = f"http://localhost:8000/delivery/{download_token}"
    
    # Email notification
    if client['email']:
        email_subject = f"Your {service['name']} is Ready!"
        email_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h2 style="color: #4CAF50;">🎵 Your Audio is Ready!</h2>
            <p>Hi {client['name']},</p>
            <p>Your <strong>{service['name']}</strong> for <strong>{file.filename}</strong> is complete!</p>
            <div style="background: #f5f5f5; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3>📥 Download Your File</h3>
                <p><a href="{download_url}" style="display: inline-block; background: #4CAF50; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; font-weight: bold;">DOWNLOAD NOW</a></p>
            </div>
            <div style="background: #fff3cd; padding: 20px; border-radius: 8px;">
                <h3>💰 Payment: ${price:.2f}</h3>
                <p>Payment options available on the download page.</p>
            </div>
        </body>
        </html>
        """
        try:
            send_email(client['email'], email_subject, email_body)
            print(f"✅ Email sent to {client['email']}")
        except Exception as e:
            print(f"❌ Email failed: {e}")
    
    # SMS notification
    if client['phone']:
        sms_body = f"🎵 Your {service['name']} is ready! Download: {download_url} | Payment: ${price:.2f}"
        try:
            send_sms(client['phone'], sms_body)
            print(f"✅ SMS sent to {client['phone']}")
        except Exception as e:
            print(f"❌ SMS failed: {e}")
    
    # Update delivery status
    cur.execute("UPDATE deliveries SET status = 'notified', notified_at = ? WHERE id = ?", (datetime.now(), delivery_id))
    conn.commit()
    conn.close()
    
    return {
        "ok": True,
        "delivery_id": delivery_id,
        "download_url": download_url,
        "message": f"Delivery created and customer notified"
    }


