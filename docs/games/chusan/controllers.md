!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---

!!! tip ""

    segatools, by default, only accepts keyboard input and does not recognize any
    controllers. However, it can be configured with IO DLLs to add support for controllers.

    The controller you plan on using should also be provided with these IO DLLs. If unsure,
    check the support section for your controller, or contact the vendor directly. Alternate
    options for the most common controllers are listed below.

    These IO DLLs should be copied to your game's `App\bin\` folder and referenced in
    `segatools.ini` under the `[chuniio]` section.
    
!!! tip ""

    If you have a single DLL, uncomment the `path=` line by removing the leading semicolon (`;`),
    then add your DLL's file name after the `=`:

    ```ini hl_lines="5"
    [chuniio]
    ; Uncomment this if you have custom chuniio implementation comprised of a single 32bit DLL.
    ; (will use chu2to3 engine internally)
    ;(1)!
    path=controller.dll
    ```

    1. Note that there is no leading semicolon.

!!! tip ""

    If you have two DLLs, ending in `_x86.dll` and `_x64.dll` (or `_chusan.dll` and `_amdaemon.dll`),
    uncomment the `path32=` and `path64=` lines by removing the leading semicolon (`;`), then
    add your DLLs after the `=`:

    ```ini hl_lines="5 6"
    [chuniio]
    ; Uncomment both of these if you have custom chuniio implementation comprised of two DLLs.
    ; x86 chuniio to path32, x64 to path64. Both are necessary.
    ;(1)!
    path32=controller_x86.dll
    path64=controller_x64.dll
    ```

    1. Note that there is no leading semicolon.

---

### Keyboard

!!! tip ""

    Keyboard is the default input method, and while not recommended for playing the game,
    it is useful for testing purposes.
    
    The default layout uses `SDFGHJKL` for slider input, and `Space Bar` for the AIRs.

    If you wish to change the default keybinds, an explanation on how to set these is included
    above the `[io3]` section in your `segatools.ini`.

---

### Brokenithm

!!! tip ""

    Brokenithm allows you to use a mobile device as a CHUNITHM controller. It uses the bottom
    half of the screen as the ground slider, and sliding into the upper half activates the air
    sensors.

#### Android

!!! warning

    Your computer and your Android device must be on the same local network.

!!! tip ""

    - Download the latest version of [Brokenithm-Android](https://github.com/tindy2013/Brokenithm-Android/releases/latest)
    and install it on your Android device.
    - Download the latest version of [Brokenithm-Android-Server](https://github.com/tindy2013/Brokenithm-Android-Server/releases/latest)
    and extract **only `brokenithm_server.exe`** to your `App\bin\` folder.
    - Download the latest version of [Brokenithm-Evolved IO DLLs](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/releases) and extract the DLL files to your `App\bin\` folder.
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:
    
    ```ini hl_lines="2"
    [aimeio]
    path=aime_brokenithm.dll
    ```

    ```ini hl_lines="2 3"
    [chuniio]
    path32=brokenithm_x86.dll
    path64=brokenithm_x64.dll
    ```

    - Run `brokenithm_server.exe`. A command prompt window should open, saying that
    it is waiting for a device on port 52468.
    - Open the Brokenithm app on your Android device. Enter your computer's IP address
    in the Address box on the top right, then tap Start.
    - Run the game as normal.

??? info "Getting your computer's IP address"

    Open **Settings** -> **Network and Internet** and select **Properties**. Scroll down to
    the bottom and check the address under the **IPv4 address** field:

    <img src="/img/chunithm/sdhd/controllers/0_ipaddress.png">

    That is your computer's IP address.

??? info "Automatically launching the Brokenithm server when starting the game"

    **This will only work if you extracted `brokenithm_server.exe` to `App\bin\` as previously instructed.**
    
    You can edit the launch script to launch the Brokenithm server when starting the game.
    Edit `App\bin\start.bat` to add a line above the existing commands:

    ```batch hl_lines="5"
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

??? info "Improving latency"

    You can improve latency by running Brokenithm with your Android device tethered to
    your computer. However, this requires a little extra setup:

    - Connect your Android device to your computer with a USB cable.
    - If you haven't enabled Developer options on your device, do it by navigating to
    the "About" page in your phone's settings, then tap "Build number" seven times.
    This varies by device, so if unsure, look up the instructions for your specific
    one.
    - Navigate to Developer options and enable USB debugging.
    - On your computer, download and extract [Android SDK Platform Tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
    to your `App\bin\` folder.
    - Navigate to the `App\bin\platform-tools` folder in File Explorer, click on the
    address bar, type `cmd`, and hit Enter to open a command prompt.
    - In the command prompt, type the following command:

    ```batch
    adb reverse tcp:52468 tcp:52468
    ```

    - Start brokenithm_server in TCP mode with the -T command line flag, `brokenithm_server.exe -T`.
    - On your Android device, open Brokenithm, and change the address to `0.0.0.0`.
        - If the text box to the left of the "SETTINGS" button say "UDP", tap on it
    once to switch to "TCP" mode.
    - Tap on "START", and you will now be connected via the USB cable.
    - You can now start the game as normal.

    The next time you play the game, you only need to run the `adb reverse ...` command
    again. To do this automatically when the game starts, add a line to the `start.bat`
    script **before** the `brokenithm_server` line:

    ```batch hl_lines="5 6"
    @echo off

    pushd %~dp0

    start /min platform-tools\adb reverse tcp:52468 tcp:52468
    start /min brokenithm_server -T
    start /min inject_x64 -d -k chusanhook_x64.dll amdaemon.exe -c config_common.json config_server.json config_client.json config_cvt.json config_sp.json config_hook.json
    inject_x86 -d -k chusanhook_x86.dll chusanApp.exe
    taskkill /f /im amdaemon.exe > nul 2>&1

    echo.
    echo Game processes have terminated
    pause
    ```

#### iOS/iPadOS

!!! tip ""

    - Install Brokenithm on your iOS/iPadOS device by joining the [Brokenithm TestFlight](https://testflight.apple.com/join/U6kwvETm) ^^(iOS 18 only)^^.
        - If your iOS/iPadOS device doesn't have iOS 18, you will need to sideload a different [IPA](https://redive.estertion.win/ipas/Brokenithm-iOS-build-10.ipa) with [Sideloadly](https://sideloadly.io/).
    - If you have iTunes and/or iCloud installed from the Microsoft Store on your computer, **uninstall it.**
    - Install the **non-Microsoft Store** version of iTunes from the [website](https://www.apple.com/itunes/download/win64).
    - Download the latest version of [Brokenithm-Evolved-iOS server](https://redive.estertion.win/ipas/Brokenithm/Brokenithm-Evolved-iOS-v0.3.7z)
    and extract it to `App\bin\Brokenithm-Server`.
    - Download the latest version of [Brokenithm-Evolved IO DLLs](https://gitea.tendokyu.moe/Dniel97/Brokenithm-Evolved/releases) and extract the DLL files to your `App\bin\` folder.
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:
    
    ```ini hl_lines="2"
    [aimeio]
    path=aime_brokenithm.dll
    ```

    ```ini hl_lines="2 3"
    [chuniio]
    path32=brokenithm_x86.dll
    path64=brokenithm_x64.dll
    ```

    - Run `App\bin\Brokenithm-Server\Brokenithm-Evolved-iOS.exe`. A command prompt window
    should open, saying that it is waiting for a device.
    - On your iOS/iPadOS device, open Brokenithm, and connect it to your computer with a
    USB cable.
    - Run the game as normal.

??? info "Automatically launching the Brokenithm server when starting the game"

    **This will only work if you extracted the server to `App\bin\Brokenithm-Server` as previously instructed.**
    
    You can edit the launch script to launch the Brokenithm server when starting the game.
    Edit `App\bin\start.bat` to add a line above the existing commands:

    ```batch hl_lines="5"
    @echo off

    pushd %~dp0

    start /min Brokenithm-Server\Brokenithm-Evolved-iOS.exe
    start /min inject_x64 -d -k chusanhook_x64.dll amdaemon.exe -c config_common.json config_server.json config_client.json config_cvt.json config_sp.json config_hook.json
    inject_x86 -d -k chusanhook_x86.dll chusanApp.exe
    taskkill /f /im amdaemon.exe > nul 2>&1

    echo.
    echo Game processes have terminated
    pause
    ```

### TASOLLER

!!! warning

    This guide only covers TASOLLERs running the v2.0 touch firmware. If you've purchased the
    controller after January 2022, the update should have already been applied.

    If you've purchased the controller before then, you will need to update the touch
    firmware by following the instructions on [DJ-DAO's support page](https://www.dj-dao.com/en/support/11.html).

!!! tip ""

    - Install the [custom Host and LED firmware](https://pixeldrain.com/u/DajSPEoa) to your controller.
    Instructions on how to do so is provided in the linked archive.
    - Pick one of these two TASOLLER IO DLLs to download and extract to your `App\bin` folder.
    They should be functionally the same, but if one doesn't work, you can try the other:
        - [chuniio-tasoller](https://gitea.tendokyu.moe/Scribbler/chuniio-tasoller/releases) (download `lib.zip`)
        - [chuniio-rs](https://gitea.tendokyu.moe/beerpsi/chuniio-rs/releases) (download `chusan.zip`)
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:

    ```ini
    [chuniio]
    path32=chuniio_tasoller.dll;(1)!
    path64=chuniio_tasoller_x64.dll;(2)!
    ```
    
    1. Or `chuniio_tasoller_v2_chusan.dll` if you downloaded `chuniio-rs`.
    2. Or `chuniio_tasoller_v2_amdaemon.dll` if you downloaded `chuniio-rs`.

    - Connect the controller to your computer, and then start the game.

### YubiDeck

!!! tip ""

    - Switch your YubiDeck to HID output mode. Instructions on how to do so are provided
    in the [YubiDeck manual](https://drive.google.com/file/d/11KVlKbg3zGCRwI7R-30t2IJc6OQwDEgo/view).
    - Download the latest version of [YubiDeck IO DLLs](https://gitea.tendokyu.moe/beerpsi/chuniio-yubideck/releases)
    and extract it to your `App\bin` folder.
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:

    ```ini
    [chuniio]
    path32=chuniio_yubideck_chusan.dll
    path64=chuniio_yubideck_amdaemon.dll
    ```

    - Optionally, reference the included AimeIO DLL to use the controller's
    built-in card reader:

    ```ini
    [aimeio]
    path=aimeio_yubideck.dll
    ```

    - Connect the controller to your computer, and then start the game.

### Arcade hardware and other controllers

!!! tip ""

    If you're interested in using a cabinet slider and air sensors, or possibly even
    making your own controller, the [Cons&Stuff website](https://consandstuff.github.io/)
    and Discord community is a great place to start!
