; Alioop Send Plugin - Windows One-Click Installer
; Built with NSIS (Nullsoft Scriptable Install System)
; Ultra-simple for non-technical users - just click Next twice!

; Modern UI
!include "MUI2.nsh"
!include "x64.nsh"
!include "FileFunc.nsh"

; Plugin details
!define PRODUCT_NAME "Alioop Send"
!define PRODUCT_VERSION "1.0.0"
!define PRODUCT_PUBLISHER "Alioop"
!define PRODUCT_WEB_SITE "https://github.com/trentbecknell/audomte"
!define PLUGIN_BUNDLE_NAME "AlioopSend"

; Installer name and output
Name "${PRODUCT_NAME}"
OutFile "output\${PLUGIN_BUNDLE_NAME}-Windows-v${PRODUCT_VERSION}.exe"

; Default installation directory (VST3 common files)
InstallDir "$COMMONFILES64\VST3"

; Request admin privileges
RequestExecutionLevel admin

; Modern UI settings
!define MUI_ABORTWARNING
!define MUI_ICON "..\icon.ico"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "installer-header.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP "installer-welcome.bmp"

; Simplified pages - minimal clicks!
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!define MUI_FINISHPAGE_SHOWREADME "$DESKTOP\Alioop Plugin Quick Start.txt"
!define MUI_FINISHPAGE_SHOWREADME_TEXT "Show Quick Start Guide"
!define MUI_FINISHPAGE_SHOWREADME_NOTCHECKED
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

; Languages
!insertmacro MUI_LANGUAGE "English"

; Version info
VIProductVersion "${PRODUCT_VERSION}.0"
VIAddVersionKey "ProductName" "${PRODUCT_NAME}"
VIAddVersionKey "CompanyName" "${PRODUCT_PUBLISHER}"
VIAddVersionKey "FileVersion" "${PRODUCT_VERSION}"
VIAddVersionKey "ProductVersion" "${PRODUCT_VERSION}"
VIAddVersionKey "FileDescription" "${PRODUCT_NAME} Installer"

Section "MainSection" SEC01
    SetOutPath "$INSTDIR"
    
    ; Install VST3 plugin
    File /r "..\Builds\VisualStudio2022\x64\Release\VST3\${PLUGIN_BUNDLE_NAME}.vst3"
    
    ; Create uninstaller
    WriteUninstaller "$INSTDIR\${PLUGIN_BUNDLE_NAME}-Uninstall.exe"
    
    ; Write registry keys for uninstaller
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" \
        "DisplayName" "${PRODUCT_NAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" \
        "UninstallString" "$INSTDIR\${PLUGIN_BUNDLE_NAME}-Uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" \
        "DisplayIcon" "$INSTDIR\${PLUGIN_BUNDLE_NAME}.vst3"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" \
        "Publisher" "${PRODUCT_PUBLISHER}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" \
        "URLInfoAbout" "${PRODUCT_WEB_SITE}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" \
        "DisplayVersion" "${PRODUCT_VERSION}"
    
    ; Create Quick Start Guide on Desktop
    FileOpen $0 "$DESKTOP\Alioop Plugin Quick Start.txt" w
    FileWrite $0 "🎵 ALIOOP PLUGIN - QUICK START GUIDE$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "✅ Plugin installed successfully!$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "📍 WHERE TO FIND IT:$\r$\n"
    FileWrite $0 "In your DAW, look for:$\r$\n"
    FileWrite $0 "- 'Alioop Send' in plugin list$\r$\n"
    FileWrite $0 "- Category: Audio Effect / Other$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "🚀 QUICK WORKFLOW:$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "1. INSERT PLUGIN$\r$\n"
    FileWrite $0 "   - Insert on Master track$\r$\n"
    FileWrite $0 "   - Or any track you want to send$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "2. RECORD AUDIO$\r$\n"
    FileWrite $0 "   - Click 'Start Recording' in plugin$\r$\n"
    FileWrite $0 "   - Play your session$\r$\n"
    FileWrite $0 "   - Click 'Stop Recording'$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "3. FILL CLIENT INFO$\r$\n"
    FileWrite $0 "   - Client Name: John Smith$\r$\n"
    FileWrite $0 "   - Email: john@example.com$\r$\n"
    FileWrite $0 "   - Phone: +1 555-0100$\r$\n"
    FileWrite $0 "   - Price: $$50$\r$\n"
    FileWrite $0 "   - Service: Mixing$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "4. SEND!$\r$\n"
    FileWrite $0 "   - Click 'Send Delivery'$\r$\n"
    FileWrite $0 "   - Done! Client gets email instantly$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "⏱️ Total time: ~3 minutes$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "📚 FULL DOCS:$\r$\n"
    FileWrite $0 "https://github.com/trentbecknell/audomte/tree/main/alioop-plugin$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "💡 TIP:$\r$\n"
    FileWrite $0 "Plugin remembers your last client info - perfect for repeat customers!$\r$\n"
    FileWrite $0 "$\r$\n"
    FileWrite $0 "📍 INSTALLED TO:$\r$\n"
    FileWrite $0 "$INSTDIR\${PLUGIN_BUNDLE_NAME}.vst3$\r$\n"
    FileClose $0
    
    ; Auto-detect installed DAWs and show info
    DetailPrint "Checking for installed DAWs..."
    
    IfFileExists "$PROGRAMFILES\Avid\Pro Tools\ProTools.exe" 0 +2
        DetailPrint "✓ Detected: Pro Tools"
    
    IfFileExists "$PROGRAMFILES\Ableton\Live*\Program\Ableton Live*.exe" 0 +2
        DetailPrint "✓ Detected: Ableton Live"
    
    IfFileExists "$PROGRAMFILES\PreSonus\Studio One*\Studio One.exe" 0 +2
        DetailPrint "✓ Detected: Studio One"
    
    IfFileExists "$PROGRAMFILES\Steinberg\Cubase*\Cubase*.exe" 0 +2
        DetailPrint "✓ Detected: Cubase"
    
    IfFileExists "$PROGRAMFILES\REAPER\reaper.exe" 0 +2
        DetailPrint "✓ Detected: REAPER"
    
    DetailPrint ""
    DetailPrint "Plugin installed successfully!"
    DetailPrint "Please rescan plugins in your DAW or restart your DAW."
SectionEnd

Section "Uninstall"
    ; Remove plugin
    RMDir /r "$INSTDIR\${PLUGIN_BUNDLE_NAME}.vst3"
    
    ; Remove uninstaller
    Delete "$INSTDIR\${PLUGIN_BUNDLE_NAME}-Uninstall.exe"
    
    ; Remove registry keys
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
    
    ; Remove Quick Start guide
    Delete "$DESKTOP\Alioop Plugin Quick Start.txt"
SectionEnd

; Installer functions
Function .onInit
    ; Check if 64-bit Windows
    ${IfNot} ${RunningX64}
        MessageBox MB_OK|MB_ICONSTOP "This plugin requires 64-bit Windows."
        Abort
    ${EndIf}
    
    ; Welcome message
    MessageBox MB_ICONINFORMATION "Welcome to ${PRODUCT_NAME} installer!$\r$\n$\r$\nThis will install the plugin to:$\r$\n$COMMONFILES64\VST3$\r$\n$\r$\nClick OK to continue."
FunctionEnd

Function .onInstSuccess
    ; Show success message
    MessageBox MB_ICONINFORMATION "Installation complete!$\r$\n$\r$\nNext steps:$\r$\n1. Open your DAW$\r$\n2. Rescan plugins (or restart your DAW)$\r$\n3. Insert 'Alioop Send' on your master track$\r$\n$\r$\nA Quick Start guide has been placed on your Desktop."
FunctionEnd
