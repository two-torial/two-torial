# Workarounds for exclusive audio

!!! warning "Before reading:"
	This section describes various workarounds and tips for dealing with games that use exclusive mode audio.

	In the recent years, BEMANI games started using WASAPI exclusive mode and ASIO to output game audio. While these provide great benefit when it comes to audio latency perceived by the player, they present additional challenges when trying to use other audio applications at the same time (e.g. a Discord voice call) or when capturing game audio for recording and streaming. This page explains how you can work around these issues. Read on carefully, as there are many things that can go wrong when dealing with audio.

	**Remember, don't stream or upload recordings to public places! Privately among friends only!**

## Setting up audio

There are advantages and disadvantages to each of the methods, so read carefully.

### Option 1 - force shared audio

 - Enables: audio device sharing (voice calls while playing), recording, streaming
 - Advantage: very easy to set up, as seen below.
 - Disadvantages: may add significant audio latency to your game, depending on the game and your hardware, to a point where it becomes unplayable.

!!! tip "Sound Voltex"
	- Enable "Shared mode WASAPI" hex edit.
	- If you run into any issues, change the audio playback device to output at 44.1khz and 16 bit.

!!! tip "IIDX"
	- For TDJ mode, ensure that the sound output device is set to WASAPI.
		- In SpiceTools, set -iidxsounddevice to wasapi.
	- Enable "Force shared audio" hex edit.
	- If you run into any issues, change the audio playback device to output at 44.1khz and 16 bit.

- That's really all there is. If you use OBS or Discord to capture the game, you will not have any issues recording audio with this configuration.

### Option 2 - Stereo Mix

 - Enables: recording, streaming
 - Does NOT enable: audio device sharing (voice calls while playing)
 - Advantages: nothing to set up, no added latency to audio playback
 - Disadvantages: only works with some audio cards (most Realtek devices should work), recorded audio may be delayed or off-sync

Some sound cards have a thing called Stereo Mix, which presents itself as a recording device that mirrors everything that is being outputted from the sound card. Conveniently this can be captured even when a game has exclusive control of the audio device.

!!! tip "Enabling stereo mix"
	1. Ensure that you have the latest audio drivers.
		- For example, if you have a Realtek audio device, use a Realtek driver and not the generic Windows HD Audio driver.
	1. Go to Windows Sound device settings. In the Playback tab, make sure the default audio device is set to the sound card output (speakers or headphones).
	1. Go to Recording devices tab.
	1. Look for Stereo Mix. If you don't see it, right click and check "Show Disabled Devices" and try again.
		- <img src="/img/voicemeeter/stereomix.png">

!!! tip "Capturing audio in OBS with Stereo Mix"
	1. Add a new Audio Input Capture source.
	1. Set the device as Stereo Mix.
	1. You can now capture audio.
	1. You'll probably want to set to "Monitor Off" so you don't get duplicated audio.

### Option 3 - audio splitter cable (lo-tech method)

 - Enables: recording, streaming
 - Does NOT enable: audio device sharing (voice calls while playing)
 - Advantages: easy one-time set up, no added latency to audio playback
 - Disadvantages: costs money, recorded audio may be delayed or off-sync, audio may become quieter

!!! tip "Equipment"
	1. Buy an audio splitter cable, and a headphone extension cable.
	1. Split the audio coming out of your computer into two: one into speakers/headphones, another into the extension cable, which then goes into the "line in" port of your PC.

!!! tip "Capturing audio in OBS"
	- Add "Line In" as an audio input source.

### Option 4 - FlexASIO

 - Enables: audio device sharing (voice calls while playing), recording, streaming
 - Advantages: one-time set up, does not affect other audio configuration
 - Disadvantages: not as flexible as Voicemeeter when it comes to recording, adds a small latency

FlexASIO is a virtual ASIO service that can redirect output to various backends, including shared mode WASAPI.

!!! tip "FlexASIO set up"
	1. Install [FlexASIO](https://github.com/dechamps/FlexASIO/releases)
	1. Create a FlexASIO.toml configuration file in your user folder (C:\Users\Your Name)
	1. Insert these lines inside your configuration file:
	
			backend = "Windows WASAPI"
			bufferSizeSamples = 386
			channels = 2
			wasapiExclusiveMode = false

			[output]
			suggestedLatencySeconds = 0.0

	Try to lower bufferSizeSamples for minimal latency - recommended value is 128. If you hear audio crackling, increase bufferSizeSamples.

!!! tip "Sound Voltex"
	- Disable "Shared mode WASAPI" hex edit. You want the game to output in exclusive mode for lower overall latency.

!!! tip "IIDX"
	- For TDJ mode, ensure that the sound output device is set to WASAPI.
		- In SpiceTools, set -iidxsounddevice to wasapi.
	- Disable "Force shared audio" hex edit. You want the game to output in exclusive mode for lower overall latency.

!!! tip "SpiceTools set up to use ASIO"
	1. Under the options tab, make sure that ```IIDX Sound Output Device``` is set to default.
	2. Directly below it is an option called ```IIDX ASIO Driver```. Type ```FlexASIO``` into it.

	<img src="/img/flexasio/1.png">

- To capture audio, you can capture desktop audio as you normally would in OBS.

### Option 5 - Voicemeeter

- Enables: audio device sharing (voice calls while playing), recording, streaming
- Advantages: highly configurable, adds very little latency
- Disadvantages: can be a challenge to set up, difficult to troubleshoot when things go wrong, need to run Voicemeeter every time

Voicemeeter is free virtual audio mixer for Windows. It allows you to "mux" audio input streams into audio output streams; here, we take advantage of this application to redirect the game audio so that you enable audio capture & simultaneously enable other audio streams like voice calls.

!!! tip "Initial Voicemeeter set up"
	1. Download [Voicemeeter Potato](https://vb-audio.com/Voicemeeter/banana.htm).
		- Potato comes with all three versions - regular Voicemeeter, Banana, and Potato.
		- Regular Voicemeeter is not good enough if you are following this guide. Banana is good enough if you want to mux two audio sources (say, game audio and Discord). Potato is recommended if you want to stream to Discord via OBS using instructions in the next section.
	1. Install and **REBOOT YOUR COMPUTER** when prompted.
	1. Launch Voicemeeter Banana or Potato, whichever one you prefer.
	1. On the right hand side, you will see flashing red text that says "Select Main Output Device (A1). Look immediately to the left, click on A1 with a down arrow, and choose your output device. Typically you want the one that starts with "WDM:", but if your audio device supports it, "ASIO:" option will provide lower latency.
		- <img src="/img/voicemeeter/a1.png">
	1. In Windows sound settings, set your default audio playback device to Voicemeeter Input (and not Voicemeeter AUX Input!)

!!! tip "Discord or other voice applications"
	- Configure the output device to Voicemeeter AUX Input.

!!! tip "Sound Voltex"
	- Disable "Shared mode WASAPI" hex edit. You want the game to output in exclusive mode for lower overall latency.

!!! tip "IIDX"
	- Disable "Force shared audio" hex edit. You want the game to output in exclusive mode for lower overall latency.
	- For TDJ mode, ensure that the sound output device is set to WASAPI.
		- In SpiceTools, set -iidxsounddevice to wasapi.
	- (Optionally, you can output the game audio using SpiceTools -audiobackend asio and outputting to Voicemeeter ASIO instead of doing it over WASAPI, but probably provides negligible benefit to latency)

At this point, you may want to look up various tutorials on YouTube to learn the basics of Voicemeeter. It may be daunting at first, but once you understand the concepts, it can be a very powerful tool. Plus, you can go beyond what I demonstrate below and instead do more complicated things on your own!

!!! tip "Muxing with Voicemeeter"
	1. Launch the game.
	1. In Voicemeeter, you'll notice that the VU meter under Voicemeeter VAIO is showing that it is receiving game audio. You'll want to ensure "A1" box is green so that you route the game audio to your main output device, so you can hear the game in your ears.
		- <img src="/img/voicemeeter/vumeter.png">
	1. (Similarly, audio from the voice chat would come through Voicemeeter AUX column.)
	1. At this point, you are able to hear both the game & listen to voice chat - success!

!!! tip "Capturing audio in OBS with Voicemeeter"
	1. Now, how do you capture this audio for recording? The basic idea is to route game audio to Voicemeeter's virtual output device, and capturing that output device in OBS.
	1. In the Voicemeeter VAIO column, click on B1 to make it turn green. This connects game audio to B1 channel, which is Voicemeeter Output virtual audio device.
	1. In OBS, create a new Audio Input Capture source.
	1. Double click on the new source and select VoiceMeeter Output (VB-Audio VoiceMeeter VAIO) from the drop-down.
	1. Click on the gear icon on the audio source, click on Advanced Audio Properties. In the "Audio Monitoring" column, set it to Monitor Off. This way, you can avoid double audio in your headphones when recording.
		- (Note that if you want to stream to Discord, you'll be doing something else instead; see the steps below.)
	1. You are done. You should see the game audio come through to OBS.

## Streaming to Discord

!!! danger "Important"
	**To reiterate, do NOT stream in public places! Privately among friends only!**

If you followed Option 1 (force shared mode audio), as previously mentioned, all you need is to capture the game window and stream to Discord.

If you followed other options, a bit more work is involved to stream both video and audio at the same time. One method is to capture audio and video in OBS, and screen sharing OBS to Discord. Follow these instructions:

### Setting up Virtual Audio Monitor in OBS
We are going to make OBS capture audio and redirect the result to a virtual monitor device. In other words, OBS will be "outputting" audio to a fake speaker. Since it's still outputting audio, Discord is able to capture it, but you can avoid duplicated game audio this way.

!!! tip "Option 1 - Using Virtual Audio Cable"
	1. Download and install [Virtual Audio Cable](https://vb-audio.com/Cable/index.htm).
	1. Go to OBS Settings, Audio, Advanced, Monitoring Device - set to CABLE Input.
	1. Go to Edit, Advanced Audio Properties. For any audio channels you want to stream, turn on monitor to "Monitor and Output".

!!! tip "Option 2 - Using Voicemeeter Potato"
	1. We are going to make use of an unused virtual input device which is only available in Potato. In Banana this feature is not present.
	1. Go to OBS Settings, Audio, Advanced, Monitoring Device - set to VoiceMeeter VAIO3 Input.
		- <img src="/img/voicemeeter/obsvaio3.png">
	1. Go to Edit, Advanced Audio Properties. For any audio channels you want to stream, turn on monitor to "Monitor and Output".
	1. In VoiceMeeter Potato, prevent VAIO3 output so that you don't hear the OBS monitor audio in your ears. You can do this by disabling A1, B1, and so on in the VAIO3 column.

### Streaming OBS Windowed Preview to Discord

!!! tip ""
	1. Add the game window capture as a scene, as you normally would in OBS.
	1. Right click on OBS stage and click on Windows Projector (Preview).
		- <img src="/img/voicemeeter/projector.png">
	1. Resize the new window as needed.
	1. Use Discord to screen share this Windowed Projector.
		- <img src="/img/voicemeeter/golive.png">
	1. You're done! The screen share should include both the OBS scene and the audio.

## Troubleshooting

!!! tip "General"
	- Game is too quiet!
		- IIDX in TDJ mode is especially quiet. Try LDJ mode if you don't have a way to amplify things.

!!! tip "Voicemeeter"
	- Use the right version - Banana or Potato is recommended. Regular Voicemeeter lacks features so you can't follow the steps in this guide.
	- If you hear crackling, or if you feel the latency is too high, you'll need to adjust the buffer size. This is highly dependent on your set up; it's recommended that you search "how to fix crackling audio voicemeeter" or "how to reduce latency in voicemeeter" and you'll get lots of helpful guides.

!!! tip "Discord"
	- If Discord fails to capture audio, go to Discord settings, Voice & Video, and enable "Use an experimental method to capture audio from applications". This should already be checked by default.
