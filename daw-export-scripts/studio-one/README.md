# Studio One - Alioop Integration

## Installation

### Step 1: Copy Script

```bash
# Default location on macOS:
cp AlioopSendDelivery.js ~/Documents/Studio\ One/Scripts/

# Default location on Windows:
copy AlioopSendDelivery.js "%USERPROFILE%\Documents\Studio One\Scripts\"
```

### Step 2: Restart Studio One

Close and reopen Studio One to load the new script.

### Step 3: Verify Installation

1. Open Studio One
2. Go to: **Macros → Script**
3. You should see "AlioopSendDelivery" in the list

---

## Usage

### Standard Workflow

1. **Finish your mix** in Studio One

2. **Export your mixdown:**
   - Song → Export Mixdown (Shift+E)
   - Choose format: WAV or MP3
   - Name file: `ClientName_ProjectName.wav`
   - Set location
   - Click "Export"

3. **Run Alioop script:**
   - Macros → Script → AlioopSendDelivery
   - OR press keyboard shortcut (if assigned)

4. **Fill dialog boxes:**
   - Client name
   - Client email
   - Price (default: $50)
   - Service name (parsed from song)

5. **Confirm and send:**
   - Review summary
   - Click OK → Browser opens
   - Upload exported file
   - Click Send Delivery!

### Lightning-Fast Workflow

With keyboard shortcut (recommended):

1. **Export:** `Shift+E` → Enter
2. **Send:** `F4` (or your custom shortcut)
3. **Fill** prompts → Done!

**Total time: ~30 seconds** ⚡

---

## Keyboard Shortcut Setup

### Assign to F4 (or any key)

1. **Open Keyboard Shortcuts:**
   - Studio One → Keyboard Shortcuts (F4 default menu)
   - Or: Studio One → Options → Keyboard Shortcuts

2. **Find Script Command:**
   - Search for: "AlioopSendDelivery"
   - Or browse: Macros → Scripts

3. **Assign Shortcut:**
   - Click in "Key" column
   - Press desired key (e.g., F4, Cmd+Shift+A)
   - Click "Apply"

4. **Test:**
   - Press your shortcut → Script runs!

---

## Best Practices

### File Naming Convention

Name your Studio One songs using this format:
```
ClientName_ProjectName

Examples:
✅ JohnDoe_PodcastIntro
✅ AcmeCorp_CommercialMix
✅ BandName_SingleMaster
```

Script auto-parses to:
- **Client:** John Doe
- **Service:** Podcast Intro

### Export Settings

Recommended mixdown settings:
- **Format:** Wave or MP3
- **Resolution:** 24 Bit or 320kbps
- **Sample Rate:** 44.1 kHz or 48 kHz
- **File Format:** Interleaved
- **Processing:** As needed
- **Normalize:** Off (preserve dynamics)

Save as preset: "Alioop Client Delivery"

### Project Organization

Organize exports for easy access:
```
~/Documents/Studio One/Exports/
  ├── 2025-10/
  │   ├── Client1_Mix.wav
  │   └── Client2_Master.wav
  └── Alioop/
      └── (Auto-watched by desktop app)
```

---

## Advanced Features

### Auto-Parse Song Info

The script automatically parses your song name:

**Song Name:** `JaneDoe_AlbumMastering_v3`
- ✅ Client: Jane Doe
- ✅ Service: Album Mastering

**Song Name:** `ClientProject-Final`
- ✅ Client: Client Project-Final
- ✅ Service: Mixing (default)

### Macro Integration

Combine with Studio One macros for ultimate automation:

1. **Create Macro:** "Export and Send"
2. **Add Commands:**
   - Export Mixdown
   - Run AlioopSendDelivery script
3. **Assign to button** on console or FaderPort

One button press → File exported and ready to send!

### MIDI Controller Mapping

Map script to hardware controller:

1. **External Devices → Add**
2. **Choose controller** (e.g., FaderPort)
3. **Map to script command**
4. **Save setup**

Now hardware button runs script!

---

## Combining with Desktop App

**Maximum efficiency workflow:**

1. **Set export destination** to desktop app watch folder:
   ```
   ~/Alioop/Bounces/
   ```

2. **Desktop app monitors** in background

3. **Export mixdown:**
   - Studio One exports to watch folder
   - Desktop app detects file instantly
   - Notification appears

4. **One click to send!**

Even faster than the script! 🚀

---

## Troubleshooting

### Script not appearing in menu?

**Check file location:**
- macOS: `~/Documents/Studio One/Scripts/`
- Windows: `%USERPROFILE%\Documents\Studio One\Scripts\`

**Check file extension:**
- Must be `.js` (JavaScript)

**Restart Studio One:**
- Scripts load on startup only

### Dialog boxes not showing?

**Studio One version:**
- Requires Studio One 3.5+ for full JavaScript support
- Update to latest version

**JavaScript console:**
- View errors: Macros → Show Console
- Look for error messages

### Browser doesn't open?

**Check default browser:**
- System Preferences → General → Default web browser (macOS)
- Settings → Default apps → Web browser (Windows)

**Manual URL:**
- Copy URL from confirmation dialog
- Paste in browser manually

**Firewall/Security:**
- Check if browser is blocked
- Temporarily disable firewall for testing

### URL parameters missing?

**Encoding issues:**
- Script uses JavaScript's encodeURIComponent()
- Should handle special characters automatically

**Verify in browser:**
- Check URL bar for all parameters
- Refresh page if needed

---

## Integration Options

### Phase 1: URL Handler (Current)
✅ Script opens Alioop with pre-filled form

### Phase 2: Desktop App
✅ Auto-detects exports, one-click send

### Phase 3: Export Scripts
✅ **You are here!**

### Phase 4: DAW Plugin (Future)
🔜 Full in-app integration (if requested)

---

## Export Preset Template

Create custom export preset for Alioop deliveries:

1. **Set up export options:**
   - Format: Wave File
   - Resolution: 24 Bit
   - Sample Rate: Match song
   - Location: ~/Alioop/Bounces/
   - Name: `$songname`

2. **Save as preset:** "Alioop Delivery"

3. **Quick export:**
   - Load preset
   - Hit Enter
   - Done!

---

## What's Next?

### Recommended Progression

1. ✅ **Master this script** - Get comfortable with workflow
2. 📱 **Try desktop app** - Auto-detection is amazing
3. 🎚️ **Create export macros** - Combine multiple steps
4. 🔌 **Request plugin** (Phase 4) - If you want in-DAW integration

### Additional Scripts

Want more automation?
- **Auto-name exports** with client info
- **Batch export** multiple versions
- **Send to multiple clients** at once

Let us know what would help your workflow!

---

## Resources

**Studio One JavaScript API:**
- [Official Documentation](https://www.presonus.com/learn/technical-articles)
- [Script Examples](https://github.com/presonus/studio-one-scripts)

**Macro Scripting:**
- [Studio One Macro Guide](https://www.presonus.com/products/Studio-One/macros)

**Support:**
- Report issues: https://github.com/trentbecknell/audomte/issues
- Studio One version: 3.5+ (tested on Studio One 6)
- JavaScript support: Built-in (no external dependencies)

---

## Tips from the Community

**Pro tip:** Set song naming template in Studio One preferences to automatically include client names in new projects!

**Power user:** Combine with Studio One's Project Page for mastering workflows - export from Song Page, script opens Alioop, seamless!

**Time saver:** Create a custom toolbar button for the script - right-click toolbar → Customize → Add "AlioopSendDelivery"
