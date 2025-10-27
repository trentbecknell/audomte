# Alioop "Comms + Preferences" Microservice (Local Prototype)

Minimal web app to test a microservice that abstracts CRM + payments into simple communications,
preferences, and notifications.

## Features

- **Client Management**: Track client contact info and preferences
- **Project Tracking**: Manage projects and their status
- **Communication**: Send emails and SMS to clients
- **Delivery Preferences**: Support multiple delivery methods (Drive, Dropbox, WeTransfer, Custom)
- **Payment Integration**: Support multiple payment methods (Stripe, PayPal, Zelle, Custom)
- **🔒 Phone Masking**: Privacy protection with masked phone numbers (NEW!)

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://127.0.0.1:8000
```

Or use the convenience script:
```bash
./start_server.sh
```

## Phone Masking Service

The app now includes a phone number masking service to protect privacy when using SMS communications. When enabled, clients receive a masked/proxy phone number instead of exposing their real phone number.

**Benefits:**
- Protect client phone number privacy
- Easy to change backend numbers without affecting clients
- Compliance with privacy regulations (GDPR, CCPA)
- Audit trail for all communications

**Usage:**
1. When creating a client, check "Use Phone Masking"
2. A masked number is automatically generated (e.g., `+1-555-MASK-1234`)
3. All SMS messages automatically route through the masked number

See [PHONE_MASKING.md](./PHONE_MASKING.md) for detailed documentation.

**API Endpoints:**
- `GET /clients/{id}/masked-phone` - Get masked phone for a client
- `POST /clients/{id}/masked-phone` - Create masked phone for existing client
- `DELETE /clients/{id}/masked-phone` - Release masked phone

**Test the Feature:**
```bash
python test_phone_masking.py
```

## Architecture

```
app/
├── main.py              # FastAPI app and endpoints
├── db.py                # SQLite database setup
├── schemas.py           # Pydantic models
└── adapters/
    ├── messaging.py     # Email/SMS service adapter
    ├── payments.py      # Payment link resolver
    └── phone_masking.py # Phone masking service (NEW!)
```

## Production Integration

For production use, integrate with real services:
- **Phone Masking**: Twilio Proxy, Bandwidth, or Plivo
- **Messaging**: SendGrid (email), Twilio (SMS)
- **Payments**: Stripe, PayPal, Zelle APIs

### 📧 🚀 Enable Real Email & SMS

The app is ready to send real emails and text messages! By default, it runs in DRYRUN mode (logs to console).

**Quick Setup:**
1. Get free accounts:
   - SendGrid: https://signup.sendgrid.com/ (100 emails/day free)
   - Twilio: https://www.twilio.com/try-twilio (free trial)

2. Set environment variables:
```bash
export SENDGRID_API_KEY="your_key_here"
export SENDGRID_FROM_EMAIL="you@example.com"
export TWILIO_ACCOUNT_SID="your_sid_here"
export TWILIO_AUTH_TOKEN="your_token_here"
export TWILIO_FROM_NUMBER="+15551234567"
```

3. Check configuration:
```bash
python check_config.py
```

**See [REAL_MESSAGING_SETUP.md](./REAL_MESSAGING_SETUP.md) for detailed instructions.**
