#!/usr/bin/env python3
"""
Quick start script for the Audio Delivery Portal
Launches the web server and opens the browser
"""

import os
import sys
import time
import webbrowser
import subprocess
from pathlib import Path

def main():
    # Change to the correct directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print("=" * 60)
    print("🎵 AUDIO DELIVERY PORTAL - STARTING")
    print("=" * 60)
    print()
    
    # Check if we're in the right place
    if not Path("app/main.py").exists():
        print("❌ Error: app/main.py not found")
        print("   Please run this script from the alioop-microservice-prototype directory")
        sys.exit(1)
    
    # Initialize database
    print("1. Initializing database...")
    try:
        from app.db import init_db
        init_db()
        print("   ✅ Database ready\n")
    except Exception as e:
        print(f"   ❌ Database error: {e}\n")
        sys.exit(1)
    
    # Start the web server
    print("2. Starting web server...")
    print("   URL: http://localhost:8000")
    print("   Dashboard: http://localhost:8000/dashboard")
    print()
    
    # Open browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open("http://localhost:8000")
        print("   ✅ Browser opened\n")
    
    import threading
    threading.Thread(target=open_browser, daemon=True).start()
    
    print("=" * 60)
    print("🎯 READY TO USE!")
    print("=" * 60)
    print()
    print("📱 Public Landing Page: http://localhost:8000")
    print("   - Drag-and-drop file upload")
    print("   - Client/service selection")
    print("   - Automatic notifications")
    print()
    print("🔐 Engineer Dashboard: http://localhost:8000/dashboard")
    print("   - Manage clients")
    print("   - View deliveries")
    print("   - Verify payments")
    print()
    print("⌨️  Press Ctrl+C to stop the server")
    print()
    
    # Start uvicorn
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn",
            "app.main:app",
            "--reload",
            "--port", "8000",
            "--host", "0.0.0.0"
        ])
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping server...")
        print("✅ Server stopped. Goodbye!")

if __name__ == "__main__":
    main()
