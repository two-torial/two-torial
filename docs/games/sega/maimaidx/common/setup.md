--8<-- "docs/snippets/common/data_warning.md"

!!! danger "If you're coming from a previous version of maimai DX"

    Create a new folder for the game and start from scratch.
    maimai DX **DOES NOT** like being extracted over old data!

### Preparing data

!!! danger "There are currently issues with running game data in the `E:\` or `Y:\` drive.<br>Please extract the data into other drives."

!!! tip ""

    After downloading and extracting your data, we need to make sure your files
    are not set to `Read-only`.

    - Right click the folder containing your data, then click on `Properties`.
    - In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
    - A popup will appear, select `Apply changes to this folder, subfolder and files`and press `OK`.
    - Finally, click `OK` again to exit out of properties.

    You should end up with a file structure as follows.

    <img width="500" src="/img/sega/maimaidx/common/setup/rootdir.webp">

    Create two new empty folders named `appdata` and `amfs` (and the folder `option` if not present) next to them as shown below:

    <img width="500" src="/img/sega/maimaidx/common/setup/rootdir2.webp">

    The `App` folder should have a file structure as follows.

    <img width="500" src="/img/sega/maimaidx/common/setup/appdir.webp">

??? warning "If your data doesn't look like this"

    If your data looks like the third image:

    - Create an `App` folder and move all files and folders from the image inside of it.
    - Create empty folders named `amfs`, `Option` and `AppData` next to the `App` folder.

    If extra files are present next to your folders, such as executables, scripts, etc..
    **remove them. This also means your data was tampered with and we strongly recommend
    getting new data from somewhere else.**

#### Updating the base game

!!! tip ""

    Extract your patch's files to your existing data in a way that matches its
    file structure. Agree to overwrite files if necessary.

#### Installing option data

!!! tip ""

    maimai DX content updates are distributed through option folders instead of patching
    the base game.

    Options are named with a letter followed by three numbers.

    For JPN(SDEZ) data, each new release of maimai DX increments the first letter of the Option (ie. BUDDiES is `H???` and BUDDiES+ is `I???`).

    For EXP(SDGA) data, Options will always begin with the letter `A` (i.e `A???`)

    Extract any options you've downloaded into the `Option` folder. You should end up with
    a file structure as follows. **Do not be worried if you have fewer or more option folders.**

    <img width="500" src="/img/sega/maimaidx/common/setup/options.webp">

    !!! warning "Do not mix option data between versions"

#### Installing unprotected executables

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

#### Installing ICFs

!!! tip ""

    Install Configuration Files (ICFs) tell the game what version it is.
    **Without this your game cannot go online!**

    **If your unprotected executables came with an `amfs` folder, and already has a file named `ICF1` in it, skip this step.**

    Otherwise, obtain copies of `ICF1` for your game version and place it in
    the `amfs` folder. If it is named something else, rename it to exactly
    `ICF1` **without any file extensions.**

!!! info "Showing file extensions"

    By default, file extensions on Windows are hidden. Enable them by navigating to
    the `View` tab in File Explorer and select `File name extensions`.

#### mai2.ini

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

### Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/TeamTofuShop/segatools/releases/tag/2024-03-13)
    and download the `segatools.zip` from `2024-03-13`. **Do not download the source code or latest release.**
    - Extracting the archive should give you a few more zip files. Find `mai2.zip`
    and extract it to the `App/Package` folder in your game data.

    You should now have a few more files inside the `App/Package` folder, as highlighted:

    <img width="500" src="/img/sega/maimaidx/common/setup/segatools.webp">

!!! warning

    The latest release of segatools currently has issues with maimai, and for the time being an older version of segatools is preferred.

### Configuring segatools

!!! tip ""

    Since there is no graphical configuration tool for segatools, you will have to edit the
    configuration file by hand. It is found in `App\package\segatools.ini`.

    It is recommended that you follow along using a text editor with syntax highlighting such as [Notepad++](https://notepad-plus-plus.org/).

    Each following sub-section will correspond to a section in `segatools.ini`. If any
    section is not mentioned, you can skip them.

!!! warning

    If a key already exists in the section, delete everything after `=` and replace it with your
    setting. Do not add another key.

    ```ini
    [gpio]
    dipsw1=1
    dipsw1=1 ; WRONG!
    ```

#### `[vfs]`

!!! tip ""

    If you've been matching the file structure as described in the [Preparing data](#preparing-data)
    section, you can fill in this section with the values below:

    ```ini
    [vfs]
    amfs=../../amfs
    option=../../Option
    appdata=../../AppData
    ```

??? tip "AquaMai"

    It's strongly recommended to use MelonLoader mods to improve QOL.                                                                             
    You can find info about the available mods for maimai here [AquaMai](https://github.com/MewoLab/AquaMai).                                                                         
    For general modding check [Unity modding](/extras/unity.md) page.                                                                                                                  

### Setting launch options

!!! tip ""
    Right click `App\package\start.bat`, select `Edit`. Locate the line that launches `sinmai` and edit it according to your preferences:

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
### Connecting to a network

!!! danger "Please choose one of the two solutions, not both!"

??? tip "Remote (Online Network)"

    Head to the `[dns]` section inside `segatools.ini`. Set `default` to the address
    provided by your network. **Do not add `http://` or `https://` to the address!**

    ```ini
    [dns]
    default=network.example
    ```

    Then, head to the `[keychip]` section and add & set `id` to the keychip ID provided by your network:

    ```ini
    [keychip]
    subnet=192.168.172.0
    id=A69E-XXXXXXXXXXX
    ```

    Finally, you need a card number. Create a file named `aime.txt` inside `App\package\DEVICE` and type in
    your 20-digit access code if you already have one, or make one up if you don't. If you're making one
    up, the access code **MUST NOT** start with a 3.

    <img src="/img/sega/ongeki/common/setup/4_access_code.webp">

??? warning "Local (ARTEMiS/AquaDX)"

    Both of these options require non-trivial setup. Refer to the official guides for [ARTEMiS](https://gitea.tendokyu.moe/Hay1tsme/artemis/src/branch/develop/docs/INSTALL_WINDOWS.md)
    and [AquaDX](https://github.com/hykilpikonna/AquaDX?tab=readme-ov-file#usage-v1-developmental-preview)
    to set up a local server.

### Pre-launch requirements

!!! info "These steps are required, otherwise your game won't run."

#### VCRedist & DirectX

!!! tip ""

	- Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
	- Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

#### Audio

!!! tip ""

    - Right-click on the volume setting in your taskbar and select `Sounds`.
    - Navigate to the `Playback` tab, right click on your default audio device, and click on `Properties`.
    - Go to the `Advanced` tab.
	- Check both boxes under `Exclusive Mode`.
	- Open the `Default Format` dropdown.
    - Pick either `16 bit, 48000Hz (DVD Quality)` or `24 bit, 48000Hz (Studio Quality)`, click `Apply`, then `OK`.

    <img src="/img/common/audio_16_48.webp">

#### Fixing OpenSSL on Intel 10th Gen and newer CPUs

!!! tip ""

    If you have an Intel 10th Gen CPU or newer, you need to [patch amdaemon](https://patcher.two-torial.xyz/amdaemon) and enable `OpenSSL SHA crash bug fix`.

### First launch

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](troubleshooting.md) page."

!!! tip

    Without an English patch, the service menu will be in Japanese. If you don't know Japanese, [Google Lens](https://lens.google/)
    is a handy tool for navigating this menu.

#### GAME ASSIGNMENTS

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Start the game by running `App\package\start.bat`. Let the game load until you reach a screen with the message below.

<img src="/img/sega/maimaidx/common/setup/distribution_servers_check.webp">

!!! tip ""

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the 7th option).

<img src="/img/sega/maimaidx/common/setup/service_menu.webp">

!!! tip ""

    Select **店内マッチングの設定** (`IN-STORE MATCHING SETUP`, the first option)
    and toggle this setting to **OFF**.

<img src="/img/sega/maimaidx/common/setup/service_game_settings.webp">

!!! tip ""

    Select **終了** (`EXIT`, the last option) to exit to the main service menu.

### Custom Mods

!!! info "Mods are covered on the [Unity modding](/extras/unity.md) page."

### Controllers and Troubleshooting

!!! info "Input methods and controllers are covered in the [Controllers](controllers.md) page."

!!! warning "Have any other issues?"

    Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](/errorcodes/sega.md) pages.
