#!/bin/bash
# Alioop Plugin - Complete Build Script
# Builds plugin and creates installers for distribution

set -e

echo "🎵 Alioop Plugin - Complete Build & Package"
echo "==========================================="
echo ""

# Detect platform
if [[ "$OSTYPE" == "darwin"* ]]; then
    PLATFORM="macos"
    echo "Platform: macOS"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    PLATFORM="windows"
    echo "Platform: Windows"
else
    PLATFORM="linux"
    echo "Platform: Linux"
fi

echo ""

# Step 1: Build the plugin
echo "Step 1: Building plugin..."
echo "-------------------------"

if [ "$PLATFORM" == "macos" ]; then
    # macOS build with CMake
    if ! command -v cmake &> /dev/null; then
        echo "❌ CMake not found! Install with: brew install cmake"
        exit 1
    fi
    
    mkdir -p Builds/MacOSX/build
    cd Builds/MacOSX/build
    
    cmake ../../.. -DCMAKE_BUILD_TYPE=Release
    cmake --build . --config Release
    
    cd ../../..
    
    echo "✅ Plugin built successfully!"
    echo "   VST3: Builds/MacOSX/build/AlioopSend_artefacts/Release/VST3/AlioopSend.vst3"
    echo "   AU:   Builds/MacOSX/build/AlioopSend_artefacts/Release/AU/AlioopSend.component"
    
elif [ "$PLATFORM" == "windows" ]; then
    # Windows build with CMake
    if ! command -v cmake &> /dev/null; then
        echo "❌ CMake not found! Install from: https://cmake.org/download/"
        exit 1
    fi
    
    mkdir -p Builds/VisualStudio2022
    cd Builds/VisualStudio2022
    
    cmake ../.. -G "Visual Studio 17 2022" -A x64
    cmake --build . --config Release
    
    cd ../..
    
    echo "✅ Plugin built successfully!"
    echo "   VST3: Builds/VisualStudio2022/Release/VST3/AlioopSend.vst3"
    
else
    # Linux build
    mkdir -p Builds/Linux/build
    cd Builds/Linux/build
    
    cmake ../../.. -DCMAKE_BUILD_TYPE=Release
    cmake --build . --config Release
    
    cd ../../..
    
    echo "✅ Plugin built successfully!"
    echo "   VST3: Builds/Linux/build/AlioopSend_artefacts/Release/VST3/AlioopSend.vst3"
fi

echo ""

# Step 2: Create installer
echo "Step 2: Creating installer..."
echo "----------------------------"

cd installers

if [ "$PLATFORM" == "macos" ]; then
    chmod +x macos-installer.sh
    ./macos-installer.sh
    
    echo ""
    echo "✅ macOS installer created!"
    echo "   📦 installers/output/AlioopSend-macOS-v1.0.0.pkg"
    
elif [ "$PLATFORM" == "windows" ]; then
    cmd //c build-windows-installer.bat
    
    echo ""
    echo "✅ Windows installer created!"
    echo "   📦 installers/output/AlioopSend-Windows-v1.0.0.exe"
    
else
    echo "ℹ️  Linux installer not implemented yet."
    echo "   Distribute as .tar.gz with VST3 folder"
fi

cd ..

echo ""
echo "=========================================="
echo "✅ BUILD COMPLETE!"
echo "=========================================="
echo ""
echo "📤 Next steps:"
echo "   1. Test the installer on a clean machine"
echo "   2. (Optional) Code sign the installer"
echo "   3. Upload to GitHub Releases"
echo "   4. Share download link!"
echo ""
echo "🔗 Quick test:"
if [ "$PLATFORM" == "macos" ]; then
    echo "   open installers/output/AlioopSend-macOS-v1.0.0.pkg"
elif [ "$PLATFORM" == "windows" ]; then
    echo "   start installers/output/AlioopSend-Windows-v1.0.0.exe"
fi
echo ""
