<img class="header-logo" src="/img/bemani/jubeat/clan/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Hardware Specs

!!! tip ""
    Bemani PC (ADE-704A)

    This board has a E4690 Radeon MXM card.

    CPU: Intel Celeron B810

    GPU: AMD Radeon E4690

    Chipset: Intel HM65

### My Game Is Running Slow/Lagging

!!! tip ""
    Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast!

!!! tip ""
    The most common reason for this is the game is running over its required 60 Hz, the game is hardcoded to run at 60 Hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60 Hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60 Hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Occasional Game Stutters During Play

!!! tip ""
    Sometimes you might have occasional stutters during play, while solutions can vary wildly from general performance issues to bad hard drives, try adding SpiceTools `-realtime` parameter to your .bat file.

### My Touchscreen Isn't Working!

!!! tip ""
    There's a myriad of reasons for this. With SpiceTools in most cases, try using the `-wintouch` parameter if rawinput is not working for your monitor. 