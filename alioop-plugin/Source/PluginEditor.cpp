/*
  ==============================================================================

    Alioop Send - Plugin Editor (UI)
    Implementation

  ==============================================================================
*/

#include "PluginProcessor.h"
#include "PluginEditor.h"

//==============================================================================
AlioopAudioProcessorEditor::AlioopAudioProcessorEditor (AlioopAudioProcessor& p)
    : AudioProcessorEditor (&p), audioProcessor (p)
{
    // Set editor size
    setSize (500, 600);
    
    // Title
    titleLabel.setText ("Alioop Send", juce::dontSendNotification);
    titleLabel.setFont (juce::Font (32.0f, juce::Font::bold));
    titleLabel.setColour (juce::Label::textColourId, orangeColor);
    titleLabel.setJustificationType (juce::Justification::centred);
    addAndMakeVisible (titleLabel);
    
    // Client Name
    clientNameLabel.setText ("Client Name:", juce::dontSendNotification);
    clientNameLabel.setFont (juce::Font (16.0f));
    clientNameLabel.setColour (juce::Label::textColourId, creamColor);
    addAndMakeVisible (clientNameLabel);
    
    clientNameEditor.setColour (juce::TextEditor::backgroundColourId, blackColor);
    clientNameEditor.setColour (juce::TextEditor::textColourId, creamColor);
    clientNameEditor.setColour (juce::TextEditor::outlineColourId, orangeColor);
    clientNameEditor.setFont (juce::Font (14.0f));
    addAndMakeVisible (clientNameEditor);
    
    // Client Email
    clientEmailLabel.setText ("Client Email:", juce::dontSendNotification);
    clientEmailLabel.setFont (juce::Font (16.0f));
    clientEmailLabel.setColour (juce::Label::textColourId, creamColor);
    addAndMakeVisible (clientEmailLabel);
    
    clientEmailEditor.setColour (juce::TextEditor::backgroundColourId, blackColor);
    clientEmailEditor.setColour (juce::TextEditor::textColourId, creamColor);
    clientEmailEditor.setColour (juce::TextEditor::outlineColourId, orangeColor);
    clientEmailEditor.setFont (juce::Font (14.0f));
    addAndMakeVisible (clientEmailEditor);
    
    // Client Phone
    clientPhoneLabel.setText ("Client Phone (optional):", juce::dontSendNotification);
    clientPhoneLabel.setFont (juce::Font (16.0f));
    clientPhoneLabel.setColour (juce::Label::textColourId, creamColor);
    addAndMakeVisible (clientPhoneLabel);
    
    clientPhoneEditor.setColour (juce::TextEditor::backgroundColourId, blackColor);
    clientPhoneEditor.setColour (juce::TextEditor::textColourId, creamColor);
    clientPhoneEditor.setColour (juce::TextEditor::outlineColourId, orangeColor);
    clientPhoneEditor.setFont (juce::Font (14.0f));
    addAndMakeVisible (clientPhoneEditor);
    
    // Price
    priceLabel.setText ("Delivery Price ($):", juce::dontSendNotification);
    priceLabel.setFont (juce::Font (16.0f));
    priceLabel.setColour (juce::Label::textColourId, creamColor);
    addAndMakeVisible (priceLabel);
    
    priceEditor.setText ("50");
    priceEditor.setColour (juce::TextEditor::backgroundColourId, blackColor);
    priceEditor.setColour (juce::TextEditor::textColourId, creamColor);
    priceEditor.setColour (juce::TextEditor::outlineColourId, orangeColor);
    priceEditor.setFont (juce::Font (14.0f));
    addAndMakeVisible (priceEditor);
    
    // Service
    serviceLabel.setText ("Service Name:", juce::dontSendNotification);
    serviceLabel.setFont (juce::Font (16.0f));
    serviceLabel.setColour (juce::Label::textColourId, creamColor);
    addAndMakeVisible (serviceLabel);
    
    serviceEditor.setText ("Mixing");
    serviceEditor.setColour (juce::TextEditor::backgroundColourId, blackColor);
    serviceEditor.setColour (juce::TextEditor::textColourId, creamColor);
    serviceEditor.setColour (juce::TextEditor::outlineColourId, orangeColor);
    serviceEditor.setFont (juce::Font (14.0f));
    addAndMakeVisible (serviceEditor);
    
    // Record Button
    recordButton.setButtonText ("Start Recording");
    recordButton.setColour (juce::TextButton::buttonColourId, grayColor);
    recordButton.setColour (juce::TextButton::textColourOffId, creamColor);
    recordButton.onClick = [this] { recordButtonClicked(); };
    addAndMakeVisible (recordButton);
    
    // Send Button
    sendButton.setButtonText ("Send Delivery");
    sendButton.setColour (juce::TextButton::buttonColourId, orangeColor);
    sendButton.setColour (juce::TextButton::textColourOffId, blackColor);
    sendButton.onClick = [this] { sendButtonClicked(); };
    addAndMakeVisible (sendButton);
    
    // Status Label
    statusLabel.setText ("Ready to record", juce::dontSendNotification);
    statusLabel.setFont (juce::Font (14.0f));
    statusLabel.setColour (juce::Label::textColourId, grayColor);
    statusLabel.setJustificationType (juce::Justification::centred);
    addAndMakeVisible (statusLabel);
    
    // Duration Label
    durationLabel.setText ("Duration: 0:00", juce::dontSendNotification);
    durationLabel.setFont (juce::Font (14.0f));
    durationLabel.setColour (juce::Label::textColourId, creamColor);
    durationLabel.setJustificationType (juce::Justification::centred);
    addAndMakeVisible (durationLabel);
    
    // Start timer for UI updates
    startTimer (100); // Update every 100ms
}

AlioopAudioProcessorEditor::~AlioopAudioProcessorEditor()
{
    stopTimer();
}

//==============================================================================
void AlioopAudioProcessorEditor::paint (juce::Graphics& g)
{
    // Background
    g.fillAll (blackColor);
    
    // Orange header bar
    g.setColour (orangeColor);
    g.fillRect (0, 0, getWidth(), 80);
    
    // Subtle border
    g.setColour (grayColor);
    g.drawRect (getLocalBounds(), 1);
}

void AlioopAudioProcessorEditor::resized()
{
    auto area = getLocalBounds();
    
    // Title area
    titleLabel.setBounds (area.removeFromTop (80).reduced (10));
    
    area.removeFromTop (20); // Spacing
    
    auto formArea = area.reduced (20);
    
    // Client Name
    clientNameLabel.setBounds (formArea.removeFromTop (25));
    formArea.removeFromTop (5);
    clientNameEditor.setBounds (formArea.removeFromTop (30));
    formArea.removeFromTop (15);
    
    // Client Email
    clientEmailLabel.setBounds (formArea.removeFromTop (25));
    formArea.removeFromTop (5);
    clientEmailEditor.setBounds (formArea.removeFromTop (30));
    formArea.removeFromTop (15);
    
    // Client Phone
    clientPhoneLabel.setBounds (formArea.removeFromTop (25));
    formArea.removeFromTop (5);
    clientPhoneEditor.setBounds (formArea.removeFromTop (30));
    formArea.removeFromTop (15);
    
    // Price
    priceLabel.setBounds (formArea.removeFromTop (25));
    formArea.removeFromTop (5);
    priceEditor.setBounds (formArea.removeFromTop (30));
    formArea.removeFromTop (15);
    
    // Service
    serviceLabel.setBounds (formArea.removeFromTop (25));
    formArea.removeFromTop (5);
    serviceEditor.setBounds (formArea.removeFromTop (30));
    formArea.removeFromTop (20);
    
    // Duration
    durationLabel.setBounds (formArea.removeFromTop (25));
    formArea.removeFromTop (10);
    
    // Buttons
    auto buttonArea = formArea.removeFromTop (50);
    recordButton.setBounds (buttonArea.removeFromLeft (buttonArea.getWidth() / 2).reduced (5));
    sendButton.setBounds (buttonArea.reduced (5));
    
    formArea.removeFromTop (15);
    
    // Status
    statusLabel.setBounds (formArea.removeFromTop (30));
}

void AlioopAudioProcessorEditor::timerCallback()
{
    // Update duration display
    if (audioProcessor.isRecording())
    {
        double duration = audioProcessor.getRecordedDuration();
        int minutes = (int)(duration / 60.0);
        int seconds = (int)duration % 60;
        
        durationLabel.setText (juce::String::formatted ("Duration: %d:%02d", minutes, seconds),
                              juce::dontSendNotification);
    }
}

void AlioopAudioProcessorEditor::recordButtonClicked()
{
    if (audioProcessor.isRecording())
    {
        // Stop recording
        audioProcessor.stopRecording();
        recordButton.setButtonText ("Start Recording");
        recordButton.setColour (juce::TextButton::buttonColourId, grayColor);
        statusLabel.setText ("Recording stopped - ready to send", juce::dontSendNotification);
        statusLabel.setColour (juce::Label::textColourId, orangeColor);
    }
    else
    {
        // Start recording
        audioProcessor.startRecording();
        recordButton.setButtonText ("Stop Recording");
        recordButton.setColour (juce::TextButton::buttonColourId, orangeColor);
        statusLabel.setText ("Recording audio...", juce::dontSendNotification);
        statusLabel.setColour (juce::Label::textColourId, orangeColor);
    }
}

void AlioopAudioProcessorEditor::sendButtonClicked()
{
    // Validate inputs
    if (clientNameEditor.getText().isEmpty())
    {
        juce::AlertWindow::showMessageBoxAsync (juce::AlertWindow::WarningIcon,
                                                "Missing Information",
                                                "Please enter client name");
        return;
    }
    
    if (clientEmailEditor.getText().isEmpty())
    {
        juce::AlertWindow::showMessageBoxAsync (juce::AlertWindow::WarningIcon,
                                                "Missing Information",
                                                "Please enter client email");
        return;
    }
    
    // Get price
    float price = priceEditor.getText().getFloatValue();
    if (price <= 0.0f)
        price = 50.0f;
    
    // Stop recording if still active
    if (audioProcessor.isRecording())
        audioProcessor.stopRecording();
    
    // Show confirmation
    juce::String confirmMsg = "Send delivery to:\n\n" +
                             clientNameEditor.getText() + "\n" +
                             clientEmailEditor.getText() + "\n\n" +
                             "Price: $" + juce::String(price, 2) + "\n" +
                             "Service: " + serviceEditor.getText();
    
    bool confirmed = juce::NativeMessageBox::showOkCancelBox(
        juce::MessageBoxIconType::QuestionIcon,
        "Confirm Delivery",
        confirmMsg,
        nullptr,
        nullptr
    );
    
    if (confirmed)
    {
        statusLabel.setText ("Sending delivery...", juce::dontSendNotification);
        statusLabel.setColour (juce::Label::textColourId, orangeColor);
        
        // Send via processor
        audioProcessor.sendDelivery (clientNameEditor.getText(),
                                    clientEmailEditor.getText(),
                                    clientPhoneEditor.getText(),
                                    price,
                                    serviceEditor.getText());
        
        statusLabel.setText ("Delivery sent!", juce::dontSendNotification);
        
        // Reset for next delivery
        durationLabel.setText ("Duration: 0:00", juce::dontSendNotification);
        recordButton.setButtonText ("Start Recording");
        recordButton.setColour (juce::TextButton::buttonColourId, grayColor);
    }
}
