# SOUND VOLTEX EXCEED GEAR
<img class="header-logo" src="/img/bemani/sdvx/6_exceed-gear/logo.png">

!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---
### Preparing data

!!! tip ""

	After downloading and extracting your data, we need to make sure your files aren't set to `Read-only`.

	- Right click the folder containing your data, then click on `Properties`.
	- In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
	- A popup will appear, select `Apply changes to this folder, subfolder and files` and press `OK`.
	- Finally, click `OK` again to exit out of properties.

	You should end up with a file structure with a few folders only, as follows.

<img src="/img/bemani/sdvx/6_exceed-gear/setup/1_sdvxdata.png">

??? warning "If your data doesn't look like this"

	If you're missing the `modules` folder and instead have bunch of `.dll` files next to your folders:  

	- Create a `modules` folder.
	- Move all `.dll` files inside of it so you end up with a structure as shown above.

	If extra files are present next to your folders, such as executables, scripts, etc.. **remove them**.  
	**This also means your data was tampered with and we strongly recommend getting new data from somewhere else.**

!!! info "If you don't need to update your data, you can skip over to the [Installing Spice2x](#installing-spice2x) section."

---
### Updating data

??? danger "Please make sure you're using the right update for your current data."

	SDVX Patches re-uploaded by the community tend to be appropriately named `KFC-DATECODE-to-DATECODE`.

	For example `KFC-2024043000-to-2024052100`.

	- `2024043000` being your current data's version.
	- `2024052100` being the one you would arrive at.

!!! tip ""

	- Extract your patch's files to your existing data in a way that matches its file structure. Agree to overwrite files if necessary.
	- Open `prop\ea3-config.xml` in a text editor and find the following lines near the top.

	```xml
		<soft>
			<model __type="str">KFC</model>
			<dest __type="str">J</dest>
			<spec __type="str">G</spec>
			<rev __type="str">A</rev>
			<ext __type="str">2024052100</ext>
		</soft>
	```

	On the line with `<ext __type="str">` the datecode needs to match your new version.

	- If that's already the case then great! Don't touch anything.
	- If it instead corresponds to our pre-patch datecode, replace it with the new one and save the file.

---
### Installing Spice2x

!!! info ""

	If you already have Spice2x installed, make sure it is up to date!

!!! tip ""

	- Head over to [spice2x.github.io](https://spice2x.github.io) and download the latest release.
	- Extract the `spice64.exe` and `spicecfg.exe` files from the archive to your game's directory.
  
	<img src="/img/bemani/sdvx/6_exceed-gear/setup/3_spicedata.png">

??? warning "If you're using an AMD graphics card"

	A few more files are required to make your game work with AMD as the game was built for NVIDIA.

	- From the spice2x archive, extract the `.dll` files found in `spice2x\stubs\64\` to your data's `modules` folder.

	<img src="/img/bemani/sdvx/6_exceed-gear/setup/3_dllamd.png">

### Configuring Spice2x

!!! info "Open `spicecfg.exe`, each following sub-section corresponds to a tab at the top."

#### Buttons

!!! tip ""

	Click on `Bind` then press the key you want associated with the action.

	With your controller and/or keyboard plugged in, configure your keys for:  

	- **Maintenance:** `Service, Test`
	- **Game buttons:** `BT-A, BT-B, BT-C, BT-D, FX-L, FX-R, Start`
	- **P1 Keypad**: `Keypad 0 to 9, Keypad Insert Card` 

	**Only if** you're playing using a keyboard:

	- **Knobs:** `VOL-L Left, VOL-L Right, VOL-R Left, Vol-R Right`
  
#### Analogs (controller/cab only)

!!! tip ""

	With a controller rather than binding buttons to VOL-L and VOL-R, you need to:

	- Click `Bind`.
	- In `Device`, pick your controller.
	- In `Control`, pick `X` for `VOL-L` or `Y` for `VOL-R`.
	- Turn your knob ensuring that the Preview knob turns along with it.
	- Click `Close`, leaving the rest of the settings alone.
	- Repeat for your other knob.

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

!!! info "Go through the [Spice2x Patching](/extras/patchsp2x.md) page to import patches."

!!! tip ""

	Ever since the 2024-09-10 update, patches have a description built-in to them.

	To view it, hover-over the `(?)` or `(!)` to the left of each patch's name.

!!! danger "To prevent issues, avoid patching things you don't need or understand."

#### API

!!! warning "Leave everything at default unless you know what you're doing."

#### Options

!!! info "If you don't know what an option does, hover over the question mark at the very left."

	<img src="/img/bemani/sdvx/6_exceed-gear/setup/4_opthover.png">

!!! danger "Be very careful changing options you don't understand as it may cause issues."

!!! tip "Required"

	| Category 		| Option 				| Parameter 		| Setting |
	|---------------|-----------------------|-------------------|---------|
	| Game Options	| SDVX Disable Cameras 	| -sdvxdisablecams 	| ON	  |
	| Network		| EA Service URL		| -url				| Covered in [Connecting to a network](#connecting-to-a-network) |

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
	
	<img src="/img/gen/network.png">

	Next you need a card number.  
	If you don't already have one, generate one in the `Cards` tab.  
	To keep your card number safe, create a new `.txt` file with ONLY it inside.

	Once that's done, head to the `Cards` tab, for `Player 1` click `Open...` and point to your text file.

	<img src="/img/gen/cards.png">

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
	- Pick the `16 bit, 44100 Hz (CD Quality)` option and click `Apply` then `OK`.

	<img src="/img/bemani/sdvx/6_exceed-gear/setup/6_audio.png">

#### Monitor orientation

!!! tip ""

	Before each play session, you will have to make sure your monitor is in `Portrait` or `Portrait (flipped)` mode.

	To do so:

	- Right click on your desktop.
	- Click `Display Options`.
	- Look for `Display orientation` and set it to `Portrait` or `Portrait (flipped)`.
 
	<img src="/img/bemani/sdvx/6_exceed-gear/setup/6_orientation.png">

	- Rotate your monitor vertically.
  
#### Valkyrie / Nemsys / Language settings

!!! info "Read through the [Extra Information](extras.md) page and edit your `prop\ea3-config.xml` file if necessary."

---
### First launch

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](troubleshooting.md) page."

!!! tip ""

	If you've followed all instructions correctly, you're now finally ready to launch the game!

	**First plug your controller if you have one** and run `spice64.exe`, press `Yes` when it asks for elevated privileges.

	The game will go through a series of checks, let it run, if you've done everything properly they'll pass.

#### Calibration

<img src="/img/bemani/sdvx/6_exceed-gear/calibration/1.png">

!!! tip ""

	If you're seeing this screen, it means you need to calibrate your knobs.

	Press your `Test` key. The game will instruct you where to navigate inside the menu.

	- Press `BT-A` to go up.
	- Press `BT-B` to go down.
	- Press `Start` to select.
  
	Select `I/O CHECK` and press `Start`.

<img src="/img/bemani/sdvx/6_exceed-gear/calibration/2.png">

!!! tip ""

	Select `CALIBRATION SETTINGS` and press `Start`.

<img src="/img/bemani/sdvx/6_exceed-gear/calibration/3.png">
<img src="/img/bemani/sdvx/6_exceed-gear/calibration/4.png">

!!! tip ""

	Select `CALIBRATION` and press `Start`.

	First, your left knob (`VOL-L` for keyboard players)

    1. **Slowly turn** your **LEFT knob counterclockwise** (`VOL-L Left`) until the first line says `COUNT = OK`.
	2. Press `Start`.
	3. **Slowly turn** your **LEFT knob clockwise** (`VOL-L Right`) until the first line says `COUNT = OK`.
	4. Press `Start`.

	Now same thing but for the right knob (`VOL-R` for keyboard players)

    5. **Slowly turn** your **RIGHT knob counterclockwise** (`VOL-R Left`) until the first line says `COUNT = OK`.
	6. Press `Start`.
	7. **Slowly turn** your **RIGHT knob clockwise** (`VOL-R Right`) until the first line says `COUNT = OK`.
	8. Press `Start`.
	
<img src="/img/bemani/sdvx/6_exceed-gear/calibration/5.png">

!!! tip ""
	
	Select `SAVE AND EXIT` and press `Start`.

<img src="/img/bemani/sdvx/6_exceed-gear/calibration/6.png">

!!! tip ""

	Select `GAME MODE` and press `Start`.
	
	You're all done! The game should load up properly now.

---
### Carding in

!!! tip "" 

	Once the game is done loading, you need to card in.

	- Press your `Keypad Insert Card` button.
	- Enter your code using your keypad binds.

---
### Troubleshooting

!!! warning "Have any other issue?"

	Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](/errorcodes/bemani.md) pages.

	For any more game-specific information, check out [Extra Information](extras.md).
