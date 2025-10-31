# Audomte

[![Latest Release](https://img.shields.io/github/v/release/trentbecknell/audomte?label=Latest%20Release&color=brightgreen)](https://github.com/trentbecknell/audomte/releases/latest)
[![GitHub Release Date](https://img.shields.io/github/release-date/trentbecknell/audomte)](https://github.com/trentbecknell/audomte/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **Communication microservice prototype with SMS & Email capabilities**

## 🎉 Latest: v3.0.0 - VST/AU Plugin & One-Click Installers!

**What's New:**
- 🔌 **VST/AU Plugin** - Full in-DAW integration, zero file export! (Phase 4)
- 📦 **One-Click Installers** - Mac (.pkg) & Windows (.exe) for non-technical users
- 🎹 **DAW Integration** - Call Alioop directly from Pro Tools, Logic, Ableton, Studio One
- 🖥️ **Desktop App** - Auto-detect bounces with watch folder (Phase 2)
- ⚡ **URL Handler** - Pre-fill forms via URL parameters (Phase 1)
- 📱 **PWA** - Install on any device (iOS, Android, Windows, Mac, Linux)
- 🎨 **Branded Emails** - Payment character image with orange/black/cream styling
- 💎 **Streamlined Workflow** - Send files in 10 seconds with plugin!

👉 **[Download Plugin (Mac/Windows) →](./alioop-plugin/download.html)** 🆕  
👉 **[Desktop App Documentation →](./alioop-desktop/README.md)**  
👉 **[DAW Integration Guide →](./DAW_INTEGRATION.md)**

---

## 📦 Projects

### 🔌 Alioop Plugin (NEW!)

**The ultimate DAW integration - never leave your session!**

A professional VST3/AU/AAX plugin for in-DAW audio delivery:

- 🎙️ **In-DAW Recording** - Capture audio directly from your session
- 📝 **Built-in Form** - Client info right in the plugin window
- 🚀 **Auto-Upload** - Exports WAV and sends automatically
- 💾 **Session Persistence** - Remembers last client info
- 📦 **One-Click Install** - Mac (.pkg) & Windows (.exe) installers
- 🎨 **Branded UI** - Orange/black/cream Alioop styling

**[📥 Download Now (Mac/Windows) →](./alioop-plugin/download.html)**  
**[Full Documentation →](./alioop-plugin/README.md)**  
**[Build from Source →](./alioop-plugin/docs/BUILD_GUIDE.md)**

**⏱️ Workflow: ~3 minutes** (no file export needed!)

---

### 🎹 Alioop Desktop App

**Auto-detect DAW bounces and send files instantly!**

A cross-platform Electron app that watches for new audio files and prompts instant delivery:

- 📁 **Watch Folder** - Monitors bounce directory for new files
- 🔔 **Desktop Notifications** - Instant alerts when files appear
- 🎯 **Smart Parsing** - Auto-extracts client name from filename
- 💾 **System Tray** - Runs in background, minimal footprint
- ⚙️ **Configurable** - Custom watch folder, default price, API URL

**[Quick Start Guide →](./alioop-desktop/QUICKSTART.md)**  
**[Full Documentation →](./alioop-desktop/README.md)**

**⏱️ Workflow: ~15 seconds**

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
- 🎹 **DAW Integration** - URL handlers, desktop app, export scripts, VST/AU plugin
- 📱 **PWA** - Installable on any platform
- 📦 **One-Click Installers** - Mac (.pkg) & Windows (.exe) for VST/AU plugin

**Live Demo:** [https://web-production-5748a.up.railway.app/](https://web-production-5748a.up.railway.app/)

**[View Project Documentation →](./alioop-microservice-prototype/RELEASE_NOTES.md)**

---

## ⚡ Integration Options

Choose the method that fits your workflow:

| Method | Time | Setup | Best For |
|--------|------|-------|----------|
| **Plugin (Phase 4)** 🆕 | ~3 min | 1-click install | In-DAW workflow, no exports |
| **Desktop App (Phase 2)** | ~15 sec | 5 min | Auto-detection, speed demons |
| **Export Scripts (Phase 3)** | ~30 sec | 2 min | Keyboard shortcuts |
| **URL Handler (Phase 1)** | ~1 min | None | Universal compatibility |
| **Web App** | ~2 min | None | Any browser |

**[📥 Download Plugin →](./alioop-plugin/download.html)** | **[🔧 Desktop App →](./alioop-desktop/README.md)** | **[📚 Full DAW Guide →](./DAW_INTEGRATION.md)**

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