<img class="header-logo" src="/img/konami/iidx/27_heroicverse/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Hardware Specs

!!! tip ""

    (These are the specs for non-lightning model cab running Heroic Verse)

    Bemani PC Type 9 (ADE-6291)

    Konami (2017)

    Based on an AMD Embedded R Series SoC.

    CPU: AMD RX-421BD 2.1/3.4GHz APU

    GPU: Radeon R7 800Mhz

    RAM: 4 GB

    STORAGE: innodisk 3ME2 mSATA SSD 256GB

    OS: Windows 7 Embedded 

### My Game Is Running Slow/Lagging

!!! tip ""
    Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast!

!!! tip ""
    The most common reason for this is the game is running over its required 60 Hz or 120 Hz framerate, depending on if you're in LDJ or TDJ mode. The game is hardcoded to run at these specific framerates and this cannot be changed. To solve this, set your monitor's refresh rate to match if you're in LDJ 60 Hz or TDJ 120 Hz mode. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard or around 120.00hz. If it's not around there and your monitor is indeed set correctly for the given mode, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Occasional Game Stutters During Play

!!! tip ""
    Sometimes you might have occasional stutters during play, while solutions can vary wildly from general performance issues to bad hard drives, try adding SpiceTools `-realtime` parameter to your .bat file.

### Which Offset Is Which?

!!! tip ""
    If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).

### A Note About SSE 4.2

!!! tip ""
    In the rare case you are running this game on *very* old hardware, IIDX 27 requires a processor supporting the [SSE 4.2 instruction set](https://en.wikipedia.org/wiki/SSE4#SSE4.2). But, in the event your processor does not have this, there is a patch available to bypass this.

### When I Run This Game All Other Background Audio Is Gone! What's Going On?

!!! tip ""
    64-bit versions of IIDX are now utilizing a feature in Windows called [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) to obtain less audio latency than the former 32-bit versions of the games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound). Unfortunately, this cannot be changed.

### I'm Not Getting Any Audio/My Audio Is Completely Wrecked and I'm Using an External Dac!

!!! tip ""
    Several external DACs have issues with [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) and are unable to be used entirely, it's likely you'll be forced to use your motherboard's sound chip, or find a compatible DAC.