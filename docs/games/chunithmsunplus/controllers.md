# CHUNITHM SUN PLUS Controller Setup

<img src="/img/chunithmsunplus/sunplus.png">

### How Controller Input works with segatools

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

***

!!! note "Controllers:"
    Below is a quick introduction and setup guide for the commonly used input methods.

### Keyboard

!!! tip ""
    Keyboard is the default input method, and while not recommended for playing the game, it is useful for testing purposes.  
    The default layout uses `SDFGHJKL` for the slider input, and `Space Bar` for the AIRs.  
    If you wish to change the default keybinds, an explanation for how to set these is included above the `[io3]` section in your `segatools.ini`.

### Brokenithm

!!! note "Brokenithm:"
    Brokenithm allows you to use an Android tablet or iPad as a controller for CHUNITHM. It uses the bottom half of the screen as the touch slider, and sliding from the bottom section into the top section of the screen activates the AIR sensors.

!!! tip ""
    todo:  
    android  
    ipad

### Tasoller

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

### YubiDeck

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