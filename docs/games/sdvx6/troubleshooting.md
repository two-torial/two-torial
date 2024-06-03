# SOUND VOLTEX EXCEED GEAR
<img src="/img/sdvx6/setup/0_exceedgear.png">

!!! info "Last updated: June 3rd, 2024"

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---
### My Game Is Running Crazy Fast/After Finishing a Song Loading Is Stuck

!!! tip ""

	The most common reason for this is the game is running over its required refresh rate.  
	To solve this, make sure v-sync isn't disabled in your graphics card's settings.

	For NVIDIA users, enable  `NVIDIA profile optimization (-nvprofile)` in the `Options` tab. 

---
### Which Offset Do I Use?

!!! tip ""

	Play through a chart you're comfortable with.

	If you're getting too many `Late`, increase your offset `(+)`.  
	If you're getting too many `Early`, decrease your offset `(-)`.  

	Sound Voltex Exceed Gear has two types of offset adjustments, visual and audio based, so be sure to fiddle with both to find desirable settings.

---
### Running the Game Windowed and Borderless

!!! tip ""

	Some players utilize windowed mode and use 3rd party software called [Borderless Gaming](https://github.com/Codeusa/Borderless-Gaming/releases) in order to achieve this, follow the program's instructions accordingly.

---
### Where Are All the Navigators?

!!! tip ""

	Many navigators are locked behind network requirements and they will not show unless connected to a network that has written support for the events they're typically locked behind.

---
### When I Run This Game All Other Background Audio Is Gone! What's Going On?

!!! tip ""

	Sound Voltex Exceed Gear uses [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) for audio to get better audio latency.  
	Former versions of the games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound).   
	
	You can use the `Shared Mode WASAPI` patch to deal with some hardware issues, it can also be used to hear audio outside the game at the cost of audio latency.  
	Many have reported that this edit only works when the audio is set to either 16-bit 44100Hz or 24-bit 44100Hz.

---
### I'm Not Getting Any Audio/My Audio Is Completely Wrecked and I'm Using an External Dac!

!!! tip ""

	Many setups have found some difficulty with audio due to various equipment being used. Consider using the `Shared Mode WASAPI` patch.
