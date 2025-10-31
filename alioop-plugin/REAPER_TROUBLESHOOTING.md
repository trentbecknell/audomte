# Alioop Plugin - Reaper Troubleshooting Guide

## Why isn't the plugin showing in Reaper?

This guide will help you get Alioop Send working in Reaper.

---

## Quick Checklist

Before we dig deeper, verify these basics:

- [ ] Plugin file is actually copied to the VST3 folder
- [ ] Reaper VST path includes the plugin location
- [ ] You've rescanned plugins in Reaper
- [ ] You've restarted Reaper after installing

---

## Step-by-Step: Get It Working

### 1. Verify Plugin Location

**macOS - Check these folders exist:**
```bash
# Open Terminal and run:
ls -la "/Library/Audio/Plug-Ins/VST3/AlioopSend.vst3"
ls -la "/Library/Audio/Plug-Ins/Components/AlioopSend.component"
```

**Windows - Check this folder:**
```
C:\Program Files\Common Files\VST3\AlioopSend.vst3
```

**If files don't exist:** The plugin isn't installed yet. Follow manual installation below.

---

### 2. Manual Installation (Drag & Drop)

**macOS:**

1. **Download/Build** the plugin first
2. **Open Finder** and press `Cmd+Shift+G`
3. **Type:** `/Library/Audio/Plug-Ins/`
4. **Drag** `AlioopSend.vst3` into the `VST3` folder
5. **Drag** `AlioopSend.component` into the `Components` folder
6. **Done!** Now rescan in Reaper

**Windows:**

1. **Copy** the `AlioopSend.vst3` folder
2. **Navigate** to `C:\Program Files\Common Files\VST3\`
3. **Paste** the folder (need admin permission)
4. **Done!** Now rescan in Reaper

---

### 3. Configure Reaper VST Paths

**Open Reaper Preferences:**
- Mac: `Cmd+,` or Reaper → Preferences
- Windows: `Ctrl+P` or Options → Preferences

**Check VST3 Paths:**

1. Click **"Plug-ins"** in left sidebar
2. Click **"VST"** 
3. Look at **"VST plug-in paths"** section

**macOS - Should include:**
```
/Library/Audio/Plug-Ins/VST3
```

**Windows - Should include:**
```
C:\Program Files\Common Files\VST3
```

**If path is missing:**
1. Click **"Edit path list..."**
2. Click **"Add"**
3. Browse to the folder above
4. Click **"OK"**

---

### 4. Rescan Plugins in Reaper

**Option A: Clear Cache & Rescan (Recommended)**

1. Open Reaper Preferences (`Cmd+,` or `Ctrl+P`)
2. Go to: **Plug-ins → VST**
3. Click **"Clear cache/re-scan"**
4. Wait for scan to complete (may take 1-2 minutes)
5. Click **"OK"**
6. **Restart Reaper**

**Option B: Quick Rescan**

1. Preferences → Plug-ins → VST
2. Click **"Re-scan"**
3. Wait for completion
4. Click **"OK"**

---

### 5. Find the Plugin in Reaper

**Method 1: FX Browser (Easiest)**

1. **Select Master track** (or any track)
2. Click **"fx"** button on the track
3. **Type "Alioop"** in search box at top
4. Should see: **"VST3: Alioop Send (Alioop)"**
5. **Double-click** to insert

**Method 2: Browse by Category**

1. Click **"fx"** button on track
2. Click **"All Plugins"** dropdown at top
3. Select **"VST3"**
4. Look for **"Alioop"** folder
5. Click **"AlioopSend"**

**Method 3: Right-Click Menu**

1. **Right-click** track FX button
2. **Browse → VST3 → Alioop → AlioopSend**
3. Click to insert

---

## Still Not Showing?

### Check Reaper's Plugin Scanner Results

1. Preferences → Plug-ins → VST
2. Look at **"VST plug-in versions"** list
3. **Search** for "Alioop" or "Alioop Send"

**If you see it listed:**
- ✅ Reaper found it! Try inserting again
- ❌ If it says "failed" - see Architecture Mismatch below

**If you DON'T see it:**
- Plugin file isn't in scanned folders
- Path isn't configured correctly
- Plugin file is corrupted

### Architecture Mismatch (Mac)

**Problem:** You have Apple Silicon Mac but plugin is Intel-only (or vice versa)

**Check your Mac type:**
```bash
# Run in Terminal:
uname -m

# Result means:
# arm64    = Apple Silicon (M1/M2/M3)
# x86_64   = Intel
```

**Check plugin architecture:**
```bash
# Run in Terminal:
file "/Library/Audio/Plug-Ins/VST3/AlioopSend.vst3/Contents/MacOS/AlioopSend"

# Should say "Mach-O 64-bit bundle arm64" or similar
```

**Solution:** Plugin needs to be built as Universal Binary (both architectures)

### Enable Auto-Rescan (Helpful for testing)

1. Preferences → Plug-ins → VST
2. **Check:** "Auto-detect newly installed VST plug-ins"
3. **Check:** "Also perform initial scan for newly detected VST plug-ins"
4. Click **"OK"**

Now Reaper auto-scans when it detects new plugins!

---

## Build the Plugin (If You Don't Have It Yet)

The plugin source code is ready but needs to be built:

**Requirements:**
- macOS with Xcode
- JUCE Framework
- CMake

**Quick Build:**
```bash
# Install dependencies
brew install juce cmake

# Navigate to plugin folder
cd /path/to/audomte/alioop-plugin

# Build
./build-all.sh
```

**Manual Build:**
1. Open `AlioopPlugin.jucer` in Projucer (JUCE)
2. Click "Save and Open in IDE" (opens Xcode)
3. Select **"Release"** build configuration
4. Build → Build For → Profiling (Cmd+Shift+I)
5. Plugin builds to `Builds/MacOSX/build/Release/`

---

## Test with FX Chain

If plugin inserted but not working:

1. Insert plugin on track
2. Check if **plugin window opens**
3. Check **Reaper's FX chain** shows it
4. Try clicking **"UI"** button to show/hide interface

---

## Alternative: Use Desktop App or Web App

While troubleshooting the plugin:

**Desktop App (Phase 2):** Auto-detects bounced files
- Fastest workflow (~15 sec)
- Works immediately

**Web App:** Browser-based
- https://web-production-5748a.up.railway.app/
- Works on any platform

**Export Scripts (Phase 3):** Keyboard shortcuts
- AppleScript, Python, JavaScript
- Quick automation

---

## Common Reaper Issues

### "Plugin not found" after restart
- Reaper cleared its cache
- Re-run "Clear cache/re-scan"

### Plugin shows but won't open
- Try different plugin format (VST3 vs AU on Mac)
- Check console for errors: Help → Show REAPER resource path → Open folder → reaper.log

### macOS Gatekeeper blocking
- Right-click plugin → Open
- Or: System Settings → Security → Allow

### Permission denied
- Plugin folder needs admin access
- Use `sudo` when copying via Terminal

---

## Get Help

**Still stuck?**

1. Check Reaper's log file for errors
2. Verify plugin file isn't corrupted: `ls -lh /Library/Audio/Plug-Ins/VST3/AlioopSend.vst3`
3. Try AU format on Mac (if VST3 doesn't work)
4. Open GitHub issue: https://github.com/trentbecknell/audomte/issues

**Share these details when asking for help:**
- macOS version or Windows version
- Reaper version
- Plugin file location
- Screenshot of Reaper VST preferences
- Any error messages

---

## Success Checklist

Once it's working:

- [ ] Plugin appears in Reaper FX browser
- [ ] Plugin window opens when inserted
- [ ] Can see orange/black/cream Alioop branding
- [ ] All input fields are visible
- [ ] Record button works
- [ ] Send button works

**Ready to use!** 🎉

---

**Built for audio professionals who want fast client delivery workflows!**
