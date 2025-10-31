# Audomte

[![Latest Release](https://img.shields.io/github/v/release/trentbecknell/audomte?label=Latest%20Release&color=brightgreen)](https://github.com/trentbecknell/audomte/releases/latest)
[![GitHub Release Date](https://img.shields.io/github/release-date/trentbecknell/audomte)](https://github.com/trentbecknell/audomte/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **Communication microservice prototype with SMS & Email capabilities**

## 🎉 Latest: v2.0.0 - DAW Integration & Desktop App!

**What's New:**
- 🎹 **DAW Integration** - Call Alioop directly from Pro Tools, Logic, Ableton, Studio One
- 🖥️ **Desktop App** - Auto-detect bounces with watch folder (Phase 2)
- ⚡ **URL Handler** - Pre-fill forms via URL parameters (Phase 1)
- 📱 **PWA** - Install on any device (iOS, Android, Windows, Mac, Linux)
- 🎨 **Branded Emails** - Payment character image with orange/black/cream styling
- � **Streamlined Workflow** - Send files in 30 seconds (down from 2-3 minutes)

👉 **[Desktop App Documentation →](./alioop-desktop/README.md)**
👉 **[DAW Integration Guide →](./DAW_INTEGRATION.md)**

---

## 📦 Projects

### 🎹 Alioop Desktop App (NEW!)

**Auto-detect DAW bounces and send files instantly!**

A cross-platform Electron app that watches for new audio files and prompts instant delivery:

- 📁 **Watch Folder** - Monitors bounce directory for new files
- 🔔 **Desktop Notifications** - Instant alerts when files appear
- 🎯 **Smart Parsing** - Auto-extracts client name from filename
- 💾 **System Tray** - Runs in background, minimal footprint
- ⚙️ **Configurable** - Custom watch folder, default price, API URL

**[Quick Start Guide →](./alioop-desktop/QUICKSTART.md)**
**[Full Documentation →](./alioop-desktop/README.md)**

---

### Alioop Microservice Prototype

A FastAPI-based audio delivery and payment micro-SaaS featuring:

- 📱 **SMS Integration** - Twilio-powered text messaging
- 📧 **Email Integration** - SendGrid with branded HTML templates
- 🎨 **Payment Character** - Branded emails with custom imagery
- 💰 **Payment Requests** - Instant client billing with file delivery
- 🔄 **Auto Client Creation** - No pre-setup required
- 🔒 **Phone Masking** - Privacy-focused number management
- 👥 **Client Management** - Full CRUD operations
- 📊 **Project Tracking** - Status monitoring and notifications
- 🎹 **DAW Integration** - URL handlers, desktop app, export scripts
- 📱 **PWA** - Installable on any platform

**Live Demo:** [https://web-production-5748a.up.railway.app/](https://web-production-5748a.up.railway.app/)

**[View Project Documentation →](./alioop-microservice-prototype/RELEASE_NOTES.md)**

---

## 🚀 Quick Start

### Web App (PWA)

```bash
# Navigate to project
cd alioop-microservice-prototype

# Start the server
uvicorn app.main:app --reload
```

Visit http://localhost:8000 to use the application.

### Desktop App

```bash
# Navigate to desktop app
cd alioop-desktop

# Install dependencies
npm install

# Run in development
npm start

# Build installers
npm run build
```

**[Desktop Quick Start Guide →](./alioop-desktop/QUICKSTART.md)**

### DAW Integration

Set up keyboard shortcuts in your DAW to call Alioop with one keystroke!

**[DAW Integration Guide →](./DAW_INTEGRATION.md)**

---

## 📝 Release History

- **v2.0.0** (Oct 31, 2025) - DAW Integration Phase 1 & 2, Desktop App, PWA
- **[v1.1.0](https://github.com/trentbecknell/audomte/releases/tag/v1.1.0)** (Oct 28, 2025) - Email integration verified with testing tools
- **[v1.0.0](https://github.com/trentbecknell/audomte/releases/tag/v1.0.0)** (Oct 27, 2025) - Initial release with SMS and phone masking

**[View All Releases →](https://github.com/trentbecknell/audomte/releases)**

---

## 🛠️ Tech Stack

**Backend:**
- FastAPI 0.115.2, Python 3.x
- SQLite Database
- Twilio API (SMS)
- SendGrid API (Email)
- Uvicorn ASGI Server

**Frontend:**
- Progressive Web App (PWA)
- Service Worker (offline support)
- Responsive design
- Orange/Black/Cream branding

**Desktop:**
- Electron 28
- Chokidar (file watching)
- Axios (API calls)
- Electron Store (settings)
- Electron Builder (installers)

**Deployment:**
- Railway (production)
- GitHub Actions (CI/CD ready)

---

## 📖 Documentation

- [Desktop App Quick Start](./alioop-desktop/QUICKSTART.md)
- [Desktop App Full Documentation](./alioop-desktop/README.md)
- [DAW Integration Guide](./DAW_INTEGRATION.md)
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