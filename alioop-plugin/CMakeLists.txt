cmake_minimum_required(VERSION 3.15)

project(AlioopPlugin VERSION 1.0.0)

# C++17 standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find JUCE
if(NOT DEFINED JUCE_PATH)
    set(JUCE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../JUCE" CACHE PATH "Path to JUCE framework")
endif()

if(EXISTS "${JUCE_PATH}/modules")
    add_subdirectory(${JUCE_PATH} JUCE)
else()
    message(FATAL_ERROR "JUCE not found at ${JUCE_PATH}. Please set JUCE_PATH or install JUCE.")
endif()

# Create plugin target
juce_add_plugin(AlioopSend
    COMPANY_NAME "Alioop"
    COMPANY_WEBSITE "https://web-production-5748a.up.railway.app"
    COMPANY_EMAIL "info@alioop.com"
    IS_SYNTH FALSE
    NEEDS_MIDI_INPUT FALSE
    NEEDS_MIDI_OUTPUT FALSE
    IS_MIDI_EFFECT FALSE
    EDITOR_WANTS_KEYBOARD_FOCUS TRUE
    COPY_PLUGIN_AFTER_BUILD TRUE
    PLUGIN_MANUFACTURER_CODE Alop
    PLUGIN_CODE Alsd
    FORMATS VST3 AU Standalone
    PRODUCT_NAME "Alioop Send"
    BUNDLE_ID "com.alioop.plugin"
    VST3_CATEGORIES "Fx" "Tools"
    AU_MAIN_TYPE "kAudioUnitType_Effect")

# Source files
target_sources(AlioopSend PRIVATE
    Source/PluginProcessor.cpp
    Source/PluginProcessor.h
    Source/PluginEditor.cpp
    Source/PluginEditor.h
    Source/AlioopAPI.cpp
    Source/AlioopAPI.h)

# JUCE modules
target_link_libraries(AlioopSend PRIVATE
    juce::juce_audio_basics
    juce::juce_audio_devices
    juce::juce_audio_formats
    juce::juce_audio_plugin_client
    juce::juce_audio_processors
    juce::juce_audio_utils
    juce::juce_core
    juce::juce_data_structures
    juce::juce_events
    juce::juce_graphics
    juce::juce_gui_basics
    juce::juce_gui_extra
    juce::juce_recommended_config_flags
    juce::juce_recommended_lto_flags
    juce::juce_recommended_warning_flags)

# Compiler definitions
target_compile_definitions(AlioopSend PUBLIC
    JUCE_WEB_BROWSER=0
    JUCE_USE_CURL=1
    JUCE_VST3_CAN_REPLACE_VST2=0
    JUCE_DISPLAY_SPLASH_SCREEN=0
    JUCE_REPORT_APP_USAGE=0
    JUCE_STRICT_REFCOUNTEDPOINTER=1)

# Platform-specific settings
if(APPLE)
    set_target_properties(AlioopSend PROPERTIES
        XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY ""
        XCODE_ATTRIBUTE_DEVELOPMENT_TEAM "")
endif()

# Install target
install(TARGETS AlioopSend
    LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
    RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}")

# Print build info
message(STATUS "Building Alioop Send Plugin v${PROJECT_VERSION}")
message(STATUS "JUCE Path: ${JUCE_PATH}")
message(STATUS "Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Formats: VST3, AU, Standalone")
