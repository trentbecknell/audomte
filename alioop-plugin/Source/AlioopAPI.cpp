/*
  ==============================================================================

    Alioop API Handler
    Implementation

  ==============================================================================
*/

#include "AlioopAPI.h"

//==============================================================================
AlioopAPI::AlioopAPI()
{
}

AlioopAPI::~AlioopAPI()
{
}

//==============================================================================
juce::File AlioopAPI::exportAudioToWAV(const juce::AudioBuffer<float>& buffer, double sampleRate)
{
    // Create temporary file
    juce::File tempDir = juce::File::getSpecialLocation(juce::File::tempDirectory);
    juce::File audioFile = tempDir.getChildFile("alioop_export_" + 
                                                juce::String(juce::Time::currentTimeMillis()) + 
                                                ".wav");
    
    // Create audio format writer
    std::unique_ptr<juce::AudioFormatWriter> writer;
    juce::WavAudioFormat wavFormat;
    
    std::unique_ptr<juce::FileOutputStream> outputStream (audioFile.createOutputStream());
    
    if (outputStream != nullptr)
    {
        writer.reset(wavFormat.createWriterFor(outputStream.get(),
                                               sampleRate,
                                               buffer.getNumChannels(),
                                               24, // 24-bit
                                               {},
                                               0));
        
        if (writer != nullptr)
        {
            outputStream.release(); // writer takes ownership
            writer->writeFromAudioSampleBuffer(buffer, 0, buffer.getNumSamples());
            writer.reset(); // Closes file
            
            return audioFile;
        }
    }
    
    lastError = "Failed to create WAV file";
    return juce::File();
}

bool AlioopAPI::uploadFile(const juce::File& audioFile,
                          const juce::String& clientName,
                          const juce::String& clientEmail,
                          const juce::String& clientPhone,
                          float price,
                          const juce::String& serviceName)
{
    if (!audioFile.existsAsFile())
    {
        lastError = "Audio file does not exist";
        return false;
    }
    
    // Prepare multipart form data
    juce::URL uploadUrl(apiUrl + "/api/upload-delivery");
    
    // Create form data
    juce::StringPairArray formData;
    formData.set("clientName", clientName);
    formData.set("clientEmail", clientEmail);
    formData.set("clientPhone", clientPhone);
    formData.set("deliveryPrice", juce::String(price));
    formData.set("serviceName", serviceName);
    
    // Create upload stream
    auto inputStream = audioFile.createInputStream();
    if (inputStream == nullptr)
    {
        lastError = "Could not read audio file";
        return false;
    }
    
    // Upload using POST with multipart data
    juce::URL::InputStreamOptions options(juce::URL::ParameterHandling::inAddress);
    options = options.withExtraHeaders("Content-Type: multipart/form-data");
    
    // For a real implementation, you'd use JUCE's URL::createOutputStream() or curl
    // This is a simplified version showing the concept
    
    juce::String uploadCommand = 
        "curl -X POST " + uploadUrl.toString(false) + " \\\n" +
        "  -F \"clientName=" + clientName + "\" \\\n" +
        "  -F \"clientEmail=" + clientEmail + "\" \\\n" +
        "  -F \"clientPhone=" + clientPhone + "\" \\\n" +
        "  -F \"deliveryPrice=" + juce::String(price) + "\" \\\n" +
        "  -F \"serviceName=" + serviceName + "\" \\\n" +
        "  -F \"file=@" + audioFile.getFullPathName() + "\"";
    
    // Execute upload (simplified - real implementation would use JUCE networking)
    juce::ChildProcess uploadProcess;
    if (uploadProcess.start(uploadCommand))
    {
        uploadProcess.waitForProcessToFinish(30000); // 30 second timeout
        int exitCode = uploadProcess.getExitCode();
        
        if (exitCode == 0)
        {
            // Clean up temp file
            audioFile.deleteFile();
            return true;
        }
    }
    
    lastError = "Upload failed - check internet connection";
    return false;
}

void AlioopAPI::sendDelivery(const juce::String& clientName,
                             const juce::String& clientEmail,
                             const juce::String& clientPhone,
                             float price,
                             const juce::String& serviceName,
                             const juce::AudioBuffer<float>& audioBuffer,
                             double sampleRate)
{
    if (sending)
    {
        lastError = "Already sending a delivery";
        return;
    }
    
    sending = true;
    lastError = "";
    
    // Export audio to WAV
    juce::File audioFile = exportAudioToWAV(audioBuffer, sampleRate);
    
    if (!audioFile.existsAsFile())
    {
        sending = false;
        return;
    }
    
    // Upload to API
    bool success = uploadFile(audioFile, clientName, clientEmail, clientPhone, 
                             price, serviceName);
    
    if (success)
    {
        // Show success notification
        juce::AlertWindow::showMessageBoxAsync(
            juce::AlertWindow::InfoIcon,
            "Delivery Sent!",
            "Successfully sent to " + clientName + "\nClient will receive email with download link."
        );
    }
    else
    {
        // Show error
        juce::AlertWindow::showMessageBoxAsync(
            juce::AlertWindow::WarningIcon,
            "Upload Failed",
            "Could not send delivery: " + lastError
        );
    }
    
    sending = false;
}

bool AlioopAPI::testConnection()
{
    juce::URL testUrl(apiUrl + "/");
    
    // Try to connect to API
    auto inputStream = testUrl.createInputStream(juce::URL::InputStreamOptions(
        juce::URL::ParameterHandling::inAddress).withConnectionTimeoutMs(5000));
    
    if (inputStream != nullptr)
    {
        juce::String response = inputStream->readEntireStreamAsString();
        return response.isNotEmpty();
    }
    
    return false;
}
