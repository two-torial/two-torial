<img class="header-logo" src="/img/sega/wacca/reverse/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

--8<-- "docs/snippets/sega/common/data_old.md"

!!! warning "Wireless Device"
    
    The Chinese SDJE Version requires a custom piece of hardware that will likely not work with known tools.

    If you're having issues with a "Wireless Device" during boot or network testing, you likely need a different version of the game data.

## Preparing data

--8<-- "docs/snippets/sega/common/data_driveletter.md"

--8<-- "docs/snippets/common/data_readonly.md"

--8<-- "docs/snippets/sega/common/data_preparation.md"

    ```
    📂bin
    📂pxbin
    📂WindowsNoEditor
    📄firewall.cfg
    ▶️game.bat
    ▶️pxGetHwinfo.exe
    📝pxGetHwInfo.ini
    📄system_config.json
    ```

--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating data

--8<-- "docs/snippets/sega/common/data_updating.md"

## Installing ICFs

--8<-- "docs/snippets/sega/common/data_icfs.md"

## Patching the game

--8<-- "docs/snippets/sega/common/patching.md"

## Installing segatools

--8<-- "docs/snippets/sega/common/segatools_install.md"
    - Find `mercury.zip` and extract it to your data's `App\bin` folder

    You should now have these files added to your `App\bin` directory:

    ```
    📂DEVICE
    ▶️inject.exe
    ⚙️mercuryhook.dll
    📝segatools.ini
    ▶️launch.bat
    ```

## Configuring segatools

--8<-- "docs/snippets/sega/common/segatools_preamble_bin.md"

=== "[vfs]"

--8<-- "docs/snippets/sega/common/segatools_relativepaths.md"

--8<-- "docs/snippets/sega/common/segatools_vfs.md"

## Configuring audio

--8<-- "docs/snippets/common/audio_48khz.md"

## Connecting to a network

--8<-- "docs/snippets/sega/common/network_preamble.md"

--8<-- "docs/snippets/sega/common/network_remote.md"

--8<-- "docs/snippets/sega/common/network_local.md"

## Installing FTDI LEDs driver

!!! tip ""

    - Download the [FTDI drivers](https://ftdichip.com/wp-content/uploads/2023/09/CDM-v2.12.36.4-WHQL-Certified.zip)
    - Extract them
    - Copy `CDM-v2.12.36.4-WHQL-Certified/amd64/ftd2xx64.dll`  
      to `/App/WindowsNoEditor/Mercury/Binaries/Win64/`
    - Rename the file to `ftd2xx.dll`

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Set your display orientation to portrait mode.

    Start the game by running `App\bin\launch.bat`.

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    You can also use the Volume buttons (default `UP` and `DOWN` keys) to navigate
    and the `ENTER` key to select.

    Navigate to **SYSTEM SETTING**.

    <img src="/img/sega/wacca/reverse/setup/servicemenu/1_systemsetting.webp">

    Navigate to **CLOSING TIME SETTINGS**.

    <img src="/img/sega/wacca/reverse/setup/servicemenu/2_closingtime.webp">

    Navigate to **ALL DAYS OF THE WEEK** and use the `Service` button
    to toggle the setting until it says **OFF**.

    <img src="/img/sega/wacca/reverse/setup/servicemenu/3_closingtimesetting.webp">

    Select **APPLY SETTINGS AND RE-BOOT** to save the settings.

    Note that this will close your game and you will have to start it again
    with `launch.bat`.

--8<-- "docs/snippets/sega/common/success.md"

## Help

--8<-- "docs/snippets/common/help.md"
