# SOUND VOLTEX EXCEED GEAR
<img class="header-logo" src="/img/bemani/sdvx/6_exceedgear/logo.png">

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---
### I'm having performance issues!

!!! tip ""

    If you're having performance issues of some kind, spice2x's [PC optimization](https://github.com/spice2x/spice2x.github.io/wiki/PC-optimization) guide is worth looking at.

---
### My game is running slow/fast, After finishing a song the game gets stuck loading!

!!! tip ""

	The most common reason for this is the game is running over its required refresh rate.  
	To solve this, make sure v-sync isn't disabled in your graphics card's settings.

	For NVIDIA users, enable  `NVIDIA profile optimization (-nvprofile)` in the `Options` tab. 

---
### How do I set my offset?

!!! tip ""

	Play through a chart you're comfortable with.

	If you're getting too many `Late`, decrease your offset `(-)`.  
	If you're getting too many `Early`, increase your offset `(+)`.  

	Sound Voltex Exceed Gear has two types of offset adjustments, visual and audio based, so be sure to fiddle with both to find desirable settings.

---
### How do I run the game windowed borderless?

!!! tip ""

	Some players utilize windowed mode and use 3rd party software called [Borderless Gaming](https://github.com/Codeusa/Borderless-Gaming/releases) in order to achieve this, follow the program's instructions accordingly.

---
### Where are all the navigators?

!!! tip ""

	Many navigators are locked behind network requirements and they will not show unless connected to a network that has written support for the events they're typically locked behind.

---
### My game audio is super quiet!

!!! tip ""

	Press your `Test` key to enter its menu, go to `SOUND OPTIONS` and change the volume from `20` to `30`.

---
### When I run the game all other audio is gone!

!!! tip ""

	Sound Voltex Exceed Gear uses [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) for audio to get better audio latency.  
	Unlike former versions of the games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound).   
	
	You can use the `Shared Mode WASAPI` patch to deal with some hardware issues, it can also be used to hear audio outside the game at the cost of audio latency.  

---
### I'm not getting any audio / My game crashes due to audio

!!! tip ""

	Many setups have found some difficulty with audio due to various equipment being used. Consider using the `Shared Mode WASAPI` patch.
