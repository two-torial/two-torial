# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

--8<-- "docs/snippets/sega/common/old_data.md"

## Preparing data

--8<-- "docs/snippets/sega/common/drive_warning.md"

--8<-- "docs/snippets/common/data_readonly.md"

--8<-- "docs/snippets/sega/common/preparing_data.md"

    ```
    📂bin
	📂data
	📂firm
	📂startup
    📄firewall.cfg
    📄game.bat
    ▶️oxGetHwInfo.ini
    📄oxGetHwInfo.ini
    ```

--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating the base game

--8<-- "docs/snippets/sega/common/updating.md"

## Installing option data

--8<-- "docs/snippets/sega/chunithm/option_data.md"

## Installing ICFs

--8<-- "docs/snippets/sega/common/icfs.md"

## Patching the game

--8<-- "docs/snippets/sega/chunithm/patching.md"

| Patch                        | Recommendation | Description |
|------------------------------|----------------|-------------|
| Disable shop close lockout   | Either         | Disables the shop lockout from 12 to 8PM JST. |
| Force shared audio mode      | Either         | Force the game to use shared mode audio output, letting you listen to other audio sources while the game is running **at the cost of audio latency.** |
| Force 2 channel audio output | Either         | Try enabling this patch if you don't get audio output at all. |
| Disable song select timer    | Either         | Disables the song select timer. |

## Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/Dniel97/segatools/releases)
    and download `segatools.zip`. **Do not download the source code.**
    - Extracting the archive should give you a few more zip files. Find **`chuni.zip`**
    and extract it to the `App\bin` folder in your game data.

    You should now have a few more files inside the folder, as shown:

    ```
    📂DEVICE
    [...]
    📄chunihook.dll
    [...]
    ▶️inject.exe
    [...]
    📄segatools.ini
    ▶️start.bat
    [...]
    ```

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
        option=../../Option
        appdata=../../AppData
        ```

--8<-- "docs/snippets/sega/common/segatools_vfs.md"

=== "[gfx]"

--8<-- "docs/snippets/sega/chunithm/segatools_gfx.md"

## Connecting to a network

!!! danger "Pick one or the other, not both!"

--8<-- "docs/snippets/sega/common/online_network.md"

--8<-- "docs/snippets/sega/chunithm/only_artemis.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Audio properties

--8<-- "docs/snippets/common/audio_properties.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

--8<-- "docs/snippets/sega/common/first_launch_info.md"

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Start the game by running `App\bin\start.bat`. Let the game load until it reaches the screen below.

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/0_asettings.webp">

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the fourth option).

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/1_gamesettings.webp">

    Select **配信サーバー設定** (`DISTRIBUTION SEVER SETTING`, the first option)
    and toggle this setting to **サーバー** (`SERVER`).

    Select **筐体グループ設定** (`CABINET GROUP SETTINGS`, the second option)
    and toggle this setting to **OFF**.

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/2_reference.webp">

    Select **終了** (`EXIT`, the last option) to exit to the main service menu.

    Select **はい** (`YES`) and select **閉じる**

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/3_referenceconfirm.webp">

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/4_referenceconfirm.webp">

    After this, your game will close. Open it back up, and enter the service menu again.

    Navigate to **閉店設定** (`CLOSE SETTING`, the tenth option).

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/5_closingsetting.webp">

    Navigate to **時** (`HOUR`, the second option) and use the `Service` button
    to toggle the setting until it says **全時刻** (`ALL TIME`).

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/6_alltime.webp">

    Select **終了** (`EXIT`, the last option) to exit to the main service menu, then select **終了**
    (also the last option) in the main menu to exit the service menu.

!!! tip ""

    If you're stuck at the `Waiting for Distribution Server` screen below, close the game and relaunch.

    <img src="/img/sega/chunithm/common/setup/chuni/servicemenu/7_distserver.webp">

--8<-- "docs/snippets/sega/common/finish.md"

## Help

--8<-- "docs/snippets/common/help.md"
