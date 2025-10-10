!!! tip ""

    - Open your `iidxhook-xx.conf` (xx being your game version)

    - Locate and change the options we're interested in:
    
    ```
    gfx.framed=false                    # Only matters if windowed. False for borderless, True for decorations (title bar, etc..)
    gfx.frame_rate_limit=0.0            # Set this to 59.95
    gfx.windowed=false                  # False for fullscreen, True for windowed
    gfx.window_width=0                  # Set to your desired game width (recommended: monitor width)
    gfx.window_height=0                 # Set to your desired game height (recommended: monitor height)
    gfx.scale_back_buffer_width=0       # Set to your desired game width (recommended: monitor width)
    gfx.scale_back_buffer_height=0      # Set to your desired game height (recommended: monitor height)
    gfx.scale_back_buffer_filter=none   # Set to point or linear (pick one from examples below)
    ```

    Here are visual examples of the two filter options:

    ??? info "point (sharp, pixel perfect)"

        <img src="/img/konami/iidx/14_gold/iidx14_point.webp">
    
    ??? info "linear (less sharp, not pixel perfect)"

        <img src="/img/konami/iidx/14_gold/iidx14_linear.webp">
