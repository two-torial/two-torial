# CHUNITHM SUN PLUS

<img src="/img/chunithmsunplus/sunplus.png">

!!! note "Author Note:"
	Last updated: 25.01.2024 (Currently using `SDHD 2.16.00`)
	
	For hex edits: Go to [Missless Patcher](https://patcher.missless.net/chunisunplus.html) (should probably find a patcher host who's happy to be featured here)

!!! danger "Warning:"
	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.

	If you obtained data from a torrent file, make sure you're not seeding the data before proceeding as well.

	This guide will use [Dniel97's segatools](https://gitea.tendokyu.moe/Dniel97/segatools/releases), which is a fork of segatools that gets regular updates and will be needed to get the game running.

### Getting Started

!!! tip ""
	Before we even touch the game, there are some prerequisites we should install to minimise issues.

	First off we should make sure our <a href="https://github.com/abbodi1406/vcredist">Microsoft Visual C++ Runtimes</a> are up to date.

	Grab the latest version of the AIO installer from the <a href="https://github.com/abbodi1406/vcredist/releases">releases tab</a>. Make sure to get the version that installs both x86 and x64 versions.

	Run the downloaded `VisualCppRedist_AIO_x86_x64.exe` and press next. The installer will proceed to download and install the required files. This may take some time.

<img src="/img/chunithmsunplus/AIO_finished.png">

!!! tip ""
	Next we should make sure we have all the required DirectX files.

	Download the DirectX Redist (June 2010) from the <a href="https://www.microsoft.com/en-gb/download/details.aspx?id=8109">Microsoft Website</a>.

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
	SEGA data is also commonly distributed as single `.app` and `.opt` files. These files are useful for archive purposes, but are not required to run the game. Always download the unpacked data for home use.

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
	Obtain unpacked copies of `chusanApp.exe` and `amdaemon.exe`. If these weren't provided with your data, join the <a href="https://discord.gg/cZRUmEPK78">Discord</a> for assistance.  
	Copy `chusanApp.exe` and `amdaemon.exe` to the `App\bin\` folder of your game data. When asked, overwrite the existing files.

### Setting up segatools

!!! note "segatools:"
	`segatools` is a loader and hardware emulator for SEGA arcade games. It will allow us to launch the game, as well as configure inputs and network settings. More information can be found at the <a href="https://gitea.tendokyu.moe/Dniel97/segatools"> segatools gitea page</a>.

!!! tip ""
	Download the latest version of segatools from <a href="https://gitea.tendokyu.moe/Dniel97/segatools/releases">the release tab</a> of the segatools page. This will be a file named `segatools.zip`.   
	As segatools supports many games, the `segatools.zip` file will contain several more zip files. For CHUNITHM SUN PLUS, we will need to open the `chusan.zip`.

<img src="/img/chunithmsunplus/chusanzip.png">

!!! tip ""
	Copy the files from `chusan.zip` to your `App/bin` folder.  
	Here is how your `App/bin` folder should look after everything has been copied correctly.

<img src="/img/chunithmsunplus/appbincomplete.png">

!!! tip ""
	Open segatools.ini with a text editor  
	Configure `[vfs]`  

!!! tip ""
	120hz vs 60hz  
	dipswitches  
	patch exe for 60hz  

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section.