# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

### My game crashes on launch

!!! tip ""

    Some monitors and display adapters may not support the odd resolution that the game runs at, which is 1360x768 as opposed to the occasionally seen 1366x768. To resolve this, set a custom resolution in your graphics card's settings, or enable GPU resolution scaling.

### My game is too slow/fast

!!! tip ""
    
    Potential causes:

    1. The game could be running over/under its required refresh rate (60)  
    To solve this, make sure v-sync isn't disabled in your graphics card's settings.
    For NVIDIA users, enable `NVIDIA profile optimization (-nvprofile)` in the `Options` tab.
    You can also set `Force Refresh Rate` to 60.
    2. It could be that your computer's performance isn't good enough to keep a steady framerate.

### My game doesn't have audio

!!! tip ""

    Enable the `HDMI Audio Fix` patch.