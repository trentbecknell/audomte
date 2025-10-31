"""
Simple standalone version - Run from terminal or MIDI controller
This version doesn't require Ableton's Control Surface framework
"""

import webbrowser
import urllib.parse
import sys


def send_to_alioop(client_name="", client_email="", price="50", service="Production"):
    """
    Open Alioop with pre-filled information
    
    Args:
        client_name: Name of the client
        client_email: Client's email address
        price: Delivery price in dollars
        service: Type of service (Mixing, Mastering, Production, etc.)
    """
    
    # Base URL
    base_url = "https://web-production-5748a.up.railway.app/"
    
    # Build parameters
    params = {}
    
    if client_name:
        params['client'] = client_name
    if client_email:
        params['email'] = client_email
    if price:
        params['price'] = price
    if service:
        params['service'] = service
    
    # Encode and build URL
    url_params = urllib.parse.urlencode(params)
    alioop_url = f"{base_url}?{url_params}"
    
    # Open in browser
    print(f"Opening Alioop for client: {client_name or 'Unknown'}")
    print(f"URL: {alioop_url}")
    webbrowser.open(alioop_url)
    
    return True


def interactive_mode():
    """Interactive CLI mode for sending deliveries"""
    
    print("=" * 50)
    print("   Alioop Send Delivery - Ableton Live")
    print("=" * 50)
    print()
    
    # Get client info
    client_name = input("Client Name: ").strip()
    if not client_name:
        print("Error: Client name is required!")
        sys.exit(1)
    
    client_email = input("Client Email: ").strip()
    if not client_email:
        print("Error: Email is required!")
        sys.exit(1)
    
    price = input("Delivery Price ($) [50]: ").strip() or "50"
    service = input("Service Name [Production]: ").strip() or "Production"
    
    print()
    print("Summary:")
    print(f"  Client: {client_name}")
    print(f"  Email: {client_email}")
    print(f"  Price: ${price}")
    print(f"  Service: {service}")
    print()
    
    confirm = input("Open Alioop? (y/n): ").strip().lower()
    
    if confirm == 'y':
        send_to_alioop(client_name, client_email, price, service)
        print()
        print("✓ Alioop opened! Upload your exported file and click Send.")
    else:
        print("Cancelled.")


if __name__ == "__main__":
    """
    Usage:
    
    Interactive mode:
        python alioop_standalone.py
    
    Command line:
        python alioop_standalone.py "John Smith" "john@example.com" "75" "Mixing"
    """
    
    if len(sys.argv) > 1:
        # Command line mode
        client_name = sys.argv[1] if len(sys.argv) > 1 else ""
        client_email = sys.argv[2] if len(sys.argv) > 2 else ""
        price = sys.argv[3] if len(sys.argv) > 3 else "50"
        service = sys.argv[4] if len(sys.argv) > 4 else "Production"
        
        send_to_alioop(client_name, client_email, price, service)
    else:
        # Interactive mode
        interactive_mode()
