/*
  ==============================================================================

    Alioop Send - Plugin Editor (UI)
    Header

  ==============================================================================
*/

#pragma once

#include <juce_audio_processors/juce_audio_processors.h>
#include <juce_gui_basics/juce_gui_basics.h>
#include "PluginProcessor.h"

//==============================================================================
/**
 * Plugin UI Editor with Alioop branding
 */
class AlioopAudioProcessorEditor : public juce::AudioProcessorEditor,
                                    private juce::Timer
{
public:
    AlioopAudioProcessorEditor (AlioopAudioProcessor&);
    ~AlioopAudioProcessorEditor() override;

    //==============================================================================
    void paint (juce::Graphics&) override;
    void resized() override;
    
private:
    void timerCallback() override;
    void sendButtonClicked();
    void recordButtonClicked();
    
    // Reference to processor
    AlioopAudioProcessor& audioProcessor;
    
    // Alioop brand colors
    const juce::Colour orangeColor = juce::Colour(0xfff05709);
    const juce::Colour blackColor = juce::Colour(0xff161614);
    const juce::Colour creamColor = juce::Colour(0xfffcf5eb);
    const juce::Colour grayColor = juce::Colour(0xff71706e);
    
    // UI Components
    juce::Label titleLabel;
    
    juce::Label clientNameLabel;
    juce::TextEditor clientNameEditor;
    
    juce::Label clientEmailLabel;
    juce::TextEditor clientEmailEditor;
    
    juce::Label clientPhoneLabel;
    juce::TextEditor clientPhoneEditor;
    
    juce::Label priceLabel;
    juce::TextEditor priceEditor;
    
    juce::Label serviceLabel;
    juce::TextEditor serviceEditor;
    
    juce::TextButton recordButton;
    juce::TextButton sendButton;
    
    juce::Label statusLabel;
    juce::Label durationLabel;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (AlioopAudioProcessorEditor)
};
