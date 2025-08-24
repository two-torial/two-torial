<img class="header-logo" src="/img/konami/sdvx/5_vividwave/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Hardware Specs

!!! tip ""

    Konami PC Type 4

    CPU: Intel i3-4300 3.5GHz

    GPU: Nvidia GeForce GTX 1050 2GB

    RAM: 8GB DDR3L PC3-12800 (4GB*2)

    OS: Windows 7 Embedded

### My Game Is Running Slow/Lagging

!!! tip ""

    Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

    At the time of writing, some individuals with more than capable PCs have had framerate issues, most notably with Ryzen CPUs. There's really no fix as the issues seem largely random, but it's worth noting regardless to consider trying different computers if you have them available.

### My Game Is Running Crazy Fast/After Finishing a Song Loading Is Stuck

!!! tip ""

    The most common reason for this is the game is running over its required 60 Hz, the game is hardcoded to run at 60 Hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60 Hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60 Hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Which Offset Is Which?

!!! tip ""

    If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-). Sound Voltex V has two types of offset adjustments, visual and audio based, so be sure to fiddle with both to find desirable settings.

### Running the Game Windowed and Borderless

!!! tip ""

    Some players utilizing windowed mode use 3rd party software called [Borderless Gaming](https://github.com/Codeusa/Borderless-Gaming/releases) in order to achieve this, follow the program's instructions accordingly.

### Where Are All the Navigators?

!!! tip ""

    Many navigators are locked behind network requirements and they will not show unless connected to a network that has written support for the events that they're typically locked behind.

### A Note About SSE 4.2

!!! tip ""

    In the rare case you are running this game on *very* old hardware, SDVX V requires a processor supporting the [SSE 4.2 instruction set](https://en.wikipedia.org/wiki/SSE4#SSE4.2). But, in the event your processor does not have this, there is a patch available to bypass this.

### When I Run This Game All Other Background Audio Is Gone! What's Going On?

!!! tip ""

    64-bit versions of SDVX     are now utilizing a feature in Windows called [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) to obtain less audio latency than the former 32-bit versions of the games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound). You can use the `Shared Mode WASAPI` patch to deal with some hardware issues, it can also be used to hear background audio outside the game so that the game does not take total control. Many have reported that this edit only works when the audio is set to either 16-bit 44100Hz or 24-bit 44100Hz.

### I'm Not Getting Any Audio/My Audio Is Completely Wrecked and I'm Using an External Dac!

!!! tip ""

    Several external DACs have issues with [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) and are unable to be used entirely, it's likely you'll be forced to use your motherboard's sound chip, or find a compatible DAC.

    Alongside this, many setups have found some difficulty with audio due to various equipment being used. Consider applying the `Shared Mode WASAPI` patch.
