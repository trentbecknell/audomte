-- Alioop Send Delivery Script for Logic Pro
-- Automates: Bounce → Parse Info → Open Alioop  
-- Install: ~/Music/Audio Music Apps/Scripts/ or use Script Editor
-- Usage: Run from Scripts menu or keyboard shortcut (Opt+Cmd+7)

tell application "Logic Pro"
	-- Get current project info
	try
		set projectName to name of front document
	on error
		display dialog "No Logic project is open!" buttons {"OK"} default button 1
		return
	end try
end tell

-- Prompt for client name
set dialogResult to display dialog "Client Name:" default answer "" with title "Alioop - Send Delivery" buttons {"Cancel", "Continue"} default button 2

if button returned of dialogResult is "Cancel" then
	return
end if

set clientName to text returned of dialogResult

if clientName is "" then
	display dialog "Client name is required!" buttons {"OK"} default button 1
	return
end if

-- Prompt for client email
set dialogResult to display dialog "Client Email:" default answer "" with title "Alioop - Send Delivery" buttons {"Cancel", "Continue"} default button 2

if button returned of dialogResult is "Cancel" then
	return
end if

set clientEmail to text returned of dialogResult

if clientEmail is "" then
	display dialog "Email is required!" buttons {"OK"} default button 1
	return
end if

-- Prompt for delivery price
set dialogResult to display dialog "Delivery Price ($):" default answer "50" with title "Alioop - Send Delivery" buttons {"Cancel", "Send"} default button 2

if button returned of dialogResult is "Cancel" then
	return
end if

set deliveryPrice to text returned of dialogResult

if deliveryPrice is "" then
	set deliveryPrice to "50"
end if

-- Service name from project name or default
set serviceName to projectName
if serviceName is "" then
	set serviceName to "Mixing"
end if

-- Construct Alioop URL
set baseURL to "https://web-production-5748a.up.railway.app/"

-- URL encode parameters
set clientNameEncoded to my urlEncode(clientName)
set clientEmailEncoded to my urlEncode(clientEmail)
set serviceNameEncoded to my urlEncode(serviceName)

set alioopURL to baseURL & "?client=" & clientNameEncoded & "&email=" & clientEmailEncoded & "&price=" & deliveryPrice & "&service=" & serviceNameEncoded

-- Show confirmation
set confirmMsg to "Opening Alioop with:" & return & return & �
	"Client: " & clientName & return & �
	"Email: " & clientEmail & return & �
	"Price: $" & deliveryPrice & return & �
	"Service: " & serviceName & return & return & �
	"Make sure you've bounced your file!" & return & �
	"(File → Bounce → Project or Section)"

set dialogResult to display dialog confirmMsg buttons {"Cancel", "Open Alioop"} default button 2 with title "Alioop - Ready to Send"

if button returned of dialogResult is "Cancel" then
	return
end if

-- Open in browser
do shell script "open " & quoted form of alioopURL

-- Show success message
display notification "Alioop opened! Upload your bounced file and click Send." with title "Alioop Send Delivery"

-- Helper function for URL encoding
on urlEncode(theText)
	set theText to do shell script "php -r 'echo rawurlencode(" & quoted form of theText & ");'"
	return theText
end urlEncode
