# Controllers

--8<-- "docs/snippets/common/data_warning.md"

!!! tip ""

    segatools, by default, only accepts keyboard input and does not recognize any
    controllers. However, it can be configured with IO DLLs to add support for controllers.

    The controller you plan on using should also be provided with these IO DLLs. If unsure,
    check the support section for your controller, or contact the vendor directly. Alternate
    options for the most common controllers are listed below.

    These IO DLLs should be copied to your game's `App\Package` folder and referenced in
    `segatools.ini` under the `[mai2io]` section.

!!! tip ""

    If you have a single DLL, uncomment the `path=` line by removing the leading semicolon (`;`),
    then add your DLL's file name after the `=`:

    ```ini hl_lines="5"
    [mai2io]
    ; To use a custom maimai DX IO DLL enter its path here.
    ; Leave empty if you want to use Segatools built-in keyboard input.
    ;(1)!
    path=controller.dll
    ```

    1. Note that there is no leading semicolon.

### Keyboard/Touchscreen

!!! tip ""

    Keyboard/Touchscreen is the default input method

    The default layout uses `QWEDCXZA` for physical buttons (each key representing the physical button's location relative to the center screen)

    If you wish to change the default keybinds, an explanation on how to set these is included
    above the `[io4]` section in your `segatools.ini`.

    Touch input should automatically work after connecting a touch-screen display

### ADX Controller

!!! tip ""

    First, you will need to purchase a compatible monitor if your controller did not come with one. A list of compatible monitors can be found on [this spreadsheet](https://docs.google.com/spreadsheets/d/1WN50pyJEPpXR32UTsEzsKe4Qm-EUAQgwmkCBX3kWB1Q)

    Plug your controller in and open `Device Manager`.

    Under the `Ports (COM & LPT)` section, ensure the correct ports are set for both the Touch Panel and Button LED.

    - (Touch Panel) USB Serial Device: `COM3`
    - (Button LED) USB-SERIAL CH340: `COM21`

    If they are different change the port of the device by `Right Clicking on the Device -> Properties -> Port Settings -> COM Port Number`

    Finally ensure the `mai2.ini` file in your data's `App/Package` folder has the following values set under the `[AM]` section
    ```
    [AM]
    Target=0
    DummyTouchPanel=0
    DummyLED=0
    ```

    This gets your controller working with keyboard inputs. Its highly recommended that you also view [this setup guide](https://github.com/maimai-dx/ADX-Controller-Guide/blob/master/document/Setup.md) which provides more detailed instructions, improved drivers, and help with adjusting touch panel sensitivity.

!!! warning
    You **DO NOT** need to follow the Network Setup steps in the linked guide above if you've already done so while setting up game data

    You **DO NOT** need to follow the Aime Reader setup in the linked guide above if you do not own one.



### Arcade hardware and other controllers

!!! tip ""

    If you're interested in using a cabinet, or possibly even
    making your own controller, the [Cons&Stuff website](https://consandstuff.github.io/)
    and Discord community is a great place to start!
