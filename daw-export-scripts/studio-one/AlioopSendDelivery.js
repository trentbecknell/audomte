/**
 * Alioop Send Delivery Script for Studio One
 * Automates: Export → Parse Info → Open Alioop
 * 
 * Installation:
 * 1. Copy to: [Documents]/Studio One/Scripts/
 * 2. Restart Studio One
 * 3. Access: Macros → Script → AlioopSendDelivery
 * 
 * Usage:
 * - Run from Scripts menu
 * - Assign to keyboard shortcut (F4 by default)
 * - Map to MIDI controller button
 */

// Get the current song
var song = Studio.getActiveSong();

if (!song) {
    alert("No song is currently open in Studio One!");
    throw new Error("No active song");
}

// Get song name
var songName = song.getName();

/**
 * Show input dialog and get client information
 */
function getClientInfo() {
    // Parse client name from song name if using convention
    var clientName = songName;
    var serviceName = "Mixing";
    
    if (songName.indexOf('_') > -1) {
        var parts = songName.split('_');
        clientName = parts[0].replace(/-/g, ' ');
        serviceName = parts[1] || "Mixing";
    }
    
    // Prompt for client name
    clientName = Studio.getUserInput("Client Name:", clientName);
    if (!clientName || clientName === "") {
        alert("Client name is required!");
        throw new Error("No client name");
    }
    
    // Prompt for client email
    var clientEmail = Studio.getUserInput("Client Email:", "");
    if (!clientEmail || clientEmail === "") {
        alert("Email is required!");
        throw new Error("No email");
    }
    
    // Prompt for price
    var price = Studio.getUserInput("Delivery Price ($):", "50");
    if (!price || price === "") {
        price = "50";
    }
    
    // Prompt for service name
    serviceName = Studio.getUserInput("Service Name:", serviceName);
    if (!serviceName || serviceName === "") {
        serviceName = "Mixing";
    }
    
    return {
        name: clientName,
        email: clientEmail,
        price: price,
        service: serviceName
    };
}

/**
 * URL encode a string
 */
function urlEncode(str) {
    return encodeURIComponent(str);
}

/**
 * Open Alioop with client information
 */
function openAlioop(clientInfo) {
    var baseUrl = "https://web-production-5748a.up.railway.app/";
    
    var params = [
        "client=" + urlEncode(clientInfo.name),
        "email=" + urlEncode(clientInfo.email),
        "price=" + urlEncode(clientInfo.price),
        "service=" + urlEncode(clientInfo.service)
    ];
    
    var url = baseUrl + "?" + params.join("&");
    
    // Show confirmation
    var confirmMsg = "Opening Alioop with:\n\n" +
                     "Client: " + clientInfo.name + "\n" +
                     "Email: " + clientInfo.email + "\n" +
                     "Price: $" + clientInfo.price + "\n" +
                     "Service: " + clientInfo.service + "\n\n" +
                     "Make sure you've exported your mixdown!\n" +
                     "(Song → Export Mixdown)";
    
    if (!confirm(confirmMsg)) {
        return false;
    }
    
    // Open URL in default browser
    Studio.openURL(url);
    
    return true;
}

/**
 * Main execution
 */
function main() {
    try {
        // Get client information
        var clientInfo = getClientInfo();
        
        // Open Alioop
        if (openAlioop(clientInfo)) {
            // Show success message
            var msg = "Alioop opened for " + clientInfo.name + "!\n\n" +
                      "Upload your exported file and click Send.";
            alert(msg);
        }
        
    } catch (e) {
        if (e.message !== "No client name" && e.message !== "No email") {
            alert("Error: " + e.message);
        }
    }
}

// Run the script
main();
