<img class="header-logo" src="/img/bemani/museca/1plushalf/logo.png">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Hardware Specs

!!! tip ""
	Bemani PC (ADE-6291)

	Konami (2018)

	Based on an AMD Embedded R Series SoC.

	CPU: AMD RX-421BD

	GPU: Radeon R7

	RAM: 4 GB

	OS: Windows 7 Embedded 

### My Game Is Running Slow/Lagging

!!! tip ""
	Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast!

!!! tip ""
	The most common reason for this is the game is running over its required 60hz, the game is hardcoded to run at 60hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Occasional Game Stutters During Play

!!! tip ""
	Sometimes you might have occasional stutters during play, while solutions can vary wildly from general performance issues to bad hard drives, try adding SpiceTools `-realtime` parameter to your .bat file.

### Which Offset Is Which?

!!! tip ""
	If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).

### Booting the Game in Offline Mode

!!! tip ""
	If your game version is PIX-2018073002, this version supports turning off E-Amusement. In order to do that, change the game code to `J:B:A` (`<spec>B</spec>` in `prop/ea3-config.xml`), disable/disconnect all network adapters and turn set the E-Amusement setting in the game's operator menu to OFF.

### When I Run This Game All Other Background Audio Is Gone! What's Going On?

!!! tip ""
	Museca is a 64-bit game utilizing a feature in Windows called [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) to obtain less audio latency. Unfortunately, this cannot be changed.

### I'm Not Getting Any Audio/My Audio Is Completely Wrecked and I'm Using an External Dac!

!!! tip ""
	Several external DACs have issues with [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) and are unable to be used entirely, it's likely you'll be forced to use your motherboard's sound chip, or find a compatible DAC.