# Taiko no Tatsujin Nijiiro


<img src="/img/taikonijiiro/taikonijiiro.png">

!!! note "Author Note:"
	Last updated: 08.02.2024 (Currently using `JP/39.06`)

!!! danger "Warning:"
	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.

	If you obtained data from a torrent file, make sure you're not seeding the data before proceeding as well.

	This guide will use [esuo1198's TaikoArcadeLoader](https://github.com/esuo1198/TaikoArcadeLoader/actions), which is a fork of TaikoArcadeLoader that gets regular updates and will be needed to get the game running.

### Getting Started

!!! tip ""
	Before we even touch the game, there are some prerequisites we should install to minimise issues.

	First off we should make sure our [Microsoft Visual C++ Runtimes](https://github.com/abbodi1406/vcredist) are up to date.

	Grab the latest version of the AIO installer from the [releases tab](https://github.com/abbodi1406/vcredist/releases). Make sure to get the version that installs both x86 and x64 versions.

	Run the downloaded `VisualCppRedist_AIO_x86_x64.exe` and press next. The installer will proceed to download and install the required files. This may take some time.

<img src="/img/taikonijiiro/AIO_finished.png">

!!! tip ""
	Next we should make sure we have all the required DirectX files.

	Download the DirectX Redist (June 2010) from the [Microsoft Website](https://www.microsoft.com/en-gb/download/details.aspx?id=8109).

	Run the downloaded `directx_Jun2010_redist.exe` and accept the License Agreement. You will be asked to pick a location to extract the installer too, it's recommended you create a new folder somewhere as it will extract a lot of files.

	Go to the folder you extracted the installer to, find the `DXSETUP.exe` and run it. Accept the License Agreement and start the installation. Once it's complete, press Finish.

	You can delete the folder you extracted the installer to once the install is complete.

<img src="/img/taikonijiiro/redist_finished.png">

### Verifying your Game Data

!!! tip ""
	Taiko is generally distributed as a single folder. For Nijiiro, this will be `SBWY 39.06`.

<img src="/img/taikonijiiro/1.png">

!!! tip ""
	The game folder should contain an `AMCUS`, `Data` and `Executable` folder.

<img src="/img/taikonijiiro/2.png">

!!! danger "Warning:"
	Nijiiro is a rolling release so please verify your game version by opening `AMCUS\AMConfig.ini` and verifying that `cacfg-game_ver=39.06`

!!! note "Other Data Formats:"
	NAMCO data is also distributed as `.VHDX` and `.VHD` files. These files are useful for archival purposes, but are not required to run the game. Always download the unpacked data for home use.

### Setting Up the Game Data

!!! tip ""
	Choose a location for your game data, for example, `C:\TaikoNijiiro\`.  
	Copy/move the folders and files from `Taiko no Tatsujin Nijiiro Version (SBWY 39.06)` to this new folder.  

!!! note "TaikoArcadeLoader:"
	`TaikoArcadeLoader` is a loader and hardware emulator for Nijiiro. It will allow us to launch the game, as well as configure inputs and network settings. More information can be found at the [TAL github page](https://github.com/esuo1198/TaikoArcadeLoader).

!!! tip ""
	Download the latest version of TAL from [the actions tab](https://github.com/esuo1198/TaikoArcadeLoader/actions) of the TAL page. This will be a file named `dist`.   
	You will need to be logged into github to download this file.

<img src="/img/taikonijiiro/dist.png">

!!! tip ""
	Copy the files from `dist.zip` to your `Executable/Release` folder. When asked, choose to replace the existing files with the newly copied files.  
	Here is how your `Executable/Release` folder should look after everything has been copied correctly.

<img src="/img/taikonijiiro/executablereleasecomplete.png">

### Configuring config.toml

!!! tip ""
	The configuration information for segatools is stored within `config.toml`.  
	Open up `config.toml` with a text editor of your choice. We'll be using [Notepad++](https://notepad-plus-plus.org/).  
	`config.toml` is separated into several sections, indicated by the section name in `[square brackets]`.  
	Information for this can be found at the [TAL github page](https://github.com/esuo1198/TaikoArcadeLoader). We will go over the most important ones below.  

!!! tip ""
	The `[amauth]` section contains network related config.  

	`server =` can be left default if playing on a [local server](https://github.com/asesidaa/TaikoLocalServer/tree/Refactor) or offline but it is recommend to play on a [network](networks.md).                                 
	`port =` do not change unless you know what you are doing.                                                                           
	`chassis_id =` do not change unless you know what you are doing.    
	`shop_id =` mostly visual. change if you want to.                            
	`game_ver =` mostly visual. change if you want to.                                                                
	`country_code =` do not change unless you know what you are doing.                                                           

	Example image below.

<img src="/img/taikonijiiro/amauth.png">

!!! tip ""
	The `[patches]` section contains patches.  

	`version =` do not change unless you know what you are doing.                                 
	`res =` change to your display's resolution.                                                                           
	`windowed =` set to `true` if you want to run the game in windowed.    
	`vsync =` set to `true` if your display is set to 120hz.                            
	`unlock_songs =` do not change unless you know what you are doing.                                                                                                                           

	Example image below.

<img src="/img/taikonijiiro/patches.png">

!!! tip ""
	Save and close `config.toml` then run `Taiko.exe` to start the game.


### Further Configuration

!!! note "Controllers:"
	As there are several different input methods, each with different setup procedures, these will be covered in the [Controllers](controllers.md) section.

!!! note "Networks:"
	Local Network options will be covered in the [Networks](networks.md) section.

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section.