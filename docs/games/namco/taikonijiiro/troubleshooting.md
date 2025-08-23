<img class="header-logo" src="/img/namco/taikonijiiro/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

### Changing the Language

!!! tip ""

    Nijiiro supports changing the language from the test menu. The officially supported languages are:

    - Japanese (Default)                                                                   
    - English                                                                           
    - Chinese (zh-TW)                                                                   
    - Korean                 
    
    An unofficial mod allows you to change the language to Chinese (simplified), this can be found on the [Discord](https://discord.gg/cZRUmEPK78).
     
    Using ++f1++, the `arrow keys` and ++enter++, navigate to `OTHERS` -> `LANGUAGE`

<img src="/img/namco/taikonijiiro/troubleshooting/lang.webp">

### My game is frozen/black screen

!!! tip ""

    You can fix this by running the game as admin. You can also try updating windows and gpu drivers.

### My game takes a long time to boot

!!! info "First boot after connecting to a network will be very long (>90s)"

!!! tip ""

    The game files for Nijiiro consists of thousands of small `.bin` files and Windows Defender is known to spend a long time scanning through them during game boot up.

    One way to massively speed up boot times is to add the entire game folder as a Windows Defender Exception.

    Doing this will prevent Defender from scanning your game folder for viruses.

!!! danger "Only do this if you trust the source of your data!"

!!! tip ""

    - Open `Virus & threat protection`.  
    - Under `Virus & threat protection settings` click the `Manage Settings` button.  
    - Scroll down to `Exclusions` and click on `Add or remove exclusions`.  
    - Click the `Add an exclusion` button, select the `folder` option, navigate to the root of your game installation and click `Select Folder`.

<img src="/img/namco/taikonijiiro/troubleshooting/defender.webp">

### My game is running crazy fast/slow

!!! tip ""

    The game needs to be ran at 120 FPS or things will break.
    
    ??? tip "If you have a display that supports 120 Hz or higher"                           
        - Set your display to 120 Hz. You may need to make a [custom resolution](https://customresolutionutility.net/).                                                                              
        - In `config.toml` set `vsync =` to `true`.  
     
    ??? tip "If you have a display that is less than 120 Hz"                                                   
        - In `config.toml` set `vsync =` to `false` and `windowed =` to `true`.  
        - Alternatively you can use [RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).                                                                         

### My game is not connected to a network but I set one up

!!! tip "Disable shop close time or you won't always be able to connect to the network"

    Using ++f1++ `arrow keys` and ++enter++ navigate to `GAME OPTIONS` -> `CLOCK/CLOSE TIME SETTING` -> `SCHEDULE TYPE`.

    <img src="/img/namco/taikonijiiro/troubleshooting/close.webp">

    If you are still unable to connect that means you have incorrectly configured your `config.toml` or your server.

### My game is still too big/small after setting the resolution in `config.toml`

!!! tip ""

    This will happen if you incorrectly set your resolution or scale.

    You can check your display resolution by right clicking your desktop and selecting `Display settings`.

    You can set your scale to `100%` right above where it says your resolution.

    <img src="/img/namco/taikonijiiro/troubleshooting/scale.webp">

### My controller is dropping inputs / I can't hit good drumrolls

!!! tip ""

    This a common issue on some controllers.

    In `config.toml` increase `wait_period =` by 1, then test it in-game and repeat until it feels correct.

### Best settings for Nvidia GPUs

!!! tip ""

    This will help with latency and other issues
    
    In `NVIDIA Control Panel` set the following settings for `Taiko.exe`.    

    - Low Latency Mode `Ultra`                                                                                      
    - Power management mode `Prefer maximum performance`                                         
    - Vertical sync `Fast`                                                  

### Audio

!!! tip ""

    By default the game will use WASAPI Shared
    
    To use WASAPI exclusive:

    - Inside `config.toml`, set `wasapi_shared =` to `false`                             

    To use ASIO:

    - Inside `config.toml`, set `wasapi_shared =` to `false` and set `asio =` to `true`.
    - Change `asio_driver =` to `asio_driver = "<Your ASIO Driver Name>"`

    For more information refer to the general [Audio](/extras/audio.md) guide.
