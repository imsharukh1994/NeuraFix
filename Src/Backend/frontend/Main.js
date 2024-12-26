// main.js
const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");
const fs = require("fs");

// Keep a global reference of the window object
let mainWindow;

function createMainWindow() {
  // Create the browser window
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"), // Preload script
      contextIsolation: true,
      enableRemoteModule: false,
      nodeIntegration: false,
    },
  });

  // Load the index.html of the app
  mainWindow.loadFile(path.join(__dirname, "frontend", "index.html"));

  // Open DevTools in development mode
  if (!app.isPackaged) {
    mainWindow.webContents.openDevTools();
  }

  // Handle window close
  mainWindow.on("closed", () => {
    mainWindow = null;
  });
}

// This method will be called when Electron has finished initialization
app.on("ready", createMainWindow);

// Quit when all windows are closed
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

// Re-create the window on macOS when the dock icon is clicked
app.on("activate", () => {
  if (mainWindow === null) {
    createMainWindow();
  }
});

// IPC Communication for Backend Integration
ipcMain.handle("run-code", async (event, { code, language }) => {
  const compiler = require("./src/backend/compiler");
  const compiled = new compiler.Compiler(code, language);
  const result = compiled.compile_code();
  return result;
});
