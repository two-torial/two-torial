# beatmania IIDX 31 EPOLIS
<img src="/img/iidx31/epolis.png">

!!! info "Last updated: June 5th, 2024"

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

	If you're getting too many `Fast`, increase your offset `(+)`.   
	If you're getting too many `Slow`, decrease your offset `(-)`.


---
### My inputs aren't working / I can't get past error messages!

!!! tip ""

	If **none** of your inputs are working, try updating [spice2x](https://spice2x.github.io/), you can also try using the beta versions if the stable releases don't work for you.

---
### My game audio is super quiet!

!!! tip ""

	When using `TDJ mode` the audio is very quiet by default. To mitigate this, you can use the `Increase Game Volume` patch.

---
### When I run the game all other audio is gone!

!!! tip ""

	IIDX uses [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) for audio to get better audio latency.  
	Unlike former versions of the games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound).   
	
	You can use the `Shared Mode WASAPI` patch to deal with some hardware issues, it can also be used to hear audio outside the game at the cost of audio latency.

---
### I'm not getting any audio, or my audio is completely wrecked and I'm using an External Dac!

!!! tip ""

	Many setups have found some difficulty with audio due to various equipment being used. Consider using the `Shared Mode WASAPI` patch.