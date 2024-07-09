# CHUNITHM SUN PLUS

<img src="/img/chunithmsunplus/sunplus.png">

!!! info "Last updated: July 9th, 2024"

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

***

!!! warning "`Segatools` does not come with any built-in controller support. By default it will only accept keyboard input."

## Keyboard

!!! info "Keyboard is the default input method, and while not recommended for playing the game, it is useful for testing purposes."

    The default layout uses `SDFGHJKL` for the slider input, and `Space Bar` for the AIRs.  
    If you wish to change the default keybinds, an explanation on how to set these is included above the `[io3]` section in your `segatools.ini`.

***

## How Controller Input works with segatools

!!! example "How Controller Input works with segatools"
    
    The input files you wish to use need to be referenced in the `[chuniio]` section of `segatools.ini`.  
    
    If the `dll` files you plan to use consist of 2 files, with names ending in `_x86.dll` and `_x64.dll`, uncomment the `path32` and `path64` lines by removing the `;` from the beginning. Add your file names after the `=`.

    ```ini
	[chuniio]
	; Uncomment this if you have custom chuniio implementation comprised of a single 32bit DLL.
    ; (will use chu2to3 engine internally)
    ;path=

    ; Uncomment both of these if you have custom chuniio implementation comprised of  two DLLs.
    ; x86 chuniio to path32, x64 to path64. Both are necessary.
    path32=controller_x86.dll
    path64=controller_x64.dll
	```

    ??? info "If the input file you wish to use consists of a single `*.dll`, uncomment only the `path` line, and enter the dll name after the `=`."
        
        ```ini
	    [chuniio]
	    ; Uncomment this if you have custom chuniio implementation comprised of a single 32bit DLL.
        ; (will use chu2to3 engine internally)
        path=controller.dll

        ; Uncomment both of these if you have custom chuniio implementation comprised of  two DLLs.
        ; x86 chuniio to path32, x64 to path64. Both are necessary.
        ;path32=
        ;path64=
	    ```

***

## Brokenithm

!!! info "Brokenithm allows you to use an Android tablet or iPad as a controller for CHUNITHM."
    It uses the bottom half of the screen as the touch slider. Sliding from the bottom section into the top section of the screen activates the AIR sensors.

### Brokenithm Android

??? tip "How to setup Brokenithm Android"
    - Download the latest version of [Brokenithm-Android](https://github.com/tindy2013/Brokenithm-Android) from the [releases section](https://github.com/tindy2013/Brokenithm-Android/releases). 
  
    - Copy the `app-release.apk` to your Android device and install it.  

    - Download the latest version of [Brokenithm-Android-Server](https://github.com/tindy2013/Brokenithm-Android-Server) from the [releases section](https://github.com/tindy2013/Brokenithm-Android-Server/releases)
    
    - Extract just the `brokenithm_server.exe` to your `\App\bin\` folder.  

    - Download the latest version of the [Brokenithm-Evolved](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/) IO dll files from the [releases tab](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/releases). 
  
    - Extract the 3 dll files to your `\App\bin\` folder.  

    - Open your `segatools.ini` with a text editor, and modify the `[aimeio]` section as shown.  
  
    ```ini
    [aimeio]
    ; Uncomment this if you have custom (x64) aime implementation.
    ; Leave empty if you want to use Segatools built-in keyboard input.
    path=aime_brokenithm.dll
    ``` 

    - Modify the `[chuniio]` section as shown.  
    
    ```ini
    [chuniio]
    ; Uncomment this if you have custom chuniio implementation comprised of a single 32bit DLL.
    ; (will use chu2to3 engine internally)
    ;path=

    ; Uncomment both of these if you have custom chuniio implementation comprised of two DLLs.
    ; x86 chuniio to path32, x64 to path64. Both are necessary.
    path32=brokenithm_x86.dll
    path64=brokenithm_x64.dll
    ```  

    - Run the `brokenithm_server.exe` you extracted previously. A CMD window should open, with a message that it is waiting for a device on port 52468.  
    
    - Open the Brokenithm App on your Android device.
    
    - At the top right, in the Address box, enter your PCs local IP address and then press the start button.  
    
    - You can now run your game via the `start.bat` as normal.

#### Automatically launching the Brokenithm server for Android

??? tip "If you want the `brokenithm_server.exe` to automatically run when launching the game"
    
    You will need to modify `start.bat`.  

    - Open `start.bat` with a text editor
    
    - Add a new line containing `start /min brokenithm_server` above the existing `start /min inject_x64 ...` line as shown below.  
    
    ```bat
    @echo off

    pushd %~dp0

    start /min brokenithm_server
    start /min inject_x64 -d -k chusanhook_x64.dll amdaemon.exe -c config_common.json config_server.json config_client.json config_cvt.json config_sp.json config_hook.json
    inject_x86 -d -k chusanhook_x86.dll chusanApp.exe
    taskkill /f /im amdaemon.exe > nul 2>&1

    echo.
    echo Game processes have terminated
    pause
    ```  
    This will only work if you copied the `brokenithm_server.exe` file to your `\App\bin` folder.

#### Slider Lights

??? tip "Enabling Slider Lights on Brokenithm Android"
    By default, the Brokenithm Server runs in `UDP` mode. This is done to decrease latency when connected over WiFi, however it does not send any lighting data to the tablet. The server also supports a `TCP` mode, which does send lighting data.  

    To run the Brokenithm Server in TCP mode, we need to start it with the ` -T` flag.  

    - Navigate to the folder that contains your `brokenithm_server.exe`
  
    - Click on the Address Bar at the top of the folder, type `CMD`, and hit enter. A Command Prompt window should open.  
    
    - In the Command Prompt window, type `brokenithm_server -T` and hit enter.  

    - On your Android device, find the button labeled `UDP` at the top-center of the Brokenithm application. 
  
    - Tap the button to toggle to `TCP` mode. You should now be able to connect using your PC's local IP, as described above.  

    If you are running the Brokenithm Server via the `start.bat` as shown in the previous step, simply add ` -T` to the end of the brokenithm_server line, as shown below.
    
    ```bat
    start /min brokenithm_server -T
    ```

#### Improving Latency

??? tip "Improving Latency via a USB connection"
    As WiFi isn't the best for latency, it is preferable to run Brokenithm with your Android device tethered to your PC. This will require enabling Developer options, and USB debugging on your tablet. As this process varies by device, instructions are not included here.  

    Once you have USB debugging enabled
    
    - Download and extract the [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools) to somewhere on your PC.  
    
    - Navigate to the folder you extracted the tools to, click in the Address bar, type `CMD` and hit enter to open a Command Prompt window.

    - Make sure your Android device is connected and that USB debugging is enabled.  

    - In the Command Prompt window, type one of the following commands, depending on which mode you plan to run the server in.  

    **TCP**  
    ```bat
    adb reverse tcp:52468 tcp:52468
    ```

    **UDP**  
    ```bat
    adb reverse udp:52468 udp:52468
    ```

    - Start your `brokenithm_server.exe`.  
    
    - Open Brokenithm on your Android device, in the address bar change the IP to `0.0.0.0`. 
  
    - Press the start button to connect. You will now be connected via the USB cable.  
    
    - Run the game via the `start.bat` as normal.  

    If you extract the `platform-tools` folder to your `\Bin\app\` folder, you can add the following line to your `start.bat` to run this command when the game launches.
    
    ```bat
    start /min platform-tools/adb reverse tcp:52468 tcp:52468
    ```

    This should go above the line which starts the `brokenithm_server.exe`.

***

### Brokenithm iOS

??? tip "Running Brokenithm on an iPad requires either a jailbroken device, or another method to install `.ipa` files."
    Using [Sideloady](https://sideloadly.io/) is a popular method.  

    Before proceeding, you must uninstall the Microsoft Store versions of iTunes and iCloud (if present) then install the non-Microsoft Store version from the [iTunes website](https://www.apple.com/itunes/download/win64). This is also covered under the **Important Windows Task** section of the Sideloady website.  

    - Download the latest version of `Brokenithm-iOS` from the [redive.estertion.win](https://redive.estertion.win/ipas/Brokenithm-iOS-build-10.ipa) website.
  
    - Install the `.ipa` to your device using your preferred method.  
    
    - Download the latest version of the `Brokenithm-Evolved-iOS` server from the [redive.estertion.win](https://redive.estertion.win/ipas/Brokenithm/Brokenithm-Evolved-iOS-v0.3.7z) website.
    
    - Extract the files to your `\App\bin\` folder. `aimeio.dll` and `chuniio.dll` can be deleted, as they are not required.  

    - Download the latest version of the [Brokenithm-Evolved](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/) IO dll files from the [releases tab](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/releases). 
  
    - Extract the 3 dll files to your `\App\bin\` folder.  

    - Open your `segatools.ini` with a text editor, and modify the `[aimeio]` section as shown.  

    ```ini
    [aimeio]
    ; Uncomment this if you have custom (x64) aime implementation.
    ; Leave empty if you want to use Segatools built-in keyboard input.
    path=aime_brokenithm.dll
    ```   

    Modify the `[chuniio]` section as shown.  

    ```ini
    [chuniio]
    ; Uncomment this if you have custom chuniio implementation comprised of a single 32bit DLL.
    ; (will use chu2to3 engine internally)
    ;path=

    ; Uncomment both of these if you have custom chuniio implementation comprised of two DLLs.
    ; x86 chuniio to path32, x64 to path64. Both are necessary.
    path32=brokenithm_x86.dll
    path64=brokenithm_x64.dll
    ``` 

    - Run the `Brokenithm-Evolved-iOS.exe` you extracted previously. A CMD window should open, with a message that it is waiting for a device. 
   
    - Open the Brokenithm App on your iPad, and connect it to your PC via a USB cable.  
  
    - You can now run your game via the `start.bat` as normal.

    !!! info "As Brokenithm for iOS only connects via USB connection, there is no need to configure any extra network settings to improve latency."
    

#### Automatically launching the Brokenithm server for iOS

??? tip " If you want the `Brokenithm-Evolved-iOS.exe` to automatically run when launching the game"
    You will need to modify `start.bat`. 

    - Open `start.bat` with a text editor. 
    
    - Add a new line containing `start /min Brokenithm-Evolved-iOS` above the existing `start /min inject_x64 ...` line, as shown below.  
    
    ```bat
    @echo off

    pushd %~dp0

    start /min Brokenithm-Evolved-iOS
    start /min inject_x64 -d -k chusanhook_x64.dll amdaemon.exe -c config_common.json config_server.json config_client.json config_cvt.json config_sp.json config_hook.json
    inject_x86 -d -k chusanhook_x86.dll chusanApp.exe
    taskkill /f /im amdaemon.exe > nul 2>&1

    echo.
    echo Game processes have terminated
    pause
    ``` 

    This will only work if you copied the `Brokenithm-Evolved-iOS.exe` file to your `\App\bin` folder.

***

## Tasoller

???+ info "The Tasoller is an arcade accurate controller, produced by DJ-DAO. "
 
    Out of the box, the Tasoller will only offer keyboard input, with no lighting support.
    
    To get full compatability with CHUNITHM, you will need to install [custom firmware](https://pixeldrain.com/u/DajSPEoa). Instructions on how to install the firmware are included in the archive.

???+ danger "The Tasoller custom firmware is only compatabile with controllers running the DJ-DAO 2.0 firmware."

    If your controller was purchased **^^after January 2022^^**, it should have shipped with the update already applied.

    If your Tasoller was purchased **^^before 2022^^** and is still using the original firmware it shipped with, you will need to first update to 2.0 by following the guide on [DJ-DAO's website](https://www.dj-dao.com/en/support/11.html).  

    Once you've updated your controller to the DJ-DAO 2.0 firmware, you can follow the instructions included with the Custom Firmware as normal.

???+ tip "DJ-DAO doesn't directly provide any input assistance for customers wanting to play on data."

    Thankfully there are community members creating open source alternatives. 

    There are two up to date drivers available for the Tasoller, with full support for Dniel97's segatools fork. Functionally these work the same as each other, with the only difference being the language they are written in.  

    [chuniio-tasoller](https://gitea.tendokyu.moe/Scribbler/chuniio-tasoller) written in `zig`.  
    [chuniio-rs](https://gitea.tendokyu.moe/beerpsi/chuniio-rs) written in `rust`.  

    - Head to the `Releases` tab for your chosen driver and download the latest package. 
    
    - For `chuniio-rs` make sure you download the `chusan.zip`.  
    
    - Extract the `*.dll` files to your `\App\bin\` folder.  
  
    - Make the required changes to `segatools.ini`, as shown in the `Configuration` section of the `readme` for the driver you have downloaded.

***

## YubiDeck

!!! info "The YubiDeck is an arcade accurate controller, produced by ZhouSensor and sold by YubiParts. It also includes a built in Aime card scanner."

???+ tip "YubiDeck firmware updates are provided in the support section of the YubiParts website. Unfortunately the IO driver they provide is no longer available for download."
    
    An open source alternative is available, [chuniio-yubideck](https://gitea.tendokyu.moe/beerpsi/chuniio-yubideck).  

    - Head to the `Releases` tab and download the latest package. Extract the `*.dll` files to your `\App\bin\` folder. 
 
    - Make the required changes to `segatools.ini`, as shown in the `Configuration` section of the chuniio-yubideck readme.  

    - If you want to make use of the built-in card scanner, add the following line to the `[aimeio]` section in `segatools.ini`.  
    
    ```ini
    path=aimeio_yubideck.dll
    ```

***

## Arcade Panels and other Controllers

!!! tip ""
    If you're interested in connecting a real cabinet Slider and Airs, or possibly even DIYing your own controller, the [Cons&Stuff](https://consandstuff.github.io/) website and Discord community is a great place to start!