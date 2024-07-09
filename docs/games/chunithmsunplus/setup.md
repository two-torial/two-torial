# CHUNITHM SUN PLUS

<img src="/img/chunithmsunplus/sunplus.png">

!!! info "Last updated: July 9th, 2024"

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

***

### About data

!!! info "SEGA games are generally distributed as a base game folder and sequential update folders. For SUN PLUS, this will be a base `SDHD 2.15.00` and a `SDHD 2.16.00` update."

	The base game folder should contain an :material-folder:`amfs`, :material-folder:`App` and :material-folder:`Option` folders and the update folder should only contain an :material-folder:`App` folder.

	<img src="/img/chunithmsunplus/1.png">
	<img src="/img/chunithmsunplus/2.png">

??? note "Other Data Formats:"

	SEGA data is also commonly distributed as single :material-floppy:`.app` and :material-floppy:`.opt` files. These files are useful for archival purposes, but are not required to run the game. Always download the unpacked data for home use.

***

### Updating and preparing data

!!! danger "Segatools is currently unable to be run from the `E:\` drive. Please ensure your data is setup on another drive letter!"
	
!!! tip ""
	
	- Create a new folder, for example `C:\CHUNITHMSUNPLUS\`
	- Extract the contents of `SDHD 2.15.00` into the new game folder.
	- Copy the `App` folder from `SDHD 2.16.00` to your new game folder.
  
 	When asked, overwrite the existing files.

	Next, we need to replace the protected executables with copies that will run on a regular PC.

	- Obtain unpacked copies of `chusanApp.exe` and `amdaemon.exe`.
	- Copy `chusanApp.exe` and `amdaemon.exe` to the `App\bin\` folder of your game data.
  
	When asked, overwrite the existing files again.

	If these weren't provided with your data, join the [Discord](https://discord.gg/cZRUmEPK78) for assistance.

***

### Installing Segatools

!!! info "`Segatools` is a game loader and hardware emulator for SEGA arcade games. It will allow us to launch the game, as well as configure inputs and network settings. More information can be found at the [Segatools gitea page](https://gitea.tendokyu.moe/Dniel97/segatools)."

!!! tip ""

	- Download the latest version of Dniel97's Segatools from [the release tab.](https://gitea.tendokyu.moe/Dniel97/segatools/releases)

	- Copy the files from `chusan.zip` to your `App/bin` folder.  

	You should end up with a file structure, as follows.

<img src="/img/chunithmsunplus/appbincomplete.png">

### Configuring segatools.ini

!!! info "The configuration information for segatools is all stored within `segatools.ini`"
	
!!! tip ""
	
	Open `segatools.ini` with a text editor of your choice. We'll be using [Notepad++](https://notepad-plus-plus.org/).

	`segatools.ini` is separated into several sections, indicated by the section name in `[square brackets]`.  

	Most options will have comments describing their function and how to configure them. We will go over the most important ones below.  

!!! example "[vfs]"

	The `[vfs]` section contains paths to important game files. You can use either relative or absolute paths, however if your path name has spaces in it, you must wrap the path in "quotations marks".  

	- `amfs=` should point to the `amfs` folder, which should be in the root of your game folder. This folder should contain an ICF1 file.
	- `option=` should point to the `Option` folder, which contains game data update folders, with A**XXX** names. This should also be in the root of your game folder, next to `amfs`.
	- `appdata=` is a new folder created for the games appdata. You can either create a folder somewhere to point this too, or simply enter `appdata=appdata` to have a folder created within your `App/bin` folder.

	The example below was created with the base game folder of `C:\CHUNITHMSUNPLUS\`.

	```ini
	[vfs]
	; Insert the path to the game AMFS directory here (contains ICF1 and ICF2)
	amfs="C:\CHUNITHMSUNPLUS\amfs"
	; Insert the path to the game Option directory here (contains Axxx directories)
	option="C:\CHUNITHMSUNPLUS\Option"
	; Create an empty directory somewhere and insert the path here.
	; This directory may be shared between multiple SEGA games.
	; NOTE: This has nothing to do with Windows %APPDATA%.
	appdata=appdata
	```

!!! example "[dns]"

	The `[dns]` section is for connecting to a server, however this will also need to be changed for offline play. In most cases this will be set to your local IPv4 Address.  
	
	!!! danger "Please choose one of the two solutions, not both!"

	??? info "Remote (Online Network) / Local AIME Emulator"

		- Replace `127.0.0.1` with the IP address of your network.

		```ini
		[dns]
		; Insert the hostname or IP address of the server you wish to use here.
		; Note that 127.0.0.1, localhost etc are specifically rejected.
		default=http://yoururl.com/
		```

	??? info "Offline Play"

		- Open your Command Prompt from the start menu, and type `ipconfig`.
		- Find the line that says `IPv4 Address. . . .` and copy the address. This will normally be in the format of **192.168.x.x**, though this may vary.  
		- Replace `127.0.0.1` with the IP address you copied from Command Prompt.

		<img src="/img/chunithmsunplus/dns.png">

		```ini
		[dns]
		; Insert the hostname or IP address of the server you wish to use here.
		; Note that 127.0.0.1, localhost etc are specifically rejected.
		default=192.168.1.118
		```

		- Open `config_hook.json` and replace its content with the following:

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

!!! example "[gpio]"

	The `[gpio]` section is where we can change between 60 FPS and 120 FPS.  

	- For 60 FPS, leave the settings as they are.  
	- For 120 FPS, change `dipsw2` and `dipsw3` from `1` to `0`.

	```ini
	[gpio]
	; ALLS DIP switches.
	enable=1

	; Enable freeplay mode. This will disable the coin slot and set the game to
	; freeplay. Keep in mind that some game modes (e.g. Freedom/Time Modes) will not
	; allow you to start a game in freeplay mode.
	freeplay=0

	; LAN Install: If multiple machines are present on the same LAN then set 
	; this to 1 on exactly one machine and set this to 0 on all others.
	dipsw1=1
	; Monitor type: 0 = 120FPS, 1 = 60FPS
	dipsw2=0
	; Cab type: 0 = SP, 1 = CVT. SP will enable VFD and eMoney. This setting will switch
	; the LED 837-15093-06 COM port and the AiMe reder hardware generation as well.
	dipsw3=0
	```

!!! info "When you're done making your changes, save and close `segatools.ini`"

??? danger "If your PC has a 10th Gen or newer Intel CPU"
	
	Due to an [issue with OpenSSL](https://www.intel.com/content/www/us/en/developer/articles/troubleshooting/openssl-sha-crash-bug-requires-application-update.html), AMDaemon will fail to launch without the following changes.

	- Find the `start.bat` file in your games bin folder, and open it with a text editor.  
	- At the very top of the file, above the `@echo off` line, add the following:

	```bat
	set OPENSSL_ia32cap=:~0x20000000
	```

	- Save and close `start.bat`.

***

### Input Methods (Controller etc.)

!!! warning "`Segatools` does not come with any built-in controller support. By default it will only accept keyboard input."
	  
!!! tip ""

	The controller you plan on using with the game should also be provided with IO files, in the form of `.dll` files. These `.dll` files should be copied to your `\App\bin\` folder, alongside `chusanApp.exe` and referenced in your `segatools.ini`.
	
	If unsure, you can check the support section of the site you purchased your controller from, or email the vendor directly. 

	The input files you wish to use need to be referenced in the `[chuniio]` section of `segatools.ini`

??? info "If the input files you wish to use consists of 2 `.dll` files with names ending in `_x86.dll` and `_x64.dll`"

    - Uncomment the `path32` and `path64` lines by removing the `;` from the beginning.
    - Add your file names after the `=`.

	Below is an example using `controller_x86.dll` and `controller_x64.dll`. The file names may vary.

	```ini
	[chuniio]
	; Uncomment this if you have custom chuniio implementation comprised of a single 32bit DLL.
	; (will use chu2to3 engine internally)
	;path=

	; Uncomment both of these if you have custom chuniio implementation comprised of two DLLs.
	; x86 chuniio to path32, x64 to path64. Both are necessary.
	path32=controller_x86.dll
	path64=controller_x64.dll
	```

??? info "If the input files you wish to use consists of a single `.dll` file"

	- Uncomment only the `path` line, and enter the dll name after the `=`.

	```ini
	[chuniio]
	; Uncomment this if you have custom chuniio implementation comprised of a single 32bit DLL.
	; (will use chu2to3 engine internally)
	path=controller.dll

	; Uncomment both of these if you have custom chuniio implementation comprised of two DLLs.
	; x86 chuniio to path32, x64 to path64. Both are necessary.
	;path32=
	;path64=
	```

***

### Pre-launch requirements

!!! info "These steps are required, otherwise your game won't run."

#### VCRedist & DirectX

!!! tip ""	

	- Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
	- Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

	There is one last step before running the game.

***

### First launch 

!!! info "Without an English patch the Service Menu will be in Japanese. [Google Lens](https://lens.google/) is a very handy tool for navigating this menu."

#### Closing settings

!!! tip ""

	If you've followed all instructions correctly, you're now finally ready to launch the game!

	Start the game by launching `start.bat` from the games `App/bin` folder.

	Let the game load until it gets to the following screen.

<img src="/img/chunithmsunplus/asettings.png">

!!! tip ""
	
  	Press ++f1++ on your keyboard to enter the Service Menu (++1++ on older versions of Segatools).  
  	
	Use ++d++ and ++f++ to navigate the menu, and ++l++ to select an option.  
  	
	Navigate to `Game Settings`, the 4th option from the top.

<img src="/img/chunithmsunplus/gamesettings.png">

!!! tip ""

	Select the second option, `reference machine settings` and toggle this setting to `reference machine`, as shown below.

<img src="/img/chunithmsunplus/reference.png">

!!! tip ""

	Select the last option from the menu, to return to the previous menu.  

	Once back to the main Service Menu, select the 10th option in the list, `closing setting`.

<img src="/img/chunithmsunplus/closingsetting.png">

!!! tip ""

	Select the second option, `hour`, and toggle with ++l++ until the option `all time` is selected.

<img src="/img/chunithmsunplus/alltime.png">

!!! tip ""

	Select the last option from the menu to return to the previous menu, then select the last option of the main menu to save your settings and continue booting the game.  

??? info "If you get stuck at a `Waiting for Distribution Server` message"
	
	Shown below:

	<img src="/img/chunithmsunplus/distserver.png">
	
	Close the game and launch it again. 
	
	This is because the dipswitch settings `dipsw1`, `dipsw2` and `dipsw3` are not set the first time you run the game, as some system files still need to be created.
	
	If the game is running at the wrong frame rate, you may need to exit and re-open the game for these settings to apply.

!!! tip ""

	If everything has been set up correctly, you should now be at the game's Attract Screen. 

	++f2++ and ++f3++ will let you insert service/coin credits (++1++ and ++2++ on older versions of Segatools).
	Now that we know the game is working, we can move on to configuring controllers and network access.

***

### Further Configuration

!!! info "As there are several different input methods, each with different setup procedures, these will be covered in the [Controllers](controllers.md) section."
	

!!! note "Local Network options will be covered in the [Networks](networks.md) section."

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section.