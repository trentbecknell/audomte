#!/usr/bin/env python3
"""
Quick SendGrid Email Test
Tests sending an email with your configured API key
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_test_email():
    api_key = os.getenv("SENDGRID_API_KEY")
    from_email = os.getenv("SENDGRID_FROM_EMAIL")
    
    if not api_key or api_key == "REPLACE_WITH_NEW_KEY":
        print("❌ No API key configured!")
        print()
        print("To fix:")
        print("  1. Get a NEW API key from: https://app.sendgrid.com/settings/api_keys")
        print("  2. Click 'Create API Key'")
        print("  3. Name it 'Alioop-Test'")
        print("  4. Select 'Restricted Access'")
        print("  5. Enable 'Mail Send' → Full Access")
        print("  6. Copy the key")
        print()
        print("  7. Edit .env file and replace REPLACE_WITH_NEW_KEY with your actual key")
        return
    
    print("=" * 60)
    print("📧 SendGrid Email Test")
    print("=" * 60)
    print()
    print(f"From Email: {from_email}")
    print(f"API Key: {api_key[:10]}...{api_key[-10:]}")
    print()
    
    to_email = input("Enter email to send test to: ").strip()
    
    if not to_email:
        print("❌ No recipient email provided")
        return
    
    print()
    print("📧 Sending test email...")
    
    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject='✅ Alioop Email Test Successful!',
            html_content='''
            <div style="font-family: Arial, sans-serif; padding: 20px;">
                <h2 style="color: #4CAF50;">🎉 Success!</h2>
                <p>Your SendGrid email integration is working perfectly!</p>
                <p>You can now send emails from your Alioop app.</p>
                <hr>
                <p style="color: #666; font-size: 12px;">
                    Sent from Alioop Comms + Preferences Microservice
                </p>
            </div>
            '''
        )
        
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        
        print()
        print("=" * 60)
        print("✅ EMAIL SENT SUCCESSFULLY!")
        print("=" * 60)
        print(f"Status Code: {response.status_code}")
        print(f"To: {to_email}")
        print()
        print("✅ Check your inbox!")
        print("✅ Your SendGrid is now fully configured")
        print()
        
    except ImportError:
        print("❌ SendGrid library not installed")
        print("   Run: pip install sendgrid")
        
    except Exception as e:
        print()
        print("=" * 60)
        print("❌ EMAIL FAILED")
        print("=" * 60)
        print(f"Error: {e}")
        print()
        
        if "401" in str(e) or "Unauthorized" in str(e):
            print("🔑 API Key Issue:")
            print("   Your API key is invalid, expired, or revoked")
            print()
            print("   Create a NEW key:")
            print("   1. Go to: https://app.sendgrid.com/settings/api_keys")
            print("   2. DELETE the old key if it exists")
            print("   3. Create a BRAND NEW key")
            print("   4. Make sure 'Mail Send' is enabled")
            print("   5. Copy the ENTIRE key")
            print("   6. Update .env file")
            print()
            
        elif "403" in str(e) or "Forbidden" in str(e):
            print("📧 Sender Email Issue:")
            print("   Your sender email is not verified")
            print()
            print("   Verify it:")
            print("   1. Go to: https://app.sendgrid.com/settings/sender_auth/senders")
            print("   2. Add and verify your sender email")
            print()

if __name__ == "__main__":
    try:
        send_test_email()
    except KeyboardInterrupt:
        print("\n\n⚠️  Test cancelled")
