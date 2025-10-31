/*
  ==============================================================================

    Alioop API Handler
    Handles communication with Alioop backend

  ==============================================================================
*/

#pragma once

#include <juce_core/juce_core.h>
#include <juce_audio_formats/juce_audio_formats.h>
#include <juce_gui_extra/juce_gui_extra.h>

//==============================================================================
/**
 * Handles all communication with the Alioop backend API
 */
class AlioopAPI
{
public:
    AlioopAPI();
    ~AlioopAPI();
    
    /**
     * Send audio delivery to client
     * 
     * @param clientName Client's name
     * @param clientEmail Client's email address
     * @param clientPhone Client's phone number (optional)
     * @param price Delivery price
     * @param serviceName Service description
     * @param audioBuffer Audio buffer to send
     * @param sampleRate Sample rate of audio
     */
    void sendDelivery(const juce::String& clientName,
                     const juce::String& clientEmail,
                     const juce::String& clientPhone,
                     float price,
                     const juce::String& serviceName,
                     const juce::AudioBuffer<float>& audioBuffer,
                     double sampleRate);
    
    /**
     * Test API connection
     */
    bool testConnection();
    
    /**
     * Get API URL
     */
    juce::String getAPIUrl() const { return apiUrl; }
    
    /**
     * Set custom API URL (for development)
     */
    void setAPIUrl(const juce::String& url) { apiUrl = url; }
    
    /**
     * Check if currently sending
     */
    bool isSending() const { return sending; }
    
    /**
     * Get last error message
     */
    juce::String getLastError() const { return lastError; }

private:
    /**
     * Export audio buffer to WAV file
     */
    juce::File exportAudioToWAV(const juce::AudioBuffer<float>& buffer, 
                                double sampleRate);
    
    /**
     * Upload file to Alioop API
     */
    bool uploadFile(const juce::File& audioFile,
                   const juce::String& clientName,
                   const juce::String& clientEmail,
                   const juce::String& clientPhone,
                   float price,
                   const juce::String& serviceName);
    
    juce::String apiUrl = "https://web-production-5748a.up.railway.app";
    bool sending = false;
    juce::String lastError;
    
    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (AlioopAPI)
};
