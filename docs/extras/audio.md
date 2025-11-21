!!! info "Synopsis"

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

    💡 **Pro tip**: Use spice2x's `-lowlatencysharedaudio` setting to reduce latency.

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

    <img src="/img/common/audio_exclusive.webp">

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

!!! info "This guide assumes your game already uses ASIO and you want to record/stream with audio"

### Required software

!!! tip ""

    ASIO bypasses the Windows audio system that recording/streaming applications use, so you'll need additional software to route the audio:

    - [Voicemeeter Banana](https://vb-audio.com/Voicemeeter/banana.htm) - For audio routing
    - [OBS Studio](https://obsproject.com/) - For recording and streaming

    Install both applications before continuing.

### Game configuration

!!! tip ""

    Set your game's ASIO output device to `Voicemeeter Virtual ASIO`:

    - For spice2x games: Look for settings like `-iidxasio` or `-sdvxasio` at the top of spicecfg's `Options` tab
    - For other games: The location depends on your setup, but look for ASIO device selection

### Voicemeeter configuration

!!! tip ""

    First, configure recommended settings:

    1. Click `Menu` in the top right
    2. Enable settings shown below to ensure Voicemeeter:
        - Starts with Windows
        - Auto-recovers from audio issues

    <img src="/img/extras/audio/voicemeeter_menuopts.webp">

    Next, set up ASIO output:

    1. Click the `A1` button in the top right
    2. Select the `ASIO (Steinberg)` tab 
    3. Choose your ASIO device

    Finally, configure audio routing:

    1. Locate the 4th column in the interface
    2. Enable only the `A1` and `B1` toggles as shown:

    <img src="/img/extras/audio/voicemeeter_outputs.webp">

### OBS Studio Configuration

!!! tip ""

    1. Run OBS Studio's initial configuration wizard if you haven't already

    2. Set up audio capture:
        - In the Sources panel, click `+` and select `Audio Input Capture`
        <img src="/img/extras/audio/obs_inputcapture.webp">
        - For the Device, select `VoiceMeeter Output (B1)`
        <img src="/img/extras/audio/obs_capturedevice.webp">

    3. Enable audio monitoring:
        - Click the gear icon in the Audio Mixer panel
        - Find your Audio Input Capture source
        - Change `Audio Monitoring` to `Monitor and Output`
        <img src="/img/extras/audio/obs_monitorandoutput.webp">

    4. Configure OBS audio settings:
        - Go to `File` > `Settings`
        <img src="/img/extras/audio/obs_settings.webp">
        - In the `Audio` tab:
            - Set `Sample Rate` to match your ASIO/game settings
            - For `Monitoring Device`, select any unused input such as a `VoiceMeeter In`
        <img src="/img/extras/audio/obs_audiosettings.webp">
        - Save changes with `Apply` and `OK`

    5. Add video capture:
        - In Sources, add either `Display Capture` or `Game Capture`
        - Adjust OBS video and output settings as needed

### Using this setup

!!! tip ""

    First, ensure Voicemeeter and OBS Studio are running.

    Next, configure your desired OBS output and video settings.

    - For streaming and recording, now use OBS as normal.

    - For Discord sharing:
        - Right-click the OBS preview window
        - Select `Fullscreen Projector (Preview)` 
        - Choose which monitor to show the projector on
        - Press Alt+Tab to switch away from the projector window
        - In Discord, share the projector window

### Further reading

* [spice2x wiki](https://github.com/spice2x/spice2x.github.io/wiki/Audio-modes-demystified)
