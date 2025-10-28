# Changelog

All notable changes to the Alioop Comms + Preferences Microservice will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.0] - 2025-10-28

### Added
- 🧪 **quick_email_test.py** - Simple email testing utility
- 🔧 **setup_sendgrid.py** - Interactive SendGrid configuration wizard
- 🔑 **test_sendgrid_key.py** - API key validation tool

### Changed
- ✅ **Email Integration Verified** - SendGrid fully tested and operational
- 📧 Email sending now confirmed working in production
- 🔧 Improved email setup documentation and troubleshooting

### Fixed
- 🐛 SendGrid configuration workflow streamlined
- 📝 Better error messages for email authentication issues

## [1.0.0] - 2025-10-27

### Added
- 🎉 Initial release of Alioop Comms + Preferences Microservice
- 📱 Real SMS integration with Twilio
- 📧 Real email integration with SendGrid
- 🔒 Phone masking service for privacy protection
- 📞 Automatic E.164 phone number formatting
- 👥 Client management system (name, email, phone, preferences)
- 📋 Project management with status tracking
- 💬 Multi-channel messaging (email/SMS)
- 🗄️ SQLite database with full schema
- 🎨 Clean UI with Pico CSS framework
- ⚙️ Environment variable management (.env support)
- 📚 Comprehensive documentation suite
- 🔧 Helper scripts for setup and testing
- 🛡️ Input validation with Pydantic schemas
- 🔄 DRYRUN mode for testing without sending real messages

### Fixed
- ✅ Project creation form client dropdown validation
- ✅ Client messaging button functionality  
- ✅ Phone number format validation for Twilio compatibility
- ✅ Database schema alignment for phone masking

### Security
- 🔐 Secure credential management (no hardcoded secrets)
- 🚫 `.gitignore` properly configured to exclude sensitive files
- 🔒 Privacy protection via phone masking
- ✅ Input validation on all endpoints

### Documentation
- 📖 RELEASE_NOTES.md - Complete release documentation
- 📖 CHANGELOG.md - Version history and changes
- 📖 PHONE_MASKING.md - Phone masking service guide
- 📖 REAL_MESSAGING_SETUP.md - Twilio & SendGrid setup guide
- 📖 VERIFY_NUMBERS.md - Phone number verification guide
- 📖 FIX_A2P_ERROR.md - A2P 10DLC troubleshooting

### Scripts
- 🔧 check_config.py - Configuration verification tool
- 🔧 validate_phone.py - Phone number testing utility
- 🔧 setup_twilio.py - Interactive Twilio setup assistant
- 🔧 test_phone_masking.py - Phone masking API test suite
- 🔧 start.sh - Quick server start script

## [Unreleased]

### Planned
- Real Twilio Proxy integration for production phone masking
- Webhook handlers for message delivery tracking
- Message history and audit logs
- Client authentication portal
- Rate limiting for abuse prevention
- Advanced analytics dashboard
- Multi-language support
- PostgreSQL/MySQL database option

---

**Legend:**
- 🎉 Major feature
- ✨ Enhancement
- 🐛 Bug fix
- 🔒 Security
- 📚 Documentation
- 🔧 Tools/Scripts
- ⚠️ Deprecation
