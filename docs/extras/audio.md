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

| 	 	                 | DirectSound 		  | WASAPI Shared      | WASAPI Exclusive  | ASIO                          |
| ---------------------- | :----------------: | :----------------: | :---------------: | :--------------------------:  |
| Latency                | Highest            | Medium             | Low               | Lowest when setup correctly   |
| Compatibility          | Highest 			  | High               | High              | Low                           |
| Multiple audio streams | :material-check:	  | :material-check:   | :material-close:  | with extra steps 			   |
| Audio capture          | :material-check:   | :material-check:   | :material-close:  | with extra steps              |

### DirectSound

!!! tip ""

	Very similar to WASAPI Shared, with higher latency and compatibility. Typically used by older games.

	✔️ **Pros**:

	  - Multiple audio sources can be sent to one audio device.
	  - Audio can be captured using OBS or Discord for example.
	  - Very high compatibility.

	❌ **Cons**:

	  - Higher latency than WASAPI Shared.
	  - Mostly used by older games.

### WASAPI Shared

!!! tip ""

	This is the standard for Windows. Allows **all** applications to have **partial** control of your audio device.

	✔️ **Pros**:

	  - Multiple audio sources can be sent to one audio device.
	  - Audio can be captured using OBS or Discord for example.
	  - Greater compatibility as this is the Windows standard.

	❌ **Cons**:

	  - Higher latency than WASAPI Exclusive.
	  - Not all games support Shared audio. Some WASAPI Exclusive games can be configured or patched to work, some can't.

	This is the **recommended mode to use for most games**, unless its latency is not acceptable to you.
	
	**Note**: there are ways to lower latency slightly, for example with spice2x's `-lowlatencysharedaudio` setting.

### WASAPI Exclusive

??? warning "Your audio device must support this and be configured to allow being taken over by applications."

	<img src="/img/common/audio_exclusive.png">

!!! tip ""

	Allows **one** application to have **exclusive** control of your audio device.

	✔️ **Pros**:

	  - Lower latency than WASAPI Shared.

	❌ **Cons**:

	  - Can't hear applications other than the one who took ownership of your audio device.
	  - Can't capture audio using OBS or Discord.

### ASIO

!!! tip ""

	ASIO is a driver designed for audio interfaces, typically used by musicians and audio professionals.

	It skips Windows audio overhead by letting applications communicate with compatible audio interfaces directly.

	✔️ **Pros**:

	  - Gives you direct control over buffer size.
	  - *Can* (but won't always) allow for lower latency than WASAPI exclusive.

	❌ **Cons**:

	  - Requires an ASIO compatible audio interface.
	  - Requires extra setup for most games.
	  - Most interfaces won't allow Shared audio playback, meaning the ASIO driver can only be used by one application at a time.
	  - Can't capture audio using OBS or Discord by default, workarounds exist at the cost of slightly higher latency.
	  - Gets unstable as you lower the buffer size to achieve lower latency, **your results will greatly vary depending on how powerful and optimized your system is**.

	**Note**: Yes, ASIO can be used without specialized hardware, using software like ASIO4ALL and FlexASIO. However the extra setup and resulting latency are typically not worth the hassle. Seriously consider using WASAPI instead.