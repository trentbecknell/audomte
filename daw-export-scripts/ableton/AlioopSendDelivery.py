"""
Alioop Send Delivery Script for Ableton Live
Automates: Export → Parse Info → Open Alioop

Installation:
1. Place in: ~/Music/Ableton/User Library/Remote Scripts/Alioop/
2. Restart Ableton Live
3. Preferences → Link/Tempo/MIDI → Control Surface → Select "Alioop"

Usage:
- Map to MIDI controller or keyboard shortcut
- Or run from Scripts menu (if available)
"""

import Live
import webbrowser
import urllib.parse
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_NOTE_TYPE


class AlioopSendDelivery(ControlSurface):
    """Alioop integration for Ableton Live"""
    
    def __init__(self, c_instance):
        super(AlioopSendDelivery, self).__init__(c_instance)
        
        self.c_instance = c_instance
        self.show_message("Alioop Send Delivery - Ready!")
        
        # Log to Ableton's Log.txt
        self.log_message("Alioop Send Delivery script loaded")
    
    def disconnect(self):
        """Cleanup on script unload"""
        self.show_message("Alioop Send Delivery - Disconnected")
        super(AlioopSendDelivery, self).disconnect()
    
    def send_delivery(self):
        """Main function to send delivery"""
        
        # Get current set name
        song = self.song()
        set_name = song.get_name() if hasattr(song, 'get_name') else "Untitled"
        
        # Show in Ableton's status bar
        self.show_message("Alioop: Preparing to send delivery...")
        
        # Get client info from user (simplified - in real implementation would use dialog)
        # For Ableton, we'll use track names or set name as hints
        
        # Parse client name from set name if using convention: ClientName_ProjectName
        if '_' in set_name:
            parts = set_name.split('_')
            client_name = parts[0].replace('-', ' ')
            service_name = parts[1] if len(parts) > 1 else "Mixing"
        else:
            client_name = set_name
            service_name = "Mixing"
        
        # Default values (user will update in browser)
        client_email = ""  # User fills in browser
        delivery_price = "50"
        
        # Construct Alioop URL
        base_url = "https://web-production-5748a.up.railway.app/"
        
        params = {
            'client': client_name,
            'service': service_name,
            'price': delivery_price
        }
        
        # Add email only if we have it
        if client_email:
            params['email'] = client_email
        
        # Build URL
        url_params = urllib.parse.urlencode(params)
        alioop_url = f"{base_url}?{url_params}"
        
        # Open in browser
        webbrowser.open(alioop_url)
        
        # Notify user
        self.show_message(f"Alioop opened! Client: {client_name}")
        self.log_message(f"Opened Alioop for client: {client_name}")
    
    def build_midi_map(self, midi_map_handle):
        """Map MIDI controls"""
        # Example: Map Note C-2 (MIDI note 0) to trigger send_delivery
        # Users can customize this
        pass


def create_instance(c_instance):
    """Required factory function for Ableton to load the script"""
    return AlioopSendDelivery(c_instance)
