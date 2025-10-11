<img class="header-logo" src="/img/konami/iidx/26_rootage/logo.webp">
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
    The most common reason for this is the game is running over its required 60 Hz, the game is hardcoded to run at 60 Hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60 Hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60 Hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Camera Device Error Message

!!! tip ""
    The game released with two USB cameras and naturally it's looking for them, if you do not have two cameras plugged into your computer then the game outputs this error, which can be ignored simply by hitting `Test` or waiting 60 seconds for it to be auto-dismissed.

    But if you're tired of this message every time you start up the game, the `CAMERA DEVICE ERROR` message can be removed via a patch.

### Occasional Game Stutters During Play

!!! tip ""
    Sometimes you might have occasional stutters during play, while solutions can vary wildly from general performance issues to bad hard drives, try adding SpiceTools `-realtime` parameter to your .bat file.

### HD and HD*

!!! tip ""
    This version of IIDX has removed having two HD mode options, leaving only HD. `HD` and `HD*` neither is inherently better than the other, the only difference is HD* is an additional + 1.0 offset in-game, now applied to the lone `HD` mode. The official reasoning is to account for a different set of monitors on arcade cabs.

### Which Offset Is Which?

!!! tip ""
    If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).

### A Note About SSE 4.2

!!! tip ""
    In the rare case you are running this game on *very* old hardware, IIDX 26 requires a processor supporting the [SSE 4.2 instruction set](https://en.wikipedia.org/wiki/SSE4#SSE4.2). But, in the event your processor does not have this, there is a patch available to bypass this.

### When I Run This Game All Other Background Audio Is Gone! What's Going On?

!!! tip ""
    64-bit versions of IIDX are now utilizing a feature in Windows called [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) to obtain less audio latency than the former 32-bit versions of the games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound). Unfortunately, this cannot be changed.

### I'm Not Getting Any Audio/My Audio Is Completely Wrecked and I'm Using an External Dac!

!!! tip ""
    Several external DACs have issues with [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) and are unable to be used entirely, it's likely you'll be forced to use your motherboard's sound chip, or find a compatible DAC.