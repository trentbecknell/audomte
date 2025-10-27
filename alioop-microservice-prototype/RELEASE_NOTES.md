# Release Notes

## Version 1.0.0 - October 27, 2025

### 🎉 Initial Release: Alioop Comms + Preferences Microservice

A FastAPI-based microservice prototype for managing client communications, delivery preferences, and payment methods with built-in privacy protection.

---

## ✨ Features

### 📱 Real SMS & Email Integration
- **Twilio SMS**: Send real text messages to clients with automatic phone number formatting
- **SendGrid Email**: Professional email delivery system
- **DRYRUN Mode**: Test without sending real messages (logs to console)
- **Environment Variables**: Secure credential management with `.env` support

### 🔒 Phone Masking Service
- **Privacy Protection**: Generate masked/proxy phone numbers for client communications
- **Database Integration**: Track masked numbers with full audit trail
- **Automatic Routing**: Messages automatically use masked numbers when enabled
- **API Endpoints**: Full REST API for managing masked phone numbers

### 📞 Automatic Phone Number Formatting
- **E.164 Format**: Automatically converts any phone format to international standard
- **Client-Side Validation**: JavaScript formatting for immediate user feedback
- **Server-Side Processing**: Double-layer validation ensures data integrity
- **Flexible Input**: Accepts formats like:
  - `978-338-7220`
  - `(978) 338-7220`
  - `9783387220`
  - `+19783387220`
  - `1-978-338-7220`

### 👥 Client Management
- Store client contact information (name, email, phone)
- Track delivery preferences (Google Drive, Dropbox, WeTransfer, Custom)
- Manage payment preferences (Stripe, PayPal, Zelle, Custom)
- Optional phone masking for privacy

### 📋 Project Management
- Create projects linked to clients
- Track project status (active/completed)
- Add notes and details
- Automatic client notification on completion

### 💬 Communication System
- Send messages via email or SMS
- Choose communication channel per message
- Automatic preference detection
- Message clients directly from UI

---

## 🛠️ Technical Stack

- **Framework**: FastAPI 0.115.2
- **Server**: Uvicorn 0.30.6
- **Database**: SQLite with full schema support
- **Templates**: Jinja2 with Pico CSS
- **Validation**: Pydantic 2.9.2
- **Integrations**: 
  - Twilio 9.3.7 (SMS)
  - SendGrid 6.11.0 (Email)
  - python-dotenv 1.2.1 (Config)

---

## 📁 Project Structure

```
alioop-microservice-prototype/
├── app/
│   ├── main.py              # FastAPI application & endpoints
│   ├── db.py                # SQLite database schema
│   ├── schemas.py           # Pydantic models
│   ├── utils.py             # Phone formatting utilities
│   └── adapters/
│       ├── messaging.py     # Twilio & SendGrid integration
│       ├── payments.py      # Payment link resolver
│       └── phone_masking.py # Phone masking service
├── static/
│   └── app.js              # Client-side JavaScript
├── templates/
│   └── index.html          # Main UI template
├── requirements.txt        # Python dependencies
├── .gitignore             # Git exclusions (protects .env)
└── Documentation files...
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd alioop-microservice-prototype
pip install -r requirements.txt
```

### 2. Configure Services (Optional)
Create a `.env` file:
```bash
# Twilio SMS (optional)
TWILIO_ACCOUNT_SID=your_sid_here
TWILIO_AUTH_TOKEN=your_token_here
TWILIO_FROM_NUMBER=+15551234567

# SendGrid Email (optional)
SENDGRID_API_KEY=your_key_here
SENDGRID_FROM_EMAIL=you@example.com

# Phone Masking (optional)
PHONE_MASKING_ENABLED=true
PHONE_MASKING_PROVIDER=twilio
```

### 3. Start Server
```bash
uvicorn app.main:app --reload
# or
./start.sh
```

### 4. Open Browser
Navigate to: http://localhost:8000

---

## 📚 Documentation

- **PHONE_MASKING.md** - Complete guide to phone masking service
- **REAL_MESSAGING_SETUP.md** - Step-by-step Twilio & SendGrid setup
- **VERIFY_NUMBERS.md** - Guide for verifying phone numbers (trial accounts)
- **FIX_A2P_ERROR.md** - Solutions for A2P 10DLC registration issues

---

## 🔧 Helper Scripts

- **check_config.py** - Verify email/SMS configuration
- **validate_phone.py** - Test phone number formatting
- **setup_twilio.py** - Interactive Twilio setup assistant
- **test_phone_masking.py** - Test phone masking API endpoints

---

## 🐛 Bug Fixes

- Fixed project creation form (client dropdown validation)
- Fixed client messaging button functionality
- Corrected phone number validation to prevent Twilio errors
- Database schema updates for phone masking support
- UI improvements for better user experience

---

## 🔐 Security

- **No Hardcoded Credentials**: All sensitive data in `.env` (excluded from git)
- **Input Validation**: Pydantic schemas validate all inputs
- **Phone Masking**: Privacy protection for client phone numbers
- **E.164 Format**: Prevents phone number format errors

---

## 📝 API Endpoints

### Client Management
- `POST /clients` - Create new client
- `GET /clients/{id}/masked-phone` - Get masked phone for client
- `POST /clients/{id}/masked-phone` - Create masked phone
- `DELETE /clients/{id}/masked-phone` - Remove masked phone

### Project Management
- `POST /projects` - Create new project
- `POST /projects/{id}/complete` - Mark complete & notify client

### Messaging
- `POST /send` - Send email or SMS to client

### UI
- `GET /` - Main web interface

---

## ⚠️ Known Limitations

### Twilio Trial Accounts
- Can only send to verified phone numbers
- Messages include "Sent from your Twilio trial account"
- Limited free credits

### A2P 10DLC (US SMS)
- Regular 10-digit numbers require A2P registration
- **Solution**: Use toll-free numbers (no registration needed)
- See `FIX_A2P_ERROR.md` for details

### Phone Masking
- Currently simulates masked numbers (+1-555-MASK-XXXX)
- Production requires integration with Twilio Proxy, Bandwidth, or Plivo

---

## 🔮 Future Enhancements

- [ ] Real Twilio Proxy integration for phone masking
- [ ] Webhook handlers for delivery tracking
- [ ] Rate limiting for message sending
- [ ] Message history and logs
- [ ] Client portal for self-service
- [ ] Multi-language support
- [ ] Advanced analytics and reporting

---

## 🤝 Contributing

This is a prototype/demonstration project. For production use:
1. Replace simulated phone masking with real provider integration
2. Add authentication/authorization
3. Implement proper error handling and logging
4. Add rate limiting and abuse prevention
5. Use production database (PostgreSQL, MySQL, etc.)
6. Add comprehensive testing suite

---

## 📄 License

This project is a prototype for demonstration purposes.

---

## 🙏 Acknowledgments

- **FastAPI** - Modern Python web framework
- **Twilio** - SMS/Phone capabilities
- **SendGrid** - Email delivery
- **Pico CSS** - Beautiful minimalist CSS framework

---

## 📞 Support

For issues or questions:
- Check documentation files in the project
- Review Twilio console for SMS logs
- Use helper scripts for troubleshooting
- Validate phone numbers with `validate_phone.py`

---

**Built with ❤️ for the Alioop platform**
