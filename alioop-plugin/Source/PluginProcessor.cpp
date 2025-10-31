/*
  ==============================================================================

    Alioop Send - Audio Delivery Plugin
    Processor Implementation

  ==============================================================================
*/

#include "PluginProcessor.h"
#include "PluginEditor.h"

//==============================================================================
AlioopAudioProcessor::AlioopAudioProcessor()
#ifndef JucePlugin_PreferredChannelConfigurations
     : AudioProcessor (BusesProperties()
                     #if ! JucePlugin_IsMidiEffect
                      #if ! JucePlugin_IsSynth
                       .withInput  ("Input",  juce::AudioChannelSet::stereo(), true)
                      #endif
                       .withOutput ("Output", juce::AudioChannelSet::stereo(), true)
                     #endif
                       )
#endif
{
    apiHandler = std::make_unique<AlioopAPI>();
}

AlioopAudioProcessor::~AlioopAudioProcessor()
{
}

//==============================================================================
const juce::String AlioopAudioProcessor::getName() const
{
    return JucePlugin_Name;
}

bool AlioopAudioProcessor::acceptsMidi() const
{
   #if JucePlugin_WantsMidiInput
    return true;
   #else
    return false;
   #endif
}

bool AlioopAudioProcessor::producesMidi() const
{
   #if JucePlugin_ProducesMidiOutput
    return true;
   #else
    return false;
   #endif
}

bool AlioopAudioProcessor::isMidiEffect() const
{
   #if JucePlugin_IsMidiEffect
    return true;
   #else
    return false;
   #endif
}

double AlioopAudioProcessor::getTailLengthSeconds() const
{
    return 0.0;
}

int AlioopAudioProcessor::getNumPrograms()
{
    return 1;
}

int AlioopAudioProcessor::getCurrentProgram()
{
    return 0;
}

void AlioopAudioProcessor::setCurrentProgram (int index)
{
}

const juce::String AlioopAudioProcessor::getProgramName (int index)
{
    return {};
}

void AlioopAudioProcessor::changeProgramName (int index, const juce::String& newName)
{
}

//==============================================================================
void AlioopAudioProcessor::prepareToPlay (double sampleRate, int samplesPerBlock)
{
    currentSampleRate = sampleRate;
    currentBuffer.setSize(2, samplesPerBlock);
    recordedBuffer.setSize(2, sampleRate * 300); // Max 5 minutes
}

void AlioopAudioProcessor::releaseResources()
{
}

#ifndef JucePlugin_PreferredChannelConfigurations
bool AlioopAudioProcessor::isBusesLayoutSupported (const BusesLayout& layouts) const
{
  #if JucePlugin_IsMidiEffect
    juce::ignoreUnused (layouts);
    return true;
  #else
    if (layouts.getMainOutputChannelSet() != juce::AudioChannelSet::mono()
     && layouts.getMainOutputChannelSet() != juce::AudioChannelSet::stereo())
        return false;

   #if ! JucePlugin_IsSynth
    if (layouts.getMainOutputChannelSet() != layouts.getMainInputChannelSet())
        return false;
   #endif

    return true;
  #endif
}
#endif

void AlioopAudioProcessor::processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages)
{
    juce::ScopedNoDenormals noDenormals;
    auto totalNumInputChannels  = getTotalNumInputChannels();
    auto totalNumOutputChannels = getTotalNumOutputChannels();

    // Clear extra output channels
    for (auto i = totalNumInputChannels; i < totalNumOutputChannels; ++i)
        buffer.clear (i, 0, buffer.getNumSamples());

    // Pass audio through (this is a utility plugin, not an effect)
    // Just copy input to output
    
    // If recording, capture audio
    if (recording && recordedSamples < recordedBuffer.getNumSamples())
    {
        int samplesToRecord = juce::jmin(buffer.getNumSamples(), 
                                         recordedBuffer.getNumSamples() - recordedSamples);
        
        for (int channel = 0; channel < juce::jmin(2, buffer.getNumChannels()); ++channel)
        {
            recordedBuffer.copyFrom(channel, recordedSamples, 
                                   buffer, channel, 0, samplesToRecord);
        }
        
        recordedSamples += samplesToRecord;
    }
    
    // Store current buffer for reference
    currentBuffer.makeCopyOf(buffer);
}

//==============================================================================
bool AlioopAudioProcessor::hasEditor() const
{
    return true;
}

juce::AudioProcessorEditor* AlioopAudioProcessor::createEditor()
{
    return new AlioopAudioProcessorEditor (*this);
}

//==============================================================================
void AlioopAudioProcessor::getStateInformation (juce::MemoryBlock& destData)
{
    // Save plugin state
    std::unique_ptr<juce::XmlElement> xml (new juce::XmlElement ("AlioopPluginState"));
    
    xml->setAttribute ("lastClientName", lastClientName);
    xml->setAttribute ("lastClientEmail", lastClientEmail);
    xml->setAttribute ("lastDeliveryPrice", lastDeliveryPrice);
    
    copyXmlToBinary (*xml, destData);
}

void AlioopAudioProcessor::setStateInformation (const void* data, int sizeInBytes)
{
    // Restore plugin state
    std::unique_ptr<juce::XmlElement> xmlState (getXmlFromBinary (data, sizeInBytes));
    
    if (xmlState.get() != nullptr)
    {
        if (xmlState->hasTagName ("AlioopPluginState"))
        {
            lastClientName = xmlState->getStringAttribute ("lastClientName");
            lastClientEmail = xmlState->getStringAttribute ("lastClientEmail");
            lastDeliveryPrice = (float) xmlState->getDoubleAttribute ("lastDeliveryPrice", 50.0);
        }
    }
}

//==============================================================================
// Alioop-specific functionality

void AlioopAudioProcessor::startRecording()
{
    recording = true;
    recordedSamples = 0;
    recordedBuffer.clear();
}

void AlioopAudioProcessor::stopRecording()
{
    recording = false;
}

double AlioopAudioProcessor::getRecordedDuration() const
{
    if (currentSampleRate <= 0.0)
        return 0.0;
    return recordedSamples / currentSampleRate;
}

void AlioopAudioProcessor::sendDelivery(const juce::String& clientName,
                                        const juce::String& clientEmail,
                                        const juce::String& clientPhone,
                                        float deliveryPrice,
                                        const juce::String& serviceName)
{
    // Save for next time
    lastClientName = clientName;
    lastClientEmail = clientEmail;
    lastDeliveryPrice = deliveryPrice;
    
    // Use API handler to send
    if (apiHandler)
    {
        apiHandler->sendDelivery(clientName, clientEmail, clientPhone, 
                                deliveryPrice, serviceName, recordedBuffer, 
                                currentSampleRate);
    }
}

//==============================================================================
// Plugin factory
juce::AudioProcessor* JUCE_CALLTYPE createPluginFilter()
{
    return new AlioopAudioProcessor();
}
