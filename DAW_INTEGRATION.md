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
