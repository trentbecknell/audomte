const { app, BrowserWindow, ipcMain, Notification, Menu, Tray } = require('electron');
const chokidar = require('chokidar');
const path = require('path');
const fs = require('fs');
const os = require('os');
const Store = require('electron-store');

const store = new Store();
let mainWindow;
let tray;
let watcher;

// Default settings
const DEFAULT_WATCH_FOLDER = path.join(os.homedir(), 'Alioop', 'Bounces');
const DEFAULT_PRICE = '50';
const API_URL = 'https://web-production-5748a.up.railway.app';

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 500,
    height: 700,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
    icon: path.join(__dirname, 'assets/icon.png'),
    show: false
  });

  mainWindow.loadFile('index.html');
  
  // Show window when ready
  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
  });

  // Hide to tray instead of closing
  mainWindow.on('close', (event) => {
    if (!app.isQuitting) {
      event.preventDefault();
      mainWindow.hide();
      
      // Show notification
      new Notification({
        title: 'Alioop Running',
        body: 'App minimized to tray. Still watching for bounces!',
        icon: path.join(__dirname, 'assets/icon.png')
      }).show();
    }
  });
}

function createTray() {
  tray = new Tray(path.join(__dirname, 'assets/tray-icon.png'));
  
  const contextMenu = Menu.buildFromTemplate([
    {
      label: 'Open Alioop',
      click: () => {
        mainWindow.show();
      }
    },
    {
      label: 'Settings',
      click: () => {
        mainWindow.show();
        mainWindow.webContents.send('show-settings');
      }
    },
    { type: 'separator' },
    {
      label: 'Watch Folder: ' + (store.get('watchFolder', DEFAULT_WATCH_FOLDER)),
      enabled: false
    },
    {
      label: 'Watching: ' + (store.get('watching', true) ? 'ON' : 'OFF'),
      type: 'checkbox',
      checked: store.get('watching', true),
      click: (item) => {
        store.set('watching', item.checked);
        if (item.checked) {
          startWatching();
        } else {
          stopWatching();
        }
      }
    },
    { type: 'separator' },
    {
      label: 'Quit',
      click: () => {
        app.isQuitting = true;
        app.quit();
      }
    }
  ]);
  
  tray.setContextMenu(contextMenu);
  tray.setToolTip('Alioop - Audio Delivery Automation');
  
  tray.on('click', () => {
    mainWindow.show();
  });
}

function startWatching() {
  const watchFolder = store.get('watchFolder', DEFAULT_WATCH_FOLDER);
  
  // Create folder if it doesn't exist
  if (!fs.existsSync(watchFolder)) {
    fs.mkdirSync(watchFolder, { recursive: true });
  }
  
  // Stop existing watcher
  if (watcher) {
    watcher.close();
  }
  
  // Watch for audio files
  watcher = chokidar.watch(watchFolder, {
    ignored: /(^|[\/\\])\../,
    persistent: true,
    ignoreInitial: true,
    awaitWriteFinish: {
      stabilityThreshold: 2000,
      pollInterval: 100
    }
  });
  
  watcher.on('add', (filePath) => {
    const ext = path.extname(filePath).toLowerCase();
    const audioExts = ['.wav', '.mp3', '.flac', '.aiff', '.m4a', '.ogg', '.aac', '.wma'];
    
    if (audioExts.includes(ext)) {
      handleNewFile(filePath);
    }
  });
  
  console.log('👀 Watching folder:', watchFolder);
  
  new Notification({
    title: 'Alioop Watching',
    body: `Monitoring: ${watchFolder}`,
    icon: path.join(__dirname, 'assets/icon.png')
  }).show();
}

function stopWatching() {
  if (watcher) {
    watcher.close();
    watcher = null;
    console.log('⏸️ Stopped watching');
  }
}

function handleNewFile(filePath) {
  const filename = path.basename(filePath);
  const fileStats = fs.statSync(filePath);
  const fileSizeMB = (fileStats.size / 1024 / 1024).toFixed(2);
  
  console.log('🎵 New file detected:', filename);
  
  // Parse client info from filename (ClientName_ProjectName.wav)
  const parts = filename.replace(path.extname(filename), '').split('_');
  const clientName = parts[0]?.replace(/[-_]/g, ' ') || '';
  const projectName = parts[1]?.replace(/[-_]/g, ' ') || '';
  
  // Show notification
  new Notification({
    title: '🎵 New Audio File Detected!',
    body: `${filename} (${fileSizeMB}MB)\nClick to send to client`,
    icon: path.join(__dirname, 'assets/icon.png')
  }).show();
  
  // Show main window with file info
  mainWindow.show();
  mainWindow.webContents.send('new-file', {
    filePath,
    filename,
    clientName,
    projectName,
    fileSize: fileSizeMB
  });
}

// IPC Handlers
ipcMain.handle('get-settings', () => {
  return {
    watchFolder: store.get('watchFolder', DEFAULT_WATCH_FOLDER),
    defaultPrice: store.get('defaultPrice', DEFAULT_PRICE),
    apiUrl: store.get('apiUrl', API_URL),
    watching: store.get('watching', true)
  };
});

ipcMain.handle('save-settings', (event, settings) => {
  store.set('watchFolder', settings.watchFolder);
  store.set('defaultPrice', settings.defaultPrice);
  store.set('apiUrl', settings.apiUrl);
  
  // Restart watcher with new folder
  if (store.get('watching', true)) {
    startWatching();
  }
  
  return { success: true };
});

ipcMain.handle('send-delivery', async (event, data) => {
  try {
    const FormData = require('form-data');
    const axios = require('axios');
    
    const form = new FormData();
    form.append('file', fs.createReadStream(data.filePath));
    form.append('client_name', data.clientName);
    form.append('client_email', data.clientEmail);
    form.append('price', data.price);
    
    if (data.clientPhone) {
      form.append('client_phone', data.clientPhone);
    }
    if (data.serviceName) {
      form.append('service_name', data.serviceName);
    }
    
    const apiUrl = store.get('apiUrl', API_URL);
    const response = await axios.post(`${apiUrl}/api/upload-delivery`, form, {
      headers: form.getHeaders()
    });
    
    // Show success notification
    new Notification({
      title: '✅ File Sent!',
      body: `Delivered to ${data.clientName}`,
      icon: path.join(__dirname, 'assets/icon.png')
    }).show();
    
    return { success: true, data: response.data };
  } catch (error) {
    console.error('Upload error:', error);
    return { success: false, error: error.message };
  }
});

ipcMain.handle('choose-folder', async () => {
  const { dialog } = require('electron');
  const result = await dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory', 'createDirectory']
  });
  
  if (!result.canceled && result.filePaths.length > 0) {
    return result.filePaths[0];
  }
  return null;
});

// App lifecycle
app.whenReady().then(() => {
  createWindow();
  createTray();
  
  // Start watching if enabled
  if (store.get('watching', true)) {
    startWatching();
  }
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

app.on('before-quit', () => {
  stopWatching();
});
