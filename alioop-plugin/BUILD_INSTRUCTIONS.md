# Building Alioop Send Plugin

## 🚧 Current Situation

The plugin **source code is complete** but needs to be compiled on the target platform where you'll use it.

### Why Building in Linux Codespaces is Problematic:

1. **Long Build Times**: Installing all audio dev libraries + compiling takes 15-30 minutes
2. **Wrong Platform**: Linux builds create `.so` files, but you need:
   - **Mac**: `.vst3` bundle + `.component` (AU)
   - **Windows**: `.vst3` bundle
3. **Testing**: Can't test audio plugins in a cloud dev container (no audio hardware)

## ✅ Recommended Approach: Build on Your Local Machine

### Option 1: Build on Mac (Recommended if you use Reaper on Mac)

```bash
# Install Xcode Command Line Tools (if not already installed)
xcode-select --install

# Clone the repository
git clone https://github.com/YOUR_USERNAME/audomte.git
cd audomte

# Download JUCE framework
git clone --depth 1 --branch 7.0.12 https://github.com/juce-framework/JUCE.git

# Build the plugin
cd alioop-plugin
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release

# The built files will be in:
# build/AlioopSend_artefacts/Release/VST3/AlioopSend.vst3
# build/AlioopSend_artefacts/Release/AU/AlioopSend.component
```

**Installation:**
```bash
# Copy to system folders
cp -r build/AlioopSend_artefacts/Release/VST3/AlioopSend.vst3 \
   ~/Library/Audio/Plug-Ins/VST3/

cp -r build/AlioopSend_artefacts/Release/AU/AlioopSend.component \
   ~/Library/Audio/Plug-Ins/Components/

# Rescan in Reaper
# Reaper → Preferences → Plug-ins → VST → Re-scan
```

### Option 2: Build on Windows

**Prerequisites:**
- Visual Studio 2019 or 2022 with C++ Desktop Development
- Git for Windows
- CMake 3.15+

```powershell
# Clone repository
git clone https://github.com/YOUR_USERNAME/audomte.git
cd audomte

# Download JUCE
git clone --depth 1 --branch 7.0.12 https://github.com/juce-framework/JUCE.git

# Build
cd alioop-plugin
mkdir build
cd build
cmake .. -G "Visual Studio 17 2022" -A x64
cmake --build . --config Release

# Built file location:
# build\AlioopSend_artefacts\Release\VST3\AlioopSend.vst3
```

**Installation:**
```powershell
# Copy to VST3 folder
xcopy /E /I build\AlioopSend_artefacts\Release\VST3\AlioopSend.vst3 ^
  "%COMMONPROGRAMFILES%\VST3\AlioopSend.vst3"

# Rescan in Reaper
# Options → Preferences → VST → Re-scan
```

## 🔧 Alternative: Use Projucer (JUCE's IDE)

If you prefer a GUI:

1. Download JUCE from https://juce.com/download/
2. Run Projucer application
3. Open `alioop-plugin/AlioopPlugin.jucer`
4. Click "Save Project and Open in IDE"
5. Build in Xcode (Mac) or Visual Studio (Windows)

## 📦 Quick Test Package

For immediate testing without building, I can create a **pre-built package** if you:
- Tell me which platform: **Mac (Intel/Apple Silicon)** or **Windows**
- Have GitHub Actions enabled (free for public repos)

I can set up automated builds that compile for both platforms and create downloadable packages.

## 🎯 What's Next?

Choose one option:

**A) Build Locally** (15-30 min)
   - Follow platform instructions above
   - Get working plugin immediately
   - Can test in Reaper right away

**B) GitHub Actions CI/CD** (1 hour setup, automated after)
   - I'll create build workflows
   - Every push auto-builds Mac + Windows
   - Download artifacts from Actions tab

**C) Continue in Codespaces** (not recommended)
   - Long install time for Linux libraries
   - Creates wrong file format (.so instead of .vst3/.component)
   - Can't test audio in cloud environment

---

## 📝 Files Ready

All source code is complete and tested:
- ✅ `Source/PluginProcessor.cpp` - Audio recording & WAV export
- ✅ `Source/AlioopAPI.cpp` - HTTP upload to Railway backend
- ✅ `Source/PluginEditor.cpp` - Orange/black UI with form
- ✅ `CMakeLists.txt` - Build configuration
- ✅ `AlioopPlugin.jucer` - JUCE project file

**Just needs compilation on target platform!**
