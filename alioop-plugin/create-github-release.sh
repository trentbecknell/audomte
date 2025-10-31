#!/bin/bash
# GitHub Release Deployment Script
# This script creates a GitHub Release with installers

set -e

VERSION="1.0.0"
RELEASE_NAME="Alioop Plugin v${VERSION} - Professional Audio Delivery"
REPO="trentbecknell/audomte"

echo "🚀 Preparing GitHub Release v${VERSION}"
echo "========================================"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) not found!"
    echo "   Install from: https://cli.github.com/"
    echo "   Or use: brew install gh"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub!"
    echo "   Run: gh auth login"
    exit 1
fi

# Check if installers exist
MACOS_INSTALLER="installers/output/AlioopSend-macOS-v${VERSION}.pkg"
WINDOWS_INSTALLER="installers/output/AlioopSend-Windows-v${VERSION}.exe"

if [ ! -f "$MACOS_INSTALLER" ]; then
    echo "⚠️  Warning: macOS installer not found: $MACOS_INSTALLER"
    echo "   Build it first with: ./build-all.sh"
fi

if [ ! -f "$WINDOWS_INSTALLER" ]; then
    echo "⚠️  Warning: Windows installer not found: $WINDOWS_INSTALLER"
    echo "   Build it on Windows with: build-windows-installer.bat"
fi

echo ""
echo "📋 Release Details:"
echo "   Version: v${VERSION}"
echo "   Tag: v${VERSION}"
echo "   Repository: ${REPO}"
echo ""

# Create git tag
echo "🏷️  Creating git tag..."
git tag -a "v${VERSION}" -m "Alioop Plugin v${VERSION} - First Release" 2>/dev/null || echo "Tag already exists"

# Push tag
echo "⬆️  Pushing tag to GitHub..."
git push origin "v${VERSION}" 2>/dev/null || echo "Tag already pushed"

echo ""
echo "📦 Creating GitHub Release..."

# Create release notes
RELEASE_NOTES="# Alioop Plugin v${VERSION}

**Professional audio delivery directly from your DAW!**

## 🎉 First Release

Send client deliveries without leaving your DAW session:
- Record audio directly from your session
- Fill client form in plugin window
- Click Send → Client gets email instantly
- ~3 minutes total (no file export needed!)

## 📥 Download

**macOS (10.13+):**
- Supports: VST3 + AU
- DAWs: Pro Tools, Logic Pro, Ableton, Studio One, etc.
- Installation: Double-click → 4 clicks → Done!

**Windows (10+):**
- Supports: VST3
- DAWs: Pro Tools, Ableton, Studio One, Cubase, REAPER, etc.
- Installation: Double-click → 5 clicks → Done!

## 🚀 Quick Start

1. Download installer for your OS
2. Double-click to install (plugin auto-installs)
3. Open your DAW and rescan plugins
4. Insert \"Alioop Send\" on master track
5. Record, fill form, send!

**[Full Documentation →](https://github.com/${REPO}/tree/main/alioop-plugin)**

## 💡 Features

- 🎙️ In-DAW recording - Capture session audio directly
- 📝 Built-in form - Client info right in plugin
- 🚀 Auto-upload - Exports WAV and sends automatically
- 💾 Session persistence - Remembers last client
- 🎨 Branded UI - Orange/black/cream Alioop styling
- 📧 Email delivery - Instant client notification
- 💳 Payment link - Stripe integration

## 📋 What's Included

- VST3/AU plugin (Mac & Windows)
- One-click installers
- Quick Start guide (auto-appears on Desktop)
- Complete documentation

## 🔧 System Requirements

**macOS:**
- macOS 10.13 (High Sierra) or later
- VST3 or AU compatible DAW
- 64-bit Intel or Apple Silicon

**Windows:**
- Windows 10 or later
- VST3 compatible DAW
- 64-bit only

## 🆘 Support

- [Documentation](https://github.com/${REPO}/tree/main/alioop-plugin)
- [Report Issues](https://github.com/${REPO}/issues)
- [Build from Source](https://github.com/${REPO}/tree/main/alioop-plugin/docs/BUILD_GUIDE.md)

## 🎹 Complete DAW Integration

This is Phase 4 of our complete DAW integration suite:
- **Phase 1:** URL Handler (no install, ~1 min)
- **Phase 2:** Desktop App (auto-detection, ~15 sec)
- **Phase 3:** Export Scripts (keyboard shortcuts, ~30 sec)
- **Phase 4:** VST Plugin (in-DAW, ~3 min) ✨

Choose the method that fits your workflow!

---

**First time using Alioop?** Check out the Quick Start guide that appears on your Desktop after installation!"

# Create release with gh CLI
echo "$RELEASE_NOTES" > /tmp/release-notes.md

gh release create "v${VERSION}" \
    --repo "$REPO" \
    --title "$RELEASE_NAME" \
    --notes-file /tmp/release-notes.md \
    ${MACOS_INSTALLER:+--attach "$MACOS_INSTALLER"} \
    ${WINDOWS_INSTALLER:+--attach "$WINDOWS_INSTALLER"}

rm /tmp/release-notes.md

echo ""
echo "✅ SUCCESS! GitHub Release created!"
echo ""
echo "🔗 View release:"
echo "   https://github.com/${REPO}/releases/tag/v${VERSION}"
echo ""
echo "📥 Download links:"
if [ -f "$MACOS_INSTALLER" ]; then
    echo "   macOS: https://github.com/${REPO}/releases/download/v${VERSION}/AlioopSend-macOS-v${VERSION}.pkg"
fi
if [ -f "$WINDOWS_INSTALLER" ]; then
    echo "   Windows: https://github.com/${REPO}/releases/download/v${VERSION}/AlioopSend-Windows-v${VERSION}.exe"
fi
echo ""
echo "🎉 Next steps:"
echo "   1. Update download.html with real download URLs"
echo "   2. Test installers on clean systems"
echo "   3. Share with users!"
echo ""
