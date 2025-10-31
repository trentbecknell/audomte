# Alioop Plugin Installers

**One-click installers for non-technical users!**

Zero configuration, minimal clicks, automatic installation.

## 🎯 Philosophy

**Make it stupid simple:**
- Users don't need to know what VST3 or AU means
- No folder selection, no configuration
- Double-click installer → Done
- Quick Start guide auto-opens on Desktop

## 📦 Installer Types

### macOS Installer (.pkg)

**What it does:**
- ✅ Auto-installs VST3 to `/Library/Audio/Plug-Ins/VST3/`
- ✅ Auto-installs AU to `/Library/Audio/Plug-Ins/Components/`
- ✅ Places Quick Start guide on Desktop
- ✅ Detects installed DAWs
- ✅ Shows welcome/readme screens

**User experience:**
1. Double-click `.pkg` file
2. Click "Continue" twice
3. Enter password (macOS requires admin for system folders)
4. Click "Install"
5. Done! Quick Start opens automatically

**Total clicks: 4** (Continue, Continue, Install, Close)

### Windows Installer (.exe)

**What it does:**
- ✅ Auto-installs VST3 to `C:\Program Files\Common Files\VST3\`
- ✅ Places Quick Start guide on Desktop
- ✅ Detects installed DAWs
- ✅ Adds uninstaller to Control Panel
- ✅ Shows welcome screen

**User experience:**
1. Double-click `.exe` file
2. Click "OK" on welcome
3. Click "Next"
4. Click "Install"
5. Click "Finish"
6. Done! Quick Start opens automatically

**Total clicks: 5** (OK, Next, Install, Finish, Close)

## 🔨 Building Installers

### macOS

**Requirements:**
- macOS 10.13+
- Xcode Command Line Tools
- Built plugin files

**Build:**
```bash
cd installers
chmod +x macos-installer.sh
./macos-installer.sh
```

**Output:**
- `output/AlioopSend-macOS-v1.0.0.pkg`

**Optional - Code Signing (for distribution):**
```bash
# Sign the installer (prevents macOS Gatekeeper warnings)
productsign --sign "Developer ID Installer: Your Name" \
  output/AlioopSend-macOS-v1.0.0.pkg \
  output/AlioopSend-macOS-v1.0.0-Signed.pkg
```

### Windows

**Requirements:**
- Windows 10+
- NSIS (Nullsoft Scriptable Install System)
- Built plugin files

**Install NSIS:**
```bash
# Via Chocolatey
choco install nsis

# Or download from:
# https://nsis.sourceforge.io/Download
```

**Build:**
```bash
cd installers
build-windows-installer.bat
```

**Output:**
- `output\AlioopSend-Windows-v1.0.0.exe`

**Optional - Code Signing (for distribution):**
```bash
# Sign the installer (prevents Windows SmartScreen warnings)
signtool sign /f YourCertificate.pfx /p YourPassword \
  /t http://timestamp.digicert.com \
  output\AlioopSend-Windows-v1.0.0.exe
```

## 🎨 Customizing Installer Graphics

### macOS
The script uses text-based screens. For custom graphics:
1. Edit `macos-installer.sh`
2. Add `--background` flag to `productbuild`
3. Provide custom background image (620x418 pixels)

### Windows
Replace these placeholder files with branded images:

**Header Image** (`installer-header.bmp`):
- Size: 150 x 57 pixels
- Shows at top of installer window
- Use Alioop orange/black branding

**Welcome Image** (`installer-welcome.bmp`):
- Size: 164 x 314 pixels
- Shows on welcome/finish pages
- Use Alioop brand colors

**Example branding:**
```
Orange: #f05709
Black:  #161614
Cream:  #fcf5eb
```

## 📤 Distribution

### GitHub Releases (Recommended)

**Upload installers to GitHub Releases:**

1. Create a new release:
   ```bash
   git tag -a v1.0.0 -m "Alioop Plugin v1.0.0"
   git push origin v1.0.0
   ```

2. Go to GitHub → Releases → Draft a new release

3. Upload both installers:
   - `AlioopSend-macOS-v1.0.0.pkg` (or signed version)
   - `AlioopSend-Windows-v1.0.0.exe` (or signed version)

4. Add release notes with simple instructions

### Simple Download Page

Create a landing page with big download buttons:

```html
<div class="downloads">
  <a href="https://github.com/.../releases/.../AlioopSend-macOS.pkg" 
     class="btn-download mac">
    🍎 Download for Mac
  </a>
  
  <a href="https://github.com/.../releases/.../AlioopSend-Windows.exe" 
     class="btn-download windows">
    🪟 Download for Windows
  </a>
</div>
```

## ✅ Testing Checklist

### Before Release:

**macOS:**
- [ ] Test on clean Mac (no plugin folders exist)
- [ ] Test with Logic Pro installed
- [ ] Test with Pro Tools installed
- [ ] Verify plugin appears in DAW after rescan
- [ ] Test uninstaller
- [ ] Check Quick Start guide appears on Desktop
- [ ] Test on macOS 10.13, 11.0, 12.0, 13.0, 14.0

**Windows:**
- [ ] Test on clean Windows (no plugin folders exist)
- [ ] Test with Ableton installed
- [ ] Test with Pro Tools installed
- [ ] Test with Studio One installed
- [ ] Verify plugin appears in DAW after rescan
- [ ] Test uninstaller (Control Panel)
- [ ] Check Quick Start guide appears on Desktop
- [ ] Test on Windows 10, 11

### User Testing:

Give installers to **non-technical users** and watch:
- Can they install without help?
- Do they find the plugin in their DAW?
- Do they understand the Quick Start guide?
- Do they successfully send their first delivery?

**If they ask questions, improve the installer/guide!**

## 🆘 Troubleshooting

### macOS: "Cannot be opened because it is from an unidentified developer"

**Solution 1: Code sign the installer** (recommended for distribution)
- Requires Apple Developer account ($99/year)
- Sign with Developer ID Installer certificate

**Solution 2: User can bypass (not recommended)**
- Right-click installer → Open → Open
- Or: System Settings → Security → Allow

### Windows: "Windows protected your PC" SmartScreen warning

**Solution 1: Code sign the installer** (recommended for distribution)
- Requires code signing certificate (~$100-300/year)
- Sign with trusted CA certificate

**Solution 2: User can bypass**
- Click "More info" → "Run anyway"

### Plugin doesn't appear in DAW

**Most common cause:** User needs to rescan plugins

**Add to installer success message:**
```
⚠️ IMPORTANT: Rescan plugins in your DAW!

Pro Tools: Setup → Plug-ins
Logic: Preferences → Plug-in Manager → Reset & Rescan
Ableton: Preferences → Plug-ins → Rescan
Studio One: Options → Locations → Reset Blacklist → Scan
```

## 🔒 Code Signing (Optional but Recommended)

### Why Sign?

**Unsigned installers:**
- macOS Gatekeeper blocks by default
- Windows SmartScreen shows scary warnings
- Users have to jump through hoops

**Signed installers:**
- ✅ Install with zero warnings
- ✅ Professional appearance
- ✅ Users trust it more

### macOS Code Signing

**Requirements:**
- Apple Developer account ($99/year)
- Developer ID Installer certificate

**Process:**
```bash
# 1. Get certificate from Apple Developer
# 2. Import to Keychain
# 3. Sign the installer:

productsign --sign "Developer ID Installer: Your Name (TEAM_ID)" \
  output/AlioopSend-macOS-v1.0.0.pkg \
  output/AlioopSend-macOS-v1.0.0-Signed.pkg

# 4. Verify signature:
pkgutil --check-signature output/AlioopSend-macOS-v1.0.0-Signed.pkg

# 5. Notarize with Apple (required for macOS 10.15+):
xcrun notarytool submit \
  output/AlioopSend-macOS-v1.0.0-Signed.pkg \
  --apple-id you@example.com \
  --team-id TEAM_ID \
  --password app-specific-password \
  --wait

# 6. Staple notarization ticket:
xcrun stapler staple output/AlioopSend-macOS-v1.0.0-Signed.pkg
```

### Windows Code Signing

**Requirements:**
- Code signing certificate from trusted CA
  - DigiCert, Sectigo, etc. (~$100-300/year)

**Process:**
```bash
# Sign the installer:
signtool sign \
  /f YourCertificate.pfx \
  /p YourPassword \
  /tr http://timestamp.digicert.com \
  /td sha256 \
  /fd sha256 \
  output\AlioopSend-Windows-v1.0.0.exe

# Verify signature:
signtool verify /pa output\AlioopSend-Windows-v1.0.0.exe
```

## 📊 Installer Analytics (Optional)

Track installation success rate:

**Option 1: Phone Home**
Add to postinstall script:
```bash
curl -X POST https://your-api.com/analytics/install \
  -d "platform=macos&version=1.0.0" \
  > /dev/null 2>&1
```

**Option 2: GitHub Release Downloads**
- Check GitHub Insights → Traffic
- See download counts per release

## 🎯 Success Metrics

**Good installer experience:**
- ✅ < 5 clicks to install
- ✅ < 2 minutes total time
- ✅ 90%+ of users install successfully without help
- ✅ Quick Start guide answers 90%+ of questions
- ✅ Plugin appears in DAW after rescan
- ✅ Users successfully send first delivery within 5 minutes

**If metrics are lower, iterate on:**
- Clearer installer messages
- Better Quick Start guide
- Auto-DAW configuration (if possible)
- Video tutorial link in installer

## 🚀 Future Improvements

**Auto-DAW Detection & Configuration:**
- Detect installed DAWs
- Offer to auto-scan plugins
- Pre-configure plugin in DAW template

**Installer should:**
- Detect Pro Tools → Trigger plugin scan
- Detect Logic → Trigger plugin scan  
- Detect Ableton → Add to MIDI Remote Scripts?
- Detect Studio One → Auto-add to macros?

**One-Click Setup:**
Ultimate goal: Install → DAW auto-opens → Plugin ready → User sends first delivery

---

**Questions? Issues?**  
Open an issue: https://github.com/trentbecknell/audomte/issues
