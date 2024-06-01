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

### My game occasionally drops frames/stutters

!!! tip ""
    While frame drops can be caused by running the game on under-powered hardware, it is also common for this to happen when running on hardware that is too over-powered!  
    As a lot of the game consists of mostly 2D assets, your GPU is unlikely to be pushed very hard. Modern GPUs attempt to be as energy efficient as possible by changing power-states when under-utilised. If these power-state changes happen mid song, this can lead to slight frame drops and stutters.  
    This can be solved by forcing the GPU to stay in its maximum power-state while the game is running.

!!! note "NVIDIA:"
    In the Windows Taskbar Icon Tray, right click the NVIDIA Settings icon, and select `NVIDIA Control Panel`.  
    On the left, select `Manage 3D settings`.  
    On the right, click on the `Program Settings` tab.  
    Click the add button, and navigate to your `\CHUNITHMSUNPLUS\App\bin\` folder, and select `chusanApp.exe`.  
    In the `Feature` list, scroll down to `Power management mode` and select `Prefer maximum performance`.  
    Save your settings and close `NVIDIA Control Panel`. Your game will now always run in the highest power-state!

<img src="/img/chunithmsunplus/nvidiaperf.png">

!!! note "AMD:"
    In the Windows Taskbar Icon Tray, right click the `AMD Software` icon, and select `Open AMD Software: Adrenalin Edition`.  
    At the top of the window, select the `Gaming` tab.  
    If `chusanApp` isn't already listed in your Games Library, click on the 3 dots at the top right of the window, then click on `Add A Game...`. Navigate to your `\CHUNITHMSUNPLUS\App\bin\` folder, and select `chusanApp.exe`.  
    Select `chusanApp` from the Games Library.  
    Under the `Graphics` section, set the `Graphics Profile` to `Performance`.

<img src="/img/chunithmsunplus/amdperf.png">

!!! note "AMD, continued:"
    While the above will help to reduce any issues, it's not quite the same as the `Power management mode` offered by NVIDIA.  
    A similar configuration can be achieved by adding a custom Overlocking Game Profile in the `Performance` > `Tuning` section of the AMD Software, and increasing the minimum `GPU Frequency` for each `State`.  
    As these settings will vary wildly from one GPU to another, and as overclocking comes with its own risks, specifics for this won't be included on this page.