<img class="header-logo" src="/img/konami/gitadora/exchain/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Hardware Specs

!!! tip ""
    Bemani PC Type 4

    CPU: AMD Athlon 64 X2 4400

    GPU: ATI Radeon HD 2400

    RAM: 1 GB

    OS: Windows 7 Embedded

### My Game Is Running Slow/Lagging

!!! tip ""
    Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast!

!!! tip ""
    The most common reason for this is the game is running over its required 60 Hz, the game is hardcoded to run at 60 Hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60 Hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60 Hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Game Stuck On Title Screen (AMD Ryzen 3900X)

!!! tip ""
    If you have AMD Ryzen 3900X-series processor and the game gets stuck on the title screen (or a black screen) you are running into a known processor bug for games using Media Foundation to play videos. The workaround is to disable simultaneous multithreading (SMT) in the system's BIOS settings. See [this GitHub issue for Proton](https://github.com/ValveSoftware/Proton/issues/838#issuecomment-557081962)

### Occasional Graphical Stuttering During Gameplay

!!! tip ""
    Disable fullscreen optimizations for spice64.exe instance. Right click on spice64.exe, click on Properties. Click on Compatibility tab, "Change settings for all users", and check "Disable fullscreen optimizations".

### I get an IP Change Error!

!!! tip ""
    Apply the `Fix IP Change Error` patch.

### Which Offset Is Which?

!!! tip ""
    If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-). Gitadora features BOTH a visual offset and an audio based one, so experiment accordingly.

### Why Are My Videos Freezing (Usually Towards the End of the Song)?

!!! tip ""
    If you're using Windows 10, there is a bug that is caused by the difference between the ASF stream decoder between Windows 7 and Windows 10 wherein it fails to properly detect the end of file of the video stream which causes the video decoder to throw an exception, which is why the video freezes. At the time of writing, SpiceTools does not have a fix for this, but there are hooks available to resolve this issue.

### I Tried Switching to SpiceTools to Follow the Guide and It Crashes!

!!! tip ""
    This is a known issue, make sure to replace all of the `.dll` files from the ``contents`` folder of the game with ones from a fresh install, other tools currently modify these files in a way that SpiceTools cannot deal with.

### My Drum Pedal Isn't Working!

!!! tip ""
    Some drum kits utilize hi-hat control with the pedal resulting in different MIDI addresses that require additional bindings, make sure to follow your drum kit's manual to see these other bindings and bind them in your desired tool's accordingly. Gitadora does not do this, so the game utilizes just 1 binding for every level of sensitivity on the pedal and multiple bindings are typically required with most drum kits.

### When I Run This Game All Other Background Audio Is Gone! What's Going On?

!!! tip ""
    Gitadora is a 64-bit game that utilizes a feature in Windows called [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) to obtain less audio latency than the former 32-bit versions of BEMANI games which used [DirectSound](https://en.wikipedia.org/wiki/DirectSound). Unfortunately, this cannot be changed.

### Note on 2-channel and 4-channel Audio

!!! tip ""
    For most setups, the `-2ch` parameter will be mandatory to hear any functional audio. 4-channel setups aren't really working in general and there's buffer issues, please avoid using it.
