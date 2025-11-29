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
    ▶️pwGetHwinfo.exe
    📝pxGetHwInfo.ini
    📄system_config.json
    ```
--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating data

--8<-- "docs/snippets/sega/common/data_updating.md"

## Installing option data

!!! tip ""

    SEGA games receive content updates through option folders rather than direct game file updates.

    - maimai DX JPN(SDEZ): each new release of maimai DX increments the first letter of the Options (ie. `H???` for BUDDiES, `I???` BUDDiES+)
    - maimai DX EXP(SDGA): Options will always begin with the letter `A` (i.e `A???`)
    - `???` represents a sequence of numbers

    After downloading option files, extract them into your game's `Option` folder.

    ```
    📂amfs
    📂App
    📂AppData
    📂Option
    ┣━📂H005
    ┣━📂H011
    ┣━📂H031
    ┗━ etc.
    ```

!!! info "Option numbers don't always follow a sequential pattern<br>It's common to see the numbers jump, for example `H005` then `H011`"

!!! warning "Do not mix option data between game versions"

## Installing unprotected executables

!!! tip ""

    maimai DX executables are protected and will not run on a regular computer.

    - Obtain unprotected (also called "unpacked" or "decrypted" by the community) copies of of the following folders and files:

    ```
    ▶️amdaemon.exe
    ▶️Sinmai.exe
    📂Sinmai_Data
    ┣━📂Plugins
    ┃  ┣━⚙️amdaemon_api.dll
    ┃  ┗━⚙️Cake.dll (JPN/SDEZ only)
    ┗━📂Managed
       ┣━⚙️AMDaemon.NET.dll
       ┗━⚙️Assembly-CSharp.dll
    📝mai2.ini
    ```

    - Copy all of the above to your data's `App\package` folder
    - Agree to overwrite when asked

!!! warning "Assembly-CSharp Notes"

    `Assembly-CSharp.dll` **must** match your game version.  
    All other files can be reused between game versions.

## Installing ICFs

--8<-- "docs/snippets/sega/common/data_icfs.md"

## mai2.ini

!!! tip ""

    Ensure that the `App\package` folder contains `mai2.ini`.

    If this configuration file is missing, create one using the contents below:

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

--8<-- "docs/snippets/sega/common/segatools_install.md"
    - Find `mai2.zip` and extract it to your data's `App\package` folder

    You should now have these files added to your `App\package` directory:

    ```
    📂DEVICE
    ▶️inject.exe
    ⚙️mai2hook.dll
    📝segatools.ini
    ▶️launch.bat
    ```

## Configuring segatools

--8<-- "docs/snippets/sega/common/segatools_preamble_package.md"

=== "[vfs]"

--8<-- "docs/snippets/sega/common/segatools_relativepaths.md"

--8<-- "docs/snippets/sega/common/segatools_vfs.md"

??? tip "AquaMai"

    Find more information about AquaMai on their [GitHub page](https://github.com/MewoLab/AquaMai).  
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

    <img src="/img/sega/maimaidx/common/setup/distribution_servers_check.webp">

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the 7th option).

    <img src="/img/sega/maimaidx/common/setup/service_menu.webp">

    Select **店内マッチングの設定** (`IN-STORE MATCHING SETUP`, the first option)
    and toggle this setting to **OFF**.

    <img src="/img/sega/maimaidx/common/setup/service_game_settings.webp">

    Select **終了** (`EXIT`, the last option) to exit to the main service menu.

--8<-- "docs/snippets/sega/common/success.md"

## Help

--8<-- "docs/snippets/common/help.md"