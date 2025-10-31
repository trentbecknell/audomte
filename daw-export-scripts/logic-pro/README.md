# Logic Pro - Alioop Integration

## Installation

### Option 1: Scripts Folder (Recommended)

1. **Copy Script:**
   ```bash
   mkdir -p ~/Music/Audio\ Music\ Apps/Scripts/
   cp AlioopSendDelivery.scpt ~/Music/Audio\ Music\ Apps/Scripts/
   ```

2. **Access in Logic:**
   - Open Logic Pro
   - Go to: `Script Editor → Open Script Folder`
   - Double-click "AlioopSendDelivery.scpt" to run

### Option 2: Script Menu

1. **Enable Script Menu:**
   - Open Script Editor app
   - Preferences → General
   - Check "Show Script menu in menu bar"

2. **Add Script:**
   - Copy `AlioopSendDelivery.scpt` to: `~/Library/Scripts/Applications/Logic Pro/`
   - Script appears in menu bar Script menu

### Option 3: Keyboard Shortcut (Best!)

Logic Pro supports custom keyboard shortcuts for AppleScripts:

1. **Open Keyboard Shortcuts:**
   - Logic Pro → Key Commands → Edit (Opt+K)

2. **Create Custom Command:**
   - Click "Options" → "Run Script..."
   - Select "AlioopSendDelivery.scpt"
   - Assign shortcut (e.g., `Opt+Cmd+A`)
   - Click "Save"

Now hit your shortcut anytime to send delivery!

## Usage

### Standard Workflow

1. **Finish your mix** in Logic Pro
2. **Bounce your mix:**
   - File → Bounce → Project or Section (Cmd+B)
   - Choose format: WAV or MP3
   - Name file: `ClientName_ProjectName.wav`
   - Set destination
   - Click "Bounce"
3. **Run Alioop Script:**
   - Scripts Menu → AlioopSendDelivery
   - OR hit your keyboard shortcut
4. **Fill Dialog Boxes:**
   - Client name
   - Client email  
   - Price (default: $50)
5. **Click "Open Alioop"**
   - Browser opens with pre-filled form
   - Drag-drop or select your bounced file
   - Click Send Delivery!

### Lightning-Fast Workflow

With keyboard shortcut configured:

1. **Bounce:** `Cmd+B` → Enter
2. **Send:** `Opt+Cmd+A`
3. **Fill prompts** → Done!

**Total time: ~30 seconds** ⚡

## Best Practices

### Recommended Bounce Settings

For client deliveries:
- **Format:** PCM (WAV) or MP3
- **Resolution:** 24-bit or 320kbps
- **Sample Rate:** 44.1kHz or 48kHz
- **File Type:** Interleaved Stereo
- **Normalize:** Off (preserve dynamics)
- **Dithering:** As needed for 16-bit

Save as preset: "Alioop Client Delivery"

### File Naming Convention

Use consistent naming for easy parsing:
```
ClientName_ProjectName_Version.wav

Examples:
✅ JohnDoe_AlbumMaster_v3.wav
✅ AcmeCorp_JingleFinal.wav  
✅ BandName_SingleMix.wav
```

### Project Organization

Keep bounces organized:
```
~/Music/Bounces/
  ├── 2025-10/
  │   ├── Client1_Project.wav
  │   └── Client2_Project.wav
  └── Alioop/
      └── (Auto-watched by desktop app)
```

## Advanced: Automated Bounce

### Create Bounce Automation

Logic Pro supports scripting bounces! Extend the script:

```applescript
tell application "Logic Pro"
    -- Auto-bounce before sending
    bounce front document to file "~/Desktop/ClientBounce.wav"
end tell
```

### Combine with Desktop App

For ultimate automation:
1. Set bounce destination to watch folder
2. Desktop app auto-detects
3. One-click send!

## Troubleshooting

### Script permission denied?
```bash
chmod +x AlioopSendDelivery.scpt
```

### Script not in menu?
- Check file location
- Restart Logic Pro
- Enable Script Menu in Script Editor prefs

### URL encoding issues?
- Requires PHP installed (default on macOS)
- Alternative: Use Python or pure AppleScript encoding

### Browser doesn't open?
- Set default browser in System Preferences
- Check internet connection
- Copy URL manually from dialog

## Integration with Desktop App

**Phase 2 Desktop App** watches a folder automatically!

Combined workflow:
1. Set Logic bounce destination to `~/Alioop/Bounces`
2. Desktop app running in background
3. Bounce file → Desktop notification
4. One click to send!

Even faster than script! 🚀

## What's Next?

- **Try Desktop App** (Phase 2) - Zero-click file detection
- **Export Script Templates** - Save bounce presets
- **DAW Plugin** (Phase 4) - Full in-app integration

## Support

Having issues? Check:
- Logic Pro version (10.7+)
- macOS version (11.0+)  
- Script permissions
- Default browser settings

Report bugs: https://github.com/trentbecknell/audomte/issues
