# Taiko no Tatsujin Nijiiro Common Problems/Tips

<img src="/img/taikonijiiro/taikonijiiro.png">

### Change Language

!!! tip ""
    Nijiiro support changing the language from the test menu. The officially supported languages are                                                                              
    Japanese(Default)                                                                   
    English                                                                           
    Chinese(zh-TW)                                                                   
    Korean                 
    
    An unofficial mod allows you to change the language to Chinese(simplified) this can be found on the [Discord](https://discord.gg/cZRUmEPK78).
    
    Using `F1` `arrow keys` and `ENTER` navigate to `OTHERS` -> `LANGUAGE`

<img src="/img/taikonijiiro/lang.png">

### My game takes a long time to boot

!!! danger "Warning:"
    First boot after connecting to a network will be very long (>90s)

!!! tip ""
    The game files for Nijiiro consists of thousands of small .bin files, and Windows Defender is known to spend a long time scanning through them during game boot up.  
    One way to massively speed up boot times is to add the entire game folder as a Windows Defender Exception.

!!! danger "Warning:"
    Doing this will prevent Defender from scanning your game folder for viruses. Only do this if you trust the source of your data.

!!! tip ""
    Open `Virus & threat protection`.  
    Under `Virus & threat protection settings` click the `Manage Settings` button.  
    Scroll down to `Exclusions` and click on `Add or remove exclusions`.  
    Click the `Add an exclusion` button, select the `folder` option, navigate to the base of your game install and click `Select Folder`.

<img src="/img/taikonijiiro/defender.png">

### My game is running crazy fast/slow

!!! tip ""
    The game needs to be ran at 120fps or things will break.
    
    If you have a >=120hz display.                                  
    Set your display to 120hz. you may need to make a custom resolution.                                                                              
    In `config.toml` set `vsync =` to `true`.  
     
    If you have a <120hz display.                                                    
    In `config.toml` set `vsync =` to `false`.                                                                        
    Limit the FPS for `Taiko.exe` using your GPU settings or [RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)      
    
<img src="/img/taikonijiiro/fps.png">

### My game is not connected to a network but I set one up

!!! tip ""
    Disable shop close time or you won't always be able to connect to the network.

    Using `F1` `arrow keys` and `ENTER` navigate to `GAME OPTIONS` -> `CLOCK/CLOSE TIME SETTING` -> `SCHEDULE TYPE`.

    If you are still unable to connect that means you have incorrectly configured your `config.toml` or your server.

<img src="/img/taikonijiiro/close.png">

### Help some game modes are missing

!!! tip ""
    This will happen if you did not correctly apply the unlock game modes mod or card in.

    You can download the mod on the [Discord](https://discord.gg/cZRUmEPK78).

    You can card in by pressing `P` by default.

<img src="/img/taikonijiiro/game.png">

### My game is still too big/small after setting resolution in `config.toml`

!!! tip ""
    This will happen if you incorrectly set your resolution or scale.

    You can check your display resolution by right clicking your desktop and selecting `Display settings`.

    You can set your scale to `100%` right above where it says your resolution.

<img src="/img/taikonijiiro/scale.png">