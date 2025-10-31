# Building Alioop Plugin

Complete guide for building the Alioop Send plugin from source.

---

## Prerequisites

### All Platforms

1. **JUCE Framework 7.0+**
   ```bash
   # Download from https://juce.com/get-juce/download
   # Or clone from GitHub
   git clone https://github.com/juce-framework/JUCE.git
   cd JUCE
   git checkout 7.0.0
   ```

2. **CMake 3.15+** (optional, for command-line builds)
   ```bash
   # macOS
   brew install cmake
   
   # Ubuntu/Debian
   sudo apt install cmake
   
   # Windows
   # Download from https://cmake.org/download/
   ```

### macOS

- **Xcode 13+**
  ```bash
  xcode-select --install
  ```

- **Xcode Command Line Tools**

### Windows

- **Visual Studio 2022** (Community Edition OK)
  - Workload: "Desktop development with C++"
  - Windows 10 SDK

### Linux

- **Build essentials:**
  ```bash
  sudo apt update
  sudo apt install build-essential pkg-config
  sudo apt install libasound2-dev libfreetype6-dev libx11-dev libxinerama-dev libxrandr-dev libxcursor-dev libwebkit2gtk-4.0-dev libglu1-mesa-dev mesa-common-dev
  ```

---

## Method 1: Using Projucer (Recommended)

### Step 1: Install Projucer

```bash
# macOS
# Download Projucer from JUCE website or:
open /Applications/JUCE/Projucer.app

# Windows
# Run Projucer.exe from JUCE installation

# Linux
cd ~/JUCE/extras/Projucer/Builds/LinuxMakefile
make
./build/Projucer
```

### Step 2: Configure JUCE Modules

1. Open Projucer
2. File → Global Paths
3. Set "Path to JUCE" to your JUCE folder
4. Set "VST3 SDK" (optional, for VST3 builds)
5. Set "AAX SDK" (optional, requires Avid developer account)

### Step 3: Open Project

1. File → Open
2. Navigate to `alioop-plugin/AlioopPlugin.jucer`
3. Click Open

### Step 4: Generate IDE Files

1. Click "Save Project" (Cmd+S / Ctrl+S)
2. Projucer generates platform-specific build files:
   - macOS: `Builds/MacOSX/AlioopPlugin.xcodeproj`
   - Windows: `Builds/VisualStudio2022/AlioopPlugin.sln`
   - Linux: `Builds/LinuxMakefile/Makefile`

### Step 5: Build

**macOS (Xcode):**
```bash
cd Builds/MacOSX
xcodebuild -configuration Release
```

Or open `.xcodeproj` in Xcode and build (Cmd+B)

**Windows (Visual Studio):**
```cmd
cd Builds\VisualStudio2022
msbuild AlioopPlugin.sln /p:Configuration=Release
```

Or open `.sln` in Visual Studio and build (F7)

**Linux (Make):**
```bash
cd Builds/LinuxMakefile
make CONFIG=Release
```

### Step 6: Locate Built Plugins

**macOS:**
```
Builds/MacOSX/build/Release/
├── AlioopSend.vst3
├── AlioopSend.component  (AU)
└── AlioopSend.aaxplugin  (AAX, if SDK configured)
```

**Windows:**
```
Builds\VisualStudio2022\x64\Release\VST3\
├── AlioopSend.vst3
└── AlioopSend.aaxplugin  (AAX, if SDK configured)
```

**Linux:**
```
Builds/LinuxMakefile/build/
└── AlioopSend.vst3
```

---

## Method 2: Using CMake

### Step 1: Create CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.15)

project(AlioopPlugin VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)

# Add JUCE
add_subdirectory(path/to/JUCE JUCE)

# Create plugin target
juce_add_plugin(AlioopSend
    COMPANY_NAME "Alioop"
    IS_SYNTH FALSE
    NEEDS_MIDI_INPUT FALSE
    NEEDS_MIDI_OUTPUT FALSE
    IS_MIDI_EFFECT FALSE
    EDITOR_WANTS_KEYBOARD_FOCUS FALSE
    COPY_PLUGIN_AFTER_BUILD TRUE
    PLUGIN_MANUFACTURER_CODE Alop
    PLUGIN_CODE Alsd
    FORMATS VST3 AU Standalone
    PRODUCT_NAME "Alioop Send")

# Source files
target_sources(AlioopSend PRIVATE
    Source/PluginProcessor.cpp
    Source/PluginEditor.cpp
    Source/AlioopAPI.cpp)

# JUCE modules
target_link_libraries(AlioopSend PRIVATE
    juce::juce_audio_basics
    juce::juce_audio_devices
    juce::juce_audio_formats
    juce::juce_audio_plugin_client
    juce::juce_audio_processors
    juce::juce_audio_utils
    juce::juce_core
    juce::juce_data_structures
    juce::juce_events
    juce::juce_graphics
    juce::juce_gui_basics
    juce::juce_gui_extra)

# Compiler definitions
target_compile_definitions(AlioopSend PUBLIC
    JUCE_WEB_BROWSER=0
    JUCE_USE_CURL=1
    JUCE_VST3_CAN_REPLACE_VST2=0)
```

### Step 2: Configure

```bash
mkdir build
cd build
cmake .. -DJUCE_PATH=/path/to/JUCE
```

### Step 3: Build

```bash
# All formats
cmake --build . --config Release

# VST3 only
cmake -DJUCE_BUILD_VST3=ON -DJUCE_BUILD_AU=OFF ..
cmake --build . --config Release

# AU only (macOS)
cmake -DJUCE_BUILD_VST3=OFF -DJUCE_BUILD_AU=ON ..
cmake --build . --config Release
```

---

## Installing Built Plugins

### macOS

**VST3:**
```bash
cp -r Builds/MacOSX/build/Release/AlioopSend.vst3 ~/Library/Audio/Plug-Ins/VST3/
```

**AU:**
```bash
cp -r Builds/MacOSX/build/Release/AlioopSend.component ~/Library/Audio/Plug-Ins/Components/
```

**AAX:**
```bash
sudo cp -r Builds/MacOSX/build/Release/AlioopSend.aaxplugin /Library/Application\ Support/Avid/Audio/Plug-Ins/
```

**Verify installation:**
```bash
ls ~/Library/Audio/Plug-Ins/VST3/AlioopSend.vst3
ls ~/Library/Audio/Plug-Ins/Components/AlioopSend.component
```

### Windows

**VST3:**
```cmd
xcopy /E /I "Builds\VisualStudio2022\x64\Release\VST3\AlioopSend.vst3" "%COMMONPROGRAMFILES%\VST3\AlioopSend.vst3"
```

**AAX:**
```cmd
xcopy /E /I "Builds\VisualStudio2022\x64\Release\AAX\AlioopSend.aaxplugin" "%COMMONPROGRAMFILES%\Avid\Audio\Plug-Ins\AlioopSend.aaxplugin"
```

### Linux

**VST3:**
```bash
mkdir -p ~/.vst3
cp -r Builds/LinuxMakefile/build/AlioopSend.vst3 ~/.vst3/
```

---

## Building for Distribution

### Code Signing (macOS)

**Required for Gatekeeper:**

1. **Get Developer ID:**
   - Enroll in Apple Developer Program
   - Request Developer ID Application certificate

2. **Sign plugin:**
   ```bash
   codesign --force --sign "Developer ID Application: Your Name" \
            --timestamp \
            AlioopSend.vst3
   
   codesign --force --sign "Developer ID Application: Your Name" \
            --timestamp \
            AlioopSend.component
   ```

3. **Notarize:**
   ```bash
   # Create archive
   ditto -c -k --keepParent AlioopSend.vst3 AlioopSend-vst3.zip
   
   # Submit for notarization
   xcrun notarytool submit AlioopSend-vst3.zip \
     --apple-id your@email.com \
     --team-id TEAMID \
     --wait
   
   # Staple ticket
   xcrun stapler staple AlioopSend.vst3
   ```

### Code Signing (Windows)

**Optional but recommended:**

1. **Get code signing certificate**
2. **Sign with signtool:**
   ```cmd
   signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com AlioopSend.vst3
   ```

---

## Troubleshooting

### JUCE modules not found

**Fix paths in Projucer:**
1. Open AlioopPlugin.jucer
2. File → Global Paths
3. Set correct "Path to JUCE"
4. Save and regenerate

### Missing dependencies (Linux)

```bash
# Install all JUCE dependencies
sudo apt install $(cat <<EOF
libasound2-dev
libfreetype6-dev
libx11-dev
libxinerama-dev
libxrandr-dev
libxcursor-dev
libxcomposite-dev
libwebkit2gtk-4.0-dev
libglu1-mesa-dev
mesa-common-dev
libcurl4-openssl-dev
EOF
)
```

### Build errors with curl

**Add to target:**
```cmake
target_compile_definitions(AlioopSend PRIVATE JUCE_USE_CURL=1)
target_link_libraries(AlioopSend PRIVATE curl)
```

### AAX build fails

**AAX SDK required:**
1. Sign up at https://www.avid.com/alliance-partner-program
2. Download AAX SDK
3. Set path in Projucer: Modules → AAX SDK Folder

---

## Build Optimization

### Release builds

**Optimization flags:**
```cmake
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
set(CMAKE_BUILD_TYPE Release)
```

**Strip symbols (smaller file):**
```bash
# macOS
strip -x AlioopSend.vst3/Contents/MacOS/AlioopSend

# Linux
strip --strip-unneeded AlioopSend.vst3/Contents/x86_64-linux/AlioopSend.so
```

### Debug builds

```bash
cmake --build . --config Debug
```

**Debug symbols:**
```cmake
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
```

---

## Continuous Integration

### GitHub Actions Example

```yaml
name: Build Plugin

on: [push, pull_request]

jobs:
  build:
    strategy:
      matrix:
        os: [macos-latest, windows-latest, ubuntu-latest]
    
    runs-on: ${{ matrix.os }}
    
    steps:
    - uses: actions/checkout@v2
      with:
        submodules: recursive
    
    - name: Install JUCE
      run: |
        git clone https://github.com/juce-framework/JUCE.git
        cd JUCE && git checkout 7.0.0
    
    - name: Build
      run: |
        cd alioop-plugin
        cmake -B build -DJUCE_PATH=../JUCE
        cmake --build build --config Release
    
    - name: Upload Artifacts
      uses: actions/upload-artifact@v2
      with:
        name: plugin-${{ matrix.os }}
        path: build/*/Release/
```

---

## Resources

- **JUCE Documentation:** https://docs.juce.com/
- **JUCE Forum:** https://forum.juce.com/
- **JUCE GitHub:** https://github.com/juce-framework/JUCE
- **Plugin Development Guide:** https://docs.juce.com/master/tutorial_create_projucer_basic_plugin.html

---

**Need help? Open an issue on GitHub!**
