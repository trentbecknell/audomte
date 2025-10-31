# Release Notes

## Version 3.0.0 - October 31, 2025 🚀

### 🎉 MAJOR RELEASE: Complete DAW Integration Suite + VST/AU Plugin

**Alioop is now a complete professional audio delivery platform with full DAW integration!**

From web app to native VST/AU plugin - choose the workflow that fits you best.

---

## 🆕 What's New in v3.0.0

### 🔌 Phase 4: VST/AU/AAX Plugin (NEW!)

**Professional audio delivery directly from your DAW - never leave your session!**

- **In-DAW Recording** - Capture audio directly from your session (no bounce needed!)
- **Built-in Client Form** - Fill client details right in the plugin window
- **Auto-Upload & Email** - Exports WAV and sends automatically
- **Session Persistence** - Plugin remembers last client info
- **Branded UI** - Orange/black/cream Alioop styling
- **Multi-Format** - VST3, AU (macOS), AAX (future)
- **Cross-Platform** - macOS 10.13+, Windows 10+

**Workflow:** Record → Fill form → Send → Done in ~3 minutes!

### 📦 One-Click Installers (NEW!)

**Zero configuration for non-technical users!**

**macOS (.pkg):**
- 4 clicks to install (Continue → Continue → Install → Close)
- Auto-installs VST3 to `/Library/Audio/Plug-Ins/VST3/`
- Auto-installs AU to `/Library/Audio/Plug-Ins/Components/`
- Quick Start guide appears on Desktop
- Detects installed DAWs (Pro Tools, Logic, Ableton, Studio One)

**Windows (.exe):**
- 5 clicks to install (OK → Next → Install → Finish → Close)
- Auto-installs VST3 to `C:\Program Files\Common Files\VST3\`
- Quick Start guide appears on Desktop
- Detects installed DAWs
- Uninstaller in Control Panel

**Download:** [GitHub Releases](https://github.com/trentbecknell/audomte/releases/latest)

### 🖥️ Desktop App (Phase 2)

**Auto-detect DAW bounces and send instantly!**

- Watch folder monitoring (`~/Alioop/Bounces`)
- Desktop notifications when files appear
- Smart filename parsing (ClientName_Project.wav)
- System tray integration
- ~15 second workflow

### ⌨️ Export Scripts (Phase 3)

**Keyboard shortcuts for Pro Tools, Logic, Ableton, Studio One**

- AppleScript automation (Pro Tools, Logic)
- Python Control Surface (Ableton)
- JavaScript API (Studio One)
- ~30 second workflow

### ⚡ URL Handler (Phase 1)

**No install required - works everywhere!**

- URL parameters pre-fill client info
- Custom keyboard shortcuts in DAW
- Browser-based workflow
- ~1 minute workflow

---

## 🎯 Complete Integration Suite

| Phase | Tool | Time | Best For |
|-------|------|------|----------|
| **Phase 4** | VST/AU Plugin | ~3 min | In-DAW workflow, no exports |
| **Phase 2** | Desktop App | ~15 sec | Auto-detection, speed demons |
| **Phase 3** | Export Scripts | ~30 sec | Keyboard shortcuts |
| **Phase 1** | URL Handler | ~1 min | Universal compatibility |
| **Web App** | Browser | ~2 min | Any device |

**Choose the method that fits YOUR workflow!**

---

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

### Web Application (Railway)
- **Framework**: FastAPI 0.115.2
- **Server**: Uvicorn 0.30.6
- **Database**: SQLite with full schema support
- **Templates**: Jinja2 with Pico CSS
- **Validation**: Pydantic 2.9.2
- **PWA**: Installable on any platform
- **Integrations**: 
  - Twilio 9.3.7 (SMS)
  - SendGrid 6.11.0 (Email)
  - python-dotenv 1.2.1 (Config)

### Desktop App (Electron)
- **Framework**: Electron 28
- **File Watcher**: Chokidar
- **HTTP Client**: Axios
- **Storage**: Electron Store
- **Cross-Platform**: macOS, Windows, Linux

### VST/AU Plugin (Native)
- **Framework**: JUCE 7.0+
- **Language**: C++17
- **Formats**: VST3, AU, AAX (future)
- **Audio**: Built-in WAV recorder
- **HTTP**: JUCE URL (multipart upload)
- **Build**: CMake, Xcode, Visual Studio

### Export Scripts
- **Pro Tools**: AppleScript
- **Logic Pro**: AppleScript
- **Ableton**: Python (Control Surface + CLI)
- **Studio One**: JavaScript API

---

## 📁 Project Structure

```
audomte/
├── alioop-microservice-prototype/     # Web application (Railway)
│   ├── app/
│   │   ├── main.py                    # FastAPI endpoints
│   │   ├── db.py                      # Database schema
│   │   └── adapters/                  # SMS, Email, Payments
│   ├── templates/
│   │   ├── index.html                 # Main UI
│   │   └── landing.html               # Landing page
│   └── static/
│       └── app.js                     # Client-side JS
│
├── alioop-desktop/                    # Desktop App (Phase 2)
│   ├── main.js                        # Electron main process
│   ├── index.html                     # Desktop UI
│   ├── package.json                   # Dependencies
│   └── icons/                         # App icons
│
├── daw-export-scripts/                # Export Scripts (Phase 3)
│   ├── pro-tools/                     # AppleScript
│   ├── logic-pro/                     # AppleScript
│   ├── ableton/                       # Python
│   └── studio-one/                    # JavaScript
│
├── alioop-plugin/                     # VST/AU Plugin (Phase 4)
│   ├── Source/
│   │   ├── PluginProcessor.cpp        # Audio processing
│   │   ├── PluginEditor.cpp           # UI
│   │   └── AlioopAPI.cpp              # Backend communication
│   ├── installers/
│   │   ├── macos-installer.sh         # Mac .pkg builder
│   │   ├── windows-installer.nsi      # Windows .exe builder
│   │   └── README.md                  # Installer guide
│   ├── download.html                  # Download page
│   ├── build-all.sh                   # Build automation
│   └── create-github-release.sh       # Release automation
│
├── DAW_INTEGRATION.md                 # Complete DAW guide
├── SHIPPING_GUIDE.md                  # Deployment instructions
└── README.md                          # Project overview
```

---

## 🚀 Quick Start

### Option 1: VST/AU Plugin (Recommended for DAW users)

```bash
# Download installer
# Mac: https://github.com/trentbecknell/audomte/releases/latest
# Windows: https://github.com/trentbecknell/audomte/releases/latest

# Install (4-5 clicks)
# Plugin auto-installs to system folders

# Open your DAW
# Rescan plugins → Insert "Alioop Send" on master → Done!
```

### Option 2: Desktop App (Fastest workflow)

```bash
cd alioop-desktop
npm install
npm start

# Set watch folder in settings
# Bounce files → Auto-detected → Send!
```

### Option 3: Web App (Works anywhere)

```bash
cd alioop-microservice-prototype
pip install -r requirements.txt

# Configure .env (optional)
TWILIO_ACCOUNT_SID=your_sid_here
SENDGRID_API_KEY=your_key_here

# Start server
uvicorn app.main:app --reload

# Visit: http://localhost:8000
```

### Option 4: Export Scripts (Keyboard shortcuts)

```bash
# See DAW_INTEGRATION.md for setup
# Install script for your DAW
# Use keyboard shortcut to send
```

---

## 📚 Documentation

### DAW Integration
- **DAW_INTEGRATION.md** - Complete guide to all 4 phases
- **alioop-desktop/README.md** - Desktop app documentation
- **daw-export-scripts/README.md** - Export scripts for all DAWs
- **alioop-plugin/README.md** - Plugin documentation
- **alioop-plugin/SHIPPING_GUIDE.md** - Deployment instructions
- **alioop-plugin/RELEASE_CHECKLIST.md** - Pre-release testing

### Web Application
- **PHONE_MASKING.md** - Phone masking service guide
- **REAL_MESSAGING_SETUP.md** - Twilio & SendGrid setup
- **VERIFY_NUMBERS.md** - Phone number verification
- **FIX_A2P_ERROR.md** - A2P 10DLC registration solutions

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

### Completed ✅
- [x] DAW URL handler integration (Phase 1)
- [x] Desktop app with watch folder (Phase 2)
- [x] Export scripts for major DAWs (Phase 3)
- [x] VST/AU plugin with in-DAW recording (Phase 4)
- [x] One-click installers (Mac/Windows)
- [x] Automated GitHub Release workflow
- [x] Professional download page
- [x] Complete documentation suite

### In Progress 🚧
- [ ] AAX format for Pro Tools native support
- [ ] Linux VST3 builds and installers
- [ ] Code signing (Mac Developer ID, Windows CA cert)
- [ ] Auto-plugin rescan after install

### Planned 🔮
- [ ] Multi-file delivery (stems)
- [ ] Batch export multiple takes
- [ ] Integration with DAW markers
- [ ] Video tutorial embedded in installers
- [ ] In-plugin walkthrough for first-time users
- [ ] Real Twilio Proxy integration for phone masking
- [ ] Webhook handlers for delivery tracking
- [ ] Client portal for self-service
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
