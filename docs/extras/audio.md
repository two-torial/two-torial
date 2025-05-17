# Audio

!!! warning "Synopsis"

    This guide explains the different audio modes commonly found in arcade games and their pros and cons, helping you choose the best option for your setup.

!!! danger "Important notice"

    **Recordings and streams must only be shared privately:**
    
    - Through unlisted videos
    - In private streams with friends
    - Within trusted data communities
    
    Sharing content publicly puts you at serious risk of getting banned from arcade venues and communities. Please respect these guidelines.


## Audio modes

### TL;DR

| Mode                   | DirectSound        | WASAPI Shared      | WASAPI Exclusive  | ASIO                          |
| ---------------------- | :----------------: | :----------------: | :---------------: | :--------------------------:  |
| Latency                | Highest            | Medium             | Low               | Lowest when setup correctly   |
| Compatibility          | Highest            | High               | High              | Low                           |
| Multiple audio streams | :material-check:   | :material-check:   | :material-close:  | with extra steps              |
| Audio capture          | :material-check:   | :material-check:   | :material-close:  | with extra steps              |
| Recommended for        | Legacy games       | Most users         | Low latency needs | Lower latency needs           |

### DirectSound

!!! tip ""

    The legacy Windows audio system, still used by older games.

    ✔️ **Pros**:

      - Extremely high compatibility, especially with older games
      - Multiple audio sources can play simultaneously
      - Easy audio capture with OBS, Discord etc.
      - Simple to set up and use

    ❌ **Cons**:

      - Highest latency of all modes
      - Being phased out in favor of WASAPI
      - Limited audio quality compared to modern modes

### WASAPI Shared

!!! tip ""

    The modern Windows standard audio mode. Recommended for most users.

    ✔️ **Pros**:

      - Works with most modern games and applications
      - Multiple audio sources can play simultaneously
      - Easy audio capture with OBS, Discord etc.
      - Good balance of latency and compatibility

    ❌ **Cons**:

      - Higher latency than Exclusive mode
      - Some games may require patches/configuration for Shared mode

    💡 **Pro tip**: Use spice2x's `-lowlatencysharedaudio` setting to reduce latency.

### WASAPI Exclusive

??? warning "Hardware compatibility notice"

    Your audio device must explicitly support exclusive mode. Check your audio settings:

    <img src="/img/common/audio_exclusive.png">

!!! tip ""

    Gives one application complete control over the audio device.

    ✔️ **Pros**:

      - Significantly lower latency than Shared mode
      - More consistent audio processing than Shared mode
      - Better for rhythm games if you don't mind the cons

    ❌ **Cons**:

      - Only one application can output audio at a time
      - No audio capture without special hardware/software
      - Can cause system-wide audio interruptions

### ASIO

!!! warning "Hardware requirements"

    For optimal results, use a dedicated ASIO-compatible audio interface. Software solutions like [ASIO4ALL](https://asio4all.org/) or [FlexASIO](https://github.com/dechamps/FlexASIO) exist but have limitations:

    - Added processing overhead
    - May not improve latency over WASAPI Exclusive
    - Mostly useful when:
        - Games are incompatible with your audio device
        - ASIO is the only supported mode
        - You need specific ASIO features

!!! tip ""

    Professional audio standard designed for audio interfaces and music production.

    ✔️ **Pros**:

      - Lowest possible latency when properly configured
      - Direct hardware control
      - Precise buffer size adjustment
      - Professional-grade audio quality
      - Bypass Windows audio stack
	  - Capture is possible when routed through Voicemeeter at the cost of very little added latency

    ❌ **Cons**:

      - Requires specialized hardware for best results
      - Complex setup process
      - Usually limited to one application at a time
      - No direct audio capture support
      - System performance heavily impacts stability
      - May require significant tweaking

## ASIO Recording/Streaming

!!! info "This guide assumes you have ASIO working with your game and want to record or stream gameplay with audio."

!!! tip "Required Software"

    ASIO bypasses the Windows audio system that recording/streaming applications use, so you'll need additional software to route the audio:

    - [Voicemeeter Banana](https://vb-audio.com/Voicemeeter/banana.htm) - For audio routing
    - [OBS Studio](https://obsproject.com/) - For recording and streaming

    Install both applications before continuing.

!!! tip "Game Configuration"

    Set your game's ASIO output device to `Voicemeeter Virtual ASIO`:

    - For spice2x games: Look for settings like `-iidxasio` or `-sdvxasio` at the top of spicecfg's `Options` tab
    - For other games: The location depends on your setup, but look for ASIO device selection

??? tip "Voicemeeter Setup"

    Configure ASIO output:

    1. Click the `A1` button in the top right
    2. Select `ASIO (Steinberg)` from the dropdown
    3. Choose your ASIO device

    Configure audio routing:

    1. Find the 4th column in the interface
    2. Enable only `A1` and `B1` toggles

    <img src="/img/extras/audio/voicemeeter_outputs.png">

    Recommended settings (Menu > Options):

    <img src="/img/extras/audio/voicemeeter_menuopts.png">

    These settings ensure Voicemeeter starts with Windows and auto-recovers from audio issues.

??? tip "OBS Studio Setup"

    1. Complete the initial configuration wizard if this is a new installation

    2. Add game audio:
        - Add an Audio Input Capture source
        <img src="/img/extras/audio/obs_inputcapture.png">
        - Select `B1` as the device
        <img src="/img/extras/audio/obs_capturedevice.png">

    3. Configure audio monitoring:
        - Open Advanced Audio Properties (gear icon in audio mixer)
        - Set Audio Input Capture to `Monitor and Output`
        <img src="/img/extras/audio/obs_monitorandoutput.png">

    4. Configure audio settings:
        - Open Settings (`File` > `Settings`)
        <img src="/img/extras/audio/obs_settings.png">
        - In the `Audio` tab:
            - Match sample rate with your game/ASIO settings
            - Set monitoring device to any unused "Voicemeeter In" (1-5)
        <img src="/img/extras/audio/obs_audiosettings.png">
        - Click `Apply` then `OK`

    5. Add game video capture:
        - Add either `Display Capture` or `Game Capture` source
        - Configure OBS video/output settings as needed

    **Now nearly everything should be ready to go!**

    - For Discord: Right-click OBS preview > `Fullscreen Projector (Preview)` > Share the projector window in Discord
    - For recording: Click `Start Recording`
    - For streaming: Configure unlisted stream settings > Click `Start Streaming`