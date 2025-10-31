# DAW Export Scripts - Phase 3

**Automate your audio delivery workflow from inside your DAW!**

These scripts integrate Alioop directly into Pro Tools, Logic Pro, Ableton Live, and Studio One, allowing you to send client deliveries without leaving your music production environment.

---

## 🎹 Quick Links

- **[Pro Tools Scripts →](./pro-tools/)**
- **[Logic Pro Scripts →](./logic-pro/)**
- **[Ableton Live Scripts →](./ableton/)**
- **[Studio One Scripts →](./studio-one/)**

---

## 🚀 What These Scripts Do

### Before Export Scripts
1. Finish mix in DAW
2. Bounce/export file
3. Open browser
4. Navigate to Alioop
5. Upload file
6. Fill out form
7. Send delivery

**Time: ~2-3 minutes**

### After Export Scripts
1. Finish mix in DAW
2. Bounce/export file
3. Run script (keyboard shortcut)
4. Browser opens with pre-filled form
5. Upload → Send

**Time: ~30 seconds** ⚡

---

## 📦 Installation by DAW

### Pro Tools

```bash
cp pro-tools/AlioopSendDelivery.scpt ~/Documents/Pro\ Tools/Scripts/
```

**Access:** Setup → Scripts → AlioopSendDelivery

**[Full Documentation →](./pro-tools/README.md)**

---

### Logic Pro

```bash
cp logic-pro/AlioopSendDelivery.scpt ~/Music/Audio\ Music\ Apps/Scripts/
```

**Access:** Script Menu or keyboard shortcut (Opt+Cmd+A)

**[Full Documentation →](./logic-pro/README.md)**

---

### Ableton Live

**Option 1 - Standalone (Easiest):**
```bash
python ableton/alioop_standalone.py
```

**Option 2 - Control Surface:**
```bash
cp -r ableton/AlioopSendDelivery.py ~/Music/Ableton/User\ Library/Remote\ Scripts/Alioop/
```

**[Full Documentation →](./ableton/README.md)**

---

### Studio One

```bash
cp studio-one/AlioopSendDelivery.js ~/Documents/Studio\ One/Scripts/
```

**Access:** Macros → Script → AlioopSendDelivery

**[Full Documentation →](./studio-one/README.md)**

---

## 🎯 Best Practices

### File Naming Convention

All scripts support automatic client parsing from filenames:

```
ClientName_ProjectName_Version.wav

Examples:
✅ JohnSmith_PodcastEdit_v2.wav → Client: "John Smith"
✅ AcmeCorp_Commercial30sec.wav → Client: "Acme Corp"
✅ MaryJones_AlbumMaster.wav → Client: "Mary Jones"
```

### Keyboard Shortcuts

Set up keyboard shortcuts in each DAW for one-keystroke access:

- **Pro Tools:** Setup → Keyboard Shortcuts → Scripts
- **Logic Pro:** Key Commands → Run Script
- **Ableton:** External tools or MIDI mapping
- **Studio One:** Options → Keyboard Shortcuts → Scripts

**Recommended:** `Cmd+Shift+A` (macOS) or `Ctrl+Shift+A` (Windows)

### Export/Bounce Presets

Create dedicated presets for client deliveries:

**Preset Name:** "Alioop Client Delivery"

**Settings:**
- Format: WAV or MP3
- Bit Depth: 24-bit (WAV) or 320kbps (MP3)
- Sample Rate: 44.1 kHz or 48 kHz
- Dithering: As needed
- Normalization: Off (preserve dynamics)

---

## 🔄 Workflow Comparison

### Traditional Workflow
```
Mix → Bounce → Find File → Open Email → 
Attach → Write Message → Send → Open Payment App → 
Create Invoice → Send Invoice
```
⏱️ **Time: 5-10 minutes**

### Phase 1: URL Handler
```
Mix → Bounce → Open URL → Upload → Send
```
⏱️ **Time: ~1 minute**

### Phase 3: Export Scripts (You Are Here!)
```
Mix → Bounce → Hit Shortcut → Upload → Send
```
⏱️ **Time: ~30 seconds**

### Phase 2: Desktop App (Recommended!)
```
Mix → Bounce → Desktop Notification → Click → Send
```
⏱️ **Time: ~15 seconds**

---

## 📊 Script Comparison

| Feature | Pro Tools | Logic Pro | Ableton | Studio One |
|---------|-----------|-----------|---------|------------|
| Language | AppleScript | AppleScript | Python | JavaScript |
| Keyboard Shortcut | ✅ | ✅ | ⚙️ Manual | ✅ |
| Auto-Parse Filename | ✅ | ✅ | ✅ | ✅ |
| MIDI Mapping | ❌ | ❌ | ✅ | ✅ |
| Dialog Prompts | ✅ | ✅ | ✅ CLI | ✅ |
| Standalone Mode | ❌ | ❌ | ✅ | ❌ |
| macOS | ✅ | ✅ | ✅ | ✅ |
| Windows | ❌ | ❌ | ✅ | ✅ |

---

## 🎓 Learning Path

### Beginner
1. Start with **standalone script** (Ableton Python version works everywhere)
2. Test with manual workflow
3. Get comfortable with prompts

### Intermediate  
1. Install DAW-specific script
2. Set up keyboard shortcut
3. Create export/bounce preset

### Advanced
1. Combine with **Desktop App** (Phase 2)
2. Set bounce destination to watch folder
3. Auto-detection + one-click send
4. Ultimate workflow efficiency!

---

## 💡 Pro Tips

### Tip #1: Combine with Templates

Create project templates with:
- Pre-configured export settings
- Client naming convention in title
- Bounce destination set to watch folder

### Tip #2: Batch Processing

For multiple deliveries:
1. Export all files to watch folder
2. Desktop app detects each one
3. Send them one by one (quick!)

### Tip #3: MIDI Controller

Map script to hardware button:
- Ableton: Control Surface mapping
- Studio One: External Devices
- Other DAWs: Use OS-level MIDI tools

### Tip #4: URL Parameters

Scripts support these parameters:
- `client` - Client name
- `email` - Client email
- `price` - Delivery price
- `service` - Service name
- `file` - Filename (optional)

Customize scripts to pre-fill more fields!

---

## 🔧 Troubleshooting

### Script doesn't appear in menu?

1. **Check file location** (see DAW-specific docs)
2. **Check file extension** (.scpt, .py, .js)
3. **Restart DAW** completely
4. **Check permissions** (`chmod +x` on macOS/Linux)

### Browser doesn't open?

1. **Set default browser** in system preferences
2. **Check internet connection**
3. **Try manually** copying URL from dialog
4. **Firewall** - Temporarily disable for testing

### Form not pre-filling?

1. **Check URL parameters** in browser address bar
2. **Refresh page** if needed
3. **Clear browser cache**
4. **Update Alioop** web app to latest version

### Encoding issues with special characters?

1. Scripts handle most characters automatically
2. **Avoid:** `&`, `?`, `#` in client names
3. **Use underscores** instead of spaces in filenames
4. **Manual entry** for complex names

---

## 🌟 What's Next?

### Already Implemented

- ✅ **Phase 1:** URL Handler (deployed)
- ✅ **Phase 2:** Desktop Watch Folder App (ready)
- ✅ **Phase 3:** Export Scripts (you are here!)

### Future (If Requested)

- 🔜 **Phase 4:** VST/AU Plugin (full in-DAW integration)
- 🔜 **Batch Send** (multiple files at once)
- 🔜 **Client Database Sync** (remember past clients)
- 🔜 **Payment Tracking** (see who paid)

---

## 📚 Additional Resources

**Documentation:**
- [DAW Integration Overview](../DAW_INTEGRATION.md)
- [Desktop App Guide](../alioop-desktop/README.md)
- [Web App Documentation](../alioop-microservice-prototype/)

**Support:**
- Report Issues: https://github.com/trentbecknell/audomte/issues
- Feature Requests: Use GitHub Discussions
- Community: Share your workflows!

**Compatibility:**
- Pro Tools: 2020+ (macOS only)
- Logic Pro: 10.7+ (macOS only)
- Ableton Live: 9.7+ (macOS, Windows, Linux)
- Studio One: 3.5+ (macOS, Windows)

---

## 🙏 Contributing

Have improvements or scripts for other DAWs?

1. Fork the repository
2. Add your script in new folder
3. Include README with documentation
4. Submit pull request

**Wanted:**
- Reaper scripts
- FL Studio integration
- Cubase/Nuendo scripts
- Bitwig integration

---

**Built with ❤️ for audio engineers who value their time**

Happy mixing! 🎚️
