-- Alioop Send Delivery Script for Pro Tools
-- Automates: Bounce → Parse Info → Open Alioop
-- Install: ~/Documents/Pro Tools/Scripts/
-- Usage: Run from Pro Tools Scripts menu or keyboard shortcut

tell application "Pro Tools"
	-- Get current session info
	try
		set sessionName to name of front session
		set sessionPath to path of front session
	on error
		display dialog "No Pro Tools session is open!" buttons {"OK"} default button 1
		return
	end try
end tell

-- Prompt for client name (or parse from session)
set clientName to text returned of (display dialog "Client Name:" default answer "" buttons {"Cancel", "Continue"} default button 2)

if clientName is "" then
	display dialog "Client name is required!" buttons {"OK"} default button 1
	return
end if

-- Prompt for client email
set clientEmail to text returned of (display dialog "Client Email:" default answer "" buttons {"Cancel", "Continue"} default button 2)

if clientEmail is "" then
	display dialog "Email is required!" buttons {"OK"} default button 1
	return
end if

-- Prompt for delivery price
set deliveryPrice to text returned of (display dialog "Delivery Price ($):" default answer "50" buttons {"Cancel", "Send"} default button 2)

if deliveryPrice is "" then
	set deliveryPrice to "50"
end if

-- Set service name (default to session name or "Mixing")
set serviceName to sessionName
if serviceName is "" then
	set serviceName to "Mixing"
end if

-- Construct Alioop URL with parameters
set baseURL to "https://web-production-5748a.up.railway.app/"
set urlParams to "?client=" & clientName & "&email=" & clientEmail & "&price=" & deliveryPrice & "&service=" & serviceName

-- URL encode spaces and special characters
set urlParams to my replaceText(urlParams, " ", "%20")
set urlParams to my replaceText(urlParams, "@", "%40")

set alioopURL to baseURL & urlParams

-- Display confirmation
set confirmMsg to "Opening Alioop with:" & return & return & �
	"Client: " & clientName & return & �
	"Email: " & clientEmail & return & �
	"Price: $" & deliveryPrice & return & �
	"Service: " & serviceName & return & return & �
	"Make sure to bounce your file first!"

display dialog confirmMsg buttons {"Cancel", "Open Alioop"} default button 2

-- Open Alioop in default browser
do shell script "open " & quoted form of alioopURL

-- Helper function to replace text
on replaceText(theText, findText, replaceText)
	set AppleScript's text item delimiters to findText
	set textItems to text items of theText
	set AppleScript's text item delimiters to replaceText
	set theText to textItems as text
	set AppleScript's text item delimiters to ""
	return theText
end replaceText
