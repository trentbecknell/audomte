# Pro Tools - Alioop Integration

## Installation

1. **Copy Script to Pro Tools Scripts Folder:**
   ```bash
   cp AlioopSendDelivery.scpt ~/Documents/Pro\ Tools/Scripts/
   ```

2. **Restart Pro Tools** (if running)

3. **Access Script:**
   - Go to: `Setup → Scripts` in Pro Tools menu
   - You'll see "AlioopSendDelivery" in the list

## Usage

### Manual Workflow

1. **Finish your mix** in Pro Tools
2. **Bounce your mix:**
   - File → Bounce to → Disk
   - Choose format and location
   - Name file: `ClientName_ProjectName.wav`
   - Click Bounce
3. **Run Alioop Script:**
   - Setup → Scripts → AlioopSendDelivery
4. **Fill Dialog Boxes:**
   - Enter client name
   - Enter client email
   - Set price (default: $50)
5. **Click "Open Alioop"**
   - Browser opens with pre-filled form
   - Upload your bounced file
   - Click Send!

### Keyboard Shortcut (Recommended)

Set up a keyboard shortcut for instant access:

1. Go to: `Setup → Keyboard Shortcuts`
2. Find "Scripts" category
3. Assign shortcut to "AlioopSendDelivery" (e.g., `Cmd+Shift+A`)
4. Click Save

Now you can:
1. Bounce file
2. Hit `Cmd+Shift+A`
3. Fill prompts
4. Send!

## Best Practices

### File Naming Convention

Use this format for automatic client parsing:
```
ClientName_ProjectName_Version.wav

Examples:
✅ JohnSmith_PodcastEdit_v2.wav
✅ AcmeStudios_Commercial.wav
✅ MaryJones_MasteringFinal.wav
```

### Bounce Settings

Recommended bounce settings:
- **File Type:** WAV or MP3
- **Bit Depth:** 24-bit (WAV) or 320kbps (MP3)
- **Sample Rate:** Match session
- **File Type:** Interleaved
- **Location:** Desktop or dedicated Alioop folder

### One-Click Workflow

For ultimate speed, combine with Pro Tools bounce shortcuts:
1. `Cmd+Option+B` → Open Bounce dialog
2. `Enter` → Start bounce
3. `Cmd+Shift+A` → Run Alioop script
4. Fill prompts → Done!

Total time: **~30 seconds!**

## Troubleshooting

### Script not appearing in menu?
- Ensure script is in: `~/Documents/Pro Tools/Scripts/`
- Restart Pro Tools
- Check file has `.scpt` extension

### Browser doesn't open?
- Check default browser is set
- Manually copy URL from dialog
- Verify internet connection

### Form not pre-filled?
- Check URL parameters in address bar
- Ensure Alioop web app is updated
- Try refreshing page

## Advanced: Auto-Bounce Script

Want to automate the bounce too? Create a bounce preset:

1. Set up bounce settings as desired
2. Save as preset: "Alioop Delivery"
3. Script can then reference this preset

## What's Next?

After mastering this script, consider:
- **Phase 2:** Desktop watch folder app (auto-detects bounces)
- **Phase 4:** Full DAW plugin integration (if requested)

## Support

Issues with this script? Check:
- Pro Tools version compatibility (2020+)
- macOS version (10.15+)
- Script permissions in System Preferences → Security & Privacy

Report bugs: https://github.com/trentbecknell/audomte/issues
