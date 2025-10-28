# Audomte

[![Latest Release](https://img.shields.io/github/v/release/trentbecknell/audomte?label=Latest%20Release&color=brightgreen)](https://github.com/trentbecknell/audomte/releases/latest)
[![GitHub Release Date](https://img.shields.io/github/release-date/trentbecknell/audomte)](https://github.com/trentbecknell/audomte/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **Communication microservice prototype with SMS & Email capabilities**

## 🎉 Latest Release: v1.1.0 - Email Integration Verified!

**What's New:**
- ✅ **SendGrid Email** - Fully tested and operational
- ✅ **Twilio SMS** - Production ready
- 🧪 **Testing Tools** - Easy setup and validation utilities
- 📧 **Multi-channel** - Both email and SMS working

👉 **[View Full Release Notes](https://github.com/trentbecknell/audomte/releases/tag/v1.1.0)**

---

## 📦 Projects

### Alioop Microservice Prototype

A FastAPI-based communication microservice featuring:

- 📱 **SMS Integration** - Twilio-powered text messaging
- 📧 **Email Integration** - SendGrid-powered email delivery
- 🔄 **Auto Phone Formatting** - E.164 standard conversion
- 🔒 **Phone Masking** - Privacy-focused number management
- 👥 **Client Management** - Full CRUD operations
- 📊 **Project Tracking** - Status monitoring and notifications

**[View Project Documentation →](./alioop-microservice-prototype/RELEASE_NOTES.md)**

---

## 🚀 Quick Start

```bash
# Navigate to project
cd alioop-microservice-prototype

# Configure email (interactive)
python setup_sendgrid.py

# Test email sending
python quick_email_test.py

# Start the server
uvicorn app.main:app --reload
```

Visit http://localhost:8000 to use the application.

---

## 📝 Release History

- **[v1.1.0](https://github.com/trentbecknell/audomte/releases/tag/v1.1.0)** (Oct 28, 2025) - Email integration verified with testing tools
- **[v1.0.0](https://github.com/trentbecknell/audomte/releases/tag/v1.0.0)** (Oct 27, 2025) - Initial release with SMS and phone masking

**[View All Releases →](https://github.com/trentbecknell/audomte/releases)**

---

## 🛠️ Tech Stack

- **Backend:** FastAPI 0.115.2, Python 3.x
- **Database:** SQLite
- **SMS:** Twilio API
- **Email:** SendGrid API
- **Server:** Uvicorn ASGI

---

## 📖 Documentation

- [Release Notes v1.1.0](./alioop-microservice-prototype/RELEASE_NOTES_v1.1.0.md)
- [Release Notes v1.0.0](./alioop-microservice-prototype/RELEASE_NOTES.md)
- [Changelog](./alioop-microservice-prototype/CHANGELOG.md)

---

## 🤝 Contributing

This is a prototype project. Feel free to fork and experiment!

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

---

**Built with ❤️ for streamlined communication workflows**