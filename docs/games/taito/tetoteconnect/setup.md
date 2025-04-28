# Game Setup (Tetote X Connect)
<img class="header-logo" src="/img/taito/tetoteconnect/logo.png">

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---

### Preparing data

!!! tip ""

    After downloading and extracting your data, we need to make sure your files
    aren't set to `Read-only`.

    - Right click the folder containing your data, then click on `Properties`.
    - In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
    - A popup will appear, select `Apply changes to this folder, subfolders and files`
    and press `OK`.
    - Finally, click `OK` again to exit out of properties.

    You should end up with a file structure as follows.

    <img width="500" src="/img/taito/tetoteconnect/setup/0_data.png">

---

### Installing BepInEx

!!! tip ""

    - Download [BepInEx](https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.2/BepInEx_win_x64_5.4.23.2.zip)

    - Extract the archive to the root folder of your game data.

    You should now have a few more files, as highlighted:

    <img src="/img/taito/tetoteconnect/setup/1_databepinex.png">

---

### Installing tetoco

!!! tip ""

    - Head over to [tetoco releases](https://github.com/Redcrafter/tetoco/releases)
    and download the latest `tetoco.dll`. **Do not download the source code.**

    - Create a folder called `plugins` in the `BepInEx` folder, and move the dll file to that newly created folder.

    You should end up with a file structure as follows.

    ```
    📂BepInEx
    ┗ 📂plugins
      ┗⚙️tetoco.dll
    ```

---

### Pre-launch requirements

!!! info "These steps are required, otherwise your game won't run."

#### VCRedist & DirectX

!!! tip ""

    - Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
    - Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

#### Monitor orientation


!!! info "With tetoco installed, the game won't automatically rotate to portrait mode when starting it."

    The game can be played in landscape mode but a lot of the play area will be lost, it's best to 
    set your monitor to portrait mode before launching the game.

??? tip "Manually rotating"

    - Right click on your desktop.
	- Click `Display Options`.
	- Look for `Display orientation` and set it to `Portrait` or `Portrait (flipped)`.
 
	<img src="/img/common/orientation_portrait.png">

	- Rotate your monitor vertically.

??? tip "Automatically rotating"

    Right click on [this link](https://raw.githubusercontent.com/gmiwoj/Windows-Display-Orientation-Script/main/windows-display-orientation-script.ps1)
    then `Save Link As` and place the `windows-display-orientation-script.ps1` file in your game's directory.

    Create a new `start.bat` file, and set its content to this, it will set your monitor as **Portrait (flipped)**,
    and automatically rotate it back once you close the game.
    
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

---

### First launch

!!! tip ""

    If you've followed all instructions correctly, you're ready to launch the game.

    Start the game by running `Vision.exe`, or `start.bat` if you followed [the automatic monitor rotation part](#monitor-orientation).

!!! tip ""

    You're all done! The game should load up properly now.

    You can use the **Login as Local** button to use your local save profile. 

    The `T` key can be pressed to access the service menu.

---

### Connecting to a network

!!! info "By default, tetoco uses its own local network and saves data locally."

    Please follow this step only if you have a network to connect to.

??? tip "Remote (Online Network)"

    Open the automatically created configuration file `BepInEx\config\tetoco.cfg`.

    Set `UseLocalServer` to **false**.

    Then, set `RemoteServer` to the address provided by your network.
    
    Finally, set the `CardId` provided by your network.