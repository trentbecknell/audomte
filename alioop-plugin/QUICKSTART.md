# Alioop Plugin - Quick Setup

**Get the plugin working in 5 minutes!**

---

## ⚡ Quick Install

### macOS

**Download & Install:**
```bash
# VST3 (works in most DAWs)
curl -L https://github.com/trentbecknell/audomte/releases/latest/download/AlioopSend-macOS.vst3.zip -o AlioopSend.vst3.zip
unzip AlioopSend.vst3.zip
mv AlioopSend.vst3 ~/Library/Audio/Plug-Ins/VST3/

# AU (for Logic Pro, GarageBand)
curl -L https://github.com/trentbecknell/audomte/releases/latest/download/AlioopSend-macOS.component.zip -o AlioopSend.component.zip
unzip AlioopSend.component.zip
mv AlioopSend.component ~/Library/Audio/Plug-Ins/Components/
```

### Windows

**Download & Install:**
```cmd
REM Download from GitHub Releases
REM Extract AlioopSend.vst3 to:
xcopy /E /I AlioopSend.vst3 "%COMMONPROGRAMFILES%\VST3\AlioopSend.vst3"
```

### Linux

```bash
# Download and extract
curl -L https://github.com/trentbecknell/audomte/releases/latest/download/AlioopSend-Linux.vst3.tar.gz -o AlioopSend.vst3.tar.gz
tar -xzf AlioopSend.vst3.tar.gz
mkdir -p ~/.vst3
mv AlioopSend.vst3 ~/.vst3/
```

---

## 🎹 First Use

### 1. Rescan Plugins

**Pro Tools:**
- Setup → Plug-ins → Update Plug-in Settings

**Logic Pro:**
- Preferences → Plug-in Manager → Reset & Rescan

**Ableton Live:**
- Preferences → Plug-ins → Rescan

**Studio One:**
- Options → Locations → VST Plug-ins → Scan

### 2. Insert Plugin

**On Master Track:**
```
Track → Master
Insert → Other → Alioop Send
```

**Or on any audio track**

### 3. Record Audio

1. Click **"Start Recording"** in plugin
2. Play your session from start to finish
3. Click **"Stop Recording"** when done

### 4. Send Delivery

1. Fill in:
   - Client Name: `John Smith`
   - Client Email: `john@example.com`
   - Client Phone: `+1 555-1234` (optional)
   - Price: `50` (dollars)
   - Service: `Mixing`

2. Click **"Send Delivery"**

3. Done! Client receives email with download link.

---

## 💡 Pro Tips

### Tip 1: Place on Master

For full mixes, insert on Master/Stereo Out:
```
✅ Captures entire mix
✅ One button recording
✅ No routing needed
```

### Tip 2: Save Client Info

Plugin remembers last client used:
```
1. Send to Client A
2. Plugin saves their info
3. Next time → Client A auto-filled
4. Just hit Send!
```

### Tip 3: Use for Stems

Insert on individual tracks/busses:
```
Track 1 (Drums): Record → Send
Track 2 (Bass): Record → Send
Track 3 (Vocals): Record → Send
→ Client gets all stems!
```

### Tip 4: Quality Check

Record multiple takes before sending:
```
1. Record first take
2. Stop → Review
3. Not happy? Record again (overwrites)
4. Happy? Send!
```

---

## ⏱️ Workflow Examples

### Full Mix Delivery (3 minutes)

```
0:00 - Insert plugin on Master
0:30 - Click "Start Recording"
0:35 - Play session from start
3:00 - Song finishes, click "Stop"
3:15 - Fill client form (30 seconds)
3:45 - Click "Send Delivery"
3:50 - Done! Client gets email
```

### Stem Delivery (5 minutes)

```
0:00 - Insert on Drum bus
0:30 - Record drums
1:00 - Send "John - Drums"
1:30 - Insert on Bass track
2:00 - Record bass
2:30 - Send "John - Bass"
3:00 - Insert on Vocal track
3:30 - Record vocals
4:00 - Send "John - Vocals"
4:30 - Done! 3 separate deliveries
```

### Revision Workflow (2 minutes)

```
0:00 - Plugin already has client info saved
0:05 - Update service to "Revision 2"
0:10 - Record new mix
1:45 - Stop recording
1:50 - Click "Send" (client info still there!)
2:00 - Done!
```

---

## 🔧 Troubleshooting

### Plugin doesn't appear?

1. **Check installation path:**
   ```bash
   # macOS
   ls ~/Library/Audio/Plug-Ins/VST3/AlioopSend.vst3
   
   # Windows
   dir "%COMMONPROGRAMFILES%\VST3\AlioopSend.vst3"
   
   # Linux
   ls ~/.vst3/AlioopSend.vst3
   ```

2. **Rescan plugins in DAW** (see above)

3. **Restart DAW** completely

### No audio being recorded?

1. **Check plugin placement:**
   - Should be AFTER all effects
   - Or on Master/Stereo Out

2. **Verify audio is playing:**
   - Check track not muted
   - Verify meters moving

3. **Check recording button:**
   - Should say "Stop Recording" (orange) when active

### Upload fails?

1. **Check internet connection**

2. **Verify form fields:**
   - Name can't be empty
   - Email must be valid format

3. **File size:**
   - Max 5 minutes recording
   - Shorter recordings more reliable

4. **Test API:**
   - Visit: https://web-production-5748a.up.railway.app
   - Should load Alioop website

### Form doesn't save?

1. **Save DAW session** after filling form
2. **Reopen session** to verify persistence
3. **Try different client** to test

---

## 📚 More Help

**Full Documentation:**
- [Complete Plugin Guide](./README.md)
- [Build from Source](./docs/BUILD_GUIDE.md)
- [DAW Integration Overview](../DAW_INTEGRATION.md)

**Other Integration Options:**
- [Desktop App](../alioop-desktop/) - Auto-detect files
- [Export Scripts](../daw-export-scripts/) - Keyboard shortcuts
- [URL Handler](../DAW_INTEGRATION.md) - No installation

**Support:**
- GitHub Issues: https://github.com/trentbecknell/audomte/issues
- Email: support@alioop.com

---

**You're ready to go! Start sending deliveries in-DAW. 🎚️**
