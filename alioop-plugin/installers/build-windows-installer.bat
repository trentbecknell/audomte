@echo off
REM Alioop Plugin - Windows Installer Build Script
REM Requires NSIS (Nullsoft Scriptable Install System)
REM Download from: https://nsis.sourceforge.io/Download

echo.
echo 🎵 Building Alioop Plugin Installer for Windows...
echo.

REM Check if NSIS is installed
where makensis >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ NSIS not found! Please install NSIS first:
    echo    Download from: https://nsis.sourceforge.io/Download
    echo    Or install via Chocolatey: choco install nsis
    exit /b 1
)

REM Check if plugin is built
if not exist "..\Builds\VisualStudio2022\x64\Release\VST3\AlioopSend.vst3" (
    echo ❌ Plugin not built yet! Please build the plugin first.
    echo    Run: cd .. ^&^& build.bat
    exit /b 1
)

REM Create output directory
if not exist "output" mkdir output

REM Create installer graphics (placeholder - replace with actual branded images)
echo 📸 Creating installer graphics...

REM Create simple header bitmap (150x57 pixels) - Orange gradient
if not exist "installer-header.bmp" (
    echo Creating placeholder header image...
    REM You should replace this with actual branded Alioop header
    echo Note: Replace installer-header.bmp with branded 150x57 image
)

REM Create welcome bitmap (164x314 pixels) - Alioop branding
if not exist "installer-welcome.bmp" (
    echo Creating placeholder welcome image...
    REM You should replace this with actual branded Alioop welcome screen
    echo Note: Replace installer-welcome.bmp with branded 164x314 image
)

REM Build installer with NSIS
echo.
echo 🔨 Building installer with NSIS...
makensis windows-installer.nsi

if %errorlevel% equ 0 (
    echo.
    echo ✅ SUCCESS! Installer created:
    echo    📦 output\AlioopSend-Windows-v1.0.0.exe
    echo.
    echo 🎯 ONE-CLICK INSTALLATION:
    echo    Users just double-click the .exe file
    echo    Plugin auto-installs to C:\Program Files\Common Files\VST3
    echo    Quick Start guide appears on Desktop
    echo.
    echo 📤 NEXT STEPS:
    echo    1. Test the installer on a clean Windows machine
    echo    2. Upload to GitHub Releases
    echo    3. Share download link with users!
    echo.
) else (
    echo.
    echo ❌ Build failed! Check errors above.
    exit /b 1
)
