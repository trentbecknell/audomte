#!/bin/bash
# Create Manual Installation ZIP Package
# This creates a simple .zip file with the plugin and installation instructions

set -e

VERSION="1.0.0"
PLUGIN_NAME="AlioopSend"

echo "📦 Creating Manual Installation Package..."
echo ""

# Create package directory
PKG_DIR="manual-install-package"
rm -rf "$PKG_DIR"
mkdir -p "$PKG_DIR/VST3"
mkdir -p "$PKG_DIR/AU"
mkdir -p "$PKG_DIR"

# Check if plugin is built
BUILD_DIR="Builds/MacOSX/build"

if [ ! -d "$BUILD_DIR" ]; then
    echo "⚠️  Plugin not built yet. Creating package structure for manual build..."
    echo ""
    echo "To build the plugin first:"
    echo "  1. Open AlioopPlugin.jucer in Projucer"
    echo "  2. Click 'Save and Open in IDE'"
    echo "  3. Build in Xcode (Release configuration)"
    echo "  4. Run this script again"
    echo ""
fi

# Create installation instructions
cat > "$PKG_DIR/INSTALL.txt" << 'EOF'
╔══════════════════════════════════════════════════════════════════╗
║                  ALIOOP SEND - MANUAL INSTALLATION               ║
╚══════════════════════════════════════════════════════════════════╝

Welcome! This is a simple drag-and-drop installation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 WHAT'S INCLUDED:

• VST3/AlioopSend.vst3    - VST3 plugin (for most DAWs)
• AU/AlioopSend.component - AU plugin (for Logic Pro, GarageBand)
• This installation guide

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🍎 macOS INSTALLATION:

OPTION 1: Drag & Drop (Easiest)
-------------------------------
1. Open this folder in Finder
2. Open a NEW Finder window
3. Go → Go to Folder... (Cmd+Shift+G)
4. Type: /Library/Audio/Plug-Ins/
5. Drag "AlioopSend.vst3" to the VST3 folder
6. Drag "AlioopSend.component" to the Components folder
7. Done! Close windows and open your DAW

OPTION 2: Terminal (If you prefer)
-----------------------------------
Open Terminal and run:

sudo cp -R VST3/AlioopSend.vst3 /Library/Audio/Plug-Ins/VST3/
sudo cp -R AU/AlioopSend.component /Library/Audio/Plug-Ins/Components/

Enter your password when prompted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🪟 WINDOWS INSTALLATION:

1. Open this folder
2. Copy "AlioopSend.vst3" folder
3. Go to: C:\Program Files\Common Files\VST3\
   (You may need administrator permission)
4. Paste the folder there
5. Done! Open your DAW

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎹 REAPER SETUP:

After copying the files:

1. Open Reaper
2. Options → Preferences (or Cmd+, on Mac)
3. Click "Plug-ins" → "VST"
4. Click "Re-scan"
5. Wait for scan to complete
6. Click "OK"
7. Close Preferences

Finding the Plugin:
-------------------
1. Select your Master track (or any track)
2. Click "FX" button
3. Type "Alioop" in the search box
4. Double-click "VST3: Alioop Send (Alioop)"
5. Plugin opens! 🎉

Alternative Method:
------------------
1. Right-click track FX button
2. Browse → VST3 → Alioop → AlioopSend
3. Click to insert

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎛️ OTHER DAWs:

Pro Tools:
  Insert → Other → VST3 → Alioop Send

Logic Pro:
  Insert → Audio FX → Audio Units → Alioop → Alioop Send

Ableton Live:
  Audio Effects → VST3 → Alioop → Alioop Send

Studio One:
  Effects → VST3 → Alioop → Alioop Send

Cubase/Nuendo:
  Inserts → VST3 → Alioop → Alioop Send

FL Studio:
  Mixer → Insert → More → VST3 → Alioop Send

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 QUICK START:

1. Insert plugin on Master track
2. Click "Start Recording" button
3. Play your session from start to finish
4. Click "Stop Recording"
5. Fill in client details:
   • Client Name
   • Email
   • Phone (optional)
   • Price
   • Service Name
6. Click "Send Delivery"
7. Done! Client gets email instantly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ TROUBLESHOOTING:

Plugin doesn't appear in DAW?
• Make sure you copied to the correct folder
• Rescan plugins in your DAW settings
• Restart your DAW completely
• Check both VST3 and AU (Mac) folders

Reaper can't find it?
• Check VST paths: Preferences → Plug-ins → VST
• Make sure /Library/Audio/Plug-Ins/VST3 is in the list
• Click "Re-scan" and wait for completion
• Try clearing cache first: "Clear cache/re-scan"

Permission denied (Mac)?
• Use "sudo" in terminal commands
• Or drag to folders with administrator account

Mac says "cannot be opened"?
• Right-click plugin → Open
• Or: System Settings → Security → Allow

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 MORE HELP:

• Documentation: https://github.com/trentbecknell/audomte/tree/main/alioop-plugin
• Issues: https://github.com/trentbecknell/audomte/issues
• Web App: https://web-production-5748a.up.railway.app/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Enjoy using Alioop! 🎵

Built with ❤️ for audio professionals
EOF

# Create README for the package
cat > "$PKG_DIR/README.md" << 'EOF'
# Alioop Send - Manual Installation Package

This is a simple drag-and-drop installation package for the Alioop Send plugin.

## Quick Install

**macOS:**
1. Drag `AlioopSend.vst3` to `/Library/Audio/Plug-Ins/VST3/`
2. Drag `AlioopSend.component` to `/Library/Audio/Plug-Ins/Components/`
3. Rescan plugins in your DAW

**Windows:**
1. Copy `AlioopSend.vst3` to `C:\Program Files\Common Files\VST3\`
2. Rescan plugins in your DAW

See `INSTALL.txt` for detailed instructions.

## For Reaper Users

After copying files:
1. Options → Preferences → Plug-ins → VST
2. Click "Re-scan"
3. Insert on track: FX → VST3 → Alioop Send

## What's This Plugin?

Alioop Send lets you deliver audio files to clients directly from your DAW:
- Record audio in your session
- Fill client details in plugin
- Click Send
- Client gets email with download link

No file exports, no browser, all in your DAW!

## Need Help?

- Full docs: https://github.com/trentbecknell/audomte/tree/main/alioop-plugin
- Report issues: https://github.com/trentbecknell/audomte/issues
EOF

echo "✅ Package structure created in: $PKG_DIR/"
echo ""
echo "📋 Files to include:"
echo "   • INSTALL.txt (detailed instructions)"
echo "   • README.md (quick reference)"
echo "   • VST3/AlioopSend.vst3 (plugin file)"
echo "   • AU/AlioopSend.component (Mac only)"
echo ""
echo "🔨 Next steps:"
echo ""
echo "OPTION 1 - Build with JUCE/Xcode:"
echo "  1. Open AlioopPlugin.jucer in Projucer"
echo "  2. Save and Open in IDE (Xcode)"
echo "  3. Build → Release configuration"
echo "  4. Copy built files to $PKG_DIR/VST3/ and $PKG_DIR/AU/"
echo "  5. Run: zip -r AlioopSend-Manual-v${VERSION}.zip $PKG_DIR/"
echo "  6. Distribute the .zip file!"
echo ""
echo "OPTION 2 - Create placeholder for testing:"
echo "  The folder structure is ready."
echo "  Add your built plugin files and zip it up."
echo ""
