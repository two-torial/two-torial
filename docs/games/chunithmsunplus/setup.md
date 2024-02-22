# CHUNITHM SUN PLUS

<img src="/img/chunithmsunplus/sunplus.png">

!!! note "Author Note:"
	Last updated: 08.02.2024 (Currently using `SDHD 2.16.00`)
	
	For hex edits: Go to the CHUNITHM section of your prefered patcher host, or use the Offline Patcher included with the unpacked binaries.

!!! danger "Warning:"
	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.

	If you obtained data from a torrent file, make sure you're not seeding the data before proceeding as well.

	This guide will use [Dniel97's segatools](https://gitea.tendokyu.moe/Dniel97/segatools/releases), which is a fork of segatools that gets regular updates and will be needed to get the game running.

### Getting Started

!!! tip ""
	Before we even touch the game, there are some prerequisites we should install to minimise issues.

	First off we should make sure our [Microsoft Visual C++ Runtimes](https://github.com/abbodi1406/vcredist) are up to date.

	Grab the latest version of the AIO installer from the [releases tab](https://github.com/abbodi1406/vcredist/releases). Make sure to get the version that installs both x86 and x64 versions.

	Run the downloaded `VisualCppRedist_AIO_x86_x64.exe` and press next. The installer will proceed to download and install the required files. This may take some time.

<img src="/img/chunithmsunplus/AIO_finished.png">

!!! tip ""
	Next we should make sure we have all the required DirectX files.

	Download the DirectX Redist (June 2010) from the [Microsoft Website](https://www.microsoft.com/en-gb/download/details.aspx?id=8109).

	Run the downloaded `directx_Jun2010_redist.exe` and accept the License Agreement. You will be asked to pick a location to extract the installer too, it's recommended you create a new folder somewhere as it will extract a lot of files.

	Go to the folder you extracted the installer too, find the `DXSETUP.exe` and run it. Accept the License Agreement and start the installation. Once it's complete, press Finish.

	You can delete the folder you extracted the installer too once the install is complete.

<img src="/img/chunithmsunplus/redist_finished.png">

### Verifying your Game Data

!!! tip ""
	SEGA games are generally distributed as a base game folder and sequential update folders. For SUN PLUS, this will be a base `SDHD 2.15.00` and an `SDHD 2.16.00` update.

<img src="/img/chunithmsunplus/1.png">

!!! tip ""
	The base game folder should contain an `amfs`, `App` and `Option` folder.

<img src="/img/chunithmsunplus/2.png">

!!! tip ""
	The update folder should only contain an `App` folder.

!!! note "Other Data Formats:"
	SEGA data is also commonly distributed as single `.app` and `.opt` files. These files are useful for archival purposes, but are not required to run the game. Always download the unpacked data for home use.

### Setting Up the Game Data

!!! danger "Warning:"
	segatools is currently unable to be run from the `E:\` drive. Please ensure your data is setup on another drive letter.

!!! tip ""
	Choose a location for your game data, for example, `C:\CHUNITHMSUNPLUS\`.  
	Copy/move the `amfs`, `App` and `Option` folders from `CHUNITHM SUN PLUS (SDHD 2.15.00)` to this new folder.  
	Copy the `App` folder from `CHUNITHM SUN PLUS (SDHD 2.16.00)` to your new game folder. When asked, choose to replace the existing files with the newly copied files.

<img src="/img/chunithmsunplus/replace.png">

!!! tip ""
	Next we need to replace the protected executables with copys that will run on a regular PC.  
	Obtain unpacked copies of `chusanApp.exe` and `amdaemon.exe`. If these weren't provided with your data, join the [Discord](https://discord.gg/cZRUmEPK78) for assistance.  
	Copy `chusanApp.exe` and `amdaemon.exe` to the `App\bin\` folder of your game data. When asked, overwrite the existing files.

### Installing segatools

!!! note "segatools:"
	`segatools` is a loader and hardware emulator for SEGA arcade games. It will allow us to launch the game, as well as configure inputs and network settings. More information can be found at the [segatools gitea page](https://gitea.tendokyu.moe/Dniel97/segatools).

!!! tip ""
	Download the latest version of segatools from [the release tab](https://gitea.tendokyu.moe/Dniel97/segatools/releases) of the segatools page. This will be a file named `segatools.zip`.   
	As segatools supports many games, the `segatools.zip` file will contain several more zip files. For CHUNITHM SUN PLUS, we will need to open the `chusan.zip`.

<img src="/img/chunithmsunplus/chusanzip.png">

!!! tip ""
	Copy the files from `chusan.zip` to your `App/bin` folder.  
	Here is how your `App/bin` folder should look after everything has been copied correctly.

<img src="/img/chunithmsunplus/appbincomplete.png">

### Configuring segatools.ini

!!! tip ""
	The configuration information for segatools is all stored within `segatools.ini`.  
	Open up `segatools.ini` with a text editor of your choice. We'll be using [Notepad++](https://notepad-plus-plus.org/).  
	`segatools.ini` is seperated into several sections, indicated by the section name in `[square brackets]`.  
	Most options will have comments describing their function and how to configure them. We will go over the most important ones below.  

!!! tip ""
	The `[vfs]` section contains paths to important game files. You can use either relative or absoloute paths, however if your path name has spaces in it, you must wrap the path in "quotations marks".  

	`amfs=` should point to the `amfs` folder, which should be in the root of your game folder. This folder should contain an ICF1 file.  
	`option=` should point to the `Option` folder, which contains game data update folders, with A**XXX** names. This should also be in the root of your game folder, next to `amfs`.  
	`appdata=` is a new folder created for the games appdata. You can either create a folder somewhere to point this too, or simply enter `appdata=appdata` to have a folder created within your `App/bin` folder.

	The example image below was created with a base game folder of `C:\CHUNITHMSUNPLUS\`.

<img src="/img/chunithmsunplus/vfs.png">

!!! tip ""
	The `[dns]` section is for connecting to a server, however this will also need to be changed for offline play. In most cases this will be set to your local IPv4 Address.  
	Open your Command Prompt from the start menu, and type `ipconfig`.  
	Find the line that says `IPv4 Address. . . .` and copy the address. This will normally be in the format of **192.168.x.x**, though this may vary.  
	Replace `127.0.0.1` with the IP address you copied from Command Prompt.

<img src="/img/chunithmsunplus/dns.png">

!!! tip ""
	The `[gpio]` section is where we can change between 60 FPS and 120 FPS.  
	For 60 FPS, leave the settings as they are.  
	For 120 FPS, change `dipsw2` and `dipsw3` from `1` to `0`.

<img src="/img/chunithmsunplus/gpio.png">

!!! tip ""
	Save and close `segatools.ini`.  

	Before we can test the game offline, we need to open `config_hook.json` in a text editor, and replace its content with the following:
	```json
	{
    	"allnet_auth": {
    	    "type": "1.0"
    	},
    	"allnet_accounting": {
    	    "enable": false
    	},
    	"emoney": {
     	   "enable": false
    	}
	}
	```
	This is only needed to boot the game in offline mode, as any correctly configured server should handle the default settings properly.

### Service Menu settings

!!! note "Service Menu:"
	Without an English patch the Service Menu will be in Japanese. [Google Lens](https://lens.google/) is a very handy tool for navigating this menu.

!!! tip ""
	We are now ready to test our game setup.  
	Start the game by launching `start.bat` from the games `App/bin` folder.  
	Let the game load until it gets to the following screen.

<img src="/img/chunithmsunplus/asettings.png">

!!! tip ""
	Press `F1` on your keyboard to enter the Service Menu (`1` on older versions of segatools).  
	Use `D` and `F` to navigate the menu, and `L` to select an option.  

	Navigate to `Game Settings`, the 4th option from the top.

<img src="/img/chunithmsunplus/gamesettings.png">

!!! tip ""
	Select the second option, `reference machine settings` and toggle this setting to `follow the reference machine`, as shown below.

<img src="/img/chunithmsunplus/followreference.png">

!!! tip ""
	Select the last option from the menu, to return to the previous menu.  
	Once back to the main Service Menu, select the 10th option in the list, `closing setting`.

<img src="/img/chunithmsunplus/closingsetting.png">

!!! tip ""
	Select the second option, `hour`, and toggle with `L` until the option `all time` is selected.

<img src="/img/chunithmsunplus/alltime.png">

!!! tip ""
	Select the last option from the menu to return to the previous menu, and then select the last option of the main menu to save your settings and continue booting the game.  

	If you get stuck at a `Waiting for Distribution Server` message, shown below, close the game and relaunch. This is caused by dipswitch settings not setting themselves correctly the very first time the game is launched.

<img src="/img/chunithmsunplus/distserver.png">

!!! tip ""
	If everything has been set up correctly, you should now be at the games Attract Screen.  
	`F2` and `F3` will let you insert service/coin credits (`1` and `2` on older versions of segatools).
	Now we know the game is working, we can move on to configuring controllers and network access.

### Further Configuration

!!! note "Controllers:"
	As there are several different input methods, each with different setup procedures, these will be covered in the [Controllers](controllers.md) section.

!!! note "Networks:"
	Local Network options will be covered in the [Networks](networks.md) section.

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section.