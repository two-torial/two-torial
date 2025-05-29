# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

--8<-- "docs/snippets/sega/common/old_data.md"

## Preparing data

--8<-- "docs/snippets/sega/common/drive_warning.md"

--8<-- "docs/snippets/common/data_readonly.md"

--8<-- "docs/snippets/sega/common/preparing_data.md"

    ```
    📂license
    📂package
    📄firewall.cfg
    📄game.bat
    ▶️pxGetHwinfo.exe
    📄pxGetHwInfo.ini
    ▶️RotateDisplay.exe
    📄system_config.json
    ```

--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating the base game

--8<-- "docs/snippets/sega/common/updating.md"

## Installing option data

!!! tip ""

    O.N.G.E.K.I. content updates are distributed through option folders instead of patching
    the base game. They are named `A???`, with each `?` being a number. Custom options
    distributed by the community might use letters instead, to distinguish them from
    official ones.

    Extract any options you've downloaded into the `Option` folder. You should end up with
    a file structure as follows. **Do not be worried if you have fewer or more option folders.**

    In some cases, your data may have options in `App\package\option`. If so, move
    all contents inside to the `Option` folder where `App` and `AppData` are and delete the `App\package\option` folder.

    ```
    📂A001
    📂A002
    📂A003
    📂A004
    📂A005
    📂A006
    📂A007
    📂A008
    📂A009
    📂A010
    📂A011
    📂A012
    ```

## Installing unprotected executables

!!! tip ""

    O.N.G.E.K.I. executables are protected and will not run on a regular computer.

    Obtain unprotected (also called "unpacked" or "decrypted" by the community)
    copies of the following files and the associated configuration file:

    - `amdaemon.exe`
    - `mu3.exe`
    - `mu3_Data\Plugins\amdaemon_api.dll`
    - `mu3_Data\Plugins\chiffre.dll`
    - `mu3_Data\Plugins\libhttp.dll`
    - `mu3_Data\Plugins\QR_Image.dll`
    - `mu3_Data\Managed\AMDaemon.NET.dll`
    - `mu3_Data\Managed\Assembly-CSharp-firstpass.dll`
    - `mu3_Data\Managed\Assembly-CSharp.dll`
    - `mu3.ini`

    Copy the files and folders into the `App/Package` folder of your game data. Agree to overwrite
    when asked.

    !!! Warning "Assembly-CSharp Note"

        `Assembly-CSharp.dll` **must** match your game version.

## Installing ICFs

--8<-- "docs/snippets/sega/common/icfs.md"

## mu3.ini

!!! tip ""
    Ensure that the `App\package` folder contains `mu3.ini`.

    If this configuration file is missing, create one using the contents below.

    ```ini
    [AM]
    IgnoreError=1
    OptionDev=0
    DummyAime=0
    DummyCredit=1
    DummyJVS=0

    [Sound]
    WasapiExclusive=0
    ```

    !!! danger "Warning"
        If you are following the folder structure of this guide, you must ensure that `OptionDev` is set to `0`
        in your `mu3.ini`, or else your Option data will not load.


## Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/Dniel97/segatools/releases)
    and download `segatools.zip`. **Do not download the source code.**
    - Extracting the archive should give you a few more zip files. Find **`mu3.zip`**
    and extract it to the `App\package` folder in your game data.

    You should now have a few more files inside the folder, as highlighted:

    <img width="500" src="/img/sega/ongeki/common/setup/1_ongeki_segatools_installed.webp">

## Configuring segatools

--8<-- "docs/snippets/sega/common/segatools_stubs.md"

=== "[vfs]"

    !!! tip ""

        If you've been matching the file structure as described in the [Preparing data](#preparing-data)
        section, you can fill in this section with the values below:

        ```ini
        [vfs]
        amfs=../../amfs
        option=../../Option
        appdata=../../AppData
        ```

--8<-- "docs/snippets/sega/common/segatools_vfs.md"

??? tip "mu3-mods"

    It's strongly recommended to use BepInEx mods to improve QOL.                                                                             
    You can find info about the available mods for O.N.G.E.K.I. here [mu3-mods](https://gitea.tendokyu.moe/akanyan/mu3-mods/wiki).                                                                         
    For general modding check [Unity modding](/extras/unity.md) page.                                                                                                                  

## Setting launch options

!!! tip ""
    Right click `App\package\start.bat`, select `Edit`. Locate the line that launches `mu3` and edit it according to your preferences:

    ```bat hl_lines="6"
    @echo off

    pushd %~dp0

    start "AM Daemon" /min inject -d -k mu3hook.dll amdaemon.exe -f -c config_common.json config_server.json config_client.json
    inject -d -k mu3hook.dll mu3 -screen-fullscreen 0 -popupwindow -screen-width 1080 -screen-height 1920
    taskkill /f /im amdaemon.exe > nul 2>&1

    echo.
    echo Game processes have terminated
    pause
    ```

??? tip "Launch options"
    * `-screen-fullscreen 0`: windowed
    * `-screen-fullscreen 0 -popupwindow`: borderless windowed
    * `-screen-fullscreen 1`: exclusive fullscreen
    * `-screen-width <W> -screen-height <H>`: resolution
    ??? warning "Note about resolution"
        - The service menu will only render correctly at 1080x1920.
        - This can be fixed with a patch.
    * `-monitor <N>`: the monitor to run the game on
    ??? info "Getting the monitor index"
        Navigate to Windows display settings. Each monitor should be assigned a number.
        The monitor index is that number. For example, monitor 2 means `-monitor 2`.

## Connecting to a network

!!! danger "Pick one or the other, not both!"

--8<-- "docs/snippets/sega/common/online_network.md"

--8<-- "docs/snippets/sega/common/local_network.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Audio properties

--8<-- "docs/snippets/common/audio_properties.md"

## Fixing OpenSSL on Intel 10th Gen and newer CPUs

--8<-- "docs/snippets/sega/common/openssl.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

--8<-- "docs/snippets/sega/common/first_launch_info.md"

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Start the game by running `App\package\start.bat`. Let the game load until you reach a screen with the message below.

    <img src="/img/sega/ongeki/common/setup/servicemenu/0_ongeki_groupcheck.webp">

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the 6th option).

    <img src="/img/sega/ongeki/common/setup/servicemenu/1_gamesettings.webp">


    Select **グループ内基準機の設定** (`SET STANDARD IN GROUP`, the second option)
    and toggle this setting to **基準機** (`STANDARD`).

    <img src="/img/sega/ongeki/common/setup/servicemenu/2_reference.webp">


    Select **終了** (`EXIT`, the last option) to exit to the main service menu.



    Navigate to **閉店設定** (`CLOSE SETTING`, the 10th option).

    <img src="/img/sega/ongeki/common/setup/servicemenu/3_closesetting.webp">


    Navigate to **時** (`HOUR`, the 2nd option) and use the `Service` button
    to toggle the setting until it says **全時刻** (`ALL TIME`).

    <img src="/img/sega/ongeki/common/setup/servicemenu/4_alltime.webp">


    Select **終了** (`EXIT`, the last option) to exit to the main service menu, then select **終了**
    (also the last option) in the main menu to exit the service menu.

--8<-- "docs/snippets/sega/common/custom_mods.md"

--8<-- "docs/snippets/sega/common/finish.md"

## Help

--8<-- "docs/snippets/common/help.md"