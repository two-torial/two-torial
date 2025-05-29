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
    ▶️pwGetHwinfo.exe
    📄pxGetHwInfo.ini
    📄system_config.json
    ```
--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating the base game

!!! tip ""

    Extract your patch's files to your existing data in a way that matches its
    file structure. Agree to overwrite files if necessary.

## Installing option data

!!! tip ""

    maimai DX content updates are distributed through option folders instead of patching
    the base game.

    Options are named with a letter followed by three numbers.

    For JPN(SDEZ) data, each new release of maimai DX increments the first letter of the Option (ie. BUDDiES is `H???` and BUDDiES+ is `I???`).

    For EXP(SDGA) data, Options will always begin with the letter `A` (i.e `A???`)

    Extract any options you've downloaded into the `Option` folder. You should end up with
    a file structure as follows. **Do not be worried if you have fewer or more option folders.**

    ```
    📂H005
    📂H011
    📂H021
    📂H031
    📂H032
    📂H041
    📂H051
    📂H061
    📂H100
    ```

    !!! warning "Do not mix option data between versions"

## Installing unprotected executables

!!! tip ""

    maimai DX executables are protected and will not run on a regular computer.

    Obtain unprotected (also called "unpacked" or "decrypted" by the community)
    copies of the following files and the associated configuration file:

    - amdaemon.exe
    - Sinmai.exe
    - Sinmai_Data/Plugins/amdaemon_api.dll
    - Sinmai_Data/Plugins/Cake.dll (JPN/SDEZ only)
    - Sinmai_Data/Managed/AMDaemon.NET.dll
    - Sinmai_Data/Managed/Assembly-CSharp.dll
    - mai2.ini

    Copy the files and folders into the `App/Package` folder of your game data. Agree to overwrite
    when asked.

    !!! Warning "Assembly-CSharp Notes"

        `Assembly-CSharp.dll` **must** match your game version. All others can be
        reused from other game versions.

## Installing ICFs

--8<-- "docs/snippets/sega/common/icfs.md"

## mai2.ini

!!! tip ""
    Ensure that the `App\Package` folder contains `mai2.ini`.

    If this configuration file is missing, create one using the contents below.

    ```ini
    [Debug]
    Debug=1
    
    [AM]
    Target=0
    IgnoreError=1
    DummyTouchPanel=1
    DummyLED=1
    DummyCodeCamera=1
    DummyPhotoCamera=1
    
    [Sound]
    Sound8Ch=0
    ```

## Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/TeamTofuShop/segatools/releases/tag/2024-03-13)
    and download the `segatools.zip` from `2024-03-13`. **Do not download the source code or latest release.**
    - Extracting the archive should give you a few more zip files. Find `mai2.zip`
    and extract it to the `App/Package` folder in your game data.

    You should now have a few more files inside the `App/Package` folder, as highlighted:

    <img width="500" src="/img/sega/maimaidx/common/setup/segatools.webp">

!!! warning

    The latest release of segatools currently has issues with maimai, and for the time being an older version of segatools is preferred.

## Configuring segatools

!!! tip ""

    Since there is no graphical configuration tool for segatools, you will have to edit the
    configuration file by hand. It is found in `App\Package\segatools.ini`.

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

--8<-- "docs/snippets/sega/common/segatools_relative_directories.md"

??? tip "AquaMai"

    It's strongly recommended to use MelonLoader mods to improve QOL.                                                                             
    You can find info about the available mods for maimai here [AquaMai](https://github.com/MewoLab/AquaMai).                                                                         
    For general modding check [Unity modding](/extras/unity.md) page.                                                                                                                  

## Setting launch options

!!! tip ""
    Right click `App\Package\start.bat`, select `Edit`. Locate the line that launches `sinmai` and edit it according to your preferences:

    ```bat hl_lines="6"
    @echo off
    
    pushd %~dp0
    
    start "AM Daemon" /min inject -d -k mai2hook.dll amdaemon.exe -f -c config_common.json config_server.json config_client.json
    inject -d -k mai2hook.dll sinmai -screen-fullscreen 0 -popupwindow -screen-width 2160 -screen-height 1920  -silent-crashes
    
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
    * `-monitor <N>`: the monitor to run the game on
    ??? info "Getting the monitor index"
        Navigate to Windows display settings. Each monitor should be assigned a number.
        The monitor index is that number. For example, monitor 2 means `-monitor 2`.

## Connecting to a network

!!! danger "Pick one or the other, not both!!"

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

    <img src="/img/sega/maimaidx/common/setup/distribution_servers_check.webp">

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the 7th option).

    <img src="/img/sega/maimaidx/common/setup/service_menu.webp">

    Select **店内マッチングの設定** (`IN-STORE MATCHING SETUP`, the first option)
    and toggle this setting to **OFF**.

    <img src="/img/sega/maimaidx/common/setup/service_game_settings.webp">

    Select **終了** (`EXIT`, the last option) to exit to the main service menu.

--8<-- "docs/snippets/sega/common/custom_mods.md"

--8<-- "docs/snippets/sega/common/finish.md"

## Help

--8<-- "docs/snippets/common/help.md"