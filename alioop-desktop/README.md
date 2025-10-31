# Alioop Desktop - Phase 2

Auto-detect DAW bounces and send files to clients instantly!

## 🚀 Features

- **📁 Watch Folder** - Monitors a folder for new audio files
- **⚡ Auto-Detect** - Pops up when new files appear
- **🎯 Smart Parsing** - Extracts client name from filename
- **💾 System Tray** - Runs in background, minimal footprint
- **🔔 Notifications** - Desktop alerts for new files & sent deliveries
- **⚙️ Configurable** - Set watch folder, default price, API URL

## 📦 Installation

### Download (Coming Soon)
- **Mac:** `Alioop-0.1.0.dmg` (3MB)
- **Windows:** `Alioop-Setup-0.1.0.exe` (3MB)
- **Linux:** `Alioop-0.1.0.AppImage` (3MB)

### Build from Source

```bash
cd alioop-desktop
npm install
npm start  # Development
npm run build  # Production builds
```

## 🎹 Setup for DAW Workflow

### 1. Configure Watch Folder

In Alioop Desktop:
1. Open Settings tab
2. Click "Browse" next to Watch Folder
3. Select or create folder (e.g., `~/Alioop/Bounces`)
4. Save settings

### 2. Set DAW Bounce Location

**Pro Tools:**
- File → Bounce to → Disk
- Choose bounce folder: `~/Alioop/Bounces`
- Use filename format: `ClientName_ProjectName.wav`

**Logic Pro:**
- File → Bounce → Project or Section
- Set destination: `~/Alioop/Bounces`
- Filename: `ClientName_ProjectName.wav`

**Ableton:**
- File → Export Audio/Video
- Choose: `~/Alioop/Bounces`
- Rendered Track Name: `ClientName_ProjectName.wav`

**Studio One:**
- Song → Export Mixdown
- Location: `~/Alioop/Bounces`
- File Name: `ClientName_ProjectName.wav`

### 3. Bounce & Send Workflow

1. **Finish your mix** in DAW
2. **Bounce to watch folder** with filename: `ClientName_Project.wav`
3. **Alioop auto-detects** file (desktop notification)
4. **Review pre-filled info** (client name parsed from filename)
5. **Enter email & price** (or use defaults)
6. **Click Send** → Client gets email instantly!

## 🎯 Filename Convention

Use this format for automatic client name parsing:

```
ClientName_ProjectName_Version.wav

Examples:
✅ JohnSmith_PodcastEdit_v2.wav      → Client: "John Smith"
✅ MaryJones_MasteringFinal.wav      → Client: "Mary Jones"
✅ AcmeStudios_Commercial30sec.wav   → Client: "Acme Studios"
```

## ⚙️ Configuration

### Settings

- **Watch Folder:** Where DAW bounces files (default: `~/Alioop/Bounces`)
- **Default Price:** Pre-fill price field (default: $50)
- **API URL:** Alioop backend (default: production server)

### System Tray

Right-click tray icon:
- **Open Alioop** - Show main window
- **Settings** - Configure app
- **Watching: ON/OFF** - Toggle file monitoring
- **Quit** - Exit app

## 🔧 Technical Details

### Built With
- **Electron** - Cross-platform desktop framework
- **Chokidar** - File system watcher
- **Electron Store** - Settings persistence
- **Axios** - API communication

### File Watching
- Monitors folder for: `.wav`, `.mp3`, `.flac`, `.aiff`, `.m4a`, `.ogg`, `.aac`, `.wma`
- Waits for file write completion (2 second stability)
- Ignores hidden files/folders
- Auto-creates watch folder if missing

### Performance
- **App Size:** ~3MB (vs 50MB+ for typical Electron apps)
- **Memory:** ~60MB idle
- **CPU:** Minimal (event-driven watching)
- **Startup:** < 1 second

## 📱 Integration with Web PWA

Desktop app complements the web version:
- **Desktop:** Auto-detect bounces, background monitoring
- **Web/PWA:** Drag-drop manual uploads, mobile access
- **Both:** Same API, same clients database

## 🐛 Troubleshooting

### File not detected?
- Check watch folder path in Settings
- Ensure "Watching: ON" in system tray
- Verify file extension is supported
- Check file isn't still being written

### Can't send file?
- Verify internet connection
- Check API URL in Settings
- Ensure email/price filled correctly
- View logs in Dev Tools (Help → Toggle Developer Tools)

### App won't start?
- Check system requirements (macOS 10.13+, Windows 10+, Linux)
- Try reinstalling
- Check antivirus isn't blocking

## 🔮 Roadmap

- ✅ Phase 2: Desktop app with watch folder (current)
- 🔜 Auto-update mechanism
- 🔜 Multiple watch folders
- 🔜 Batch send (multiple files)
- 🔜 Client database sync
- 🔜 Payment status tracking
- 🔜 Analytics dashboard

## 📄 License

MIT License - See main project LICENSE

## 🤝 Contributing

Issues and PRs welcome at: https://github.com/trentbecknell/audomte
