#!/usr/bin/env python3
"""
Test Twilio SMS delivery
"""
import os
import sys
from pathlib import Path
from twilio.rest import Client

# Load environment variables
from dotenv import load_dotenv
env_path = Path(__file__).parent / 'alioop-microservice-prototype' / '.env'
load_dotenv(env_path)

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_FROM_NUMBER = os.getenv('TWILIO_FROM_NUMBER')

# Validate configuration
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER]):
    print("❌ Error: Twilio configuration not found in .env file")
    print(f"   Looking for: {env_path}")
    print(f"   TWILIO_ACCOUNT_SID: {'✓' if TWILIO_ACCOUNT_SID else '✗'}")
    print(f"   TWILIO_AUTH_TOKEN: {'✓' if TWILIO_AUTH_TOKEN else '✗'}")
    print(f"   TWILIO_FROM_NUMBER: {'✓' if TWILIO_FROM_NUMBER else '✗'}")
    sys.exit(1)

def test_sms(to_number):
    """Send a test SMS"""
    
    message_body = """🎵 Alioop Audio Delivery

Your audio file is ready for download!

📦 File: test-audio-mix.wav
⏱️ Expires: 7 days

This is a test message from your Alioop audio delivery system.

✅ SMS notifications working!
🎨 New brand colors applied
🚀 System ready for production

- Alioop Audio Delivery"""
    
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_FROM_NUMBER,
            to=to_number
        )
        
        print(f"✅ SMS sent successfully!")
        print(f"   Message SID: {message.sid}")
        print(f"   Status: {message.status}")
        print(f"   From: {TWILIO_FROM_NUMBER}")
        print(f"   To: {to_number}")
        print(f"\n📱 Check your phone at {to_number}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending SMS: {str(e)}")
        if "valid" in str(e).lower() and "number" in str(e).lower():
            print(f"\n💡 Tip: Phone number must include country code (e.g., +1234567890)")
        return False

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        recipient = sys.argv[1]
    else:
        print("❌ Error: Please provide a phone number")
        print(f"\nUsage: python {sys.argv[0]} +1234567890")
        print(f"Example: python {sys.argv[0]} +19785551234")
        sys.exit(1)
    
    # Validate phone number format
    if not recipient.startswith('+'):
        print(f"⚠️  Warning: Phone number should start with + and country code")
        print(f"   Got: {recipient}")
        print(f"   Expected format: +1234567890")
        confirm = input("\nContinue anyway? (y/n): ")
        if confirm.lower() != 'y':
            sys.exit(0)
    
    print(f"\n🚀 Sending test SMS...")
    print(f"   Using Account: {TWILIO_ACCOUNT_SID[:20]}...")
    print(f"   From: {TWILIO_FROM_NUMBER}")
    print(f"   To: {recipient}\n")
    
    test_sms(recipient)
