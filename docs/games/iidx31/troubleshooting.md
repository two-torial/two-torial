# beatmania IIDX 31 EPOLIS
<img src="/img/iidx30-31/epolis.png">

!!! info "Last updated: July 9th, 2024"

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---
### My game crashes on launch!

!!! tip ""

    Could be due to **many** things. The most common of which is you need to patch the DLL for your game with `Force Audio Output Mode` set to `WASAPI` or `ASIO`.
	Also see the audio section in the [setup guide](setup.md).

---
### My game is running too slow/fast / Game gets stuck / Monitor error at boot / Error 5-1503-0043

!!! tip ""

	Potential causes:

	1. The game could be running over/under its required refresh rate (60 for LDJ, 120 for TDJ)  
	To solve this, make sure v-sync isn't disabled in your graphics card's settings.
	For NVIDIA users, enable `NVIDIA profile optimization (-nvprofile)` in the `Options` tab. 
	2. It could be that your computer's performance isn't good enough to keep a steady framerate.
	
---
### I'm having performance issues / my FPS fluctates!

!!! tip ""

    If you're having performance issues of some kind, spice2x's [PC optimization](https://github.com/spice2x/spice2x.github.io/wiki/PC-optimization) guide is worth looking at.
	If none of that works, your PC probably isn't good enough to run the game, sorry.

---
### Unable to login / Eamuse error / Network error

!!! tip ""

	Get the proper Asphyxia plugin from our [Discord server](https://discord.gg/cZRUmEPK78) in the #iidx channel > Resources post.
	Make sure you didn't enable `-smartea` in spicecfg's options.

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
	
	You can use the `Shared Mode WASAPI` patch to hear other apps while the game is running, at the cost of some audio latency.

---
### I'm not getting any audio, or my audio is completely wrecked and I'm using an External Dac!

!!! tip ""

	Many setups have found some difficulty with audio due to various equipment being used. Consider using the `Shared Mode WASAPI` patch.