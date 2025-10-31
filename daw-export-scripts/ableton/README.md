# Ableton Live - Alioop Integration

## Two Integration Options

### Option 1: Standalone Script (Easiest) ⭐

**Best for:** Quick sends, command line users, MIDI controllers

### Option 2: Control Surface Script (Advanced)

**Best for:** Deep Ableton integration, custom MIDI mapping

---

## Option 1: Standalone Script Setup

### Installation

1. **Make Script Executable:**
   ```bash
   chmod +x alioop_standalone.py
   ```

2. **Optional - Add to PATH:**
   ```bash
   # Add alias to ~/.zshrc or ~/.bashrc
   echo 'alias alioop="python ~/path/to/alioop_standalone.py"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Usage

**Interactive Mode:**
```bash
python alioop_standalone.py
```

Follow the prompts:
1. Enter client name
2. Enter client email
3. Set price (default: $50)
4. Set service name (default: Production)
5. Confirm → Browser opens!

**Command Line Mode:**
```bash
python alioop_standalone.py "John Smith" "john@example.com" "75" "Mixing"
```

**With Alias:**
```bash
alioop "Jane Doe" "jane@example.com" "100" "Mastering"
```

### Workflow

1. **Export your track** in Ableton:
   - File → Export Audio/Video (Cmd+Shift+R)
   - Choose format and location
   - Name: `ClientName_ProjectName.wav`
   - Click Export
   
2. **Run standalone script:**
   ```bash
   python alioop_standalone.py
   ```
   
3. **Fill prompts** → Browser opens

4. **Upload file** → Click Send!

---

## Option 2: Control Surface Script

### Installation

1. **Create Script Folder:**
   ```bash
   mkdir -p ~/Music/Ableton/User\ Library/Remote\ Scripts/Alioop/
   ```

2. **Copy Script:**
   ```bash
   cp AlioopSendDelivery.py ~/Music/Ableton/User\ Library/Remote\ Scripts/Alioop/
   ```

3. **Create __init__.py:**
   ```bash
   touch ~/Music/Ableton/User\ Library/Remote\ Scripts/Alioop/__init__.py
   ```

4. **Restart Ableton Live**

### Activation

1. Open **Preferences** (Cmd+,)
2. Go to **Link/Tempo/MIDI** tab
3. Under **Control Surface**, select dropdown
4. Choose **"Alioop"**
5. Click **OK**

### Usage

The script integrates with Ableton's framework:
- Parses set name for client info
- Shows status in Ableton's status bar
- Can be mapped to MIDI controllers

**Trigger via MIDI:**
1. Set up MIDI controller in preferences
2. Map controller to trigger script
3. Press button → Alioop opens!

---

## Best Practices

### File Naming Convention

Name your Ableton sets using this format:
```
ClientName_ProjectName

Examples:
✅ JohnSmith_PodcastTheme
✅ AcmeCorp_CommercialJingle
✅ BandName_AlbumMaster
```

The script auto-parses this to:
- **Client:** John Smith
- **Service:** Podcast Theme

### Export Settings

Recommended export settings:
- **Rendered Track:** Master
- **File Type:** WAV or MP3
- **Sample Rate:** 44100 Hz or 48000 Hz
- **Bit Depth:** 24-bit (WAV) or 320 kbps (MP3)
- **Dither Options:** As needed
- **Normalize:** Off
- **Create Analysis File:** Off

Save as preset: "Alioop Client Delivery"

### Project Organization

```
~/Music/Ableton/Exports/
  ├── 2025-10/
  │   ├── Client1_Project.wav
  │   └── Client2_Project.wav
  └── Alioop/
      └── (Auto-watched by desktop app)
```

---

## Advanced: MIDI Controller Integration

### Map to Push, Launchpad, or Any Controller

Example with Ableton Push:

1. **Modify AlioopSendDelivery.py:**
   ```python
   def build_midi_map(self, midi_map_handle):
       # Map to a specific note or CC
       # Example: Note C-2 (MIDI note 0)
       send_button = ButtonElement(True, MIDI_NOTE_TYPE, 0, 0)
       send_button.add_value_listener(self.send_delivery)
   ```

2. **Assign to physical button**
3. **Press button** → Alioop opens!

### Keyboard Shortcut

Create keyboard shortcut using macOS/Windows automation:
- **macOS:** Automator + Keyboard Maestro
- **Windows:** AutoHotkey

Example AutoHotkey (Windows):
```ahk
^!a::  ; Ctrl+Alt+A
Run, python "C:\path\to\alioop_standalone.py"
return
```

---

## Integration with Desktop App

**Best of both worlds:**

1. Set Ableton export destination to watch folder:
   ```
   ~/Alioop/Bounces/
   ```

2. Desktop app auto-detects exports

3. One notification → One click → Sent!

**Even faster than scripts!** ⚡

---

## Troubleshooting

### Standalone script issues?

**Python not found:**
```bash
# Check Python version
python3 --version

# Use python3 explicitly
python3 alioop_standalone.py
```

**Browser doesn't open:**
- Check default browser setting
- Manually copy URL from terminal
- Verify internet connection

### Control Surface issues?

**Script not in dropdown:**
- Check folder path exactly matches
- Ensure `__init__.py` exists in folder
- Restart Ableton completely
- Check Ableton version (9.7+)

**Status messages not showing:**
- Look in Ableton's status bar (bottom left)
- Check Log.txt: `~/Library/Preferences/Ableton/Live <version>/Log.txt`

**MIDI mapping not working:**
- Requires modifying `build_midi_map()` function
- Reference Ableton's _Framework documentation
- Start with standalone script first

---

## What's Next?

### Recommended Progression

1. ✅ **Start with standalone script** - Get comfortable
2. 📱 **Try desktop app** (Phase 2) - Auto-detection
3. 🎛️ **Add control surface** - Deep integration
4. 🔌 **Request VST plugin** (Phase 4) - Full in-DAW experience

### Export Templates

Create Ableton export templates for common scenarios:
- WAV Stereo Master (client delivery)
- MP3 320kbps (demos)
- Stems Package (mixing projects)

---

## Resources

**Ableton Control Surface Framework:**
- [Ableton Developer Docs](https://docs.cycling74.com/max8/vignettes/live_object_model)
- [Community Scripts](https://github.com/AbletonAG/)

**Python Integration:**
- [Remote Scripts Tutorial](https://julienbayle.studio/ableton-live-midi-remote-scripts/)

**Support:**
- Report issues: https://github.com/trentbecknell/audomte/issues
- Ableton version: 9.7+ (tested on Live 11)
- Python version: 2.7 (Ableton's built-in) or 3.x (standalone)
