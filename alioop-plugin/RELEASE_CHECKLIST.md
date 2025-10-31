# Release Checklist for Alioop Plugin v1.0.0

## Pre-Release Testing

### macOS Testing
- [ ] Test installer on clean macOS 10.13 (High Sierra)
- [ ] Test installer on macOS 11 (Big Sur)
- [ ] Test installer on macOS 12 (Monterey)
- [ ] Test installer on macOS 13 (Ventura)
- [ ] Test installer on macOS 14 (Sonoma)
- [ ] Verify VST3 installs to `/Library/Audio/Plug-Ins/VST3/`
- [ ] Verify AU installs to `/Library/Audio/Plug-Ins/Components/`
- [ ] Check Quick Start appears on Desktop
- [ ] Test in Pro Tools (VST3)
- [ ] Test in Logic Pro (AU)
- [ ] Test in Ableton Live (VST3)
- [ ] Test in Studio One (VST3)
- [ ] Test recording functionality
- [ ] Test upload to Railway backend
- [ ] Verify email delivery to client
- [ ] Test uninstaller

### Windows Testing
- [ ] Test installer on clean Windows 10
- [ ] Test installer on Windows 11
- [ ] Verify VST3 installs to `C:\Program Files\Common Files\VST3\`
- [ ] Check Quick Start appears on Desktop
- [ ] Check uninstaller appears in Control Panel
- [ ] Test in Pro Tools (VST3)
- [ ] Test in Ableton Live (VST3)
- [ ] Test in Studio One (VST3)
- [ ] Test in Cubase (VST3)
- [ ] Test in REAPER (VST3)
- [ ] Test recording functionality
- [ ] Test upload to Railway backend
- [ ] Verify email delivery to client
- [ ] Test uninstaller

### User Experience Testing

**Test with non-technical users:**
- [ ] Can they install without asking questions?
- [ ] Do they find the plugin in their DAW?
- [ ] Do they understand the Quick Start guide?
- [ ] Can they successfully record audio?
- [ ] Can they fill the form correctly?
- [ ] Do they successfully send their first delivery?
- [ ] Time from install to first successful send < 10 minutes?

**If users struggle, update:**
- [ ] Installer messages
- [ ] Quick Start guide
- [ ] Plugin UI labels
- [ ] Error messages

## Code Signing (Optional but Recommended)

### macOS
- [ ] Obtain Apple Developer account ($99/year)
- [ ] Request Developer ID Installer certificate
- [ ] Sign installer: `productsign --sign "Developer ID Installer: Your Name" ...`
- [ ] Verify signature: `pkgutil --check-signature ...`
- [ ] Notarize with Apple: `xcrun notarytool submit ...`
- [ ] Staple ticket: `xcrun stapler staple ...`
- [ ] Test signed installer on clean Mac

### Windows
- [ ] Obtain code signing certificate (~$100-300/year)
- [ ] Sign installer: `signtool sign /f cert.pfx ...`
- [ ] Verify signature: `signtool verify /pa ...`
- [ ] Test signed installer on clean Windows

## Documentation Review

- [ ] README.md has download links
- [ ] Installation instructions are clear
- [ ] Usage workflow is documented
- [ ] Troubleshooting section is complete
- [ ] Screenshots/GIFs show plugin in action
- [ ] System requirements are listed
- [ ] Supported DAWs are listed
- [ ] Contact/support info is provided

## Build Artifacts

### macOS
- [ ] Build plugin: `./build-all.sh`
- [ ] Verify VST3 works: `Builds/MacOSX/build/.../AlioopSend.vst3`
- [ ] Verify AU works: `Builds/MacOSX/build/.../AlioopSend.component`
- [ ] Create installer: `cd installers && ./macos-installer.sh`
- [ ] Output: `installers/output/AlioopSend-macOS-v1.0.0.pkg`
- [ ] File size reasonable (< 50MB)?
- [ ] Test installer on clean Mac

### Windows
- [ ] Build plugin with Visual Studio
- [ ] Verify VST3 works
- [ ] Create installer: `cd installers && build-windows-installer.bat`
- [ ] Output: `installers\output\AlioopSend-Windows-v1.0.0.exe`
- [ ] File size reasonable (< 50MB)?
- [ ] Test installer on clean Windows

## GitHub Release

- [ ] Create git tag: `git tag -a v1.0.0 -m "Alioop Plugin v1.0.0"`
- [ ] Push tag: `git push origin v1.0.0`
- [ ] Go to GitHub → Releases → Draft a new release
- [ ] Select tag: v1.0.0
- [ ] Release title: "Alioop Plugin v1.0.0 - Professional Audio Delivery"
- [ ] Upload macOS installer (unsigned or signed)
- [ ] Upload Windows installer (unsigned or signed)
- [ ] Write release notes (see template below)
- [ ] Publish release

### Release Notes Template

```markdown
# Alioop Plugin v1.0.0

**Professional audio delivery directly from your DAW!**

## 🎉 First Release

Send client deliveries without leaving your DAW session:
- Record audio directly from your session
- Fill client form in plugin window
- Click Send → Client gets email instantly
- ~3 minutes total (no file export needed!)

## 📥 Download

**macOS (10.13+):**
- [AlioopSend-macOS-v1.0.0.pkg](link)
- Supports: VST3 + AU
- DAWs: Pro Tools, Logic Pro, Ableton, Studio One, etc.

**Windows (10+):**
- [AlioopSend-Windows-v1.0.0.exe](link)
- Supports: VST3
- DAWs: Pro Tools, Ableton, Studio One, Cubase, REAPER, etc.

## 🚀 Quick Start

1. Download installer for your OS
2. Double-click to install (plugin auto-installs)
3. Open your DAW and rescan plugins
4. Insert "Alioop Send" on master track
5. Record, fill form, send!

**[Full Documentation →](https://github.com/trentbecknell/audomte/tree/main/alioop-plugin)**

## 📋 What's Included

- VST3/AU plugin (Mac & Windows)
- One-click installers
- Quick Start guide (auto-appears on Desktop)
- Complete documentation

## 💡 Features

- 🎙️ In-DAW recording
- 📝 Built-in client form
- 🚀 Auto-upload & email delivery
- 💾 Session persistence (remembers clients)
- 🎨 Branded Alioop UI
- 📧 Instant email with download link
- 💳 Payment link included

## 🐛 Known Issues

None currently! Please report issues on GitHub.

## 🆘 Support

- [Documentation](https://github.com/trentbecknell/audomte/tree/main/alioop-plugin)
- [Report Issues](https://github.com/trentbecknell/audomte/issues)
- [Build from Source](https://github.com/trentbecknell/audomte/tree/main/alioop-plugin/docs/BUILD_GUIDE.md)

---

**First time using Alioop?** Check out the Quick Start guide that appears on your Desktop after installation!
```

## Post-Release

- [ ] Announce on social media
- [ ] Update website with download links
- [ ] Monitor GitHub Issues for bug reports
- [ ] Track download numbers
- [ ] Collect user feedback
- [ ] Plan v1.1.0 improvements

## Metrics to Track

**Installation Success Rate:**
- % of users who successfully install
- % of users who find plugin in DAW
- % of users who send first delivery
- Average time from download to first send

**Usage Metrics (if you add analytics):**
- Number of installations
- Number of sends per user
- Most popular DAWs
- Average workflow time
- Drop-off points

**Support Metrics:**
- Number of support requests
- Most common issues
- Documentation gaps
- Feature requests

## Future Improvements (v1.1.0+)

Based on user feedback:
- [ ] Auto-DAW plugin rescan after install?
- [ ] Video tutorial embedded in installer?
- [ ] In-plugin tutorial/walkthrough?
- [ ] Preset client templates?
- [ ] Multi-file delivery (stems)?
- [ ] VST2 support (if needed)?
- [ ] AAX support for Pro Tools?
- [ ] Linux support?

---

**Ready to release?** Check every box above! 🚀
