#!/usr/bin/env python3
"""
Test SendGrid email delivery
"""
import os
import sys
from pathlib import Path
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load environment variables
from dotenv import load_dotenv
env_path = Path(__file__).parent / 'alioop-microservice-prototype' / '.env'
load_dotenv(env_path)

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDGRID_FROM_EMAIL = os.getenv('SENDGRID_FROM_EMAIL')

# Validate configuration
if not SENDGRID_API_KEY or not SENDGRID_FROM_EMAIL:
    print("❌ Error: SendGrid configuration not found in .env file")
    print(f"   Looking for: {env_path}")
    print(f"   SENDGRID_API_KEY: {'✓' if SENDGRID_API_KEY else '✗'}")
    print(f"   SENDGRID_FROM_EMAIL: {'✓' if SENDGRID_FROM_EMAIL else '✗'}")
    sys.exit(1)

def test_email(to_email):
    """Send a test email"""
    
    message = Mail(
        from_email=SENDGRID_FROM_EMAIL,
        to_emails=to_email,
        subject='🎵 Test Email - Alioop Audio Delivery',
        html_content=f'''
        <html>
        <head>
            <style>
                body {{ font-family: 'Space Grotesk', Arial, sans-serif; background: #fcf5eb; padding: 20px; }}
                .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 12px; padding: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
                .payment-character {{ text-align: center; margin-bottom: 20px; }}
                .payment-character img {{ max-width: 200px; height: auto; border-radius: 8px; }}
                .header {{ background: #161614; color: white; padding: 30px; border-radius: 8px; text-align: center; margin-bottom: 30px; }}
                .content {{ color: #333; line-height: 1.6; }}
                .button {{ display: inline-block; background: linear-gradient(135deg, #f05709 0%, #d94d08 100%); color: white; padding: 15px 30px; border-radius: 8px; text-decoration: none; font-weight: bold; margin: 20px 0; }}
                .footer {{ text-align: center; color: #71706e; font-size: 14px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e0e0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="payment-character">
                    <img src="https://raw.githubusercontent.com/trentbecknell/audomte/main/alioop-microservice-prototype/static/payment-character.png" alt="Payment Please!" />
                </div>
                <div class="header">
                    <h1 style="margin: 0;">🎵 Alioop Audio Delivery</h1>
                    <p style="margin: 10px 0 0 0; opacity: 0.9;">Professional Audio File Delivery</p>
                </div>
                
                <div class="content">
                    <h2 style="color: #f05709;">Email Test Successful! ✅</h2>
                    
                    <p>This is a test email from your Alioop audio delivery system.</p>
                    
                    <p><strong>Configuration verified:</strong></p>
                    <ul>
                        <li>✅ SendGrid API connected</li>
                        <li>✅ Email delivery working</li>
                        <li>✅ New brand colors applied</li>
                        <li>✅ Modern Space Grotesk font loaded</li>
                    </ul>
                    
                    <p>Your audio delivery system is ready to send download links to your customers!</p>
                    
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="https://github.com/trentbecknell/audomte" class="button">View on GitHub</a>
                    </div>
                </div>
                
                <div class="footer">
                    <p><strong>Alioop Audio Delivery</strong></p>
                    <p>Professional audio file delivery and payment system</p>
                    <p style="margin-top: 10px; font-size: 12px;">Sent via SendGrid</p>
                </div>
            </div>
        </body>
        </html>
        '''
    )
    
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        
        print(f"✅ Email sent successfully!")
        print(f"   Status Code: {response.status_code}")
        print(f"   To: {to_email}")
        print(f"   From: {SENDGRID_FROM_EMAIL}")
        print(f"\n📧 Check your inbox at {to_email}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        recipient = sys.argv[1]
    else:
        # Default to sender email for testing
        recipient = SENDGRID_FROM_EMAIL
        print(f"No recipient specified, sending test to: {recipient}")
    
    print(f"\n🚀 Sending test email...")
    print(f"   Using API Key: {SENDGRID_API_KEY[:20]}...")
    print(f"   From: {SENDGRID_FROM_EMAIL}")
    print(f"   To: {recipient}\n")
    
    test_email(recipient)
