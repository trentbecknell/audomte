#!/bin/bash
# Alioop Plugin - macOS One-Click Installer
# This script builds a .pkg installer that auto-installs the plugin with zero user interaction

set -e

PLUGIN_NAME="AlioopSend"
VERSION="1.0.0"
BUILD_DIR="$(pwd)/../Builds/MacOSX/build/Release"
PKG_ROOT="$(pwd)/pkg-root"
SCRIPTS_DIR="$(pwd)/pkg-scripts"
OUTPUT_DIR="$(pwd)/output"

echo "🎵 Building Alioop Plugin Installer for macOS..."

# Clean previous builds
rm -rf "$PKG_ROOT" "$SCRIPTS_DIR" "$OUTPUT_DIR"
mkdir -p "$PKG_ROOT" "$SCRIPTS_DIR" "$OUTPUT_DIR"

# Check if plugin is built
if [ ! -d "$BUILD_DIR/${PLUGIN_NAME}.vst3" ] && [ ! -d "$BUILD_DIR/${PLUGIN_NAME}.component" ]; then
    echo "❌ Plugin not built yet! Please build the plugin first."
    echo "   Run: cd .. && ./build.sh"
    exit 1
fi

# Create directory structure that mirrors installation paths
mkdir -p "$PKG_ROOT/Library/Audio/Plug-Ins/VST3"
mkdir -p "$PKG_ROOT/Library/Audio/Plug-Ins/Components"

# Copy plugins to package root
if [ -d "$BUILD_DIR/${PLUGIN_NAME}.vst3" ]; then
    echo "📦 Packaging VST3..."
    cp -R "$BUILD_DIR/${PLUGIN_NAME}.vst3" "$PKG_ROOT/Library/Audio/Plug-Ins/VST3/"
fi

if [ -d "$BUILD_DIR/${PLUGIN_NAME}.component" ]; then
    echo "📦 Packaging AU..."
    cp -R "$BUILD_DIR/${PLUGIN_NAME}.component" "$PKG_ROOT/Library/Audio/Plug-Ins/Components/"
fi

# Create postinstall script to trigger DAW rescans
cat > "$SCRIPTS_DIR/postinstall" << 'EOF'
#!/bin/bash
# Auto-trigger DAW plugin rescans after installation

echo "✅ Alioop plugin installed successfully!"
echo ""
echo "📍 Installed to:"
echo "   VST3: /Library/Audio/Plug-Ins/VST3/AlioopSend.vst3"
echo "   AU:   /Library/Audio/Plug-Ins/Components/AlioopSend.component"
echo ""
echo "🎹 Next steps:"
echo "   1. Open your DAW (Pro Tools, Logic, Ableton, etc.)"
echo "   2. Rescan plugins (or restart your DAW)"
echo "   3. Insert 'Alioop Send' on your master track"
echo "   4. Record and send deliveries instantly!"
echo ""

# Try to detect and notify about installed DAWs
if [ -d "/Applications/Pro Tools.app" ]; then
    echo "✓ Detected: Pro Tools"
fi
if [ -d "/Applications/Logic Pro X.app" ] || [ -d "/Applications/Logic Pro.app" ]; then
    echo "✓ Detected: Logic Pro"
fi
if [ -d "/Applications/Ableton Live"*.app ]; then
    echo "✓ Detected: Ableton Live"
fi
if [ -d "/Applications/Studio One"*.app ]; then
    echo "✓ Detected: Studio One"
fi

# Create desktop shortcut to quick start guide
DESKTOP_PATH="$HOME/Desktop"
if [ -d "$DESKTOP_PATH" ]; then
    cat > "$DESKTOP_PATH/Alioop Plugin Quick Start.txt" << 'GUIDE'
🎵 ALIOOP PLUGIN - QUICK START GUIDE

✅ Plugin installed successfully!

📍 WHERE TO FIND IT:
In your DAW, look for:
- "Alioop Send" in plugin list
- Category: Audio Effect / Other

🚀 QUICK WORKFLOW:

1. INSERT PLUGIN
   - Insert on Master track
   - Or any track you want to send

2. RECORD AUDIO
   - Click "Start Recording" in plugin
   - Play your session
   - Click "Stop Recording"

3. FILL CLIENT INFO
   - Client Name: John Smith
   - Email: john@example.com
   - Phone: +1 555-0100
   - Price: $50
   - Service: Mixing

4. SEND!
   - Click "Send Delivery"
   - Done! Client gets email instantly

⏱️ Total time: ~3 minutes

📚 FULL DOCS:
https://github.com/trentbecknell/audomte/tree/main/alioop-plugin

💡 TIP:
Plugin remembers your last client info - perfect for repeat customers!

GUIDE
    echo "📄 Created Quick Start guide on your Desktop"
fi

exit 0
EOF

chmod +x "$SCRIPTS_DIR/postinstall"

# Build the package
echo "🔨 Building installer package..."
pkgbuild \
    --root "$PKG_ROOT" \
    --scripts "$SCRIPTS_DIR" \
    --identifier "com.alioop.send.plugin" \
    --version "$VERSION" \
    --install-location "/" \
    "$OUTPUT_DIR/${PLUGIN_NAME}-Installer-Unsigned.pkg"

# Create product archive with welcome/readme
echo "📝 Creating distribution package..."

# Create welcome text
cat > "$OUTPUT_DIR/welcome.txt" << 'WELCOME'
Welcome to Alioop Send!

This installer will install the Alioop plugin to your system.

The plugin will be installed to:
• /Library/Audio/Plug-Ins/VST3 (for most DAWs)
• /Library/Audio/Plug-Ins/Components (for Logic Pro)

After installation, simply rescan plugins in your DAW and you're ready to go!

No configuration needed - just insert the plugin and start sending deliveries.
WELCOME

# Create readme
cat > "$OUTPUT_DIR/readme.txt" << 'README'
ALIOOP SEND PLUGIN

A professional audio delivery plugin for DAWs.

SUPPORTED FORMATS:
✓ VST3 (Pro Tools, Ableton, Studio One, Reaper, etc.)
✓ AU (Logic Pro, GarageBand)

WORKFLOW:
1. Insert plugin on Master track
2. Record your session (plugin captures audio)
3. Fill in client details
4. Click Send - done!

SUPPORT:
GitHub: https://github.com/trentbecknell/audomte
Docs: https://github.com/trentbecknell/audomte/tree/main/alioop-plugin

REQUIREMENTS:
• macOS 10.13 or later
• Any VST3 or AU compatible DAW
README

# Build distribution package with welcome/readme screens
productbuild \
    --package "$OUTPUT_DIR/${PLUGIN_NAME}-Installer-Unsigned.pkg" \
    --resources "$OUTPUT_DIR" \
    "$OUTPUT_DIR/${PLUGIN_NAME}-macOS-v${VERSION}.pkg"

# Clean up intermediate files
rm "$OUTPUT_DIR/${PLUGIN_NAME}-Installer-Unsigned.pkg"
rm "$OUTPUT_DIR/welcome.txt"
rm "$OUTPUT_DIR/readme.txt"

echo ""
echo "✅ SUCCESS! Installer created:"
echo "   📦 $OUTPUT_DIR/${PLUGIN_NAME}-macOS-v${VERSION}.pkg"
echo ""
echo "🎯 ONE-CLICK INSTALLATION:"
echo "   Users just double-click the .pkg file"
echo "   Plugin auto-installs to system folders"
echo "   Quick Start guide appears on Desktop"
echo ""
echo "📤 NEXT STEPS:"
echo "   1. Test the installer on a clean Mac"
echo "   2. (Optional) Code sign for macOS Gatekeeper"
echo "   3. Upload to GitHub Releases"
echo "   4. Share download link with users!"
echo ""
echo "🔒 CODE SIGNING (optional but recommended):"
echo "   productsign --sign 'Developer ID Installer: Your Name' \\"
echo "     ${PLUGIN_NAME}-macOS-v${VERSION}.pkg \\"
echo "     ${PLUGIN_NAME}-macOS-v${VERSION}-Signed.pkg"
echo ""
