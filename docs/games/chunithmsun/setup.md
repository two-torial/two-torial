# Game Setup (SUN)
<img src="/img/chunithm/sdhd/sun.png">

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

!!! danger "If you're coming from a previous version of CHUNITHM"

    You'll want to create a new folder for the game and start from scratch.
    CHUNITHM **DOES NOT** like being extracted over old data!

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

    <img width="500" src="/img/chunithm/sdhd/setup/0_chunithmdata.png">

    Create another empty folder named `AppData` next to them. It should now look like below.

    <img width="500" src="/img/chunithm/sdhd/setup/0_chunithmdata_withappdata.png"> 

    The `App` folder should have a file structure as follows.

    <img width="500" src="/img/chunithm/sdhd/setup/1_chunithmapp.png">

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

    CHUNITHM content updates are distributed through option folders instead of patching
    the base game. They are named `A???`, with each `?` being a number. Custom options
    distributed by the community might use letters instead, to distinguish them from
    official ones.

    Extract any options you've downloaded into the `Option` folder. You should end up with
    a file structure as follows. **Do not be worried if you have fewer or more option folders.**

    <img width="500" src="/img/chunithm/sdhd/setup/2_chunithmoption.png">

!!! warning "If you plan to connect to a network (Hosted or Local), the `A001` option folder for your specific game version is required. This option contains a special Event file that lets the game connect."

#### Installing ICFs

!!! tip ""

    Install Configuration Files (ICFs) tell the game what version it is.
    **Without this your game cannot go online!**

    If your `amfs` folder already has a file named `ICF1`, skip this step.

    Otherwise, obtain copies of `ICF1` for your game version and place it in
    the `amfs` folder. If it is named something else, rename it to exactly
    `ICF1` **without any file extensions.**

!!! info "Showing file extensions"

    By default, file extensions on Windows are hidden. Enable them by navigating to
    the `View` tab in File Explorer and select `File name extensions`.
    

#### Installing unprotected executables

!!! tip ""

    CHUNITHM executables are protected and will not run on a regular computer.

    Obtain unprotected (also called "unpacked" or "decrypted" by the community)
    copies of `chusanApp.exe` and `amdaemon.exe` for your game version.

    Copy `chusanApp.exe` and `amdaemon.exe` to the `bin` folder of your game data. Agree
    to overwrite when asked.

---

### Patching the game

!!! info "Go through the [Web Patching](../../extras/patchweb.md) guide to learn how to use a web patcher."

    There are **many** patches for CHUNITHM.

    We will only bring up the ones we think could be genuinely useful.

!!! danger "As a general rule of thumb, if you're not sure what a patch does or you're not absolutely certain you need it, leave it alone, regardless of recommendations below."

| Patch                        | Recommendation | Description |
|------------------------------|----------------|-------------|
| Force shared audio mode      | Either         | Force the game to use shared mode audio output, letting you listen to other audio sources while the game is running **at the cost of audio latency.**
| Force 2 channel audio output | Either         | Try enabling this patch if you don't get audio output at all. |
| Disable song select timer    | Either         | Disables the song select timer. |
| No encryption                | ON             | Disable encrypting network requests. **Required if you plan to run a local server.** |
| No TLS                       | ON             | Disable checking if the server is `HTTPS` or not. **Required if you plan to run a local server.** |
| Bypass 1080p monitor check   | Either         | Disable checking if the monitor is 1080p when enabling 120FPS. Enable if you cannot set your monitor to 1080p. |
| Bypass 120Hz monitor check   | Either         | Disable checking if the monitor is **exactly 120Hz** when enabling 120FPS. Enable if you cannot set your monitor to 120Hz. |

---

### Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/Dniel97/segatools/releases)
    and download `segatools.zip`. **Do not download the source code.**
    - Extracting the archive should give you a few more zip files. Find **`chusan.zip`**
    and extract it to the `App\bin` folder in your game data.

    You should now have a few more files inside the folder, as highlighted:

    <img width="500" src="/img/chunithm/sdhd/setup/3_segatools_installed.png">

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

#### `[system] (formerly [gpio])`

!!! warning

    As of 2024-08-20, the [gpio] section in segatools has been renamed to [system].

!!! tip ""

    - If you have a 120Hz monitor, set `dipsw2` and `dipsw3` to 0:

    ```ini
    [system]
    dipsw2=0
    dipsw3=0
    ```

    - If you have a 60Hz monitor, set `dipsw2` and `dipsw3` to 1:

    ```ini
    [system]
    dipsw2=1
    dipsw3=1
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

    <img src="/img/chunithm/sdhd/setup/4_access_code.png">

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

    <img src="/img/chunithm/sdhd/setup/5_audio.png">

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

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](../chunithmsun/troubleshooting.md) page."

!!! tip

    Without an English patch, the service menu will be in Japanese. If you don't know Japanese, [Google Lens](https://lens.google/)
    is a handy tool for navigating this menu.

#### GAME ASSIGNMENTS

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Start the game by running `App\bin\start.bat`. Let the game load until it reaches the screen below.

<img src="/img/chunithm/sdhd/setup/servicemenu/0_asettings.png">

!!! tip ""

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    Navigate to **ゲーム設定** (`GAME ASSIGNMENTS`, the 4th option).

<img src="/img/chunithm/sdhd/setup/servicemenu/1_gamesettings.png">

!!! tip ""

    Select **グループ内基準機設定** (`SET STANDARD IN GROUP`, the second option)
    and toggle this setting to **基準機** (`STANDARD`).

<img src="/img/chunithm/sdhd/setup/servicemenu/2_reference.png">

!!! tip ""

    Select **終了** (`EXIT`, the last option) to exit to the main service menu.

#### CLOSE SETTING

!!! tip ""

    Navigate to **閉店設定** (`CLOSE SETTING`, the 10th option).

<img src="/img/chunithm/sdhd/setup/servicemenu/3_closingsetting.png">

!!! tip ""

    Navigate to **時** (`HOUR`, the 2nd option) and use the `Service` button
    to toggle the setting until it says **全時刻** (`ALL TIME`).

<img src="/img/chunithm/sdhd/setup/servicemenu/4_alltime.png">

!!! tip ""

    Select **終了** (`EXIT`, the last option) to exit to the main service menu, then select **終了**
    (also the last option) in the main menu to exit the service menu.

#### Waiting for Distribution Server

!!! tip ""

    If you're stuck at the `Waiting for Distribution Server` screen below, close the game and relaunch.

<img src="/img/chunithm/sdhd/setup/servicemenu/5_distserver.png">

!!! tip ""

    You're all done! The game should load up properly now.

    You can add coins using the `Coin` key (default `F3`) and card in by holding the `Enter` key.

### Further configuration

!!! info "Input methods and controllers are covered in the [Controllers](../chunithmsun/controllers.md) page."

!!! warning "Have any other issues?"

	Check out the [Troubleshooting](../chunithmsun/troubleshooting.md) and [Error Codes](../../errorcodes/sega.md) pages.
