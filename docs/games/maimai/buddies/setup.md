# MAIMAI BUDDIES
<img src="/img/maimai/buddies/buddies.png">

---

### 1 - Introduction

!!! danger "Important - Read Carefully"

	This guide is created and maintained by volunteers. If you encounter
	any errors in the guide or have trouble with any of the steps, please
	[join the two-torial discord](https://discord.gg/cZRUmEPK78) and let 
	us know in the appropriate section.

	The guide is organized by numbered chapters which can be accessed from 
	the right sidebar. Each chapter contains collapsible sections with 
	the following labels and colors:
	
	!!! note "Mandatory - Must Read and Follow Steps Exactly"
	
	!!! question "Optional - Can Skip Steps"

	!!! example "Decide - Choose ONLY ONE from the Group"

	!!! tip "Info - Extra Information and Notes"

	!!! danger "Important - Read Carefully"

---

### 2 - Downloads

!!! danger "This guide assumes you are starting with clean unmodified data"

	Packages that are already Modified or Patched are difficult to debug 
	and may not work with the steps in this guide.

??? note "**Find the Following:**"

	- Maimai DX Buddies SDEZ 1.40
	- Unpacked / Decrypted Files
	- ICF Files
	- (optional) English Patch
	- (optional) Option Files
	- (optional) Mega Omnimix

	!!! danger "The above are version specific. Do not mix files across different versions.<br>If you are coming from a previous version of MAIMAI:"

		Create a new folder for the game and start from scratch.
		MAIMAI **DOES NOT** like being extracted over old data!

	!!! danger "The 1.41 update is NOT recommended."

??? note "**Download the Following:**"

	- [Dniel97 segatools.zip 2024-06-30](https://gitea.tendokyu.moe/Dniel97/segatools/releases/tag/2024-06-30)
	- [Visual C++ Redistributable Runtime](https://github.com/abbodi1406/vcredist/releases/latest)

---

### 3 - Preparing Data

??? note "**Folder Structure**"

	!!! danger "There are currently issues with running game data in the `E:\` or `Y:\` drive.<br>Please extract the data into other drives."

	After downloading and extracting your data, make sure your files
	are not set to `Read-only`.

	- Right click the folder containing your data, then click on 
	`Properties`.
	- In the `General` tab go down to `Attributes`, untick `Read-only` 
	and click `Apply`.
	- A popup will appear, select `Apply changes to this folder, subfolder 
	and files`and press `OK`.
	- Finally, click `OK` again to exit out of properties.

	Extract Maimai DX Buddies. The root directory file structure is as 
	follows:

	<img width="500" src="/img/maimai/buddies/setup_rootdir.png">
	
	Rename `Option` to `option`. Create empty folders `appdata` and `amfs` 
	in the root directory:

	<img width="500" src="/img/maimai/buddies/setup_rootdir2.png"> 

	The `App` folder should have a file structure as follows.

	<img width="500" src="/img/maimai/buddies/setup_appdir.png">

	??? danger "If your data doesn't look like this:"

		If extra files are present next to your folders, such as 
		executables, scripts, etc.. **This most likely means your 
		data was tampered with and we strongly recommend getting 
		new data from somewhere else.**

??? note "**Installing ICFs**"

	Install Configuration Files (ICFs) tell the game what version it is.
	**Without this your game cannot go online!**

	If your `amfs` folder already has files named `ICF1` and `ICF2`, skip 
	this step.

	Otherwise, obtain a copy of SDEZ_1.40.icf and rename to `ICF1` 
	**without any file extensions**. Create a copy of ICF1 and rename the 
	copy to ICF2. Place both files in the `amfs` folder.

	??? tip "Showing File Extensions"

		By default, file extensions on Windows are hidden. Enable them
		by navigating to the `View` tab in File Explorer and select 
		`File name extensions`.

	??? tip "Creating ICF Files"

		It is also possible to create (encode) the 1.40 ICF files 
		using the [icf-reader project](https://gitea.tendokyu.moe/beerpsi/icf-reader/releases)
		and the following json:
		```
		[
			{
			"type": "System",
			"id": "ACA",
			"version": "80.01.01",
			"required_system_version": "80.01.01",
			"datetime": "2021-11-10T13:45:11",
			"is_prerelease": false
			},
			{
			"type": "App",
			"id": "SDEZ",
			"version": "1.40.00",
			"required_system_version": "80.01.01",
			"datetime": "2023-08-02T13:00:07",
			"is_prerelease": false
			}
		]
		```

		```
		./icf-reader.exe [input_json] [output_ICF]
		```

??? note "**Installing Unprotected Executables**"

	MAIMAI executables are protected and will not run on a regular 
	computer.

	Obtained unprotected (also called `unpacked` or `decrypted` by the 
	community) copies of `Sinmai.exe`, `amdaemon.exe`, and the folder 
	`Sinmai_Data` with the modified dll's for your game version. 

	Copy the files and folder into the `App\Package` folder. Agree to overwrite
	files. 

??? question "**Installing English Patch**"

	The patch should contain a `Sinmai_Data` folder. Copy the contents
	into the game's `Sinmai_Data` and agree to overwrite files.

??? question "**Installing Option Data**"

	MAIMAI content updates are distributed through option folders instead 
	of patching the base game. They are named `A???`, with each `?` 
	being a number. Custom options distributed by the community might use 
	different letters instead such as `H???`, to distinguish them from 
	official ones.

	**Place options folders `A???` / `H???` inside the `option` folder**

---

### 4 - Configuring the Game

??? note "Installing Segatools"

	- Extract [segatools.zip](https://gitea.tendokyu.moe/Dniel97/segatools/releases/tag/2024-06-30)
	- Inside segatools, extract `mai2.zip` which should contain the following 
	contents:

	<img width="500" src="/img/maimai/buddies/setup_segatools.png">

	- Place the above `mai2` contents inside the `App\Package` folder.

??? note "Configuring Segatools"

	Since there is no graphical configuration tool for segatools, you 
	will have to edit the configuration file by hand. It is found in 
	`App\Package\segatools.ini`.

	It is recommended that you follow along using a text editor with 
	syntax highlighting such as [Notepad++](https://notepad-plus-plus.org/).

	If you've been matching the file structure as described in the 
	[Preparing data](#preparing-data) section, you can fill in this 
	section with the values below:

	```ini
	[vfs]
	amfs=../../amfs
	option=../../option
	appdata=../../appdata
	```

	```ini
	[dns]
	default=YOUR_IPv4_Address
	```

	??? tip "Finding IPv4 Address"

		Open a command promt. Type `ipconfig` and look for the IPv4
		address. Place those digits here otherwise you will get stuck 
		on the DNS(LAN) check.

	```ini
	[gpio]
	freeplay=1
	```

	!!! danger "All other settings are config specific - Leave for now"

??? note "Configuring Patches"

	The unprotected files call upon a configuration file to load various 
	patches for the game:
	
	- **mai2.ini** - if using english patch
	- **maimaiDX.ini** - if **not** using english patch 

	Create the appropriate file inside the `App\Package` folder with the 
	following contents:
	
	```ini
	[AM]
	Target=0
	IgnoreError=1
	DummyTouchPanel=1
	DummyLED=1
	DummyCodeCamera=1
	DummyPhotoCamera=1

	[Patches]
	EnablePatchLog=0
	EnableLoadAssetSupportPng=0
	EnablePickImageToCamera=0
	EnableSkipInformationDialog=0
	EnableSkipRegionalDiscover=0
	EnableSinglePlayer=1
	EnableRemoveNetworkEncryption=1

	[Sound]
	Sound8Ch=0

	[Debug]
	Debug=1
	SinglePlayer=1
	MaxTrack=3
	AllOpen=1
	```

	??? tip "More Configuration Options"

		The following have been present in various .ini files and may 
		or may not work with a specific version. Many of these have 
		already been moved into segatools and are no longer used:

		```ini
		[AM]
		Target=0 // for hardware/cabinet targeting
		IgnoreError=1 // ignores errors instead of crashing
		// the following are to fake hardware so that the game runs
		DummyTouchPanel=1
		DummyLED=1
		DummyCodeCamera=1
		DummyPhotoCamera=1 

		[Sound]
		Sound8Ch=0 // changing to 1 causes no sound

		[aime]
		enable=1 // seems to be the same as segatools aime enable

		[Patches]
		EnablePatchLog=1 // writes to dppatchlog.log
		EnableLoadAssetSupportPng=0 // for reading custom jackets
		EnablePickImagetoCamera=0 // for setting avatar from file
		// the following are self explanatory
		EnableSkipInformationDialog=1
		EnableSkipRegionalDiscover=1
		EnableSinglePlayer=1
		EnableRemoveNetworkEncryption=1
	
		[Debug]
		Debug=1 // enables these options
		SinglePlayer=1 // game defaults to 2 player
		// automatically unlock the following
		AllOpen=1
		AllMap=1
		AllCollection=1
		AllChara=1
		EventOverride=1 // ???
		MaxTrack=6 // number of tracks to play during normal mode (default 3)
		MusicSelectTime=65535 // not working
		Creative=1 // ???
		```

??? note "Configuring Aime Card"

	!!! danger "If you have a card reader - disconnect it for now." 

		Follow these steps even if you have a card reader. 

	Create a file named `aime.txt` inside `App\Package\DEVICE` and type 
	in your 20-digit access code if you already have one, or make one up 
	if you don't. If you're making one up, the access code **MUST NOT** 
	start with a 3.

	<img src="/img/maimai/buddies/setup_aime.png">

---

### 5 - Guest Mode Test

!!! danger "These steps are required, otherwise your game will not run."

??? note "VCRedist"

	- Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
	- Restart the computer

??? note "Fixing OpenSSL on Intel 10th Gen and newer CPUs"

	If you have an Intel 10th Gen CPU or newer, right click 
	`App\bin\start.bat`, select `Edit`, and add the highlighted line to 
	the top of the file.

	```batch hl_lines="2"
	@echo off
	set OPENSSL_ia32cap=:~0x20000000

	pushd %~dp0
	...
	```

??? note "Test Launch"

	!!! danger "If you are not using the English Patch"

		The menu items follow the same order in either language

	Double click `start.bat` in the `App\Package` folder. If everything 
	is setup properly, there will be three windows. The cmd windows should 
	show the following:

	<img src="/img/maimai/buddies/setup_cmd.png">

	The other window `AM Daemon` can be ignored.

	The last window is Sinmai.exe which goes through a sequence of 
	checks. The first is the data check which also ensures the program 
	is running on appropriate hardware (make sure Target=0 in mai2.ini):

	<img src="/img/maimai/buddies/setup_sinmai.png">

	The next check is for the aime reader which segatools is emulating:

	<img src="/img/maimai/buddies/setup_sinmai2.png">

	Afterwards the game checks the network:

	<img src="/img/maimai/buddies/setup_sinmai3.png">

	The last check is on the hardware at which point the game should 
	be stuck on `Searching for Servers`:

	<img src="/img/maimai/buddies/setup_sinmai4.png">

	To fix this, press the `F1` key on the keyboard to enter the service 
	menu:

	<img src="/img/maimai/buddies/setup_service.png">

	Navigate to `GAME SETTINGS` using the following keys:
	
	| Control | Keyboard |
	|---------|----------|
	| UP | W |
	| DOWN | C |
	| SELECT | F1 |

	Then change the `LOCAL MATCHING SETTING` to `OFF`

	<img src="/img/maimai/buddies/setup_service2.png">

	Make sure to `EXIT` on both menus to save the settings. Once you 
	are back in the menu press `ESC` to quit and close all windows 
	related to the game. 

	Relaunch `start.bat`. The game should now boot (make sure to allow 
	Sinmai.exe to communicate on local networks) in `Guest Mode` and can 
	be navigated with the following:

	| Controller | Keyboard |
	|------------|----------|
	| Button 1 | W |
	| Button 2 | E |
	| Button 3 | D |
	| Button 4 | C |
	| Button 5 | X |
	| Button 6 | Z |
	| Button 7 | A |
	| Button 8 | Q | 
	| Service | F1 |
	| Quit | ESC |

---

### 6 - Connecting to a Network

!!! danger "Please choose ONE of the three options"

	**Remote** - easier to setup but scores may be deleted at anytime<br>
	**Artemis** - completely local<br>
	**AquaDX** - **TODO**

??? example "Remote (Online Network)"

	Head to the `[dns]` section inside `segatools.ini`. Set `default` to 
	the address provided by your network. **Do not add `http://` or 
	`https://` to the address!**

	```ini
	[dns]
	default=network.example
	```

	Then, head to the `[keychip]` section and set `id` to the keychip ID 
	provided by your network host:

	```ini
	[keychip]
	id=XXXX-XXXXXXXXXXX
	```

??? example "Artemis (Local Network)"

	??? note "Install Tools" 

		- Install [Python 3.11](https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe) 
		and `Add Python to PATH` when the option is presented.

		!!! danger "Only use python 3.8 - 3.11 (3.12 will not work)"

		- Download and install [MariaDB](https://mariadb.org/download/) 
		with default settings. Set a password (`YOUR_DB_PASSWORD`) 
		and remember it.

		- Download and install [DBeaver](https://dbeaver.io/download/) 
		with default settings.

	??? note "Setup Database"

		Open DBeaver and connect to MariaDB database with 
		`YOUR_DB_PASSWORD`:

		<img src="/img/maimai/buddies/setup_dbeaver.png">

		Install drivers if prompted. 
	
		Click the `SQL Editor` dropdown and click `Open SQL Console`. 
		Paste the following into the console (replace 
		`YOUR_DB_PASSWORD`):

		```
		CREATE USER 'aime'@'localhost' IDENTIFIED BY 'YOUR_DB_PASSWORD';
		CREATE DATABASE aime;
		GRANT Alter,Create,Delete,Drop,Index,Insert,References,Select,Update ON aime.* TO 'aime'@'localhost'; 
		```

		Click the top line then click the small orange right-facing 
		triangle to run. Make sure there are no errors. Click the 
		next line and run. Click the last line and run:

		<img src="/img/maimai/buddies/setup_dbeaver2.png">

		If you expand localhost on the left, you should see the new 
		Database `aime` and the new User `aime@localhost`:

		<img src="/img/maimai/buddies/setup_dbeaver3.png">

		Lastly click the `File` dropdown then `Save` then exit. 

	??? note "Configure Artemis"

		- Download [Hay1tsme Artemis](https://gitea.tendokyu.moe/Hay1tsme/artemis) 
		(tested with master branch commit 31ca45fc68)
		- Open a command line and navigate to the extracted artemis 
		folder. Run the following:
		```
		pip install -r requirements.txt
		``` 
		and ensure there are no errors.
		- Copy the folder `example_config` and rename to `config`
		- Enter `config` and open `core.yaml` in an editor.
			- Replace `server: listen_address` with `0.0.0.0`
			- Replace `server: hostname` with `YOUR_IPv4_Address`
			- Replace `title: reboot_start_time` with `6:59`
			- Replace `database: password` with `YOUR_DB_PASSWORD`
			- Replace `aimedb: listen_address` with `0.0.0.0`
			- Replace `aimedb: key` with `KEY` (FIND THE KEY)

		??? tip "Finding IPv4 Address"

			Open a command promt. Type `ipconfig` and look for the IPv4
			address. Place those digits here otherwise you will get stuck
			on the DNS(LAN) check.

	??? note "Create Database Tables"

		Open a command line and navigate to the extracted artemis 
		folder. Run the following:
		```
		python dbutils.py create
		```
		Next import the songs and options into the database:
		```
		python read.py --game SDEZ --version 21 --binfolder /path/to/Sinmai_Data/StreamingAssets --optfolder /path/to/root/option/folder
		```
		After a successfuly import, we can check that database 
		tables are up-to-date:
		```
		python dbutils.py upgrade
		```
		We can now test by running:
		```
		python index.py
		```
		Start the game (start.bat) and it should now connect. To 
		verify, hold down `ENTER` at the start screen and it should 
		read the aime card in `DEVICES\aime.txt`. 

		??? tip "Autostart Artemis"

			Open `run` and type `shell:startup`. This will open 
			the location of startup programs. Create `artemis.bat` 
			in this folder and copy the following:

			```
			@echo off
			cd {Path to artemis}
			start /min cmd /c "python index.py"
			```
			When you restart the PC, artemis will run 
			automatically.

??? example "AquaDX"

	**TODO** - someone experienced with AquaDX needs to write this section

### 7 - Further Configuration

!!! tip "Input methods and controllers are covered in the [Controllers](controllers.md) page."

!!! tip "Have any other issues?"

	Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](../../../errorcodes/sega.md) pages.
