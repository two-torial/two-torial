<img class="header-logo" src="/img/konami/gitadora/fuzzup/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

### I'm having performance issues!

!!! tip ""

    If you're having performance issues of some kind, spice2x's [PC optimization](https://github.com/spice2x/spice2x.github.io/wiki/PC-optimization) guide is worth looking at.

### My game is running too fast!

!!! tip ""

    The most common reason for this is the game is running over its required refresh rate.
    
    To solve this, ensure the monitor running GITADORA FUZZ-UP is set to 60 Hz. This is a requirement for the game to run at the correct speed. The game is hardcoded to run at 60 Hz and there is no way to change this.
    
    In addition, make sure v-sync isn't disabled in your graphics card's settings.
    
    For NVIDIA users, enable  `NVIDIA profile optimization (-nvprofile)` in the `Options` tab.

### There's occasional graphical stuttering during gameplay!

!!! tip ""

    To fix this, you need to disable fullscreen optimizations for `spice64.exe`.

    1. Right click on `spice64.exe` and select `Properties`.
    2. Go to the `Compatibility` tab.
    3. Click the box at the bottom that says `Change settings for all users`.
    4. Check the box that says `Disable fullscreen optimizations`.
    5. Click `Apply` and then `OK`.

### How do I adjust my offset?

!!! tip ""

    Play through a chart you're comfortable with.

    If you're getting too many `Fast`, increase your offset `(+)`.  
    If you're getting too many `Slow`, decrease your offset `(-)`.  

    GITADORA FUZZ-UP has two types of offset adjustments, visual and audio based, so be sure to fiddle with both to find desirable settings.

### When I run the game, all other audio is gone!

!!! tip ""

    GITADORA FUZZ-UP uses [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) for better audio latency. 
    
    There is currently no patch available to run the game in shared mode, so you will need to use a separate audio device for the game if you want to hear other audio sources while playing.

### I want to use 4-channel audio! Why isn't it working?

!!! tip ""

    Unfortunately, most setups do not properly function with GITADORA FUZZ-UP's 4-channel audio, and the `-2ch` parameter will be mandatory to hear any audio. There are not many setups working with 4-channel audio, and there are buffer issues related to it. Please avoid using it.