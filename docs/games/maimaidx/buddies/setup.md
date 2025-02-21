# maimai DX BUDDiES

<img src="/img/maimaidx/buddies.png">

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

!!! danger "If you're coming from a previous version of maimai DX"

    Create a new folder for the game and start from scratch.
    maimai DX **DOES NOT** like being extracted over old data!

---

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

    <img width="500" src="/img/maimaidx/setup/rootdir.png">

    Create two new empty folders named `appdata` and `amfs` (and the folder `option` if not present) next to them as shown below:

    <img width="500" src="/img/maimaidx/setup/rootdir2.png"> 

    The `App` folder should have a file structure as follows.

    <img width="500" src="/img/maimaidx/setup/appdir.png">

??? warning "If your data doesn't look like this"

    If your data looks like the third image:

    - Create an `App` folder and move all files and folders from the image inside of it.
    - Create empty folders named `amfs`, `Option` and `AppData` next to the `App` folder.

    If extra files are present next to your folders, such as executables, scripts, etc..
    **remove them. This also means your data was tampered with and we strongly recommend
    getting new data from somewhere else.**

#### Installing ICFs

!!! tip ""

    Install Configuration Files (ICFs) tell the game what version it is.
    **Without this your game cannot go online!**

    If your `amfs` folder already has files`ICF1` and `ICF2`, skip this step.

    Otherwise, obtain copies of `ICF1` for your game version and place it in
    the `amfs` folder. If it is named something else, rename it to exactly
    `ICF1` **without any file extensions.** `ICF2` is a copy of `ICF1`.

??? info "Showing File Extensions"

    By default, file extensions on Windows are hidden. Enable them by navigating to
    the `View` tab in File Explorer and select `File name extensions`.

#### Installing Unprotected Executables

!!! tip ""

    maimai DX executables are protected and will not run on a regular computer.

    Obtain unprotected (also called "unpacked" or "decrypted" by the community) 
    copies of the following files and the associated configuration file:

    - amdaemon.exe
    - Sinmai.exe
    - Sinmai_Data/Plugins/amdaemon_api.dll
    - Sinmai_Data/Plugins/Cake.dll
    - Sinmai_Data/Managed/AMDaemon.NET.dll
    - Sinmai_Data/Managed/Assembly-CSharp.dll
    - mai2.ini or maimaiDX.ini

    Copy the files and folders into the `App/Package` folder of your game data. Agree to overwrite
    when asked.

    !!! Warning "Assembly-CSharp Notes"

        `Assembly-CSharp.dll` **must** match your game version. All others can be 
        reused from other game versions.

        `Assembly-CSharp.dll` **must** also contain `mai2.ini` or `maimaiDX.ini`. These configuration 
        files are specific to the unprotected `Assembly-CSharp.dll`. If your package does not 
        contain a configuration file, please create one with the following to bypass hardware 
        checks on game startup:

        ```ini
        [AM]
        Target=0
        IgnoreError=1
        DummyTouchPanel=1
        DummyLED=1
        DummyCodeCamera=1
        DummyPhotoCamera=1

        [Sound]
        Sound8Ch=0

        [Patches]
        EnablePatchLog=1
        ```
        !!! tip "If the assembly supports it, `App/Package/dpPatchLog.log` lists supported patches after the first run. Otherwise see [Custom Mods](#custom-mods)"

---

### Installing Segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/Dniel97/segatools/releases/latest)
    and download the latest `segatools.zip`. **Do not download the source code.**
    - Extracting the archive should give you a few more zip files. Find `mai2.zip`
    and extract it to the `App/Package` folder in your game data.

    You should now have a few more files inside the `App/Package` folder, as highlighted:

    <img width="500" src="/img/maimaidx/setup/segatools.png">

---

### Configuring Segatools

!!! tip ""

    Since there is no graphical configuration tool for segatools, you will have to edit the
    configuration file by hand. It is found in `App/Package/segatools.ini`.

    It is recommended that you follow along using a text editor with syntax highlighting such as [Notepad++](https://notepad-plus-plus.org/).

    Each following sub-section will correspond to a section in `segatools.ini`. If any
    section is not mentioned, you can skip them.

!!! warning

    If a key already exists in the section, delete everything after `=` and replace it with your
    setting. Do not add another key. Example:

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
    option=../../option
    appdata=../../appdata
    ```

#### `[dns]`

!!! tip ""

    Game will not pass checks unless you modify the dns:

    ```ini
    [dns]
    default=YOUR_IPv4_ADDRESS
    ```

    ??? tip "Finding Your IPv4 Address"

        Open a command promt. Type `ipconfig` and look for the IPv4 Address. 
        Place those digits here otherwise you will get stuck on the DNS(LAN) check.

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

    <img src="/img/maimaidx/setup/audio.png">

#### Fixing OpenSSL on Intel 10th Gen and newer CPUs

!!! tip ""

    If you have an Intel 10th Gen CPU or newer, right click `App/Package/start.bat`, select `Edit`, and add the
    highlighted line to the top of the file.

    ```batch hl_lines="2"
    @echo off
    set OPENSSL_ia32cap=:~0x20000000

    pushd %~dp0
    ...
    ```

---

### Test Launch

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](troubleshooting.md) page."

!!! warning "Please Disconnect any Hardware including Controllers or Card Readers at this time."

!!! tip

    Without an English patch, the service menu will be in Japanese. If you don't know Japanese, [Google Lens](https://lens.google/)
    is a handy tool for navigating this menu.

#### Game Settings

!!! tip ""

    If you've followed all instructions correctly, you are ready to launch the game!

    Start the game by running `App/Package/start.bat`. You should see a terminal pop-up with the following:

    <img src="/img/maimaidx/setup/cmd.png">

    Another window titled `Sinmai` is the actual game. It should pause on `Search for Distribution Servers`:

    <img src="/img/maimaidx/setup/distribution_servers_check.png">

!!! tip ""

    Use the following keyboard controls `F1` = `Test/Enter` and `c` = `down` to do the following:

    - Press `F1` to enter the service menu
    - Press `c` a few times to navigate to `Game Settings` or `ゲーム設定` as shown below:

    <img src="/img/maimaidx/setup/service_menu.png">

    - Press `F1` to enter the menu. Press `c` to navigate to the top option and toggle to `OFF` using `F1`. You should see the following:

    <img src="/img/maimaidx/setup/service_game_settings.png">

    - Press `ESC` to exit. Close all associated windows including `CMD`, `AMDaemon`, and `Sinmai`. Relaunch with `start.bat` and the game should boot into guest mode.

---

### Connecting to a Network

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

    Finally, you need a card number. Create a file named `aime.txt` inside `App/Package/DEVICE` and type in
    your 20-digit access code if you already have one, or make one up if you don't. If you're making one
    up, the access code **MUST NOT** start with a 3.

    <img src="/img/maimaidx/setup/access_code.png">

??? tip "Local (ARTEMiS/AquaDX)"

    Both of these options require non-trivial setup. Refer to the official guides for [ARTEMiS](https://gitea.tendokyu.moe/Hay1tsme/artemis/src/branch/develop/docs/INSTALL_WINDOWS.md)
    and [AquaDX](https://github.com/hykilpikonna/AquaDX?tab=readme-ov-file#usage-v1-developmental-preview)
    to set up a local server.

---

### Further Configuration

#### Updating the Base Game

!!! tip ""

    Extract your patch's files to your existing data in a way that matches its
    file structure. Agree to overwrite files if necessary.

    !!! Warning "Only update if an unencrypted `Assembly-CSharp.dll` is available"

#### Installing Option Data

!!! tip ""

    maimai DX content updates are distributed through option folders instead of patching
    the base game. They are named with a letter followed by three numbers. Each release 
    increments the letter (ie. BUDDiES is `H???` and BUDDiES+ is `I???`).

    Extract any options you've downloaded into the `option` folder. You should end up with
    a file structure as follows. **Do not be worried if you have fewer or more option folders.**

    <img width="500" src="/img/maimaidx/setup/options.png">

    !!! warning "Do not mix option data between versions"

---

### Custom Mods

!!! info "Mods are covered on the [Unity modding](../../../extras/unity.md) page."

### Controllers and Troubleshooting

!!! info "Input methods and controllers are covered in the [Controllers](controllers.md) page."

!!! warning "Have any other issues?"

    Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](../../../errorcodes/sega.md) pages.
