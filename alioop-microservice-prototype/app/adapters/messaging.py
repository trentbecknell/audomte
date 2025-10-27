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
            
            message = Mail(
                from_email=self.sendgrid_from,
                to_emails=to_email,
                subject=subject,
                plain_text_content=body
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
