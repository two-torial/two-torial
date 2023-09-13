# IIDX 24 Common Problems/Tips

<img src="/img/iidx24/sb.png">

### Hardware Specs

!!! danger "Warning:"
	The specs may not be correct. If something isn't correct or it's fine, [let me know](https://github.com/yxrei/bemani-guide/issues/1).

!!! tip ""
	Bemani PC (ADE-704A)

	Konami (2012-2017)

	This board has a E4690 Radeon MXM card.

	CPU: Intel Celeron B810

	GPU: AMD Radeon E4690
	
	NIC: Realtek RTL8168/8111
	
	Chipset: Intel HM65

	RAM: 4 GB

	OS: Windows XP Embedded with Service Pack 2
	
### My Game Is Running Slow/Lagging

!!! tip ""
	Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast!

!!! tip ""
	The most common reason for this is the game is running over its required 60hz, the game is hardcoded to run at 60hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Occasional Game Stutters During Play

!!! tip ""
	Sometimes you might have occasional stutters during play, while solutions can vary wildly from general performance issues to bad hard drives, try adding SpiceTools `-realtime` parameter to your .bat file.

### HD and HD*

!!! tip ""
	This version of IIDX has two HD mode options, `HD` and `HD*` neither is inherently better than the other, the only difference is HD* is an additional + 1.0 offset in-game, the official reasoning is to account for a different set of monitors on arcade cabs. In beatmania IIDX 26 ROOTAGE this option is removed entirely and only HD is present.

### Which Offset Is Which?

!!! tip ""
	If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).


