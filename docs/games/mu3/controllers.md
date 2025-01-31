!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---

!!! tip ""

    segatools, by default, only accepts keyboard input and XInput Controllers. 
    However, it can be configured with IO DLLs to add support for other controllers.

    The controller you plan on using should also be provided with these IO DLLs. If unsure,
    check the support section for your controller, or contact the vendor directly. Alternate
    options for the most common controllers are listed below.

    These IO DLLs should be copied to your game's `App\bin\` folder and referenced in
    `segatools.ini` under the `[mu3io]` section.
    
!!! tip ""

    If you have a single DLL, uncomment the `path=` line by removing the leading semicolon (`;`),
    then add your DLL's file name after the `=`:

    ```ini hl_lines="5"
    [mu3io]
    ; To use a custom O.N.G.E.K.I. IO DLL enter its path here.
    ; Leave empty if you want to use Segatools built-in keyboard/gamepad input.
    ;(1)!
    path=controller.dll
    ```

    1. Note that there is no leading semicolon.

---

### Keyboard and Mouse

!!! tip ""

    Keyboard and Mouse is the default input method.

    To enable mouse lever emulation ensure that the `mouse` option is set to `1` in the `[io4]` 
    section of your `segatools.ini`:

    ```ini hl_lines="3"
    [io4]
    ; Set "1" to enable mouse lever emulation, "0" to use XInput
    mouse=1
    ```
    
    The default layout use `ASD` for the left 3 buttons, and `JKL` for the right 3 buttons.
    `Mouse Left/Right Click` are used for the left and right bumper buttons.

    If you wish to change the default keybinds, an explanation on how to set these is included
    above the `[io4]` section in your `segatools.ini`.

---

### XInput Controller
!!! tip ""

    XInput controllers are supported by segatools. To enable XInput, ensure that the `mouse` option
    is set to `0` in the `[io4]` section of your `segatools.ini`:

    ```ini hl_lines="3"
    [io4]
    ; Set "1" to enable mouse lever emulation, "0" to use XInput
    mouse=0
    ```

    If you wish to change the default keybinds, an explanation on how to set these is included
    above the `[io4]` section in your `segatools.ini`.
---

### Mageki

!!! tip ""

    Mageki allows you to use a mobile device as a ONGEKI controller. It replicates the layout
    of an arcade ONGEKI controller on your mobile device.

    Mageki supports both Android and iOS devices. For installation instructions, please refer to
    the [English User Manual on the Mageki GitHub Repository](https://github.com/Sanheiii/Mageki/wiki/Mageki-User-Manual).

!!! warning "Configuring ongeki-io and MU3-input.dll"

	When moving the zipped contents of `MU3Input`, move all folders **EXCEPT** the `segatools.ini` file into your `App\package` folder.
    Modify the `[mu3io]` and `[aimeio]` sections of your existing `segatools.ini` file to look like the following:

    ```ini hl_lines="2 5"
    [mu3io]
    path = MU3Input.dll

    [aimeio]
    path64 = MU3Input.dll
    ```
    If these sections do not exist, add them to the end of your `segatools.ini` file.

!!! info "IOConfig doesn't launch for me/This application requires the Windows App Runtime"

    Download and extract the contents of the [Windows App Runtime Version 1.5 Redustributable](https://aka.ms/windowsappsdk/1.5/1.5.240802000/Microsoft.WindowsAppRuntime.Redist.1.5.zip)
    In the `WindowsAppSDK-Installer-x64` folder run `WindowsAppRuntimeInstall-x64.exe`

    If IOConfig still fails to launch, try using the [SelfContained version of ongeki-io](https://github.com/Sanheiii/ongeki-io/releases)

---
    
### Arcade hardware and other controllers

!!! tip ""

    If you're interested in using a cabinet slider and air sensors, or possibly even
    making your own controller, the [Cons&Stuff website](https://consandstuff.github.io/)
    and Discord community is a great place to start!
