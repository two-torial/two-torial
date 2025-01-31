# Taiko no Tatsujin Nijiiro
<img src="/img/taikonijiiro/taikonijiiro.png">

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---
### Preparing data

!!! tip ""

	Taiko is generally distributed as a single folder. For Nijiiro, this will be `SBWY 39.06`. The game folder should contain an `AMCUS`, `Data` and `Executable` folder.

<img src="/img/taikonijiiro/setup/1.png">

!!! danger "Nijiiro is a rolling release so please verify your game version by opening `AMCUS\AMConfig.ini` and verifying that it says `cacfg-game_ver=39.06`"

!!! info "NAMCO data is also distributed as `.VHDX` and `.VHD` files. These files are useful for archival purposes, but are not required to run the game. Always download the unpacked data for home use."

---
### Installing TaikoArcadeLoader (TAL)

!!! tip "TaikoArcadeLoader:"

	`TaikoArcadeLoader` is a loader and hardware emulator for Nijiiro. It will allow us to launch the game, as well as configure inputs and network settings. More information can be found at the [TAL github page](https://github.com/esuo1198/TaikoArcadeLoader).

	- Download the latest version of TAL from [the actions tab](https://github.com/esuo1198/TaikoArcadeLoader/actions) of the TAL page. This will be a file named `TaikoArcadeLoader`. You will need to be logged into github to download this file.

	- Copy the files from `TaikoArcadeLoader.zip` to your `Executable/Release` folder. When asked, choose to replace the existing files with the newly copied files.  

	<img src="/img/taikonijiiro/setup/2.png">

### Configuring TaikoArcadeLoader

!!! tip ""

	The configuration information for TaikoArcadeLoader is stored within `config.toml`.

	Open up `config.toml` with a text editor of your choice. We'll be using [Notepad++](https://notepad-plus-plus.org/).  

!!! info "`config.toml` is separated into several sections, indicated by the section name in `[square brackets]`"
 	Information for this can be found at the [TAL github page](https://github.com/esuo1198/TaikoArcadeLoader).
	
!!! tip "The `[amauth]` section contains network related config"

	- `server =` can be left default if playing on a local server or offline but it is recommend to play on an [online network](#networks).                                 
	- `port =` do not change unless you know what you are doing.                                                                           
	- `chassis_id =` do not change unless you know what you are doing.    
	- `shop_id =` mostly visual. change if you want to.                            
	- `game_ver =` mostly visual. change if you want to.                                                                
	- `country_code =` do not change unless you know what you are doing.                                                           

	```toml
	[amauth]
	server = "127.0.0.1"
	port = "54430"
	chassis_id = "284111080000"
	shop_id = "TWO-TORIAL"
	game_ver = "39.06"
	country_code = "JPN"
	```

!!! tip "The `[graphics]` section contains patches" 

	- `res =` change to your display's resolution.
	- `windowed =` set to `true` if you want to run the game in windowed.
	- `cursor =` mostly visual. change if you want to.
    - `vsync =` set to `true` if your display is set to 120hz.                                        
	- `fpslimit =` do not change unless you know what you are doing.
	- `model_res_rate =` do not change unless you know what you are doing.

	```toml
	[graphics]
	res = { x = 1920, y = 1080 }
	windowed = false
	cursor = true
	vsync = false
	# fpslimit = 0
	model_res_rate = 1.0
	```

!!! tip "The `[keyboard]` section contains keyboard related config"

	- `auto_ime =` if set to true, changes your keyboard layout to Qwerty until the game is closed.
	- `jp_layout =` should be set to `true` for **actual** japanese keyboards.

	```toml
	[keyboard]
	auto_ime = false
	jp_layout = false
	```

### Configuring Inputs

!!! tip ""

	Depending on the input method you choose, the configuration for them can change slightly. Below are all the input methods available and how to set them up.

??? tip "Keyboard"

	Keyboard is the default input method. 
	 
	The default layout uses:

	- ++d++++f++ ++j++++k++ for the P1 drum input
	- ++z++++x++ ++c++++v++ for the P2 drum input
	- ++p++ to `Insert Card`
	- ++f2++ to `SERVICE`
	- ++enter++ to add coins

	If you wish to view or change all the default keybinds, you can do so in `keyconfig.toml`

??? tip "Controller"

	The setup for both drum and normal controllers is the same.

    - In `config.toml` set `wait_period =` to `0`           
    - If you are using a controller that does not use keyboard inputs, you need to set SDL keybinds in `keyconfig.toml`
    - When you're using an analog input for the drums, you need to set `analog_input = false` to `true` in `config.toml`
  
	A list of valid SDL inputs can be found at the bottom of `keyconfig.toml`

  	!!! danger "If you're using 2 controllers, use [JoyToKey](https://joytokey.net/en/) and remove SDL inputs from `keyconfig.toml`"

??? tip "Physical Card Readers"

	You can insert your card with physical card readers. If you happen to have one, you can set them up to use them for Taiko no Tatsujin Nijiiro.
 

	??? tip "AIC Pico"
		- In `config.toml` set `card_reader =` to `false`.
    	- Update to the latest [firmware](https://github.com/whowechina/aic_pico)
    	- Inside `AMFWConfig.ini` change COM4 to the port of your AIC Pico  

	??? tip "ACR122U"
		- In `config.toml` set `card_reader =` to `true`.
    	- Use AkaiiKitsune's [tal-cardreader plugin](https://gitea.farewell.dev/AkaiiKitsune/tal-cardreader)

!!! note "If you don't have a physical card reader, you can skip over to the [Networks](#networks) section"

---
### Networks

!!! danger "Please choose one of the two solutions, not both!"

??? tip "Online Hosted Servers (Recommended)"

	There are a few online hosted servers that support Nijiiro, however most of them are currently invite only. Ask your friends where they play, and maybe they'll invite you!

	**Elara Global Taiko Server**

	[EGTS](https://egts.ca/guide) is the only public Nijiiro server that also comes with an Omnimix verison that includes custom songs and songs from other Taiko games. 

??? tip "Self Hosted Local Servers (Complex)"

	If you wish to run the game locally, but with the ability to create and save a profile, you can run a server on the same computer you are playing the game on. This server will need to be running before you launch the game, however it can be shut down when you are no longer playing.  

    Any provided setup instructions are likely to become outdated rather quickly.  

    Please refer to the included setup instructions on each projects respective web page.

	- [TLS](https://github.com/asesidaa/TaikoLocalServer/tree/Refactor) - A network service emulator for Nijiiro. Setup can be complex as you are required to build TLS from source using [VisualStudio](https://visualstudio.microsoft.com/) and `.sln` files.

---
### Pre-launch requirements

!!! info "These steps are required, otherwise your game won't run."

#### VCRedist & DirectX

!!! tip ""	

	- Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
	- Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

---
### First Launch

!!! tip ""

	Run `Taiko.exe` to start the game.

    Enter the I/O setup screen by pressing ++f1++ on the Attract screen then using the `arrow keys` and ++enter++, navigate to `I/O TEST` -> `TAIKO TEST`. Adjust these settings to your liking as they vary between controllers and keyboards. If you are unsure just leave the defaults as is.

	If you would like to adjust patch settings enter the test menu by pressing ++f1++ on the Attract screen then using the `arrow keys` and ++enter++, navigate to `MOD MANAGER`.

	<img src="/img/taikonijiiro/setup/mod.png">

!!! tip ""
	
	You're all done! The game should load up properly now.

---
### Troubleshooting

!!! warning "Have any other issue?"

	Check out the [Troubleshooting](troubleshooting.md) page.