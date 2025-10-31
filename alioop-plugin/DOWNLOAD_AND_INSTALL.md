# Automated Plugin Builds

## 🎯 Quick Start

The plugin is now set up with **automated builds** via GitHub Actions!

### ✅ What Just Happened

1. Pushed build workflow to GitHub
2. GitHub Actions is now building your plugin for:
   - **macOS** (VST3 + AU + Standalone)
   - **Windows** (VST3 + Standalone)
   - **Linux** (VST3 + Standalone)

### 📥 How to Download

#### Option A: From GitHub Actions (Available Now)

1. Go to your repo: https://github.com/trentbecknell/audomte
2. Click **Actions** tab
3. Click the latest "Build Alioop Plugin" workflow run
4. Scroll down to **Artifacts** section
5. Download the package for your platform:
   - `AlioopSend-macOS` → For Mac users
   - `AlioopSend-Windows` → For Windows users
   - `AlioopSend-Linux` → For Linux users

The build should complete in **5-10 minutes**.

#### Option B: From Releases (After First Build)

Once the first build completes successfully:
1. Go to https://github.com/trentbecknell/audomte/releases
2. Download the latest release for your platform

---

## 🔧 Installation

### macOS

```bash
# Unzip the downloaded file
unzip AlioopSend-macOS-v1.0.0.zip

# Install VST3
cp -r VST3/AlioopSend.vst3 ~/Library/Audio/Plug-Ins/VST3/

# Install AU
cp -r AU/AlioopSend.component ~/Library/Audio/Plug-Ins/Components/

# Rescan in Reaper
# Reaper → Preferences → Plug-ins → VST → Re-scan
```

### Windows

```powershell
# Unzip the downloaded file
# Then copy VST3 to:
C:\Program Files\Common Files\VST3\AlioopSend.vst3

# Rescan in Reaper
# Options → Preferences → VST → Re-scan
```

### Linux

```bash
# Extract tarball
tar -xzf AlioopSend-Linux-v1.0.0.tar.gz

# Install VST3
mkdir -p ~/.vst3
cp -r VST3/AlioopSend.vst3 ~/.vst3/

# Rescan in Reaper
# Preferences → Plug-ins → VST → Re-scan
```

---

## 🎵 Testing in Reaper

1. Open Reaper
2. Create a new track (Cmd+T or Ctrl+T)
3. Click **FX** button on the track
4. Search for **"Alioop"** or **"Alioop Send"**
5. Double-click to insert plugin

### Expected Behavior:

- **Orange/Black/Cream UI** should appear
- **Record button** to capture audio
- **Client form** to enter project details
- **Send button** to upload to Alioop platform

---

## 🚀 Build Status

Check current build status:
- Actions Tab: https://github.com/trentbecknell/audomte/actions
- Latest Build: Look for "Build Alioop Plugin" workflow

**Build Time:** ~5-10 minutes per platform
**Artifacts Expire:** After 90 days (download and save locally)

---

## 🔄 Future Builds

Every time you push changes to `alioop-plugin/` directory:
- GitHub Actions automatically rebuilds all platforms
- New builds appear in Actions → Artifacts
- Releases are auto-created on `main` branch pushes

---

## 📝 Next Steps

1. **Wait 5-10 minutes** for first build to complete
2. **Download** your platform's package from Actions tab
3. **Install** following instructions above
4. **Test** in Reaper
5. **Report** any issues as GitHub Issues

---

## ⚠️ Troubleshooting

### Plugin doesn't show in Reaper

1. **Verify installation paths** (see above)
2. **Clear plugin cache:**
   - Mac: Delete `~/Library/Application Support/REAPER/reaper-vstplugins64.ini`
   - Windows: Delete `%APPDATA%\REAPER\reaper-vstplugins64.ini`
3. **Force rescan** in Reaper preferences
4. **Check Console/Event Viewer** for loading errors

### Build failed in GitHub Actions

1. Check Actions tab for error messages
2. Most common issue: JUCE download timeout (re-run workflow)
3. Open an Issue if persists

### Can't download from Actions

- Artifacts are only visible if you're logged into GitHub
- Artifacts expire after 90 days
- Use Releases for permanent downloads

---

## 🛠️ Manual Build (Alternative)

If you prefer to build locally, see:
- `alioop-plugin/BUILD_INSTRUCTIONS.md` for detailed steps
- Requires: JUCE, CMake, Xcode/Visual Studio

---

**Built with:** JUCE 7.0.12 | CMake 3.15+ | C++17
