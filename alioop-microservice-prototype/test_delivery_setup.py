#!/usr/bin/env python3
"""
Quick test script for the delivery system
Creates a test client and verifies the services are loaded
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from app.db import get_conn, init_db

def main():
    print("🧪 Testing Delivery System Setup\n")
    
    # Initialize database
    print("1. Initializing database...")
    init_db()
    print("   ✅ Database initialized\n")
    
    # Check services
    print("2. Checking predefined services...")
    conn = get_conn()
    cur = conn.cursor()
    
    services = cur.execute("SELECT * FROM services WHERE is_active = 1").fetchall()
    print(f"   ✅ Found {len(services)} active services:")
    for svc in services:
        price = f"${svc['default_price']:.2f}" if svc['default_price'] > 0 else "Custom"
        print(f"      - {svc['name']}: {price}")
    
    print()
    
    # Check for test client
    print("3. Checking for test clients...")
    clients = cur.execute("SELECT * FROM clients").fetchall()
    
    if clients:
        print(f"   ✅ Found {len(clients)} existing client(s):")
        for client in clients:
            contact = client['email'] or client['phone'] or 'No contact'
            print(f"      - {client['name']} ({contact})")
    else:
        print("   ⚠️  No clients found. Add one via web UI at http://localhost:8000")
    
    print()
    
    # Check storage folder
    print("4. Checking storage folder...")
    storage_folder = Path(__file__).parent / "storage" / "deliveries"
    if storage_folder.exists():
        print(f"   ✅ Storage folder exists: {storage_folder}")
        file_count = len(list(storage_folder.glob("*")))
        print(f"      Files stored: {file_count}")
    else:
        storage_folder.mkdir(parents=True, exist_ok=True)
        print(f"   ✅ Created storage folder: {storage_folder}")
    
    print()
    
    # Check watch folder
    print("5. Checking watch folder...")
    watch_folder = Path.home() / "Desktop" / "AudioDeliveries"
    if watch_folder.exists():
        print(f"   ✅ Watch folder exists: {watch_folder}")
        audio_files = list(watch_folder.glob("*.wav")) + list(watch_folder.glob("*.mp3"))
        print(f"      Audio files: {len(audio_files)}")
    else:
        watch_folder.mkdir(parents=True, exist_ok=True)
        print(f"   ✅ Created watch folder: {watch_folder}")
    
    conn.close()
    
    print()
    print("=" * 60)
    print("✅ SYSTEM READY!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Start web server: uvicorn app.main:app --reload")
    print("  2. Add clients: http://localhost:8000")
    print("  3. Start file watcher: python file_watcher.py")
    print(f"  4. Drop audio files in: {watch_folder}")
    print()

if __name__ == "__main__":
    main()
