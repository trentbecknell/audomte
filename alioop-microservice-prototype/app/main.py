from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .db import init_db, get_conn
from .schemas import ClientCreate, ProjectCreate, MessageSend
from .adapters.messaging import MessagingAdapter
from .adapters.payments import resolve_payment_link
from .adapters.phone_masking import PhoneMaskingAdapter
from .utils import format_phone_number

app = FastAPI(title="Alioop Comms + Preferences Microservice")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
messaging = MessagingAdapter()
phone_masking = PhoneMaskingAdapter()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
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

