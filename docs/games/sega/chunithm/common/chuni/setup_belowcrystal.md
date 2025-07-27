# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

--8<-- "docs/snippets/sega/common/data_old.md"

## Preparing data

--8<-- "docs/snippets/sega/common/data_driveletter.md"

--8<-- "docs/snippets/common/data_readonly.md"

--8<-- "docs/snippets/sega/common/data_preparation.md"

    ```
    📂bin
    📂data
    📂firm
    📂startup
    📄firewall.cfg
    ▶️game.bat
    ▶️oxGetHwInfo.exe
    📝oxGetHwInfo.ini
    ```

--8<-- "docs/snippets/sega/common/data_bad.md"

## Updating data

--8<-- "docs/snippets/sega/common/data_updating.md"

## Installing option data

--8<-- "docs/snippets/sega/chunithm/data_options.md"

## Installing ICFs

--8<-- "docs/snippets/sega/common/data_icfs.md"

## Patching the game

--8<-- "docs/snippets/sega/common/patching.md"

| Patch                        | Recommendation | Description |
|------------------------------|----------------|-------------|
| Disable shop close lockout   | Either         | Disables the shop lockout from 12 to 8PM JST. |
| Force shared audio mode      | Either         | Force the game to use shared mode audio output, letting you listen to other audio sources while the game is running **at the cost of audio latency.** |
| Force 2 channel audio output | Either         | Try enabling this patch if you don't get audio output at all. |
| Disable song select timer    | Either         | Disables the song select timer. |

## Installing segatools

--8<-- "docs/snippets/sega/common/segatools_install.md"
    - Find `chuni.zip` and extract it to your data's `App\bin` folder

    You should now have these files added to your `App\bin` directory:

    ```
    📂DEVICE
    ⚙️chunihook.dll
    ▶️inject.exe
    📝segatools.ini
    ▶️launch.bat
    ```

## Configuring audio

--8<-- "docs/snippets/common/audio_48khz.md"

## Configuring segatools

--8<-- "docs/snippets/sega/common/segatools_preamble_bin.md"

=== "[vfs]"

--8<-- "docs/snippets/sega/common/segatools_vfs.md"

=== "[gfx]"

--8<-- "docs/snippets/sega/chunithm/segatools_gfx.md"

## Connecting to a network

--8<-- "docs/snippets/sega/common/network_preamble.md"

--8<-- "docs/snippets/sega/common/network_remote.md"

--8<-- "docs/snippets/sega/common/network_local_artemisonly.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

--8<-- "docs/snippets/sega/common/service_jp_googlelens.md"

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Start the game by running `App\bin\launch.bat`. Let the game load until it reaches the screen below.

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

--8<-- "docs/snippets/sega/common/success.md"

## Help

--8<-- "docs/snippets/common/help.md"