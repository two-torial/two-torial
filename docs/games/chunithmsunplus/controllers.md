# CHUNITHM SUN PLUS Controller Setup

<img src="/img/chunithmsunplus/sunplus.png">

## How Controller Input works with segatools

!!! note "segatools:"
    `segatools`, the loader used to run CHUNITHM, does not come with any built-in controller support. By default it will only accept keyboard input.  
    The controller you plan on using with the game should also be provided with IO files, in the form of `*.dll`. If unsure, you can check the support section of the site you purchased your controller from, or email the vendor directly.  
    Alternate options for the most common controllers are listed below.  
    These `dll` files should be copied to your `\App\bin\` folder, alongside `chusanApp.exe`, and referenced in your `segatools.ini`.

!!! tip ""
    The input files you wish to use need to be referenced in the `[chuniio]` section of `segatools.ini`.  
    If the `dll` files you plan to use consist of 2 files, with names ending in `_x86.dll` and `_x64.dll`, uncomment the `path32` and `path64` lines by removing the `;` from the beginning. Add your file names after the `=`.

<img src="/img/chunithmsunplus/chuniio_twodll.png">

!!! tip ""
    If the input file you wish to use consists of a single `*.dll`, uncomment only the `path` line, and enter the dll name after the `=`.

<img src="/img/chunithmsunplus/chuniio_onedll.png">

!!! note "Controllers:"
    Below is a quick introduction and setup guide for the commonly used input methods.

***

## Keyboard

!!! tip ""
    Keyboard is the default input method, and while not recommended for playing the game, it is useful for testing purposes.  
    The default layout uses `SDFGHJKL` for the slider input, and `Space Bar` for the AIRs.  
    If you wish to change the default keybinds, an explanation for how to set these is included above the `[io3]` section in your `segatools.ini`.

***

## Brokenithm

!!! note "Brokenithm:"
    Brokenithm allows you to use an Android tablet or iPad as a controller for CHUNITHM. It uses the bottom half of the screen as the touch slider, and sliding from the bottom section into the top section of the screen activates the AIR sensors.

***

### Brokenithm Android

!!! tip ""
    Download the latest version of [Brokenithm-Android](https://github.com/tindy2013/Brokenithm-Android) from the [releases section](https://github.com/tindy2013/Brokenithm-Android/releases). Copy the `app-release.apk` to your Android device and install it.  

    Download the latest version of [Brokenithm-Android-Server](https://github.com/tindy2013/Brokenithm-Android-Server) from the [releases section](https://github.com/tindy2013/Brokenithm-Android-Server/releases) and extract just the `brokenithm_server.exe` to your `\App\bin\` folder.  

    Download the latest version of the [Brokenithm-Evolved](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/) IO dll files from the [releases tab](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/releases). Extract the 3 dll files to your `\App\bin\` folder.  

    Open your `segatools.ini` with a text editor, and modify the `[aimeio]` section as shown.  
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
    Run the `brokenithm_server.exe` you extracted previously. A CMD window should open, with a message that it is waiting for a device on port 52468.  
    Open the Brokenithm App on your Android device. At the top right, in the Address box, enter your PCs local IP address and then press the start button.  
    You can now run your game via the `start.bat` as normal.

#### Automatically launching brokenithm_server

!!! tip ""
    If you want the `brokenithm_server.exe` to automatically run when launching the game, you will need to modify `start.bat`.  
    Open `start.bat` with a text editor, and add a new line containing `start /min brokenithm_server` above the existing `start /min inject_x64 ...` line, as shown below.  
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

!!! tip ""
    By default, the Brokenithm Server runs in `UDP` mode. This is done to decrease latency when connected over WiFi, however it does not send any lighting data to the tablet. The server also supports a `TCP` mode, which does send lighting data.  

    To run the Brokenithm Server in TCP mode, we need to start it with the ` -T` flag.  

    Navigate to the folder that contains your `brokenithm_server.exe`, click on the Address Bar at the top of the folder, type `CMD`, and hit enter. A Command Prompt window should open.  
    In the Command Prompt window, type `brokenithm_server -T` and hit enter.  

    On your Android device, find the button labeled `UDP` at the top-center of the Brokenithm application. Tap the button to toggle to `TCP` mode. You should now be able to connect, using your PCs local IP, as described above.  

    If you are running the Brokenithm Server via the `start.bat` as shown in the previous step, simply add ` -T` to the end of the brokenithm_server line, as shown below.
    ```bat
    start /min brokenithm_server -T
    ```

#### Improving Latency

!!! tip ""
    As WiFi isn't the best for latency, it is preferable to run Brokenithm with your Android device tethered to your PC. This will require enabling Developer options, and USB debugging on your tablet. As this process varies by device, instructions are not included here.  

    Once you have USB debugging enabled, you will need to download and extract the [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools) to somewhere on your PC.  
    Navigate to the folder you extracted the tools too, click in the Address bar, type `CMD` and hit enter to open a Command Prompt window.

    Make sure your Android device is connected and that USB debugging is enabled.  

    In the Command Prompt window, type one of the following commands, depending on which mode you plan to run the server in.  

    **TCP**  
    ```bat
    adb reverse tcp:52468 tcp:52468
    ```

    **UDP**  
    ```bat
    adb reverse udp:52468 udp:52468
    ```
    Start your `brokenithm_server.exe`.  
    Open Brokenithm on your Android device, and in the address bar, change the IP to `0.0.0.0`. Press the start button to connect. You will now be connected via the USB cable.  
    Run the game via the `start.bat` as normal.  

    If you extract the `platform-tools` folder to your `\Bin\app\` folder, you can add the following line to your `start.bat` to run this command when the game launches.
    ```bat
    start /min platform-tools/adb reverse tcp:52468 tcp:52468
    ```
    This should go above the line which starts the `brokenithm_server.exe`.

***

### Brokenithm iOS

!!! tip ""
    Requires jailbroken iOS device, or ability to install .ipa files.  
    Sideload https://sideloadly.io/  
    Follow IMPORTANT WINDOWS TASK (Install non-Microsoft Store version of iTunes, required for USB driver)  
    Install ipa to device https://redive.estertion.win/ipas/Brokenithm-iOS-build-10.ipa  
    Download brokenithm-evolved-ios https://redive.estertion.win/ipas/Brokenithm/Brokenithm-Evolved-iOS-v0.3.7z  
    Extract all files somewhere, not including aimeio.dll and chuniio.dll  
    run brokenithm-evolved-ios  
    run brokenithm on ipad

***

## Tasoller

!!! note "Tasoller:"
    The Tasoller is an arcade accurate controller, produced by DJ-DAO.  
    Out of the box, the Tasoller will only offer keyboard input, with no lighting support. To get full compatability with CHUNITHM, you will need to install [custom firmware](https://pixeldrain.com/u/DajSPEoa). Instructions on how to install the firmware are included in the archive.

!!! danger "Warning:"
    The Tasoller custom firmware is only compatabile with controllers running the DJ-DAO 2.0 firmware. If your controller was purchased after January 2022, it should have shipped with the update already applied.  
    If your Tasoller was purchased before 2022, and is still using the original firmware it shipped with, you will need to first update to 2.0 by following the guide on [DJ-DAO's website](https://www.dj-dao.com/en/support/11.html).  
    Once you've updated your controller to the DJ-DAO 2.0 firmware, you can follow the instructions included with the Custom Firmware as normal.

!!! tip ""
    DJ-DAO doesn't directly provide any input assistance for customers wanting to play on data. Thankfully there are community members creating open source alternatives.  
    There are two up to date drivers available for the Tasoller, with full support for Dniel97's segatools fork. Functionally these work the same as eachother, with the only difference being the language they are written in.  

    [chuniio-tasoller](https://gitea.tendokyu.moe/Scribbler/chuniio-tasoller) written in `zig`.  
    [chuniio-rs](https://gitea.tendokyu.moe/beerpsi/chuniio-rs) written in `rust`.  

    Head to the `Releases` tab for your chosen driver, and download the latest package. For `chuniio-rs` make sure you download the `chusan.zip`.  
    Extract the `*.dll` files to your `\App\bin\` folder.  
    Make the required changes to `segatools.ini`, as shown in the `Configuration` section of the readme for the driver you have downloaded.

***

## YubiDeck

!!! note "YubiDeck:"
    The YubiDeck is an arcade accurate controller, produced by ZhouSensor and sold by YubiParts. It also includes a built in Aime card scanner.

!!! tip ""
    YubiDeck firmware updates are provided in the support section of the YubiParts website. Unfortunately the IO driver they provide is no longer available for download.

    An open source alternative is available, [chuniio-yubideck](https://gitea.tendokyu.moe/beerpsi/chuniio-yubideck).  
    Head to the `Releases` tab and download the latest package. Extract the `*.dll` files to your `\App\bin\` folder.  
    Make the required changes to `segatools.ini`, as shown in the `Configuration` section of the chuniio-yubideck readme.  

    If you want to make use of the built-in card scanner, add the following line to the `[aimeio]` section in `segatools.ini`.  
    ```json
    path=aimeio_yubideck.dll
    ```