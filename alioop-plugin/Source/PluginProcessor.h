/*
  ==============================================================================

    Alioop Send - Audio Delivery Plugin
    Processor Header

  ==============================================================================
*/

#pragma once

#include <juce_audio_processors/juce_audio_processors.h>
#include <juce_audio_utils/juce_audio_utils.h>
#include "AlioopAPI.h"

//==============================================================================
/**
 * Main audio processor for Alioop Send plugin
 * Handles audio pass-through and delivery coordination
 */
class AlioopAudioProcessor : public juce::AudioProcessor
{
public:
    //==============================================================================
    AlioopAudioProcessor();
    ~AlioopAudioProcessor() override;

    //==============================================================================
    void prepareToPlay (double sampleRate, int samplesPerBlock) override;
    void releaseResources() override;

   #ifndef JucePlugin_PreferredChannelConfigurations
    bool isBusesLayoutSupported (const BusesLayout& layouts) const override;
   #endif

    void processBlock (juce::AudioBuffer<float>&, juce::MidiBuffer&) override;

    //==============================================================================
    juce::AudioProcessorEditor* createEditor() override;
    bool hasEditor() const override;

    //==============================================================================
    const juce::String getName() const override;

    bool acceptsMidi() const override;
    bool producesMidi() const override;
    bool isMidiEffect() const override;
    double getTailLengthSeconds() const override;

    //==============================================================================
    int getNumPrograms() override;
    int getCurrentProgram() override;
    void setCurrentProgram (int index) override;
    const juce::String getProgramName (int index) override;
    void changeProgramName (int index, const juce::String& newName) override;

    //==============================================================================
    void getStateInformation (juce::MemoryBlock& destData) override;
    void setStateInformation (const void* data, int sizeInBytes) override;

    //==============================================================================
    // Alioop-specific functionality
    
    /**
     * Export current audio to file and send via Alioop
     */
    void sendDelivery(const juce::String& clientName,
                     const juce::String& clientEmail,
                     const juce::String& clientPhone,
                     float deliveryPrice,
                     const juce::String& serviceName);
    
    /**
     * Get the current audio buffer for export
     */
    const juce::AudioBuffer<float>& getCurrentAudioBuffer() const { return currentBuffer; }
    
    /**
     * Start/stop recording audio for delivery
     */
    void startRecording();
    void stopRecording();
    bool isRecording() const { return recording; }
    
    /**
     * Get recorded audio duration
     */
    double getRecordedDuration() const;

private:
    //==============================================================================
    // Audio recording for delivery
    juce::AudioBuffer<float> currentBuffer;
    juce::AudioBuffer<float> recordedBuffer;
    bool recording = false;
    int recordedSamples = 0;
    double currentSampleRate = 44100.0;
    
    // API handler
    std::unique_ptr<AlioopAPI> apiHandler;
    
    // Settings
    juce::String lastClientName;
    juce::String lastClientEmail;
    float lastDeliveryPrice = 50.0f;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (AlioopAudioProcessor)
};
