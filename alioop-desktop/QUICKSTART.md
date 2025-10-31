# Alioop Desktop - Quick Start Guide

## Installation & Testing

### Step 1: Install Dependencies

```bash
cd alioop-desktop
npm install
```

This will install:
- Electron (cross-platform desktop framework)
- Chokidar (file system watcher)
- Axios (API communication)
- Electron Store (settings persistence)
- Electron Builder (creating installers)

### Step 2: Run in Development Mode

```bash
npm start
```

This launches the Electron app in development mode. You should see:
- Main window (500x700px) with Upload and Settings tabs
- System tray icon (orange circle with "A")
- Status: "Watching: OFF" (until you configure watch folder)

### Step 3: Configure Watch Folder

1. Click **Settings** tab
2. Click **Browse** button
3. Create/select folder (e.g., `~/Alioop/Bounces`)
4. Set default price (e.g., `50`)
5. Click **Save Settings**
6. Status should change to "Watching: ON"

### Step 4: Test File Detection

1. Open your DAW (Pro Tools, Logic, etc.)
2. Bounce a file to the watch folder
3. Use filename format: `ClientName_ProjectName.wav`
   - Example: `JohnSmith_PodcastEdit.wav`
4. App should:
   - Show desktop notification
   - Open window automatically
   - Pre-fill client name ("John Smith")
   - Show detected file info

### Step 5: Send Delivery

1. Review pre-filled client name
2. Enter client email
3. Enter phone (optional)
4. Adjust price if needed
5. Enter service name (e.g., "Mixing")
6. Click **Send Delivery**
7. Client receives branded email with payment character!

## Building Installers

### Mac (.dmg)

```bash
npm run build:mac
```

Output: `dist/Alioop-0.1.0.dmg`

### Windows (.exe)

```bash
npm run build:win
```

Output: `dist/Alioop Setup 0.1.0.exe`

### Linux (AppImage)

```bash
npm run build:linux
```

Output: `dist/Alioop-0.1.0.AppImage`

## Troubleshooting

### "npm install" fails?
- Ensure Node.js 16+ is installed: `node --version`
- Try clearing cache: `npm cache clean --force`

### App won't start?
- Check logs in terminal when running `npm start`
- Ensure no other Electron apps are interfering
- Try deleting `node_modules` and reinstalling

### Files not detected?
- Verify watch folder path in Settings
- Check "Watching: ON" in status bar
- Ensure file extensions are supported (.wav, .mp3, etc.)
- Wait 2 seconds after bounce completes (stability check)

### Upload fails?
- Check internet connection
- Verify API URL in Settings (default should work)
- Ensure client email is valid
- Check Railway backend is running

## System Tray Menu

Right-click the orange tray icon:
- **Open Alioop** - Show main window
- **Settings** - Open settings directly
- **Watching: ON/OFF** - Toggle file monitoring
- **Quit** - Exit app completely

## Development Tips

### Enable DevTools

The app automatically opens DevTools in development mode. Use it to:
- Debug JavaScript errors
- Inspect IPC messages
- Monitor network requests
- View console logs

### Hot Reload

Changes to `index.html` and renderer JS require app restart. Changes to `main.js` require full restart.

### Testing Without DAW

Create test file manually:
```bash
cd ~/Alioop/Bounces
touch "TestClient_TestProject.wav"
```

App should detect and prompt immediately.

## Next Steps

Once testing is successful:
1. ✅ Verify all features work
2. ✅ Build installers for your platform
3. ✅ Test installer on clean machine
4. ✅ Share with beta testers
5. ✅ Move to Phase 3 (Export Scripts) if desired

## Workflow Comparison

**Before Desktop App:**
1. Finish mix
2. Bounce to file
3. Open browser
4. Go to Alioop
5. Upload file
6. Fill form
7. Send
→ **~2-3 minutes**

**With Desktop App:**
1. Finish mix
2. Bounce to watch folder
3. Click Send in notification
→ **~30 seconds!**

## Support

Issues? Check:
- README.md for feature overview
- main.js for backend logic
- index.html for UI code
- GitHub Issues: https://github.com/trentbecknell/audomte/issues
