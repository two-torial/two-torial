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
    📂license
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

--8<-- "docs/snippets/sega/chunithm/data_options.md"
    
## Installing unprotected executables

!!! tip ""

    CHUNITHM executables are protected and will not run on a regular computer.

    Obtain unprotected (also called "unpacked" or "decrypted" by the community) copies of `chusanApp.exe` and `amdaemon.exe` for your game version.

    - Copy `chusanApp.exe` and `amdaemon.exe` to data's `App\bin` folder
    - Agree to overwrite when asked

## Installing ICFs

--8<-- "docs/snippets/sega/common/data_icfs.md"

## Patching the game

--8<-- "docs/snippets/sega/common/patching.md"

| Patch                        | Recommendation | Description |
|------------------------------|----------------|-------------|
| Force shared audio mode      | Either         | Force the game to use shared mode audio output, letting you listen to other audio sources while the game is running **at the cost of audio latency.**
| Force 2 channel audio output | Either         | Try enabling this patch if you don't get audio output at all. |
| Disable song select timer    | Either         | Disables the song select timer. |
| No encryption                | ON             | Disable encrypting network requests. **Required if you plan to run a local server.** |
| No TLS                       | ON             | Disable checking if the server is `HTTPS` or not. **Required if you plan to run a local server.** |
| Bypass 1080p monitor check   | Either         | Disable checking if the monitor is 1080p when enabling 120FPS. Enable if you cannot set your monitor to 1080p. |
| Bypass 120 Hz monitor check   | Either         | Disable checking if the monitor is **exactly 120 Hz** when enabling 120FPS. Enable if you cannot set your monitor to 120 Hz. |

## Installing segatools

--8<-- "docs/snippets/sega/common/segatools_install.md"
    - Find `chusan.zip` and extract it to your data's `App\bin` folder

    You should now have these files added to your `App\bin` directory:

    ```
    📂DEVICE
    ⚙️chusanhook_x64.dll
    ⚙️chusanhook_x86.dll
    📄config_hook.json
    ▶️inject_x64.exe
    ▶️inject_x86.exe
    📝segatools.ini
    ▶️launch.bat
    ```

## Configuring segatools

--8<-- "docs/snippets/sega/common/segatools_preamble_bin.md"

=== "[vfs]"

--8<-- "docs/snippets/sega/common/segatools_relativepaths.md"

--8<-- "docs/snippets/sega/common/segatools_vfs.md"

=== "[system]"

    !!! tip ""

        - If you have a 120 Hz monitor, set `dipsw2` and `dipsw3` to 0:

        ```ini
        [system]
        dipsw2=0
        dipsw3=0
        ```

        - If you have a 60 Hz monitor, set `dipsw2` and `dipsw3` to 1:

        ```ini
        [system]
        dipsw2=1
        dipsw3=1
        ```

=== "[gfx]"

--8<-- "docs/snippets/sega/chunithm/segatools_gfx.md"

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

    Start the game by running `App\bin\launch.bat`. Let the game load until it reaches the screen below.

    <img src="/img/sega/chunithm/common/setup/chusan/servicemenu/0_asettings.webp">

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the fourth option).

    <img src="/img/sega/chunithm/common/setup/chusan/servicemenu/1_gamesettings.webp">

    Select **グループ内基準機設定** (`SET STANDARD IN GROUP`, the second option)
    and toggle this setting to **基準機** (`STANDARD`).

    <img src="/img/sega/chunithm/common/setup/chusan/servicemenu/2_reference.webp">

    Select **終了** (`EXIT`, the last option) to exit to the main service menu.

    Navigate to **閉店設定** (`CLOSE SETTING`, the tenth option).

    <img src="/img/sega/chunithm/common/setup/chusan/servicemenu/3_closingsetting.webp">

    Navigate to **時** (`HOUR`, the second option) and use the `Service` button
    to toggle the setting until it says **全時刻** (`ALL TIME`).

    <img src="/img/sega/chunithm/common/setup/chusan/servicemenu/4_alltime.webp">

    Select **終了** (`EXIT`, the last option) to exit to the main service menu, then select **終了**
    (also the last option) in the main menu to exit the service menu.

    If you're stuck at the `Waiting for Distribution Server` screen below, close the game and relaunch.

    <img src="/img/sega/chunithm/common/setup/chusan/servicemenu/5_distserver.webp">

--8<-- "docs/snippets/sega/common/success.md"

## Help

--8<-- "docs/snippets/common/help.md"