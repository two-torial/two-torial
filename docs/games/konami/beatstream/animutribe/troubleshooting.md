<img class="header-logo" src="/img/konami/beatstream/animutribe/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

### Hardware Specs

!!! tip ""
    Bemani PC Type 6 (ADE-704A)

    Based on an AMD Embedded R Series SoC.

    CPU: Intel Celeron B810

    GPU: AMD Radeon E4690

    OS: Windows 7 Embedded 

### My Game Doesn't Boot After Following the Guide!

!!! tip ""
    The most common problem present here is if you do not have an E:/ drive. To resolve this issue, you must modify your game with the `E:/drive fix` patch.

### My Touchscreen Monitor Isn't Working

!!! tip ""
    Try adding the `-wintouch` parameter to your `.bat` file, if that doesn't work, check the log and make sure it works with windows. SpiceTools at this point works with the grand majority of touchscreen monitors but no doubt some outliers are out there!

### My Game Is Running Slow/Lagging

!!! tip ""
    Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast!

!!! tip ""
    The most common reason for this is the game is running over its required 60 Hz, the game is hardcoded to run at 60 Hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60 Hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60 Hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Which Offset Is Which?

!!! tip ""
    If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).