# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

--8<-- "docs/snippets/sega/common/data_old.md"

## Preparing data

--8<-- "docs/snippets/sega/common/data_driveletter.md"

--8<-- "docs/snippets/common/data_readonly.md"

--8<-- "docs/snippets/sega/common/data_preparation.md"

    ```
    📂license
    📂package
    📄firewall.cfg
    ▶️game.bat
    ▶️pxGetHwinfo.exe
    📝pxGetHwInfo.ini
    ▶️RotateDisplay.exe
    📄system_config.json
    ```

--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating data

--8<-- "docs/snippets/sega/common/data_updating.md"

## Installing option data

!!! tip ""

    SEGA games receive content updates through option folders rather than direct game file updates.

    For O.N.G.E.K.I., official options are named `A???`, where `???` represents a sequence of numbers.  
    Community-created options often use letters instead of numbers to differentiate them from official releases.

    After downloading option files, extract them into your game's `Option` folder.

    ```
    📂amfs
    📂App
    📂AppData
    📂Option
    ┣━📂A001
    ┣━📂A002
    ┣━📂A012
    ┗━ etc.
    ```

!!! info "Option numbers don't always follow a sequential pattern<br>It's common to see the numbers jump, for example `A001` then `A012`"

## Installing unprotected executables

!!! tip ""

    O.N.G.E.K.I. executables are protected and will not run on a regular computer.

    - Obtain unprotected (also called "unpacked" or "decrypted" by the community) copies of of the following folders and files:

    ```
    ▶️amdaemon.exe
    ▶️mu3.exe
    📂mu3_Data
    ┣━📂Plugins
    ┃  ┣━⚙️amdaemon_api.dll
    ┃  ┣━⚙️chiffre.dll
    ┃  ┣━⚙️libhttp.dll
    ┃  ┗━⚙️QR_Image.dll
    ┗━📂Managed
       ┣━⚙️AMDaemon.NET.dll
       ┣━⚙️Assembly-CSharp-firstpass.dll
       ┗━⚙️Assembly-CSharp.dll
    📝mu3.ini
    ```

    - Copy all of the above to your data's `App\package` folder
    - Agree to overwrite when asked

!!! warning "Assembly-CSharp Notes"

    `Assembly-CSharp.dll` **must** match your game version.  
    All other files can be reused between game versions.

## Installing ICFs

--8<-- "docs/snippets/sega/common/data_icfs.md"

## mu3.ini

!!! tip ""

    Ensure that the `App\package` folder contains `mu3.ini`.

    If this configuration file is missing, create one using the contents below:

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

    When using the folder structure proposed in this guide, setting `OptionDev=0` in `mu3.ini` is required for the game to properly load Option data.

## Installing segatools

--8<-- "docs/snippets/sega/common/segatools_install.md"
    - Find `mu3.zip` and extract it to your data's `App\package` folder

    You should now have these files added to your `App\package` directory:

    ```
    📂DEVICE
    ▶️inject.exe
    ⚙️mu3hook.dll
    📝segatools.ini
    ▶️launch.bat
    ```

## Configuring segatools

--8<-- "docs/snippets/sega/common/segatools_preamble_package.md"

=== "[vfs]"

--8<-- "docs/snippets/sega/common/segatools_relativepaths.md"

--8<-- "docs/snippets/sega/common/segatools_vfs.md"

??? tip "mu3-mods"
                                                      
    Find more info about O.N.G.E.K.I. mods here [mu3-mods](https://gitea.tendokyu.moe/akanyan/mu3-mods/wiki).  
    Also check our [Unity modding](/extras/unity.md) guide.

## Configuring audio

--8<-- "docs/snippets/common/audio_48khz.md"

## Connecting to a network

--8<-- "docs/snippets/sega/common/network_preamble.md"

--8<-- "docs/snippets/sega/common/network_remote.md"

--8<-- "docs/snippets/sega/common/network_local.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

--8<-- "docs/snippets/sega/common/service_jp_googlelens.md"

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Start the game by running `App\package\launch.bat`. Let the game load until you reach a screen with the message below.

    <img src="/img/sega/ongeki/common/setup/servicemenu/0_ongeki_groupcheck.webp">

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the 6th option).

    <img class="portrait" src="/img/sega/ongeki/common/setup/servicemenu/1_gamesettings.webp">


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

--8<-- "docs/snippets/sega/common/success.md"

## Help

--8<-- "docs/snippets/common/help.md"
