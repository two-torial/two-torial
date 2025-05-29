<img class="header-logo" src="/img/sega/wacca/reverse/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

--8<-- "docs/snippets/sega/common/old_data.md"

## Preparing data

--8<-- "docs/snippets/sega/common/drive_warning.md"

--8<-- "docs/snippets/common/data_readonly.md"

    You should end up with a file structure as follows.

    ```
    📂amfs
    📂App
    📂AppData
    ```

    The `App` folder should have a file structure as follows.

    ```
    📂bin
    📂pxbin
    📂WindowsNoEditor
    📄firewall.cfg
    ▶️game.bat
    ▶️pxGetHwinfo.exe
    📄pxGetHwInfo.ini
    📄system_config.json
    ```

--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating the base game

!!! tip ""

    Extract all updates in order. Agree to overwrite files if necessary.

    For example, if you have `3.00.00`; install `3.01.00`, then `3.02.00`, etc.


## Installing ICFs

--8<-- "docs/snippets/sega/common/icfs.md"

## Patching the game

!!! info "Go through the [Web Patching](/extras/patchweb.md) guide to learn how to use a web patcher."

## Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/Dniel97/segatools/releases)
    and download `segatools.zip`. **Do not download the source code.**
    - Extracting the archive should give you a few more zip files. Find **`mercury.zip`**
    and extract it to the `App\bin` folder in your game data.

    You should now have a few more files inside the folder, as highlighted:

    <img width="500" src="/img/sega/wacca/reverse/setup/1_wacca_segatools_installed.webp">

## Configuring segatools

!!! tip ""

    Since there is no graphical configuration tool for segatools, you will have to edit the
    configuration file by hand. It is found in `App\bin\segatools.ini`.

--8<-- "docs/snippets/sega/common/segatools_stubs.md"

=== "[vfs]"

    !!! tip ""

        If you've been matching the file structure as described in the [Preparing data](#preparing-data)
        section, you can fill in this section with the values below:

        ```ini
        [vfs]
        amfs=../../amfs
        appdata=../../AppData
        ```

    --8<-- "docs/snippets/sega/common/segatools_relative_directories.md"

## Connecting to a network

!!! danger "Pick one or the other, not both!!"

--8<-- "docs/snippets/sega/common/online_network.md"

--8<-- "docs/snippets/sega/common/local_network.md"

## Install FTDI LEDs driver

!!! tip ""

    Download FTDI drivers from [here](https://ftdichip.com/wp-content/uploads/2023/09/CDM-v2.12.36.4-WHQL-Certified.zip)
    and extract them to a folder of your choice, then copy `CDM-v2.12.36.4-WHQL-Certified/amd64/ftd2xx64.dll` to 
    `/App/WindowsNoEditor/Mercury/Binaries/Win64` and then rename the file to `ftd2xx.dll`.

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Set your display orientation to portrait mode.

    Start the game by running `App\bin\start.bat`.

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
    with `start.bat`.

--8<-- "docs/snippets/sega/common/finish.md"

## Help

--8<-- "docs/snippets/common/help.md"