# beatmania IIDX 31 EPOLIS
<img class="header-logo" src="/img/bemani/iidx/31_epolis/logo.png">

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

!!! danger "Reasonably modern CPU required"

	beatmania IIDX 31 and above require an AVX2 capable CPU. 

	If your CPU is too old, the game will crash with an `EXCEPTION_ILLEGAL_INSTRUCTION` error.

	A known workaround is renaming/deleting the `movies` folder to prevent the game from loading them altogether. 

---
### About data

!!! info "The full game should be around 100gb while updates are only around 2-5gb in size."

!!! info "Standard (LDJ) / Lightning (TDJ)"

	Please keep the following in mind as you're going through this guide.  

	IIDX's codename is `LDJ`. For `IIDX 31 Epolis` this would be either:

	- `LDJ-010` *(TDJ, Lightning cab, 120 FPS)*
	- `LDJ-012` *(LDJ, Standard cab, 60 FPS)*

	The main difference between `010` and `012` is the game's main `.dll` file, `bm2dx.dll`.  

	This changes which features the game offers, and which conditions the game expects to run under.  
	
	- **TDJ** expects a `120hz` compatible monitor for its main screen, and a second `60hz` touchscreen compatible monitor called a subscreen. The second monitor isn't mandatory, we can get around that using spice2x.
	- **LDJ** expects `60hz` monitor for its main screen, and no subscreen.

	We'll be using the terms **TDJ** for **Lightning**, and **LDJ** for **Standard** throughout the guide.

!!! danger "If you're coming from IIDX 30 Resident"

	You'll want to [update your data](#updating-data) **from** `LDJ-003` **to** `LDJ-010` **or** `LDJ-012` **FIRST** then follow this guide as normal.  

---
### Preparing data

!!! tip ""

	After downloading and extracting your data, we need to make sure your files aren't set to `Read-only`.

	- Right click the folder containing your data, then click on `Properties`.
	- In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
	- A popup will appear, select `Apply changes to this folder, subfolder and files` and press `OK`.
	- Finally, click `OK` again to exit out of properties.

	You should end up with a file structure with a few folders only, as follows.

<img src="/img/bemani/iidx/common/setup/data.png">

??? warning "If your data doesn't look like this"

	If you're missing the `modules` folder and instead have bunch of `.dll` files next to your folders:  

	- Create a `modules` folder.
	- Move all `.dll` files inside of it so you end up with a structure as shown above.

	If extra files are present next to your folders, such as executables, scripts, etc.. **remove them**.  
	**This also means your data was tampered with and we strongly recommend getting new data from somewhere else.**

!!! info "If you don't need to update your data, you can skip over to the [Installing spice2x](#installing-spice2x) section."

---
### Updating data

??? danger "Please make sure you're using the right update for your current data."

	As we've seen in the [About data](#about-data) section, the main difference between `LDJ` and `TDJ` is the `bm2dx.dll` file.  
	When updating from a previous version to the next, our current `.dll` will be overwritten.

	Knowing that, patches re-uploaded by the community tend to be named `LDJ-DATECODE-to-LDJ-010/012-DATECODE`.  
	**Note**: If updating from `IIDX 30 Resident`, it will be `LDJ-003-DATECODE-to-LDJ-010/012-DATECODE`.

	For example `LDJ-2024032500-to-LDJ-010-2024050700`.

	- `2024032500` being your current data's version, no matter if it's using a TDJ or LDJ `.dll` file.
	- `2024050700` being the version you would arrive at.
	- `010` meaning you would end up with a `TDJ` *(Lightning Cab)* `bm2dx.dll` file.

!!! tip ""

	- Extract your patch's files to your existing data in a way that matches its file structure. Agree to overwrite files if necessary.
	- Open `prop\ea3-config.xml` in a text editor and find the following lines near the top.

	```xml
		<soft>
			<model __type="str">LDJ</model>
			<dest __type="str">J</dest>
			<spec __type="str">E</spec>
			<rev __type="str">A</rev>
			<ext __type="str">2024050700</ext>
		</soft>
	```

	On the line with `<spec __type="str">` the letter needs to match your data type:
	
    - ^^`E`^^ for Standard (LDJ-012, LDJ, 60hz)
    - ^^`D`^^ for Lightning (LDJ-010, TDJ, 120hz)
  
	Replace the letter accordingly if necessary.

	On the line with `<ext __type="str">` the datecode needs to match your new version.

	- If that's already the case then great! Don't touch anything.
	- If it instead corresponds to our pre-patch datecode, replace it with the new one.

	Now save the file.

---
### Installing spice2x

!!! info ""

	If you already have spice2x installed, make sure it is up to date!

!!! tip ""

	- Head over to [spice2x.github.io](https://spice2x.github.io) and download the latest release.
	- Extract the `spice64.exe` and `spicecfg.exe` files from the archive to your game's directory.
  
	<img src="/img/bemani/iidx/common/setup/spice2x64data.png">

### Configuring spice2x

!!! info "Open `spicecfg.exe`, each following sub-section corresponds to a tab at the top."

#### Buttons

!!! tip ""

	Click on `Bind` then press the key you want associated with the action.

	With your controller and/or keyboard plugged in, configure your keys for:  

	- **Maintenance**: `Service, Test`
	- **P1 Game buttons**: `1 to 7, Start, EFFECT, VEFX` 
	- **P1 Keypad**: `Keypad Insert Card` 

	**Only if** you're using LDJ:

	- **P1 Keypad**: `1 to 9`

	**Only if** you're playing using a keyboard:

	- **Turntable**: `TT+, TT-` **and optionally** `TT+/-` which alternates between `TT+` and `TT-` on each press.
  
#### Analogs (controller/cab only)

!!! tip ""

	With a controller rather than binding buttons to `TT+` and `TT-`, you need to:

	- For Turntable P1, click `Bind`.
	- In `Device`, pick your controller.
	- In `Control`, pick whichever one corresponds to the turntable.
	- Turn your turntable ensuring that the Preview turns along with it.
	- Click `Close`, leaving the rest of the settings alone.

#### Overlay

!!! tip ""

	Modifying buttons in this section is not required but you are free to change what you want.

	Click on `Bind` then press the key you want associated with the action.

#### Lights (controller/cab only)

!!! tip ""

	Your controller might support having its lights controlled by the game through spice2x.

	If it does, here's how you may link different actions to your lights:

	- Click `Bind`.
	- In `Device`, pick your controller.
	- In `Light Control`, select the corresponding light.
	- Click `Close`.
	- Repeat for your other lights.

#### Cards

!!! info "Covered in the [Connecting to a network](#connecting-to-a-network) section."

#### Patches

!!! info "Go through the [spice2x Patching](/extras/patchsp2x.md) page to import patches."

!!! tip ""

	Ever since EPOLIS final (2024-08-26), patches have a description built-in to them.

	To view it, hover-over the `(?)` or `(!)` to the left of each patch's name.

!!! danger "To prevent issues, avoid patching things you don't need or understand."

#### API

!!! warning "Leave everything at default unless you know what you're doing."

#### Options

!!! info "If you don't know what an option does, hover over the question mark at the very left."

	<img src="/img/common/spice2x_option_hover.png">

!!! danger "Be very careful changing options you don't understand as it may cause issues."

!!! tip "Required"

	| Category 		| Option 				| Parameter 		| Setting |
	|---------------|-----------------------|-------------------|---------|
	| Game Options	| IIDX Disable Cameras 	| -iidxdisablecams 	| ON	  |
	| Network		| EA Service URL		| -url				| Covered in [Connecting to a network](#connecting-to-a-network) |

!!! warning "Required For TDJ" 

	| Category 		| Option 				| Parameter 		| Setting |
	|---------------|-----------------------|-------------------|---------|
	| Game Options	| IIDX TDJ Mode		 	| -iidxtdj		 	| ON	  |

	**If you only have a single 120hz monitor**, and not another 60hz touchscreen:

	| Category			| Option 						| Parameter 						| Setting |
	|-------------------|-------------------------------|-----------------------------------|---------|
	| Graphics (common)	| Only Use One Monitor		 	| -graphics-force-single-adapter 	| ON	  |


!!! tip "Highly Recommended for NVIDIA users ONLY"

	| Category 			| Option 							| Parameter 	| Setting |
	|-------------------|-----------------------------------|---------------| 		  |
	| Graphics (common)	| NVIDIA profile optimization	 	| -nvprofile 	| ON	  |


#### Advanced & Development

!!! warning "Leave everything at default unless you know what you're doing."

---
### Connecting to a network

!!! danger "Please choose one of the two solutions, not both!"

??? tip "Remote (Online Network)"

	Open `spicecfg.exe` and head to the `Options` tab.
  
	In the `Network` category, set the following settings: 
	
	- `EA Service URL` to the URL provided by your network.
	- `PCBID` to the PCBID provided by your network.
	
	<img src="/img/common/spice2x_network.png">

	Next you need a card number.  
	If you don't already have one, generate one in the `Cards` tab.  
	To keep your card number safe, create a new `.txt` file with ONLY it inside.

	Once that's done, head to the `Cards` tab, for `Player 1` click `Open...` and point to your text file.

	<img src="/img/common/spice2x_cards.png">

??? tip "Local e-amuse Emulator (Asphyxia)"

	This is covered in the [Asphyxia CORE](/extras/asphyxia.md) page.

---
### Pre-launch requirements

!!! info "These steps are required, otherwise your game won't run."

#### VCRedist & DirectX

!!! tip ""	

	- Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
	- Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

#### Audio

!!! tip ""

	- Open `spicecfg.exe`.
	- At the very top, click on `Shortcuts` then `Audio Playback Devices`.
	- In the popup window, right click on your default audio device, and click on `Properties`.
	- Go to the `Advanced` tab.
	- Check both boxes under `Exclusive Mode`.
	- Open the `Default Format` dropdown.
	- Pick the `16 (or 24) bit, 44100 Hz` option, click `Apply` then `OK`.

	<img src="/img/common/audio_24_441.png">

#### Standard / Lightning / Language settings

!!! info "Read through the [Extra Information](extras.md) page and edit your `prop\ea3-config.xml` file if necessary."

---
### First launch

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](troubleshooting.md) page."

#### BACKUP DATA

!!! tip ""

	If you've followed all instructions correctly, you're now finally ready to launch the game!

	**First plug your controller if you have one** and run `spice64.exe`, press `Yes` when it asks for elevated privileges.

	If it's your first time running the game, you'll immediately be greeted with this screen.

<img src="/img/bemani/iidx/common/firstlaunch/1.png">

#### CLOCK ERROR

!!! tip "" 

	Press your `Test` key to initialize the backup data, a message will pop up stating it's been initialized.

	Next, you'll get another error.

<img src="/img/bemani/iidx/common/firstlaunch/2.png">

!!! tip ""

	Let the game run for a bit until the monitor check is complete and you should be taken to the service menu.

<img src="/img/bemani/iidx/common/firstlaunch/3.png">

!!! tip ""

	Instructions on how to navigate the menu are shown at the bottom of the screen.

	- Press `1` and `2` to go up and down.
	- Press `6` to select/execute.
  
	Start by going up to `CLOCK`.

<img src="/img/bemani/iidx/common/firstlaunch/4.png">

!!! tip ""

	Here, simply select `SAVE AND EXIT` and the clock will be set.

	You'll be back in the service menu.

#### NETWORK OPTIONS

!!! tip ""

	Go to `NETWORK OPTIONS` then `SHOP NAME SETTING`.

<img src="/img/bemani/iidx/common/firstlaunch/5.png">
<img src="/img/bemani/iidx/common/firstlaunch/6.png">

!!! tip ""

	We will need to set a shop name.
	
	- Name your shop to whatever you'd like. Instructions on how to navigate are at the bottom of the screen.
	- Go to `EXIT` then `SAVE AND EXIT`.


<img src="/img/bemani/iidx/common/firstlaunch/7.png">
<img src="/img/bemani/iidx/common/firstlaunch/3.png">

!!! tip ""

	Select `GAME MODE`.
	
	You're all done! The game should load up properly now.

---
### Carding in

!!! info "Before carding in, you have the option of changing the game's language by pressing your `EFFECT` key."

??? tip "For LDJ (Standard)"

	LDJ should accept keypad number binds:

	- Press your `Keypad Insert Card` button.
	- Enter your code using your keypad binds.

??? tip "For TDJ (Lightning)"

	TDJ will ignore keypad number binds, you need to:

	- Press your `Keypad Insert Card` button.
	- Press your `Toggle Sub Screen` overlay button *(PgUp by default)* to bring up the sub screen.
	- Enter your code by clicking on the subscreen's keypad.
	- If your code is accepted, you may now close the overlay.

---
### (optional) Installing Omnimix

!!! info "Check out the [Data Mods and Omnimix](/extras/datamods.md) guide."

---
### Troubleshooting

!!! warning "Have any other issue?"

	Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](/errorcodes/bemani.md) pages.

	For any more game-specific information, check out [Extra Information](extras.md).
