<img class="header-logo" src="/img/konami/nostalgia/op2/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Hardware Specs

!!! tip ""
    Konami PC Type 6 (ADE-704A)

    Based on an AMD Embedded R Series SoC.

    CPU: Intel Celeron B810

    GPU: AMD Radeon E4690

    OS: Windows 7 Embedded 

### My Game Is Running Slow/Lagging

!!! tip ""
    Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast!

!!! tip ""
    The most common reason for this is the game is running over its required 60 Hz, the game is hardcoded to run at 60 Hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60 Hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60 Hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Occasional Game Stutters During Play

!!! tip ""
    Sometimes you might have occasional stutters during play, while solutions can vary wildly from general performance issues to bad hard drives, try adding SpiceTools `-realtime` parameter to your .bat file.

### Which Offset Is Which?

!!! tip ""
    If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).

### No Matter What I Do, the Game Crashes and I Have Multiple Monitors!

!!! tip ""
    This problem is somewhat irregular, but sometimes Nostalgia has issues booting with multiple monitors present, particularly when trying to boot the game windowed. Make sure you're running the latest SpiceTools which has attempted to resolve all instances of this issue.


