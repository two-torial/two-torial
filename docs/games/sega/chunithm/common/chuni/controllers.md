!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---

!!! tip ""

    segatools, by default, only accepts keyboard input and does not recognize any
    controllers. However, it can be configured with an IO DLL to add support for controllers.

    The controller you plan on using should also be provided with an IO DLL. If unsure,
    check the support section for your controller, or contact the vendor directly. Alternate
    options for the most common controllers are listed below.

    These IO DLLs should be copied to your game's `App\bin\` folder and referenced in
    `segatools.ini` under the `[chuniio]` section.
    
!!! tip ""

    To add your IO DLL, ncomment the `path=` line by removing the leading semicolon (`;`),
    then add your DLL's file name after the `=`:

    ```ini hl_lines="4"
    [chuniio]
    ; To use a custom Chunithm IO DLL enter its path here.
    ; Leave empty if you want to use Segatools built-in keyboard input.
    path=controller.dll
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
### TASOLLER

!!! tip ""

    - Install the [custom Host and LED firmware](https://pixeldrain.com/u/DajSPEoa) to your controller.
    Instructions on how to do so is provided in the linked archive.
    - Download the TASOLLER IO DLL corrosponding to your firmware version and extract to your `App\bin` folder.
        - [chuniio-rs](https://gitea.tendokyu.moe/beerpsi/chuniio-rs/releases) (download `chuni.zip`)
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:

    ```ini
    [chuniio]
    path=chuniio_tasoller_v2.dll
    ```

    - Connect the controller to your computer, and then start the game.

### TASOLLER PLUS

!!! tip ""

    - Switch your TASOLLER PLUS to WINUSB mode. You can do so in TASOLLER Options
    found on the djdao [support page](https://www.dj-dao.com/en/support/22.html).
    - Download TASOLLER PLUS IO DLLs and extract to your `App\bin` folder.
        - [chuniio-rs](https://gitea.tendokyu.moe/beerpsi/chuniio-rs/releases) (download `chuni.zip`)
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:

    ```ini
    [chuniio]
    path=chuniio_tasoller_plus.dll
    ```

    - Connect the controller to your computer, and then start the game.

### YubiDeck

!!! tip ""

    - Switch your YubiDeck to HID output mode. Instructions on how to do so are provided
    in the [YubiDeck manual](https://drive.google.com/file/d/11KVlKbg3zGCRwI7R-30t2IJc6OQwDEgo/view).
    - Download the latest **chuni** version of [YubiDeck IO DLLs](https://gitea.tendokyu.moe/beerpsi/chuniio-yubideck/releases)
    and extract it to your `App\bin` folder.
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:

    ```ini
    [chuniio]
    path=chuniio_yubideck_v3.dll
    ```

    - Optionally, reference the included AimeIO DLL to use the controller's
    built-in card reader:

    ```ini
    [aimeio]
    path=aimeio_yubideck_v3.dll
    ```

    - Connect the controller to your computer, and then start the game.

### Laverita 3

!!! tip ""

    - Switch your Laverita to IO mode. You can do so in ConfigApp
    found in the yuancon [discord](https://discord.gg/4ncuRrq).
    - Change the COM port of your controller. You can do so in
    Device manager by looking for `USB Serial Device` you may need to unplug and replug your controller to properly idetify which one is the Laverita.
    - Double click on it
    - Go to Port Settings
    - Click on Advanced
    - From the dropdown select COM1
    - Restart to ensure changes took effect and saved
    - Edit your `App\bin\segatools.ini` to disable io emulation and set led:

    ```ini
    [led]
    ; Output billboard LED strip data to a named pipe called "\\.\pipe\chuni_led"
    cabLedOutputPipe=0
    ; Output billboard LED strip data to serial
    cabLedOutputSerial=1
    
    ; Output slider LED data to the named pipe
    controllerLedOutputPipe=0
    ; Output slider LED data to the serial port
    controllerLedOutputSerial=1
    ; Use the OpeNITHM protocol for serial LED output
    controllerLedOutputOpeNITHM=0
    
    ; Serial port to send data to if using serial output. Default is COM5.
    serialPort=COM1
    ; Baud rate for serial data (set to 115200 if using OpeNITHM)
    serialBaud=9600

    [slider]
    ; Enable slider emulation. If you have real AC slider, set this to 0.
    ; Slider serial port must be COM1.
    enable=0
    ```

    - Then start the game.

??? tip "Legacy"

    - Backup Laverita 3 setup if IO4 cfw is not working.
    - Switch your Laverita to HID mode. You can do so in ConfigApp
    - Download Laverita IO DLLs and extract to your `App\bin` folder.
        - [chuniio-rs](https://gitea.tendokyu.moe/beerpsi/chuniio-rs/releases) (download `chuni.zip`)
    - Edit your `App\bin\segatools.ini` to reference the extracted DLLs:

    ```ini
    [chuniio]
    path=chuniio_laverita_v3.dll
    ```

    - Connect the controller to your computer, and then start the game.

### Arcade hardware and other controllers

!!! tip ""

    If you're interested in using a cabinet slider and air sensors, or possibly even
    making your own controller, the [Cons&Stuff website](https://consandstuff.github.io/)
    and Discord community is a great place to start!
