import os

class MessagingAdapter:
    def __init__(self):
        self.sendgrid_key = os.getenv("SENDGRID_API_KEY")
        self.sendgrid_from = os.getenv("SENDGRID_FROM_EMAIL", "noreply@example.com")
        self.twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_from = os.getenv("TWILIO_FROM_NUMBER")

    def send_email(self, to_email: str, subject: str, body: str):
        if not self.sendgrid_key:
            print(f"[EMAIL:DRYRUN] to={to_email} subject={subject}\n{body}")
            return {"status": "logged"}
        
        try:
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            
            # Create HTML email with payment character and branding
            html_body = f'''
            <html>
            <head>
                <style>
                    body {{ font-family: 'Space Grotesk', Arial, sans-serif; background: #fcf5eb; padding: 20px; margin: 0; }}
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
                        <img src="https://raw.githubusercontent.com/trentbecknell/audomte/main/alioop-microservice-prototype/static/payment-character.png" alt="Payment Character" />
                    </div>
                    <div class="header">
                        <h1 style="margin: 0;">🎵 Alioop Audio Delivery</h1>
                        <p style="margin: 10px 0 0 0; opacity: 0.9;">Professional Audio File Delivery</p>
                    </div>
                    <div class="content">
                        {body.replace(chr(10), '<br>')}
                    </div>
                    <div class="footer">
                        <p><strong>Alioop Audio Delivery</strong></p>
                        <p>Professional audio file delivery and payment system</p>
                    </div>
                </div>
            </body>
            </html>
            '''
            
            message = Mail(
                from_email=self.sendgrid_from,
                to_emails=to_email,
                subject=subject,
                html_content=html_body
            )
            
            sg = SendGridAPIClient(self.sendgrid_key)
            response = sg.send(message)
            
            print(f"[EMAIL:SENDGRID] ✓ Sent to={to_email} subject={subject} status={response.status_code}")
            return {"status": "sent", "status_code": response.status_code}
        except ImportError:
            print(f"[EMAIL:ERROR] SendGrid library not installed. Run: pip install sendgrid")
            print(f"[EMAIL:DRYRUN] to={to_email} subject={subject}\n{body}")
            return {"status": "error", "error": "sendgrid not installed"}
        except Exception as e:
            print(f"[EMAIL:ERROR] Failed to send: {e}")
            return {"status": "error", "error": str(e)}

    def send_sms(self, to_phone: str, body: str):
        if not (self.twilio_sid and self.twilio_auth and self.twilio_from):
            print(f"[SMS:DRYRUN] to={to_phone}\n{body}")
            return {"status": "logged"}
        
        try:
            from twilio.rest import Client
            
            client = Client(self.twilio_sid, self.twilio_auth)
            message = client.messages.create(
                body=body,
                from_=self.twilio_from,
                to=to_phone
            )
            
            print(f"[SMS:TWILIO] ✓ Sent from={self.twilio_from} to={to_phone} sid={message.sid}")
            return {"status": "sent", "sid": message.sid}
        except ImportError:
            print(f"[SMS:ERROR] Twilio library not installed. Run: pip install twilio")
            print(f"[SMS:DRYRUN] to={to_phone}\n{body}")
            return {"status": "error", "error": "twilio not installed"}
        except Exception as e:
            print(f"[SMS:ERROR] Failed to send: {e}")
            return {"status": "error", "error": str(e)}
