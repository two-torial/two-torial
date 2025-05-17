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

    - Add processing overhead
    - May not improve latency over WASAPI Exclusive
    - Best used when:
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
	  - Capture is possible when routed through VoiceMeeter at the cost of very little added latency

    ❌ **Cons**:

      - Requires specialized hardware for best results
      - Complex setup process
      - Usually limited to one application at a time
      - No direct audio capture support
      - System performance heavily impacts stability
      - May require significant tweaking