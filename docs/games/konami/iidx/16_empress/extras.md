<img class="header-logo" src="/img/konami/iidx/16_empress/logo.webp">
# Extra Information

## Output modes
!!! info "Output Mode"

    This game supports two output modes: `S-VIDEO` and `VGA`.
    The difference between these two is:
    
    - `S-VIDEO` runs at 59.95hz
    - `VGA` runs at 60.05hz
    
    By default, the output mode is set automatically by the game.
    !!! tip "If for some reason you want to change the output mode of your game, do the following:"
        Open your `iidxhook-xx.conf`. Find a line that says:
        ```
        gfx.frame_rate_limit=xx.xx
        ```
        
        - Depending on the output mode of your choice, replace `xx.xx` with either 59.95 or 60.05
        
        Now, in the service menu of your game: 
        
        - Go to `GAME OPTIONS`
        
        <img src="/img/konami/iidx/16_empress/11.webp">
        
        - Go to the line that says `OUTPUT MODE` and change it to your desired mode
        
        - Select `SAVE AND EXIT`
        
        That's it!
        
    