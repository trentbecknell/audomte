#!/usr/bin/env python3
"""
SendGrid Email Setup and Test Script
Quick interactive setup for email testing
"""

import os
import sys

def main():
    print("=" * 60)
    print("📧 SendGrid Email Setup")
    print("=" * 60)
    print()
    print("To send real emails, you'll need:")
    print("  1. A SendGrid account (free tier available)")
    print("  2. API Key")
    print("  3. Verified sender email")
    print()
    
    has_account = input("Do you have a SendGrid account? (y/n): ").lower()
    
    if has_account != 'y':
        print()
        print("📝 Getting Started:")
        print("  1. Go to: https://signup.sendgrid.com/")
        print("  2. Sign up (100 emails/day free)")
        print("  3. Verify your email address")
        print("  4. Come back and run this script again")
        return
    
    print()
    print("=" * 60)
    print("Step 1: Get Your API Key")
    print("=" * 60)
    print()
    print("  1. Go to: https://app.sendgrid.com/settings/api_keys")
    print("  2. Click 'Create API Key'")
    print("  3. Name it (e.g., 'Alioop Local Dev')")
    print("  4. Choose 'Full Access' or 'Restricted' with Mail Send permission")
    print("  5. Copy the API key (you'll only see it once!)")
    print()
    
    api_key = input("Paste your SendGrid API Key: ").strip()
    
    if not api_key.startswith("SG."):
        print("⚠️  Warning: API key should start with 'SG.'")
        confirm = input("Continue anyway? (y/n): ").lower()
        if confirm != 'y':
            return
    
    print()
    print("=" * 60)
    print("Step 2: Verify Sender Email")
    print("=" * 60)
    print()
    print("  SendGrid requires a verified sender email address.")
    print()
    print("  1. Go to: https://app.sendgrid.com/settings/sender_auth/senders")
    print("  2. Click 'Create New Sender'")
    print("  3. Fill in your info")
    print("  4. Verify the email they send you")
    print()
    
    from_email = input("Enter your verified sender email: ").strip()
    
    print()
    print("=" * 60)
    print("Step 3: Test Email")
    print("=" * 60)
    print()
    
    test_email = input("Enter an email to send a test to: ").strip()
    
    print()
    print("📧 Sending test email...")
    
    # Test the SendGrid connection
    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        
        message = Mail(
            from_email=from_email,
            to_emails=test_email,
            subject='Test Email from Alioop',
            html_content='<strong>Success!</strong><br>Your SendGrid integration is working perfectly! 🎉'
        )
        
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        
        print(f"✅ Email sent successfully!")
        print(f"   Status: {response.status_code}")
        print(f"   Check {test_email} for the test message")
        
        # Update .env file
        print()
        save = input("Save these settings to .env file? (y/n): ").lower()
        
        if save == 'y':
            env_path = "/workspaces/audomte/alioop-microservice-prototype/.env"
            
            # Read existing .env
            with open(env_path, 'r') as f:
                lines = f.readlines()
            
            # Update SendGrid lines
            with open(env_path, 'w') as f:
                in_sendgrid_section = False
                updated = False
                
                for line in lines:
                    if '# SendGrid Configuration' in line:
                        in_sendgrid_section = True
                        f.write(line)
                        continue
                    
                    if in_sendgrid_section and line.strip() == '':
                        # End of SendGrid section - write our values
                        f.write(f"SENDGRID_API_KEY={api_key}\n")
                        f.write(f"SENDGRID_FROM_EMAIL={from_email}\n")
                        f.write("\n")
                        in_sendgrid_section = False
                        updated = True
                        continue
                    
                    # Skip commented SendGrid lines
                    if in_sendgrid_section and (
                        'SENDGRID_API_KEY' in line or 
                        'SENDGRID_FROM_EMAIL' in line
                    ):
                        continue
                    
                    f.write(line)
            
            print("✅ Settings saved to .env")
            print()
            print("🚀 Next steps:")
            print("   1. Restart your server: ./start.sh")
            print("   2. Open http://localhost:8000")
            print("   3. Create a client with an email")
            print("   4. Send them a message!")
        
    except ImportError:
        print("❌ SendGrid library not installed")
        print("   Run: pip install sendgrid")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("Troubleshooting:")
        print("  • Check your API key is correct")
        print("  • Verify sender email is confirmed in SendGrid")
        print("  • Check your internet connection")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled")
    except Exception as e:
        print(f"\n❌ Error: {e}")
