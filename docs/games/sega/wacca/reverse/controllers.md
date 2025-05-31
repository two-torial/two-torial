<img class="header-logo" src="/img/sega/wacca/reverse/logo.webp">
# Controllers

--8<-- "docs/snippets/common/data_warning.md"

!!! tip ""

    segatools, by default, only accepts keyboard input and XInput Controllers. 
    However, it can be configured with IO DLLs to add support for other controllers.

    The controller you plan on using should also be provided with these IO DLLs. If unsure,
    check the support section for your controller, or contact the vendor directly. Alternate
    options for the most common controllers are listed below.

    These IO DLLs should be copied to your game's `App\bin` folder and referenced in
    `segatools.ini` under the `[mercuryio]` section.
    
!!! tip ""

    If you have a single DLL, uncomment the `path=` line by removing the leading semicolon (`;`),
    then add your DLL's file name after the `=`:

    ```ini hl_lines="5"
    [mercuryio]
    ; To use a custom WACCA IO DLL enter its path here.
    ; Leave empty if you want to use Segatools built-in keyboard input.
    ;(1)!
    path=controller.dll
    ```

    1. Note that there is no leading semicolon.

## Touch screen / Mobile device

!!! tip ""

    Both Any2WACCAi and Toucca allows you to use a touch screen or a mobile device as a WACCA controller.
    It replicates the layout of an arcade WACCA cab.

!!! info "Installation instructions"

    [Any2WACCAi](https://gitea.tendokyu.moe/Dniel97/SEGAguide/wiki/SDFE#any2waccai-installation)  
    [Toucca](https://github.com/BlueGlassBlock/toucca/?tab=readme-ov-file#setup)

    !!! warning "com0com issues"

        If you're getting errors such as `Could not find file 'COM5'`, and particularly if you're on Windows 11, com0com v3 may be causing issues.  
        Install [com0com v2](https://sourceforge.net/projects/com0com/files/com0com/2.2.2.0/com0com-2.2.2.0-x64-fre-signed.zip/download) instead.

## WACVR

!!! tip ""

    WACVR allows you to use a VR Headset to replicate a WACCA cab and use it as a controller.

!!! tip "Setting up WACVR"

    Download WACVR from [here](https://github.com/xiaopeng12138/WACVR/releases/latest) and extract to a folder of your choice.
    Copy the `mercuryio.dll` file to the the `App/bin` folder in your data folder.

    Edit your `segatools.ini` like this:

    ```ini hl_lines="4"
    [mercuryio]
    ; To use a custom WACCA IO DLL enter its path here.
    ; Leave empty if you want to use Segatools built-in keyboard input.
    path=mercuryio.dll
    ```

    Start up your VR software as well as SteamVR, then launch WACCA and `WACVR.exe`.
    WACVR should set up with WACCA automatically.

!!! warning

    If you're experiencing a warped screen in WACVR, make sure your monitor is set to portrait mode and 
    check the `Full display capture` box in WACVR.

## Arcade hardware and other controllers

!!! tip ""

    If you want to run the game on a real cab, check the [reDIVE World website](https://redive.world/)

!!! tip ""

    If you're interested in using a cabinet slider, or possibly even
    making your own controller, the [Cons&Stuff website](https://consandstuff.github.io/)
    and Discord community is a great place to start!