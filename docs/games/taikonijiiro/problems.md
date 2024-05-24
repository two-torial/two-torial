# CHUNITHM SUN PLUS Common Problems/Tips

<img src="/img/chunithmsunplus/sunplus.png">

### I'm having audio issues

!!! tip ""
    CHUNITHM expects a specific Default Format from your sound card.  
    In Windows, go to `Playback Devices` and then right click on your default device and go to `Properties`. From there, hit the `Advanced` tab and set your `Default Format` to `16bit, 48000 Hz (DVD Quality)` and check both of the options inside `Exclusive Mode` as pictured.  

    By default, CHUNITHM uses Exclusive Audio. This means you won't be able to hear any other sounds from your PC while the game is running. A Shared Audio mode can be enabled via the chusanApp.exe Patcher website, though it should be noted that this can increase audio latency.

<img src="/img/gen/sega480.png">

### Some of my installed Songs and Events aren't visible in game

!!! tip ""
    Some content in CHUNITHM is locked behind event maps, or other requirements, such as playing the same song on another SEGA game, such as maimai.  
    We can force unlock this content, making it always available in game.  

    Download the [Chunithm_Unlocker](https://pixeldrain.com/u/Ccttn8u9) powershell script, and place it in your game folder, next to the `App` and `Option` folders.  
    Right click the file, and select `Run with Powershell`.  
    Once the script has scanned your game files, it will present you with several options for unlocking different types of content. You can either unlock everything, or only unlock specific things (such as songs), leaving the other content to be unlocked via regular gameplay.

!!! note ""
    The Chunithm_Unlocker script creates backups of any file it modifies, and has options to restore the files back to their original state. Please note that certain content (such as character unlocks) are sent to the server and saved to your profile, so reverting the unlock in your game files won't always relock that content for your game profile.

### My game takes a long time to boot

!!! tip ""
    The game files for CHUNITHM consists of thousands of small .xml files, and Windows Defender is known to spend a long time scanning through them during game boot up.  
    One way to massively speed up boot times is to add the entire game folder as a Windows Defender Exception.

!!! danger "Warning:"
    Doing this will prevent Defender from scanning your game folder for viruses. Only do this if you trust the source of your data.

!!! tip ""
    Open `Virus & threat protection`.  
    Under `Virus & threat protection settings` click the `Manage Settings` button.  
    Scroll down to `Exclusions` and click on `Add or remove exclusions`.  
    Click the `Add an exclusion` button, select the `folder` option, navigate to the base of your game install and click `Select Folder`.

<img src="/img/chunithmsunplus/defender.png">

### My game crashes when I alt-tab out of fullscreen

!!! tip ""
    As the game is intended to run on dedicated hardware, it doesn't like to be minimised.  
    One work-around for this is to use [DXVK](https://github.com/doitsujin/dxvk/) to run the game with Vulkan rather than Direct3D. This has the added benefit of smoother frame rates for some hardware configurations.  

    Download the latest version of DXVK from the [releases tab](https://github.com/doitsujin/dxvk/releases). This will be a `dxvk-x.x.tar.gz` file. Open the file with `7zip` and navigate to the `x32` folder.  
    Extract the `d3d9.dll` file to your `\CHUNITHMSUNPLUS\App\bin\` folder, alongside your `chusanApp.exe`.  
    You should now be able to tab out of fullscreeen, leaving the game running.

!!! note "Additional DXVK configuration:"
    DXVK has other options that can be changed by adding a `dxvk.conf` file next to the `d3d9.dll` file. The most common use for this is to add an FPS counter to the game.  
    If you wish to have an FPS counter, create a `dxvk.conf` file and open it with Notepad++. Add the following line.  
    ```json
    dxvk.hud = fps
    ```
    You can learn more about the available options at the [DXVK Configuration Wiki page](https://github.com/doitsujin/dxvk/wiki/Configuration).

!!! note "Controller inputs whilst minimised:"
    As the game was never designed to be minimised, it will not ignore inputs when not focused. This means any controller inputs will be accepted, so try not to lean on your slider while tabbed out!  
    The most common issue this causes is when typing the number `1` with the game minimised, as by default this will enter the test menu. If you were mid-credit, your scores will be lost.  
    If you wish to change the keyboard keys assigned to the Test, Service and Coin buttons, this can be configured in the `[io3]` section of `segatools.ini`.

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