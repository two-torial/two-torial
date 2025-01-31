# Game Setup (ONGEKI bright MEMORY)
<div style="text-align: center;">
    <img src="/img/ongeki/sddt/brightmemory.png" width="50%">
</div>

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

!!! danger "If you're coming from a previous version of ONGEKI"

    You'll want to create a new folder for the game and start from scratch.
    ONGEKI **DOES NOT** like being extracted over old data!

---

### Preparing data

!!! danger "There are currently issues with running game data in the `E:\` or `Y:\` drive.<br>Please extract the data into other drives."

!!! tip ""

	After downloading and extracting your data, we need to make sure your files
    aren't set to `Read-only`.

	- Right click the folder containing your data, then click on `Properties`.
	- In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
	- A popup will appear, select `Apply changes to this folder, subfolder and files`
    and press `OK`.
	- Finally, click `OK` again to exit out of properties.

	You should end up with a file structure as follows.

    <img width="500" src="/img/ongeki/sddt/setup/0_ongekidata.png">

    Create another empty folder named `AppData` next to them. It should now look like below.

    <img width="500" src="/img/ongeki/sddt/setup/0_ongekidata_withappdata.png">

    The `App` folder should have a file structure as follows.

    <img width="500" src="/img/ongeki/sddt/setup/1_ongekiapp.png">

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

    ONGEKI content updates are distributed through option folders instead of patching
    the base game. They are named `A???`, with each `?` being a number. Custom options
    distributed by the community might use letters instead, to distinguish them from
    official ones.

    Extract any options you've downloaded into the `Option` folder. You should end up with
    a file structure as follows. **Do not be worried if you have fewer or more option folders.**

    In some cases, your data may have options in `App\package\option`. If so, move
    all contents inside to the `Option` folder where `App` and `AppData` are and delete the `App\package\option` folder.

    <img width="500" src="/img/ongeki/sddt/setup/2_ongekioption.png">


#### Installing ICFs

!!! tip ""

    Install Configuration Files (ICFs) tell the game what version it is.
    **Without this your game cannot go online!**

    If your `amfs` folder already has a file named `ICF1`, skip this step.

    In some cases, your data may have a folder containing ICFs in `App\package\amfs`.
    If so, move all contents inside to the `amfs` folder where `App` and `AppData`,
    delete the `App\package\amfs` folder, and skip this step.

    Otherwise, obtain copies of `ICF1` for your game version and place it in
    the `amfs` folder. If it is named something else, rename it to exactly
    `ICF1` **without any file extensions.**




!!! info "Showing file extensions"

    By default, file extensions on Windows are hidden. Enable them by navigating to
    the `View` tab in File Explorer and select `File name extensions`.


#### Installing unprotected executables

!!! tip ""

    ONGEKI executables are protected and will not run on a regular computer.

    Obtain unprotected (also called "unpacked" or "decrypted" by the community)
    copies of `mu3.exe` and `amdaemon.exe` for your game version.

    Copy `mu3.exe` and `amdaemon.exe` to the `bin` folder of your game data. Agree
    to overwrite when asked.

---

### Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/Dniel97/segatools/releases)
    and download `segatools.zip`. **Do not download the source code.**
    - Extracting the archive should give you a few more zip files. Find **`mu3.zip`**
    and extract it to the `App\bin` folder in your game data.

    You should now have a few more files inside the folder, as highlighted:

    <img width="500" src="/img/ongeki/sddt/setup/3_ongeki_segatools_installed.png">

---

### Configuring segatools

!!! tip ""

    Since there is no graphical configuration tool for segatools, you will have to edit the
    configuration file by hand. It is found in `App\bin\segatools.ini`.

    It is recommended that you follow along using a text editor with syntax highlighting such as [Notepad++](https://notepad-plus-plus.org/).

    Each following sub-section will correspond to a section in `segatools.ini`. If any
    section is not mentioned, you can skip them.

!!! warning

    If a key already exists in the section, delete everything after `=` and replace it with your
    setting. Do not add another key.

    ```ini
    [system]
    dipsw2=1
    dipsw2=1 ; WRONG!
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

#### `[gfx]`

!!! tip ""

    - Set `windowed` to `0` to run in fullscreen mode and `1` to run in windowed mode.
    - If you have multiple monitors and you're running in fullscreen mode (`windowed=0`),
    set `monitor` to the index of the monitor you want to run the game on.

??? info "Getting the monitor index"

    Navigate to Windows display settings. Each monitor should be assigned a number.
    The monitor index is that number minus one. For example, monitor 2 means monitor index 1.

---

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
    subnet=192.168.139.0
    id=A69E-XXXXXXXXXXX
    ```

    Finally, you need a card number. Create a file named `aime.txt` inside `App\bin\DEVICE` and type in
    your 20-digit access code if you already have one, or make one up if you don't. If you're making one
    up, the access code **MUST NOT** start with a 3.

    <img src="/img/ongeki/sddt/setup/4_access_code.png">

??? warning "Local (ARTEMiS/AquaDX)"

    Both of these options require non-trivial setup. Refer to the official guides for [ARTEMiS](https://gitea.tendokyu.moe/Hay1tsme/artemis/src/branch/develop/docs/INSTALL_WINDOWS.md)
    and [AquaDX](https://github.com/hykilpikonna/AquaDX?tab=readme-ov-file#usage-v1-developmental-preview)
    to set up a local server.

---

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

    <img src="/img/ongeki/sddt/setup/5_audio.png">

#### Fixing OpenSSL on Intel 10th Gen and newer CPUs

!!! tip ""

    If you have an Intel 10th Gen CPU or newer, right click `App\bin\start.bat`, select `Edit`, and add the
    highlighted line to the top of the file.

    ```batch hl_lines="2"
    @echo off
    set OPENSSL_ia32cap=:~0x20000000

    pushd %~dp0
    ...
    ```

---

### First launch

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](../ongekibrightmemory/troubleshooting.md) page."

!!! tip

    Without an English patch, the service menu will be in Japanese. If you don't know Japanese, [Google Lens](https://lens.google/)
    is a handy tool for navigating this menu.

#### GAME ASSIGNMENTS

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Start the game by running `App\package\start.bat`. Let the game load until you reach a screen with the message below.

<img src="/img/ongeki/sddt/setup/4_ongeki_groupcheck.png">

!!! tip ""

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the 6th option).

<img src="/img/ongeki/sddt/setup/servicemenu/1_gamesettings.png">

!!! tip ""

    Select **グループ内基準機の設定** (`SET STANDARD IN GROUP`, the second option)
    and toggle this setting to **基準機** (`STANDARD`).

<img src="/img/ongeki/sddt/setup/servicemenu/2_reference.png">

!!! tip ""

    Select **終了** (`EXIT`, the last option) to exit to the main service menu.

#### CLOSE SETTING

!!! tip ""

    Navigate to **閉店設定** (`CLOSE SETTING`, the 10th option).

<img src="/img/ongeki/sddt/setup/servicemenu/3_closesetting.png">

!!! tip ""

    Navigate to **時** (`HOUR`, the 2nd option) and use the `Service` button
    to toggle the setting until it says **全時刻** (`ALL TIME`).

<img src="/img/ongeki/sddt/setup/servicemenu/4_alltime.png">

!!! tip ""

    Select **終了** (`EXIT`, the last option) to exit to the main service menu, then select **終了**
    (also the last option) in the main menu to exit the service menu.

!!! tip ""

    You're all done! The game should load up properly now.

    You can add coins using the `Coin` key (default `F3`) and card in by holding the `Enter` key.

---

### Custom Mods

!!! tip ""

    !!! danger "Please use BepInEx to load all mods including MelonLoader and MonoMods"

    Mods have historically been hardcoded into the unprotected `Assembly-CSharp.dll` which the user can
    enable/disable with the `mu3.ini` configuration. The modern approach is to use
    BepInEx to load custom mods without hardmodding the Assembly-CSharp file.

    To enable BepInEx, download the [BepInEx stable release](https://github.com/BepInEx/BepInEx/releases/latest),
    extract the BepInEx folder to the `App/package` folder, and modify `segatools.ini` with the following:

    ```ini
    [unity]
    enable=1
    targetAssembly=BepInEx\core\BepInEx.Preloader.dll
    ```

    - BepInEx: place mods in `BepInEx/Plugins`
    - Melonloader: use [BepInEx.MelonLoader.Loader](https://github.com/BepInEx/BepInEx.MelonLoader.Loader/releases/latest) UnityMono-BepInEx5. Place mods in `MLLoader/Mods`
    - MonoMods: use [BepInEx.MonoMod.Loader](https://github.com/BepInEx/BepInEx.MonoMod.Loader/releases/latest). Place mods in `BepInEx/monomod`

---

### Controllers and Troubleshooting

!!! info "Input methods and controllers are covered in the [Controllers](../ongekibrightmemory/controllers.md) page."

!!! warning "Have any other issues?"

	Check out the [Troubleshooting](../mu3/troubleshooting.md) and [Error Codes](../../errorcodes/sega.md) pages.
