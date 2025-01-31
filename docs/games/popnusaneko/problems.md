Pop&apos;n Usaneko Common Problems/Tips

### Hardware Specs

!!! tip ""
	Bemani PC Type 4

	CPU: Intel Celeron B810 1.6GHz

	GPU: ATI Radeon E4690 MXM

	OS: Windows XP Embedded

### My Game Is Running Slow/Lagging

!!! tip ""
	Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast/After Finishing a Song Loading Is Stuck

!!! tip ""
	The most common reason for this is the game is running over its required 60hz, the game is hardcoded to run at 60hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Why Is the In-Game Text Garbled?

!!! tip ""
	The in-game text requires a Japanese locale to display the Japanese characters correctly, look up a guide for your specific operating system on how to switch your operating system's locale to Japanese.

### The game crashes fullscreen!

!!! tip ""
	Some monitors and display adapters may not support the odd resolution the game runs at, which is 1360x768 versus the occasionally seen 1366x768. To resolve, setup a custom resolution inside your appropriate graphic's card settings, or enable GPU resolution scaling.

### Other Crashes

!!! tip ""
	This game requires an E: drive to be named by the computer. If you do not have one, make sure to apply the `E: Drive fix` patch.

	It may also fail to boot regardless of this, such as in the case of using HDMI audio. Even if you're not using HDMI audio however, some failures to boot have been noted. For safety, make sure to also apply the `HDMI Audio Fix` patch unless you're using the latest SpiceTools which fixes this issue.

### How to Unlock Songs

!!! tip ""
	Without an appropriate patch, the game is missing song unlocks. To resolve this, you will need an unlocked DLL with BOTH the HDMI audio fix and E: drive fix already applied.

	Simply replace it with your existing one inside the `contents` folder of your game installation. When asked to replace, hit yes.