!!! danger "Warning"

	Please make sure you downloaded your data from an appropriate source.
	This guide is unable to troubleshoot any problems related to bad or poorly managed data.

---
### About data

!!! info "The full game should be around 20-25gb in size."

!!! info ""

	Please keep the following in mind as you're going through this guide.  

	DDR's codename is `MDX`. Starting with `DDR A20` this would be either:

	- `MDX-001` *(Other cabs, 32 bits)*
	- `MDX-003` *(Gold cab, 64 bits)*

	The gold cab version contains more features, such as exclusive songs or the "GOLDEN LEAGUE" mode.

---
### Preparing data

!!! tip ""

	After downloading and extracting your data, we need to make sure your files aren't set to `Read-only`.

	- Right click the folder containing your data, then click on `Properties`.
	- In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
	- A popup will appear, select `Apply changes to this folder, subfolder and files` and press `OK`.
	- Finally, click `OK` again to exit out of properties.

	You should end up with a file structure with a few folders only, as follows.

<img src="/img/ddr/setup/1_data.png">

??? warning "If your data doesn't look like this"

	If you're missing the `modules` folder and instead have bunch of `.dll` files next to your folders:  

	- Create a `modules` folder.
	- Move all `.dll` files inside of it so you end up with a structure as shown above.

	If extra files are present next to your folders, such as executables, scripts, etc.. **remove them**.  
	**This also means your data was tampered with and we strongly recommend getting new data from somewhere else.**

---
### Updating data

??? danger "Please make sure you're using the right update for your current data."

	DDR Patches re-uploaded by the community tend to be appropriately named `MDX-DATECODE-to-DATECODE`.

	For example `MDX-2024091000-to-2024101500`.

	- `2024091000` being your current data's version.
	- `2024101500` being the one you would arrive at.

!!! tip ""

	- Extract your patch's files to your existing data in a way that matches its file structure. Agree to overwrite files if necessary.
	- Open `prop\ea3-config.xml` in a text editor and find the following lines near the top.

	```xml
		<soft>
			<model __type="str">MDX</model>
			<dest __type="str">J</dest>
			<spec __type="str">A</spec>
			<rev __type="str">A</rev>
			<ext __type="str">2024101500</ext>
		</soft>
	```

	On the line with `<ext __type="str">` the datecode needs to match your new version.

	- If that's already the case then great! Don't touch anything.
	- If it instead corresponds to your pre-patch datecode, replace it with the new one and save the file.

---
### Installing Spice2x

!!! info ""

	If you already have Spice2x installed, make sure it is up to date!

??? tip "For MDX-001 (32 bits)"

	- Head over to [spice2x.github.io](https://spice2x.github.io) and download the latest release.
	- Extract the `spice.exe` and `spicecfg.exe` files from the archive to your game's directory.
  
	<img src="/img/ddr/setup/2_spicedata32.png">

??? tip "For MDX-003 (64 bits)"

	- Head over to [spice2x.github.io](https://spice2x.github.io) and download the latest release.
	- Extract the `spice64.exe` and `spicecfg.exe` files from the archive to your game's directory.
  
	<img src="/img/ddr/setup/2_spicedata64.png">

### Configuring Spice2x

!!! info "Open `spicecfg.exe`, each following sub-section corresponds to a tab at the top."

#### Buttons

!!! tip ""

	Click on `Bind` then press the key you want associated with the action.

	With your controller and/or keyboard plugged in, configure your keys for:  

	- **Maintenance**: `Service, Test`
	- **P1 Panel buttons**: `Up, Down, Left, Right` 
	- **P1 Menu buttons**: ` Start, Up, Down, Left, Right`
	- **P1 Keypad**: `1 to 9, Keypad Insert Card`

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

!!! danger "To prevent issues, avoid patching things you don't need or understand."

#### API

!!! warning "Leave everything at default unless you know what you're doing."

#### Options

!!! info "If you don't know what an option does, hover over the question mark at the very left."

	<img src="/img/ddr/setup/3_opthover.png">

!!! danger "Be very careful changing options you don't understand as it may cause issues."

!!! tip "Required"

	| Category 		| Option 				| Parameter 		| Setting |
	|---------------|-----------------------|-------------------|---------|
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
	
	<img src="/img/ddr/setup/4_network.png">

	Next you need a card number.  
	If you don't already have one, generate one in the `Cards` tab.  
	To keep your card number safe, create a new `.txt` file with ONLY it inside.

	Once that's done, head to the `Cards` tab, for `Player 1` click `Open...` and point to your text file.

	<img src="/img/ddr/setup/4_cards.png">

??? tip "Local e-amuse Emulator (Asphyxia)"

	This is covered in the [Asphyxia CORE](/extras/asphyxia.md) page.

---
### Pre-launch requirements

!!! info "These steps are required, otherwise your game won't run."

#### VCRedist & DirectX

!!! tip ""	

	- Download and install the latest [VCRedist](https://github.com/abbodi1406/vcredist/releases/latest) (`VisualCppRedist_AIO_x86_x64.exe`)
	- Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

#### K-lite Codec Pack

!!! tip ""	

	- Download and install the [K-lite Codec Pack](https://codecguide.com/download_kl.htm) (the Standard version is enough)

---
### Troubleshooting

!!! warning "Have any other issue?"

	Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](/errorcodes/bemani.md) pages.