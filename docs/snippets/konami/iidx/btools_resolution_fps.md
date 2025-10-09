!!! tip ""
    Next up, we'll setup borderless window and configure the proper resolution. We're using a `1920x1080` monitor so we will use that.
    
    Open your `iidxhook-xx.conf` (xx being your game version). We want to find these lines:
    
    ```
    # Software limit the frame rate of the rendering loop in hz, e.g. 60 or 59.95 (0.0 = no software limit)
    gfx.frame_rate_limit=0.0
    
    # Run the game windowed
    gfx.windowed=false

    # Windowed width, 0 for default size
    gfx.window_width=0

    # Windowed height, 0 for default size
    gfx.window_height=0

    # Up-/downscale the back buffer's width. This does not change the game's rendering resolution but scales the final frame. Use this to target the native resolution of your monitor/TV, e.g. to avoid over-/underscan, bad image quality or latency caused by the monitors internal upscaler. 0 to disable this feature. Must be set in combination with the corresponding height parameter.
    gfx.scale_back_buffer_width=0

    # Up-/downscale the back buffer's height. This does not change the game's rendering resolution but scales the final frame. Use this to target the native resolution of your monitor/TV, e.g. to avoid over-/underscan, bad image quality or latency caused by the monitors internal upscaler. 0 to disable this feature. Must be set in combination with the corresponding width parameter.
    gfx.scale_back_buffer_height=0

    # Filter type to use for up-/downscaling the back buffer. Only used if scaling feature was enabled by setting the scaling width and height parameters. Available types: none, linear, point (refer to D3DTEXTUREFILTERTYPE  for explanation).
    gfx.scale_back_buffer_filter=none
    ```
    
    If you can't seem to find them, press `CTRL` + `F` and search for `gfx.frame_rate_limit=0.0`. This will bring you to the first line we want to edit.
    
!!! tip ""
    Listed below are the values we want to change them to.
    
    ```
    gfx.frame_rate_limit=59.95
    gfx.windowed=true
    gfx.window_width=1920
    gfx.window_height=1080
    gfx.scale_back_buffer_width=1920
    gfx.scale_back_buffer_height=1080
    gfx.scale_back_buffer_filter=linear
    ```
    Unless you'd like to have the game properly windowed you can safely ignore `gfx.framed=false`.

    Make sure to decide on whether you want `Linear` or `Point` rendering.

    ```
    gfx.scale_back_buffer_filter=linear
    gfx.scale_back_buffer_filter=point
    ```
