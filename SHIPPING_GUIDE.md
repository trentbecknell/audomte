# 🚀 SHIPPING GUIDE - Alioop Plugin v1.0.0

**Ready to ship? Follow these steps!**

---

## ⚡ Quick Ship (5 Steps)

For those who just want to ship fast:

```bash
# 1. Clone on Mac
git clone https://github.com/trentbecknell/audomte.git
cd audomte/alioop-plugin

# 2. Install JUCE
brew install juce

# 3. Build everything
chmod +x build-all.sh
./build-all.sh

# 4. Install GitHub CLI and create release
brew install gh
gh auth login
chmod +x create-github-release.sh
./create-github-release.sh

# 5. Done! Share the download link
```

**Windows users:** Do the same on Windows (requires Visual Studio + NSIS)

---

## 📋 Detailed Shipping Steps

### Step 1: Prerequisites

**On macOS:**
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install JUCE and tools
brew install juce cmake gh
```

**On Windows:**
```bash
# Install Visual Studio 2022 (Community Edition is free)
# Download from: https://visualstudio.microsoft.com/

# Install CMake
# Download from: https://cmake.org/download/

# Install NSIS (for installers)
choco install nsis
# Or download from: https://nsis.sourceforge.io/Download

# Install GitHub CLI
winget install GitHub.cli
# Or download from: https://cli.github.com/
```

### Step 2: Clone Repository

```bash
git clone https://github.com/trentbecknell/audomte.git
cd audomte/alioop-plugin
```

### Step 3: Build Plugin

**On macOS:**
```bash
# Make build script executable
chmod +x build-all.sh

# Build plugin + installer (one command!)
./build-all.sh

# Output:
# - Builds/MacOSX/build/.../AlioopSend.vst3
# - Builds/MacOSX/build/.../AlioopSend.component
# - installers/output/AlioopSend-macOS-v1.0.0.pkg
```

**On Windows:**
```bash
# Build plugin with CMake
mkdir Builds\Windows
cd Builds\Windows
cmake ..\.. -G "Visual Studio 17 2022" -A x64
cmake --build . --config Release

# Build installer
cd ..\..\installers
build-windows-installer.bat

# Output:
# - installers\output\AlioopSend-Windows-v1.0.0.exe
```

### Step 4: Test Installers

**Critical testing (don't skip!):**

**macOS:**
```bash
# Test on a CLEAN Mac if possible (or create new user account)
# 1. Double-click AlioopSend-macOS-v1.0.0.pkg
# 2. Follow installer (should be 4 clicks)
# 3. Check Quick Start appears on Desktop
# 4. Open Logic Pro or Ableton
# 5. Rescan plugins
# 6. Find "Alioop Send" in plugin list
# 7. Insert on master track
# 8. Test: Record → Fill form → Send
# 9. Verify client receives email
```

**Windows:**
```bash
# Test on a CLEAN Windows if possible
# 1. Double-click AlioopSend-Windows-v1.0.0.exe
# 2. Follow installer (should be 5 clicks)
# 3. Check Quick Start appears on Desktop
# 4. Open Ableton or Pro Tools
# 5. Rescan plugins
# 6. Find "Alioop Send" in plugin list
# 7. Insert on master track
# 8. Test: Record → Fill form → Send
# 9. Verify client receives email
```

**If anything fails:** Fix it before releasing!

### Step 5: (Optional) Code Sign

**macOS signing (removes Gatekeeper warnings):**
```bash
# Requires Apple Developer account ($99/year)
# Get Developer ID Installer certificate from Apple

# Sign the installer
productsign --sign "Developer ID Installer: Your Name (TEAM_ID)" \
  installers/output/AlioopSend-macOS-v1.0.0.pkg \
  installers/output/AlioopSend-macOS-v1.0.0-Signed.pkg

# Notarize (required for macOS 10.15+)
xcrun notarytool submit \
  installers/output/AlioopSend-macOS-v1.0.0-Signed.pkg \
  --apple-id you@example.com \
  --team-id TEAM_ID \
  --password app-specific-password \
  --wait

# Staple notarization ticket
xcrun stapler staple installers/output/AlioopSend-macOS-v1.0.0-Signed.pkg
```

**Windows signing (removes SmartScreen warnings):**
```bash
# Requires code signing certificate (~$100-300/year)
# Get from DigiCert, Sectigo, etc.

# Sign the installer
signtool sign \
  /f YourCertificate.pfx \
  /p YourPassword \
  /tr http://timestamp.digicert.com \
  /td sha256 \
  /fd sha256 \
  installers\output\AlioopSend-Windows-v1.0.0.exe
```

**Can skip for now:** Users can still install unsigned (requires extra click)

### Step 6: Create GitHub Release

**Option A: Automated (recommended):**
```bash
# Make sure you're authenticated with GitHub
gh auth login

# Run the release script
chmod +x create-github-release.sh
./create-github-release.sh

# Done! Release created automatically
```

**Option B: Manual:**
```bash
# 1. Create and push tag
git tag -a v1.0.0 -m "Alioop Plugin v1.0.0 - First Release"
git push origin v1.0.0

# 2. Go to GitHub
# https://github.com/trentbecknell/audomte/releases/new

# 3. Fill in:
# - Tag: v1.0.0
# - Title: Alioop Plugin v1.0.0 - Professional Audio Delivery
# - Description: Copy from create-github-release.sh
# - Upload: Both installers

# 4. Click "Publish release"
```

### Step 7: Update Download Page

After release is created, update `download.html` with real URLs:

```html
<!-- Change this: -->
<a href="https://github.com/trentbecknell/audomte/releases/latest/download/...">

<!-- To this: -->
<a href="https://github.com/trentbecknell/audomte/releases/download/v1.0.0/AlioopSend-macOS-v1.0.0.pkg">
  🍎 Download for Mac
</a>

<a href="https://github.com/trentbecknell/audomte/releases/download/v1.0.0/AlioopSend-Windows-v1.0.0.exe">
  🪟 Download for Windows
</a>
```

Commit and push the update:
```bash
git add download.html
git commit -m "Update download links for v1.0.0 release"
git push origin main
```

### Step 8: Host Download Page

**Option A: GitHub Pages (free, easy):**
```bash
# 1. Go to GitHub → Settings → Pages
# 2. Source: Deploy from branch
# 3. Branch: main
# 4. Folder: / (root)
# 5. Save

# Your download page will be at:
# https://trentbecknell.github.io/audomte/alioop-plugin/download.html
```

**Option B: Custom Domain:**
- Upload `download.html` to your website
- Example: `https://alioop.com/plugin/download`

### Step 9: Announce & Share!

**Share the download link:**
```
🎉 Alioop Plugin v1.0.0 is LIVE!

Professional audio delivery directly from your DAW.

📥 Download: https://trentbecknell.github.io/audomte/alioop-plugin/download.html

✨ Features:
- In-DAW recording
- Built-in client form
- Auto-upload & email
- ~3 min workflow

Supports Pro Tools, Logic, Ableton, Studio One, and more!

#AudioEngineering #MusicProduction #DAW
```

**Where to share:**
- Twitter/X
- Reddit (r/audioengineering, r/WeAreTheMusicMakers)
- Facebook groups
- Discord servers
- Your website/blog
- Email newsletter
- Direct messages to beta testers

---

## 🐛 Troubleshooting

### Build fails on macOS

**Error: "JUCE not found"**
```bash
# Install JUCE
brew install juce

# Or download manually from juce.com
# and set JUCE_PATH in CMakeLists.txt
```

**Error: "No CMAKE_CXX_COMPILER"**
```bash
# Install Xcode Command Line Tools
xcode-select --install
```

### Build fails on Windows

**Error: "Visual Studio not found"**
```bash
# Install Visual Studio 2022 Community Edition
# Download from: https://visualstudio.microsoft.com/
# Make sure to include "Desktop development with C++"
```

**Error: "NSIS not found"**
```bash
# Install NSIS
choco install nsis
# Or download from: https://nsis.sourceforge.io/Download
```

### Installer issues

**macOS: "Cannot be opened"**
- This is normal for unsigned installers
- Right-click → Open → Open (or code sign it)

**Windows: "Windows protected your PC"**
- This is normal for unsigned installers
- Click "More info" → "Run anyway" (or code sign it)

**Plugin doesn't appear in DAW**
- Make sure to rescan plugins
- Check installation path is correct
- Restart the DAW

---

## ✅ Pre-Ship Checklist

Before you announce to the world:

- [ ] Built on macOS successfully
- [ ] Built on Windows successfully
- [ ] Tested installer on clean macOS
- [ ] Tested installer on clean Windows
- [ ] Tested in Logic Pro (macOS)
- [ ] Tested in Pro Tools (both)
- [ ] Tested in Ableton (both)
- [ ] Tested recording functionality
- [ ] Tested upload to backend
- [ ] Verified email delivery
- [ ] Verified payment link works
- [ ] Quick Start guide appears
- [ ] GitHub Release created
- [ ] Download page updated
- [ ] Download page hosted
- [ ] Announcement prepared

**All checked?** Ship it! 🚀

---

## 📊 Post-Launch

### Track These Metrics

**Week 1:**
- [ ] Monitor download counts (GitHub Insights)
- [ ] Watch for GitHub Issues
- [ ] Check error logs on Railway backend
- [ ] Collect user feedback
- [ ] Note common questions

**Month 1:**
- [ ] Calculate installation success rate
- [ ] Identify most popular DAWs
- [ ] Track sends per user
- [ ] Review support requests
- [ ] Plan v1.1.0 improvements

### Quick Wins for v1.1.0

Based on early feedback, consider:
- Video tutorial (< 2 min)
- In-plugin walkthrough
- More DAW-specific guides
- FAQ updates
- Bug fixes

---

## 🎉 You're Ready!

**Everything you need to ship:**
1. ✅ Complete plugin source code
2. ✅ Professional installers (Mac/Windows)
3. ✅ Beautiful download page
4. ✅ Automated build scripts
5. ✅ GitHub Release automation
6. ✅ Complete documentation
7. ✅ Testing checklists

**Just run the build script and ship it!**

```bash
./build-all.sh               # Build on Mac
build-windows-installer.bat  # Build on Windows
./create-github-release.sh   # Create release
# Share download link → Done! 🚀
```

**Questions?** Check RELEASE_CHECKLIST.md or READY_TO_SHIP.md

**Let's ship it! 🎊**
