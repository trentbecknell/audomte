# Alioop Send - VST/AU/AAX Plugin

**Full in-DAW integration for instant audio delivery!**

Send client deliveries without leaving your DAW. Record, fill form, and send - all from one plugin window.

---

## 🎹 Features

- **In-DAW Recording** - Capture audio directly from your DAW's output
- **Built-in Form** - Client info right in the plugin
- **Branded UI** - Orange/black/cream Alioop styling
- **Auto-Export** - Exports WAV and uploads automatically
- **Session Persistence** - Remembers last client info
- **Multi-Format** - VST3, AU, AAX support
- **Cross-Platform** - macOS, Windows, Linux

---

## 📦 Installation

### Download Pre-built Plugin (Coming Soon)

**macOS:**
- VST3: `~/Library/Audio/Plug-Ins/VST3/`
- AU: `~/Library/Audio/Plug-Ins/Components/`
- AAX: `/Library/Application Support/Avid/Audio/Plug-Ins/`

**Windows:**
- VST3: `C:\Program Files\Common Files\VST3\`
- AAX: `C:\Program Files\Common Files\Avid\Audio\Plug-Ins\`

**Linux:**
- VST3: `~/.vst3/`

### Build from Source

**Requirements:**
- JUCE Framework 7.0+
- C++17 compiler
- Xcode (macOS) / Visual Studio 2022 (Windows) / GCC (Linux)

**Steps:**

1. **Install JUCE:**
   ```bash
   # Download from https://juce.com/
   # Or use package manager
   brew install juce  # macOS
   ```

2. **Clone Repository:**
   ```bash
   git clone https://github.com/trentbecknell/audomte.git
   cd audomte/alioop-plugin
   ```

3. **Open in Projucer:**
   ```bash
   # Open AlioopPlugin.jucer in Projucer
   # Configure JUCE modules path
   # Save project to generate IDE files
   ```

4. **Build:**
   
   **macOS (Xcode):**
   ```bash
   cd Builds/MacOSX
   xcodebuild -configuration Release
   ```
   
   **Windows (Visual Studio):**
   ```cmd
   cd Builds\VisualStudio2022
   msbuild AlioopPlugin.sln /p:Configuration=Release
   ```
   
   **Linux:**
   ```bash
   cd Builds/LinuxMakefile
   make CONFIG=Release
   ```

5. **Install Plugin:**
   ```bash
   # Copy built plugin to appropriate folder
   cp build/Release/AlioopSend.vst3 ~/Library/Audio/Plug-Ins/VST3/  # macOS VST3
   cp build/Release/AlioopSend.component ~/Library/Audio/Plug-Ins/Components/  # macOS AU
   ```

---

## 🚀 Usage

### Pro Tools

1. **Insert Plugin:**
   - Create new track or use existing
   - Go to Inserts → Plug-in → Other → Alioop Send

2. **Record Audio:**
   - Click "Start Recording" in plugin
   - Play/bounce your session
   - Click "Stop Recording"

3. **Send Delivery:**
   - Fill client info (name, email, phone, price, service)
   - Click "Send Delivery"
   - Client receives email instantly!

### Logic Pro

1. **Insert Plugin:**
   - Select track
   - Insert → Audio FX → Other → Alioop Send
   - Or use on Master/Stereo Out

2. **Capture Mix:**
   - Start recording in plugin
   - Play session or bounce in place
   - Stop when done

3. **Send:**
   - Complete form
   - Send → Done!

### Ableton Live

1. **Add to Master:**
   - Drag plugin to Master track
   - Or any audio track

2. **Record:**
   - Hit record in plugin
   - Play session
   - Stop recording

3. **Deliver:**
   - Fill form → Send

### Studio One

1. **Insert on Master Bus:**
   - Effects → Other → Alioop Send
   - Or on individual tracks

2. **Capture:**
   - Record button in plugin
   - Play/export
   - Stop

3. **Submit:**
   - Enter details → Send

---

## 🎯 Workflows

### Workflow 1: Quick Delivery (Fastest!)

```
1. Insert plugin on Master
2. Click "Start Recording"
3. Play session from start
4. Click "Stop Recording"  
5. Fill form (1 minute)
6. Click "Send Delivery"
→ Done in 3-5 minutes!
```

### Workflow 2: Selective Recording

```
1. Insert on specific track
2. Solo track(s) you want to send
3. Record in plugin
4. Fill form
5. Send
→ Send stems or individual tracks
```

### Workflow 3: Multiple Takes

```
1. Record first take
2. Stop recording
3. Review
4. If not satisfied, click "Start Recording" again
5. Record new take (overwrites previous)
6. Send when happy
→ Quality control before sending
```

---

## ⚙️ Plugin Settings

### Persistence

Plugin remembers:
- ✅ Last client name
- ✅ Last client email
- ✅ Last delivery price
- ✅ Window position/size

Speeds up repeat deliveries to same client!

### Audio Format

Exports as:
- **Format:** WAV
- **Bit Depth:** 24-bit
- **Sample Rate:** Matches session
- **Channels:** Stereo (or mono if single channel)

### File Size

Maximum recording: **5 minutes**
- @ 44.1kHz, 24-bit, stereo: ~75MB
- @ 48kHz, 24-bit, stereo: ~82MB
- @ 96kHz, 24-bit, stereo: ~164MB

---

## 🔧 Troubleshooting

### Plugin doesn't appear in DAW?

**Rescan plugins:**
- Pro Tools: Setup → Plug-ins → Update Plug-in Settings
- Logic Pro: Preferences → Plug-in Manager → Reset & Rescan
- Ableton: Preferences → Plug-ins → Rescan
- Studio One: Options → Locations → VST Plug-ins → Reset & Rescan

**Check installation path:**
```bash
# macOS
ls ~/Library/Audio/Plug-Ins/VST3/
ls ~/Library/Audio/Plug-Ins/Components/

# Windows
dir "C:\Program Files\Common Files\VST3\"
```

### Recording doesn't capture audio?

**Check routing:**
- Ensure plugin is on track receiving audio
- Verify track is not muted
- Check input monitoring is enabled

**Verify plugin position:**
- Place after all effects (last in chain)
- Or on Master/Stereo Out bus

### Upload fails?

**Internet connection:**
- Verify connection active
- Check firewall not blocking plugin

**File size:**
- Recordings > 5 minutes fail
- Try shorter recording

**API connection:**
- Test at: https://web-production-5748a.up.railway.app
- Report issues on GitHub

### Form fields not saving?

**Session state:**
- DAW must save plugin state
- Save session after entering info
- Reopen session to verify persistence

---

## 📊 Comparison with Other Integration Methods

| Feature | Plugin | Desktop App | Export Scripts | URL Handler |
|---------|--------|-------------|----------------|-------------|
| **No file export needed** | ✅ | ❌ | ❌ | ❌ |
| **In-DAW workflow** | ✅ | ❌ | ❌ | ❌ |
| **Auto-capture audio** | ✅ | ❌ | ❌ | ❌ |
| **One-window solution** | ✅ | ❌ | ❌ | ❌ |
| **Session persistence** | ✅ | ✅ | ❌ | ❌ |
| **Installation required** | ✅ | ✅ | ✅ | ❌ |
| **Speed** | ⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡ | ⚡ |

**Best for:**
- Plugin: Engineers who hate leaving their DAW
- Desktop App: Auto-detection without thinking
- Export Scripts: Quick keyboard shortcuts
- URL Handler: No installation, universal

---

## 🔮 Advanced Features

### Automation (Future)

Map plugin to MIDI controller:
```
Button 1: Start/Stop Recording
Button 2: Send Delivery
Knob 1: Price adjustment
```

### Batch Mode (Future)

Record multiple deliveries:
```
1. Record Client A
2. Switch to Client B form
3. Record Client B
4. Send both
```

### Templates (Future)

Save client presets:
```
Preset 1: "Regular Client A - $50 mixing"
Preset 2: "Regular Client B - $100 mastering"
```

---

## 🛠️ Development

### Project Structure

```
alioop-plugin/
├── AlioopPlugin.jucer     # JUCE project file
├── Source/
│   ├── PluginProcessor.h  # Audio processing
│   ├── PluginProcessor.cpp
│   ├── PluginEditor.h     # UI
│   ├── PluginEditor.cpp
│   ├── AlioopAPI.h        # Backend communication
│   └── AlioopAPI.cpp
├── Builds/                # Generated by Projucer
│   ├── MacOSX/           # Xcode project
│   ├── VisualStudio2022/ # VS solution
│   └── LinuxMakefile/    # Makefile
└── docs/                 # Documentation
```

### Building Different Formats

**VST3 only:**
```bash
cmake -DJUCE_BUILD_VST3=ON -DJUCE_BUILD_AU=OFF -DJUCE_BUILD_AAX=OFF ..
make
```

**AU only (macOS):**
```bash
cmake -DJUCE_BUILD_VST3=OFF -DJUCE_BUILD_AU=ON -DJUCE_BUILD_AAX=OFF ..
make
```

**AAX (requires Avid SDK):**
```bash
# Download AAX SDK from Avid
# Set AAX_SDK_PATH in Projucer
cmake -DJUCE_BUILD_AAX=ON ..
make
```

---

## 🤝 Contributing

Want to improve the plugin?

**Ideas:**
- Stem export (multiple files at once)
- Client database sync
- Payment status tracking
- Visual waveform display
- Export presets/templates
- MIDI learn for controls

**How to contribute:**
1. Fork repository
2. Create feature branch
3. Build and test
4. Submit pull request

---

## 📄 License

MIT License - See main project LICENSE

---

## 🆘 Support

**Issues?**
- GitHub: https://github.com/trentbecknell/audomte/issues
- Email: support@alioop.com

**Plugin compatibility:**
- Pro Tools: 2020+ (macOS/Windows)
- Logic Pro: 10.7+ (macOS only)
- Ableton Live: 10+ (macOS/Windows/Linux)
- Studio One: 5+ (macOS/Windows)
- FL Studio: 20+ (Windows)
- Cubase: 11+ (macOS/Windows)
- Reaper: 6+ (macOS/Windows/Linux)

---

**Built with ❤️ using JUCE Framework**

Happy mixing! 🎚️
