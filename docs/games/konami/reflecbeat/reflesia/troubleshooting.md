<img class="header-logo" src="/img/konami/reflecbeat/reflesia/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Hardware Specs

!!! tip ""
    Konami PC (ADE-704A)

    CPU: Intel Celeron B810 1.6GHz

    GPU: E4690 Radeon MXM

    OS: Windows XP Embedded

### My Game Doesn't Boot After Following the Guide!

!!! tip ""
    The most common problem present here is if you do not have an E:/ drive. To resolve this issue, you must apply the `E:/drive fix` patch.

### My Game Is Running Slow/Lagging

!!! tip ""
    Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### My Game Is Running Crazy Fast/After Finishing a Song Loading Is Stuck

!!! tip ""
    The most common reason for this is the game is running over its required 60 Hz, the game is hardcoded to run at 60 Hz and this cannot be changed. To solve this, set your monitor's refresh rate to 60 Hz. You can always check on the game's monitor check if the game is fluctuating around 59.94hz, the NTSC standard. If it's not around there and your monitor is indeed set to 60 Hz, consider trying a different panel or forcing vsync on in your GPU's graphics settings.

### Which Offset Is Which?

!!! tip ""
    If you're getting too many fasts, increase your offset (+). If you're getting too many slows, decrease your offset (-).

### Failed to Create Texture Error in SpiceTools

!!! tip ""
    If your error is along the lines of a failure to create a texture W:afputils: CTexture::create_texture テクスチャの作成に失敗しました。 then boot the game without touching anything, even your mouse, maybe give it a few tries, it's admittedly a strange issue with no exact science behind it discovered.

### I Get a White Screen That Silently Closes After a Few Seconds

!!! tip ""
    Reflesia runs at 768x1360 opposed to more common resolutions. If your monitor doesn't have support for this, try making a custom resolution in your graphic's cards options. Also, make sure your monitor is in portrait mode as opposed to landscape. 