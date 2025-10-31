# DAW Integration Guide

Streamline your workflow! Send files directly from your DAW to clients with keyboard shortcuts.

## 🎹 Quick Start (All DAWs)

### Option 1: URL Handler (Works Now!)

Create a keyboard shortcut in your DAW that opens:
```
https://web-production-5748a.up.railway.app/?client=ClientName&price=50&file=/path/to/mix.wav
```

**Example URLs:**

Basic (just pre-fill client):
```
https://web-production-5748a.up.railway.app/?client=John%20Smith&email=john@example.com&price=50
```

From exported file (auto-parse filename):
```
https://web-production-5748a.up.railway.app/?file=JohnSmith_FinalMix_v3.wav&price=50
```

---

## 🎛️ Pro Tools Setup

### Method 1: Keyboard Shortcut (Mac)

1. **Automator** → New Document → Quick Action
2. Add "Run Shell Script"
3. Paste:
```bash
#!/bin/bash
CLIENT="$1"
PRICE="50"
open "https://web-production-5748a.up.railway.app/?client=${CLIENT}&price=${PRICE}"
```
4. Save as "Send to Alioop"
5. System Settings → Keyboard → Shortcuts → Services → Assign Cmd+Shift+A

### Method 2: Post-Bounce Script

Create: `~/ProTools/Scripts/send_to_client.sh`
```bash
#!/bin/bash
BOUNCED_FILE="$1"
FILENAME=$(basename "$BOUNCED_FILE")

# Parse client from filename (e.g., "ClientName_ProjectName.wav")
CLIENT=$(echo "$FILENAME" | cut -d'_' -f1)

open "https://web-production-5748a.up.railway.app/?file=${FILENAME}&client=${CLIENT}&price=50"
```

---

## 🍎 Logic Pro Setup

### AppleScript Workflow

Create: `~/Library/Scripts/Logic Pro/Send to Alioop.scpt`

```applescript
tell application "Logic Pro"
    -- Get current project name
    set projectName to name of front document
    set clientName to text returned of (display dialog "Client Name:" default answer "")
    set price to text returned of (display dialog "Price:" default answer "50")
end tell

set urlString to "https://web-production-5748a.up.railway.app/?client=" & clientName & "&price=" & price & "&service=" & projectName

do shell script "open " & quoted form of urlString
```

**Assign Keyboard Shortcut:**
1. Fast Scripts (free plugin) or System Shortcuts
2. Cmd+Shift+A → Run script

---

## 🔲 Ableton Live Setup

### Python Script

Create: `~/Ableton/Scripts/send_to_alioop.py`

```python
#!/usr/bin/env python3
import subprocess, os

# Get from Ableton's export
CLIENT = os.getenv('CLIENT_NAME', 'Client')
PRICE = os.getenv('PRICE', '50')

url = f"https://web-production-5748a.up.railway.app/?client={CLIENT}&price={PRICE}"
subprocess.run(['open', url])  # Mac
# subprocess.run(['start', url], shell=True)  # Windows
```

**Trigger via MIDI:**
Use [Bome MIDI Translator](https://www.bome.com/products/miditranslator) to map MIDI button → Run Python script

---

## 🎚️ Studio One Setup

### Macro (Windows/Mac)

1. Studio One → Options → Keyboard Shortcuts
2. Add Macro → New
3. Commands:
   - Export Audio
   - Run External Command: `open "https://web-production-5748a.up.railway.app/?price=50"`
4. Assign to Ctrl+Shift+A (Win) or Cmd+Shift+A (Mac)

---

## 💡 Best Practices

### File Naming Convention
Use this format for auto-parsing:
```
ClientName_ProjectName_Version.wav

Examples:
- JohnSmith_PodcastEdit_v2.wav → Client: "John Smith"
- MaryJones_MasteringFinal.wav → Client: "Mary Jones"
```

### Environment Variables (Optional)
Set default values:
```bash
# Add to ~/.zshrc or ~/.bash_profile
export ALIOOP_DEFAULT_PRICE="50"
export ALIOOP_URL="https://web-production-5748a.up.railway.app"
```

---

## 📋 URL Parameters Reference

| Parameter | Example | Description |
|-----------|---------|-------------|
| `client` | `John%20Smith` | Client name (URL encoded) |
| `email` | `john@example.com` | Client email |
| `price` | `50` or `50.00` | Delivery price |
| `service` | `Mixing` | Service/project name |
| `file` | `MyMix.wav` | Filename for context |

**Full Example:**
```
https://web-production-5748a.up.railway.app/?client=John%20Smith&email=john@example.com&price=50&service=Podcast%20Editing&file=Episode12_Final.wav
```

---

## 🚀 Advanced: Watch Folder (Coming Soon)

Desktop app that auto-detects bounces:

1. Set DAW export folder: `~/Alioop/Bounces`
2. Name files: `ClientName_ProjectName.wav`
3. On export → Alioop auto-prompts to send
4. One-click confirmation

**Status:** Phase 2 (Desktop app development)

---

## 🎹 Workflow Examples

### Scenario 1: Quick Client Send
1. Finish mix in DAW
2. Hit **Cmd+Shift+A**
3. Alioop opens with price pre-filled
4. Enter client name + email
5. Click Send → Client gets email!

### Scenario 2: Batch Processing
1. Export multiple mixes with naming: `Client1_Mix.wav`, `Client2_Mix.wav`
2. Drag all to Alioop web interface
3. Auto-parses client names
4. Confirm and send all

### Scenario 3: Post-Bounce Automation
1. DAW exports to watched folder
2. Script auto-opens Alioop with details
3. Review → Send
4. Desktop notification: "✅ Sent to Client!"

---

## 💬 Need Help?

- **Issues?** Open ticket: https://github.com/trentbecknell/audomte/issues
- **Feature requests?** Let us know what DAW workflows you need!
- **Custom scripts?** We can help write integration scripts for your studio

---

## 🔜 Roadmap

- ✅ **Phase 1:** URL handler (live now!)
- ✅ **Phase 2:** Desktop app with watch folder (ready!)
- ✅ **Phase 3:** DAW-specific export scripts (available now!)
- 🎯 **Phase 4:** VST/AU plugin (if requested)

---

## 📦 Phase 3: Export Scripts (NEW!)

**Automate delivery from inside your DAW with keyboard shortcuts!**

We've created production-ready scripts for all major DAWs that integrate Alioop directly into your workflow:

### 🎹 Available Scripts

#### Pro Tools
- **Type:** AppleScript
- **Location:** `~/Documents/Pro Tools/Scripts/`
- **Access:** Setup → Scripts → AlioopSendDelivery
- **[Full Documentation →](./daw-export-scripts/pro-tools/)**

#### Logic Pro
- **Type:** AppleScript  
- **Location:** `~/Music/Audio Music Apps/Scripts/`
- **Access:** Script Menu or keyboard shortcut (Opt+Cmd+A)
- **[Full Documentation →](./daw-export-scripts/logic-pro/)**

#### Ableton Live
- **Type:** Python (Standalone or Control Surface)
- **Location:** Command line or Remote Scripts folder
- **Access:** Terminal or MIDI controller
- **[Full Documentation →](./daw-export-scripts/ableton/)**

#### Studio One
- **Type:** JavaScript
- **Location:** `~/Documents/Studio One/Scripts/`
- **Access:** Macros → Script → AlioopSendDelivery
- **[Full Documentation →](./daw-export-scripts/studio-one/)**

### ⚡ Quick Setup

```bash
# Clone the repository
git clone https://github.com/trentbecknell/audomte.git
cd audomte/daw-export-scripts

# Install for your DAW (choose one):

# Pro Tools:
cp pro-tools/AlioopSendDelivery.scpt ~/Documents/Pro\ Tools/Scripts/

# Logic Pro:
cp logic-pro/AlioopSendDelivery.scpt ~/Music/Audio\ Music\ Apps/Scripts/

# Ableton (standalone):
python ableton/alioop_standalone.py

# Studio One:
cp studio-one/AlioopSendDelivery.js ~/Documents/Studio\ One/Scripts/
```

### 🎯 Workflow with Export Scripts

1. **Finish your mix** in DAW
2. **Bounce/export** file with naming: `ClientName_ProjectName.wav`
3. **Hit keyboard shortcut** (e.g., Cmd+Shift+A)
4. **Fill dialog prompts:**
   - Client name (auto-parsed from filename)
   - Client email
   - Price (default: $50)
5. **Browser opens** with pre-filled form
6. **Upload file** → Click Send!

**Total time: ~30 seconds** ⚡

### 📚 Complete Documentation

**[View Full Export Scripts Guide →](./daw-export-scripts/README.md)**

Includes:
- Detailed installation for each DAW
- Keyboard shortcut setup
- MIDI controller mapping
- Best practices & file naming
- Troubleshooting guides
- Integration with Desktop App

---

**Start using today!** Choose your integration level:
- **Phase 1:** URL handler (no install)
- **Phase 2:** Desktop app (auto-detection)  
- **Phase 3:** Export scripts (keyboard shortcuts)
- **Phase 4:** VST/AU/AAX plugin (in-DAW, zero export!) 🆕

---

## 🔌 Phase 4: VST/AU/AAX Plugin (NEW!)

**The ultimate integration - never leave your DAW!**

Full native plugin with in-DAW recording, form filling, and sending. Zero file management required.

### 🎹 Plugin Features

- **In-DAW Recording** - Capture audio directly from your session
- **Built-in Form** - Client info right in the plugin window
- **Branded UI** - Orange/black/cream Alioop styling  
- **Auto-Export** - Exports WAV and uploads automatically
- **Session Persistence** - Remembers last client info
- **Multi-Format** - VST3, AU, AAX support
- **Cross-Platform** - macOS, Windows, Linux

### 📦 Installation

**macOS:**
```bash
# VST3 (most DAWs)
curl -L https://github.com/trentbecknell/audomte/releases/latest/download/AlioopSend-macOS.vst3.zip -o AlioopSend.vst3.zip
unzip AlioopSend.vst3.zip
mv AlioopSend.vst3 ~/Library/Audio/Plug-Ins/VST3/

# AU (Logic Pro, GarageBand)
curl -L https://github.com/trentbecknell/audomte/releases/latest/download/AlioopSend-macOS.component.zip -o AlioopSend.component.zip
unzip AlioopSend.component.zip
mv AlioopSend.component ~/Library/Audio/Plug-Ins/Components/
```

**Windows:**
```cmd
REM Download from GitHub Releases
xcopy /E /I AlioopSend.vst3 "%COMMONPROGRAMFILES%\VST3\AlioopSend.vst3"
```

**Linux:**
```bash
curl -L https://github.com/trentbecknell/audomte/releases/latest/download/AlioopSend-Linux.vst3.tar.gz -o AlioopSend.vst3.tar.gz
tar -xzf AlioopSend.vst3.tar.gz
mkdir -p ~/.vst3
mv AlioopSend.vst3 ~/.vst3/
```

### 🚀 Quick Start

1. **Insert plugin on Master track:**
   - Pro Tools: Insert → Other → Alioop Send
   - Logic: Insert → Audio FX → Other → Alioop Send
   - Ableton: Drag to Master track
   - Studio One: Effects → Other → Alioop Send

2. **Start recording in plugin:**
   - Click "Start Recording" button
   - Play your session from start
   - Click "Stop Recording" when done

3. **Fill client info:**
   - Client Name: `John Smith`
   - Client Email: `john@example.com`
   - Price: `$50`
   - Service: `Mixing`

4. **Send:**
   - Click "Send Delivery"
   - Done! Client receives email instantly

**Total time: ~3 minutes (no file export needed!)** 🚀

### 📊 Workflow Comparison

| Method | Time | Steps | Export File? |
|--------|------|-------|--------------|
| **Plugin (Phase 4)** | ~3 min | 4 steps | ❌ No! |
| **Desktop App (Phase 2)** | ~15 sec | 2 steps | ✅ Yes |
| **Export Scripts (Phase 3)** | ~30 sec | 3 steps | ✅ Yes |
| **URL Handler (Phase 1)** | ~1 min | 5 steps | ✅ Yes |
| **Manual** | ~5-10 min | 10+ steps | ✅ Yes |

**Plugin wins when:**
- You hate exporting files
- You want everything in one window
- You need to review before sending
- You want session-saved client info

**Desktop App wins when:**
- You already export files
- You want zero interaction
- You bounce multiple files
- Speed is #1 priority

### 🎯 Plugin Use Cases

**Use Case 1: Full Mix Delivery**
```
1. Insert on Master
2. Record entire session
3. Fill form
4. Send
→ Perfect for final deliveries
```

**Use Case 2: Stem Delivery**
```
1. Insert on Drum bus → Record → Send
2. Insert on Bass track → Record → Send
3. Insert on Vocal track → Record → Send
→ Multiple deliveries from one session
```

**Use Case 3: Revision Workflow**
```
1. Plugin remembers previous client
2. Update service to "Revision 2"
3. Record new mix
4. Send (client already filled in!)
→ Super fast for repeat clients
```

### 📚 Plugin Documentation

**[Plugin Quick Start →](./alioop-plugin/QUICKSTART.md)**
**[Full Plugin Guide →](./alioop-plugin/README.md)**
**[Build from Source →](./alioop-plugin/docs/BUILD_GUIDE.md)**

Includes:
- Detailed DAW-specific setup
- Recording workflows
- Client management
- Troubleshooting
- Building from source
- Advanced features

### 🛠️ Building from Source

The plugin is built with JUCE framework (industry standard):

```bash
# Clone repository
git clone https://github.com/trentbecknell/audomte.git
cd audomte/alioop-plugin

# Build with CMake
mkdir build && cd build
cmake .. -DJUCE_PATH=/path/to/JUCE
cmake --build . --config Release

# Install
# macOS
cp -r build/*/Release/AlioopSend.vst3 ~/Library/Audio/Plug-Ins/VST3/

# Windows
xcopy /E /I build\Release\VST3\AlioopSend.vst3 "%COMMONPROGRAMFILES%\VST3\AlioopSend.vst3"

# Linux
cp -r build/AlioopSend.vst3 ~/.vst3/
```

**[Full Build Guide →](./alioop-plugin/docs/BUILD_GUIDE.md)**

---

## 🎉 All Integration Phases Complete!

Choose the method that fits your workflow:

| Phase | Best For | Time | Setup |
|-------|----------|------|-------|
| **Phase 1: URL Handler** | Universal compatibility | ~1 min | None |
| **Phase 2: Desktop App** | Auto-detection | ~15 sec | 5 min |
| **Phase 3: Export Scripts** | Keyboard shortcuts | ~30 sec | 2 min |
| **Phase 4: VST Plugin** | In-DAW workflow | ~3 min | 1 min |

**Most Popular Combinations:**

**For Speed Demons:** Phase 2 (Desktop App)
- Fastest possible workflow
- Zero interaction after bounce
- Perfect for high-volume work

**For Control Freaks:** Phase 4 (Plugin)
- Everything in one window
- No file management
- Review before sending

**For Script Lovers:** Phase 3 (Export Scripts)
- Keyboard shortcut magic
- Minimal but powerful
- Great middle ground

**For Minimalists:** Phase 1 (URL Handler)
- No installation
- Works everywhere
- Quick and simple

---
