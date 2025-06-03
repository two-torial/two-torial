<img class="header-logo" src="/img/taito/tetoteconnect/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

## Preparing data

--8<-- "docs/snippets/common/data_readonly.md"

    The **complete game data** should be approximately **5 GB or larger**.

    Here's what the expected data structure should look like: 

    ```
    📂[SYSTEM]
    📂MonoBleedingEdge
    📂System Volume Information
    📂Vision_Data
    ▶️game.exe
    📄game.inf
    ▶️RunVisionProd.bat
    ▶️Setting.bat
    ▶️UnityCrashHandler64.exe
    ⚙️UnityPlayer.dll
    ▶️Vision.exe
    ⚙️WinPixEventRuntime.dll
    ```

## Installing BepInEx

!!! tip ""

    - Download the most recent [BepInEx 5 release](https://github.com/BepInEx/BepInEx/releases) (`BepInEx_win_x64_5.x.y.z.zip`)

    !!! warning "We need BepInEx 5 since as of writing, BepInEx 6 does not support the required plugin"

    - Extract the archive to the root folder of your game data

    You should now have these files added to your directory:

    ```
    📂BepInEx
    📄.doorstop_version
    📄changelog.txt
    📝doorstop_config.ini
    ⚙️winhttp.dll
    ```

## Installing tetoco

!!! tip ""

    - Head over to [tetoco releases](https://github.com/Redcrafter/tetoco/releases)
    - Download `tetoco.dll`
    - Create a folder called `plugins` in the `BepInEx` folder
    - Move the dll file to that newly created folder

    You should end up with a file structure as follows:

    ```
    📂BepInEx
    ┗ 📂plugins
      ┗⚙️tetoco.dll
    ```

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Monitor orientation

!!! info "With tetoco installed, the game won't automatically rotate to portrait mode when starting it"

    The game can be played in landscape mode but a lot of the play area will be lost, it's best to set your monitor to portrait mode before launching the game.

??? tip "Manually rotating"

    - Right click on your Desktop
    - Select `Display settings`
    - Look for `Display orientation` and set it to `Portrait` or `Portrait (flipped)`
    - Rotate your monitor 90°

??? tip "Automatically rotating"

    Right click on [this link](https://raw.githubusercontent.com/gmiwoj/Windows-Display-Orientation-Script/main/windows-display-orientation-script.ps1)
    then `Save Link As` and place the `windows-display-orientation-script.ps1` file in your game's directory.

    Create a new `start.bat` file, and set its content to this, it will set your monitor as **Portrait (flipped)**, and automatically rotate it back once you close the game.
    
    ```ini
    powershell.exe -ExecutionPolicy Bypass -File "windows-display-orientation-script.ps1" 0 90
    Vision.exe
    powershell.exe -ExecutionPolicy Bypass -File "windows-display-orientation-script.ps1" 0 0
    ```

    Alternatively, you can set it to **Portrait** *(not flipped)* by changing `90` to `270`.

    ```ini
    powershell.exe -ExecutionPolicy Bypass -File "windows-display-orientation-script.ps1" 0 270
    Vision.exe
    powershell.exe -ExecutionPolicy Bypass -File "windows-display-orientation-script.ps1" 0 0
    ```

## First launch

!!! tip ""

    If you've followed all instructions correctly, you're ready to launch the game.

    Start the game by running `Vision.exe`, or `start.bat` if you followed [the automatic monitor rotation part](#monitor-orientation).

!!! tip ""

    You're all done! The game should load up properly now.

    You can use the **Login as Local** button to use your local save profile. 

    The `T` key can be pressed to access the service menu.

## Connecting to a network

!!! info "By default, tetoco uses its own local network and saves data locally"

    Please follow this step only if you have a network to connect to.

??? tip "Remote (Online Network)"

    - Open the automatically created configuration file `BepInEx\config\tetoco.cfg`
    - Set `UseLocalServer` to **false**
    - Then, set `RemoteServer` to the address provided by your network
    - Finally, set the `CardId` provided by your network