# IIDX 31 Common Problems/Tips

<img src="/img/iidx31/epolis.png">

!!! note "Author Note:"
	For lightning specific issues, see [lightning cab notes](lightning.md#lightning-specific-troubleshooting)

### My Game Is Running Crazy Fast!

!!! tip ""
	The most common reason for this is the game is running over its required 60hz or 120hz framerate, depending on if you're in LDJ or TDJ mode. The game is hardcoded to run at these specific framerates and this cannot be changed. To solve this, set your monitor's refresh rate to match if you're in LDJ 60hz or TDJ 120hz mode. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard or around 120.00hz. If it's not around there and your monitor is indeed set correctly for the given mode, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Occasional Game Stutters During Play

!!! tip ""
	Sometimes you might have occasional stutters during play, while solutions can vary wildly from general performance issues to bad hard drives, try adding SpiceTools `-realtime` parameter to your .bat file.

### My Inputs Aren't Working / I Can't Get Past The Error Messages

!!! tip ""
	If *none* of your inputs are working, try updating [spice2x](https://spice2x.github.io/), you can also try using the beta versions if the stable releases don't work for you.

### My Game Audio Sounds Like A PS1 Horror Game

!!! tip ""
	If you decided to use `WASAPI`, make sure your `Playback Device` is set to `48000 Hz`. You can read up on it [here.](setup.md#getting-started)

### My Game Audio Is Super Quiet!

!!! tip ""
	When using `TDJ mode` the audio is very quiet by default. To mitigate this, you can use the `Increase Game Volume` patch.

### Which Offset Is Which?

!!! tip ""
	If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).

### When I Run This Game All Other Background Audio Is Gone! What's Going On?

!!! tip ""
	64-bit versions of IIDX are now utilizing a feature in Windows called [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) to obtain less audio latency than the former 32-bit versions of the games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound). You can use the `WASAPI Shared Mode` patch to avoid this issue.

### I'm Not Getting Any Audio/My Audio Is Completely Wrecked and I'm Using an External Dac!

!!! tip ""
	Several external DACs have issues with [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) and are unable to be used entirely, it's likely you'll be forced to use your motherboard's sound chip, or find a compatible DAC.


