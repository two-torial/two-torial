!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

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

    <img width="500" src="/img/sega/wacca/common/setup/0_waccadata.png">
    
    The `App` folder should have a file structure as follows.

    <img width="500" src="/img/sega/wacca/common/setup/1_waccaapp.png">

??? warning "If your data doesn't look like this"

    If your data looks like the third image:

    - Create an `App` folder and move all files and folders from the image inside of it.
    - Create empty folders named `amfs` and `AppData` next to the `App` folder.

    If extra files are present next to your folders, such as executables, scripts, etc..
    **remove them. This also means your data was tampered with and we strongly recommend
    getting new data from somewhere else.**

#### Updating the base game

!!! tip ""

    Extract all updates in order. Agree to overwrite files if necessary.

    For example, if you have `3.00.00`; install `3.01.00`, then `3.02.00`, etc.


#### Installing ICFs

!!! tip ""

    Install Configuration Files (ICFs) tell the game what version it is.
    **Without this your game cannot go online!**

    If your `amfs` folder already has a file named `ICF1`, skip this step.

    In some cases, your data may have a folder containing ICFs in `App\bin\amfs`.
    If so, move all contents inside to the `amfs` folder where `App` and `AppData`,
    delete the `App\bin\amfs` folder, and skip this step.

    Otherwise, obtain copies of `ICF1` for your game version and place it in
    the `amfs` folder. If it is named something else, rename it to exactly
    `ICF1` **without any file extensions.**


!!! info "Showing file extensions"

    By default, file extensions on Windows are hidden. Enable them by navigating to
    the `View` tab in File Explorer and select `File name extensions`.

---

### Patching the game

!!! info "Go through the [Web Patching](/extras/patchweb.md) guide to learn how to use a web patcher."

---

### Installing segatools

!!! tip ""

    - Head over to [segatools releases](https://gitea.tendokyu.moe/Dniel97/segatools/releases)
    and download `segatools.zip`. **Do not download the source code.**
    - Extracting the archive should give you a few more zip files. Find **`mercury.zip`**
    and extract it to the `App\bin` folder in your game data.

    You should now have a few more files inside the folder, as highlighted:

    <img width="500" src="/img/sega/wacca/common/setup/2_wacca_segatools_installed.png">

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
    appdata=../../AppData
    ```

!!! info "Relative Directories"

    The `../` in the above example represents the parent directory in a relative path. It is used to navigate up one level in the directory hierarchy.

    For example, your segatools.ini is located at `/App/bin/segatools.ini` and your amfs folder is located next to the App folder.

    Since segatools.ini is in the `/bin/` folder, typing `../` would move you up to the App folder. Since the amfs folder is next to the App folder, the second `../` takes you to `App`'s parent folder, which is the folder containing `App`, `amfs`, etc.

    The benefits of using this method include:

    - Avoiding issues that arise when folders have spaces in their names.

    - Being able to move your game folder without redefining the locations of your VFS folders.

    - A cleaner and easier to read segatools.ini, making spotting issues simpler.

---

### Connecting to a network

!!! danger "Please choose one of the two solutions, not both!"

    This step is not needed if you plan on running the offline patch.

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
    subnet=192.168.174.0
    id=A69E-XXXXXXXXXXX
    ```

    Finally, you need a card number. Create a file named `aime.txt` inside `App\package\DEVICE` and type in
    your 20-digit access code if you already have one, or make one up if you don't. If you're making one
    up, the access code **MUST NOT** start with a 3.

    <img src="/img/sega/wacca/common/setup/3_access_code.png">

??? warning "Local (ARTEMiS/AquaDX)"

    Both of these options require non-trivial setup. Refer to the official guides for [ARTEMiS](https://gitea.tendokyu.moe/Hay1tsme/artemis/src/branch/develop/docs/INSTALL_WINDOWS.md)
    and [AquaDX](https://github.com/hykilpikonna/AquaDX?tab=readme-ov-file#usage-v1-developmental-preview)
    to set up a local server.

---

### Pre-launch requirement

!!! info "This step is required, otherwise your game won't run."

#### Install FTDI LEDs driver

!!! tip ""

    Download FTDI drivers from [here](https://ftdichip.com/wp-content/uploads/2023/09/CDM-v2.12.36.4-WHQL-Certified.zip)
    and extract them to a folder of your choice, then copy `CDM-v2.12.36.4-WHQL-Certified/amd64/ftd2xx64.dll` to 
    `/App/WindowsNoEditor/Mercury/Binaries/Win64` and then rename the file to `ftd2xx.dll`.

#### VCRedist & DirectX

!!! tip ""

	- Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
	- Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

#### Fixing OpenSSL on Intel 10th Gen and newer CPUs

!!! tip ""

    If you have an Intel 10th Gen CPU or newer, you need to [patch amdaemon](https://patcher.two-torial.xyz/amdaemon) and enable `OpenSSL SHA crash bug fix`.

---

### First launch

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    Set your display orientation to portrait mode.

    Start the game by running `App\bin\start.bat`.

#### CLOSE SETTING

!!! tip ""

    Press your `Test` button (default `F1`) to enter the service menu. Use the `Service` button
    (default `F2`) to navigate the menu, and `Test` button to select an option.

    You can also use the Volume buttons (default `UP` and `DOWN` keys) to navigate
    and the `ENTER` key to select.

    Navigate to **SYSTEM SETTING**.

<img src="/img/sega/wacca/common/setup/servicemenu/4_systemsetting.png">

!!! tip ""

    Navigate to **CLOSING TIME SETTINGS**.

<img src="/img/sega/wacca/common/setup/servicemenu/5_closingtime.png">

!!! tip ""

    Navigate to **ALL DAYS OF THE WEEK** and use the `Service` button
    to toggle the setting until it says **OFF**.

<img src="/img/sega/wacca/common/setup/servicemenu/6_closingtimesetting.png">

!!! tip ""

    Select **APPLY SETTINGS AND RE-BOOT** to save the settings.

    Note that this will close your game and you will have to start it again
    with `start.bat`.

!!! tip ""

    You're all done! The game should load up properly now.

    You can add coins using the `Coin` key (default `F3`) and card in by holding the `Enter` key.

---

### Controllers and Troubleshooting

!!! info "Input methods and controllers are covered on the [Controllers](./controllers.md) page."

!!! warning "Have any other issues?"

	Check out the [Error Codes](/errorcodes/sega.md) page.
