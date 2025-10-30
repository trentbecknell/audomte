#!/usr/bin/env python3
"""
File Watcher Service - Monitors a folder for new audio files
When a file is detected, prompts engineer for customer/service info
Then uploads and notifies customer automatically
"""

import os
import sys
import time
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import secrets
import shutil

# Add app directory to path
sys.path.insert(0, str(Path(__file__).parent))
from app.db import get_conn, init_db
from app.adapters.messaging import send_email, send_sms

# Configuration
WATCH_FOLDER = Path.home() / "Desktop" / "AudioDeliveries"  # Default watch folder
STORAGE_FOLDER = Path(__file__).parent / "storage" / "deliveries"
AUDIO_EXTENSIONS = {'.wav', '.mp3', '.flac', '.aiff', '.m4a', '.ogg', '.aac', '.wma'}
TOKEN_EXPIRY_DAYS = 30
MAX_DOWNLOADS = 3

# Ensure folders exist
WATCH_FOLDER.mkdir(parents=True, exist_ok=True)
STORAGE_FOLDER.mkdir(parents=True, exist_ok=True)


class AudioFileHandler(FileSystemEventHandler):
    """Handles new audio file events"""
    
    def __init__(self):
        self.processing = set()  # Track files being processed
        
    def on_created(self, event):
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        
        # Check if it's an audio file
        if file_path.suffix.lower() not in AUDIO_EXTENSIONS:
            return
            
        # Avoid duplicate processing
        if str(file_path) in self.processing:
            return
            
        print(f"\n🎵 New audio file detected: {file_path.name}")
        self.processing.add(str(file_path))
        
        # Wait a bit to ensure file is fully written
        time.sleep(2)
        
        try:
            self.process_file(file_path)
        finally:
            self.processing.discard(str(file_path))
    
    def process_file(self, file_path: Path):
        """Process the detected audio file"""
        
        # Get clients and services from database
        conn = get_conn()
        cur = conn.cursor()
        
        # Get all active clients
        clients = cur.execute("SELECT id, name, email, phone FROM clients ORDER BY name").fetchall()
        if not clients:
            print("❌ No clients found. Please add clients first via the web UI.")
            return
        
        # Get all active services
        services = cur.execute(
            "SELECT id, name, default_price FROM services WHERE is_active = 1 ORDER BY id"
        ).fetchall()
        
        # Display client options
        print("\n👤 SELECT CLIENT:")
        for idx, client in enumerate(clients, 1):
            contact = client['email'] or client['phone'] or 'No contact'
            print(f"  {idx}. {client['name']} ({contact})")
        
        # Get client selection
        while True:
            try:
                choice = input("\nEnter client number: ").strip()
                client_idx = int(choice) - 1
                if 0 <= client_idx < len(clients):
                    selected_client = clients[client_idx]
                    break
                print("Invalid selection. Try again.")
            except (ValueError, KeyboardInterrupt):
                print("\n❌ Cancelled")
                return
        
        # Display service options
        print(f"\n🎛️  SELECT SERVICE for {selected_client['name']}:")
        for idx, service in enumerate(services, 1):
            price_display = f"${service['default_price']:.2f}" if service['default_price'] > 0 else "Custom"
            print(f"  {idx}. {service['name']} - {price_display}")
        
        # Get service selection
        while True:
            try:
                choice = input("\nEnter service number: ").strip()
                service_idx = int(choice) - 1
                if 0 <= service_idx < len(services):
                    selected_service = services[service_idx]
                    break
                print("Invalid selection. Try again.")
            except (ValueError, KeyboardInterrupt):
                print("\n❌ Cancelled")
                return
        
        # Get price (allow custom override)
        price = selected_service['default_price']
        if selected_service['name'] == 'Custom' or price == 0:
            while True:
                try:
                    custom_price = input(f"\nEnter price for this delivery: $").strip()
                    price = float(custom_price)
                    if price >= 0:
                        break
                    print("Price must be positive.")
                except ValueError:
                    print("Invalid price. Try again.")
                except KeyboardInterrupt:
                    print("\n❌ Cancelled")
                    return
        else:
            # Allow override
            override = input(f"\nPrice is ${price:.2f}. Press Enter to confirm or enter custom price: $").strip()
            if override:
                try:
                    price = float(override)
                except ValueError:
                    print("Invalid price, using default.")
        
        # Create delivery record
        print(f"\n📦 Processing delivery...")
        
        # Generate secure download token
        download_token = secrets.token_urlsafe(32)
        token_expires_at = datetime.now() + timedelta(days=TOKEN_EXPIRY_DAYS)
        
        # Copy file to storage with unique name
        file_size = file_path.stat().st_size
        storage_filename = f"{download_token}_{file_path.name}"
        storage_path = STORAGE_FOLDER / storage_filename
        shutil.copy2(file_path, storage_path)
        
        # Insert delivery record
        cur.execute('''
            INSERT INTO deliveries 
            (client_id, service_id, filename, file_path, file_size, price, 
             download_token, token_expires_at, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)
        ''', (
            selected_client['id'],
            selected_service['id'],
            file_path.name,
            str(storage_path),
            file_size,
            price,
            download_token,
            token_expires_at,
            datetime.now()
        ))
        
        delivery_id = cur.lastrowid
        conn.commit()
        
        # Send notification to customer
        print(f"📧 Notifying customer...")
        success = send_customer_notification(
            selected_client, 
            selected_service, 
            file_path.name,
            price, 
            download_token,
            delivery_id
        )
        
        if success:
            # Update delivery status
            cur.execute(
                "UPDATE deliveries SET status = 'notified', notified_at = ? WHERE id = ?",
                (datetime.now(), delivery_id)
            )
            conn.commit()
            print(f"✅ Customer notified successfully!")
            print(f"   Download link: http://localhost:8000/delivery/{download_token}")
        else:
            print(f"⚠️  Delivery saved but notification failed. You can resend from the web UI.")
        
        conn.close()
        
        # Optionally move processed file to archive
        archive_folder = WATCH_FOLDER / "_processed"
        archive_folder.mkdir(exist_ok=True)
        archive_path = archive_folder / file_path.name
        
        # Handle duplicate names
        counter = 1
        while archive_path.exists():
            archive_path = archive_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
            counter += 1
        
        shutil.move(str(file_path), str(archive_path))
        print(f"📁 Original file moved to: {archive_path}")
        

def send_customer_notification(client, service, filename, price, token, delivery_id):
    """Send email/SMS notification to customer with download link and payment info"""
    
    # Build download URL (update with your actual domain in production)
    download_url = f"http://localhost:8000/delivery/{token}"
    
    # Email content
    email_subject = f"Your {service['name']} is Ready!"
    email_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <h2 style="color: #4CAF50;">🎵 Your Audio is Ready!</h2>
        
        <p>Hi {client['name']},</p>
        
        <p>Your <strong>{service['name']}</strong> for <strong>{filename}</strong> is complete and ready for download!</p>
        
        <div style="background: #f5f5f5; padding: 20px; border-radius: 8px; margin: 20px 0;">
            <h3 style="margin-top: 0;">📥 Download Your File</h3>
            <p><a href="{download_url}" style="display: inline-block; background: #4CAF50; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; font-weight: bold;">DOWNLOAD NOW</a></p>
            <p style="font-size: 12px; color: #666;">Link expires in 30 days | Max 3 downloads</p>
        </div>
        
        <div style="background: #fff3cd; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #ffc107;">
            <h3 style="margin-top: 0;">💰 Payment: ${price:.2f}</h3>
            <p>Please send payment via your preferred method:</p>
            <ul style="list-style: none; padding: 0;">
                <li>💵 <strong>Zelle:</strong> [Your Zelle Email/Phone]</li>
                <li>💳 <strong>PayPal:</strong> [Your PayPal Handle]</li>
                <li>📱 <strong>Cash App:</strong> $[Your Cash App]</li>
                <li>💚 <strong>Venmo:</strong> @[Your Venmo]</li>
            </ul>
            <p style="font-size: 12px; color: #666;">After payment, click "I Paid" on the download page.</p>
        </div>
        
        <p>Thanks for your business!</p>
        
        <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
        <p style="font-size: 12px; color: #999;">Delivery ID: #{delivery_id}</p>
    </body>
    </html>
    """
    
    # SMS content (shorter version)
    sms_body = f"""🎵 Your {service['name']} is ready!

Download: {download_url}

Payment (${price:.2f}):
Zelle/PayPal/CashApp/Venmo
[Payment info on download page]

Thanks!"""
    
    # Send via preferred channel or both
    success = False
    
    if client['email']:
        try:
            send_email(client['email'], email_subject, email_body)
            success = True
            print(f"   ✅ Email sent to {client['email']}")
        except Exception as e:
            print(f"   ❌ Email failed: {e}")
    
    if client['phone']:
        try:
            send_sms(client['phone'], sms_body)
            success = True
            print(f"   ✅ SMS sent to {client['phone']}")
        except Exception as e:
            print(f"   ❌ SMS failed: {e}")
    
    return success


def main():
    """Main entry point for file watcher"""
    
    # Initialize database
    init_db()
    
    print("=" * 60)
    print("🎵 AUDIO DELIVERY FILE WATCHER")
    print("=" * 60)
    print(f"\n📁 Watching folder: {WATCH_FOLDER}")
    print(f"📦 Storage folder: {STORAGE_FOLDER}")
    print(f"\n💡 Drop audio files into the watch folder to start delivery process")
    print(f"   Supported formats: {', '.join(sorted(AUDIO_EXTENSIONS))}")
    print(f"\n⌨️  Press Ctrl+C to stop\n")
    
    # Create event handler and observer
    event_handler = AudioFileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(WATCH_FOLDER), recursive=False)
    
    # Start watching
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping file watcher...")
        observer.stop()
    
    observer.join()
    print("✅ File watcher stopped")


if __name__ == "__main__":
    main()
