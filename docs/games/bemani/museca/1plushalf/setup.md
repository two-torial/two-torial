<img class="header-logo" src="/img/bemani/museca/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

## Preparing data

--8<-- "docs/snippets/common/data_readonly.md"

	The **complete game data** should be approximately **2.7 GB**.
	
	Here's what the expected data structure should look like: 

	```
	📂data
	📂dev
	📂modules
	📂prop
	```

--8<-- "docs/snippets/bemani/common/data_bad.md"

## Installing spice2x

--8<-- "docs/snippets/bemani/common/spice2x64_install.md"

	```
	📂data
	📂dev
	📂modules
	📂prop
	🌶️spice64.exe <---
	🌶️spicecfg.exe <---
	```

--8<-- "docs/snippets/bemani/common/spice2x64_stubs.md"

## Configuring spice2x

--8<-- "docs/snippets/bemani/common/spicecfg_preamble.md"

=== "Buttons"

--8<-- "docs/snippets/bemani/common/spicecfg_buttons.md"

    !!! tip "Binding your buttons" 

        Click on `Bind` then press the key you want associated with the action.

        With your controller and/or keyboard plugged in, configure your keys for:  

        - **Maintenance:** `Service, Test, Start`
        - **Game buttons:** `Disk# Press (1 to 5), Foot Pedal`
        - **P1 Keypad**: `Keypad 0 to 9, Keypad Insert Card` 

        **Only if** you play with a keyboard:

        - **Disks:** `Disk#- (1 to 5), Disk#+ (1 to 5)` (`Disk#-` is counter-clockwise, while `Disk#+` is clockwise.)
  
--8<-- "docs/snippets/bemani/common/spicecfg_buttons_additionalinfo.md"
  
=== "Analogs"

	!!! info "This tab is used to bind analog controls like the disks"

	!!! warning "Ignore this tab if you play with a keyboard"

	!!! tip "Bind your controller's disks"

		With a controller, instead of binding your disks in the `Buttons` tab, you need to:

		- Click `Bind`
		- In `Device`, pick your controller
		- In `Control`, pick the control that updates the preview when turning the corresponding disk
		- Click `Close`, leaving the rest of the settings alone
		- Repeat for your other disks

=== "Overlay"

--8<-- "docs/snippets/bemani/common/spicecfg_overlay.md"

=== "Lights"

--8<-- "docs/snippets/bemani/common/spicecfg_lights.md"

=== "Cards"

--8<-- "docs/snippets/bemani/common/spicecfg_cards.md"

=== "Patches"

--8<-- "docs/snippets/bemani/common/spicecfg_patches.md"

=== "API"

--8<-- "docs/snippets/bemani/common/spicecfg_nochange.md"

=== "Options"

--8<-- "docs/snippets/bemani/common/spicecfg_options.md"

--8<-- "docs/snippets/bemani/common/spicecfg_options_nvprofile.md"

=== "Advanced"

--8<-- "docs/snippets/bemani/common/spicecfg_nochange.md"

=== "Development"

--8<-- "docs/snippets/bemani/common/spicecfg_nochange.md"

## Configuring Audio

!!! info "First, check out our general [Audio](/extras/audio.md) guide to understand audio modes better, at least the TL;DR. Keep in mind that MÚSECA only supports WASAPI Exclusive, which some devices do not support."

!!! tip ""

	- Open `spicecfg.exe`
	- At the very top, click on `Shortcuts` then `Audio Playback Devices`
	- In the popup window, right click on your default audio device, and click on `Properties`
	- Go to the `Advanced` tab
	- Check both boxes under `Exclusive Mode`
	- Open the `Default Format` dropdown
	- Pick the `16 bit, 44100 Hz (CD Quality)` option, click `Apply` then `OK`

## Connecting to a network

--8<-- "docs/snippets/bemani/common/setup_network.md"

## Configuring your game

!!! info "Read through the [Extra Information](extras.md) page"

## Monitor Orientation

--8<-- "docs/snippets/bemani/common/display_portraitfirst.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## First launch

!!! tip ""

	If you've followed all instructions correctly, you're finally ready to launch the game!

	Run `spice64.exe`, press `Yes` when it asks for elevated privileges.

	The game will go through a series of checks, let it run, if you've done everything properly they'll pass.

	<img class="header-logo" src="/img/bemani/museca/backupdata.webp">

	If you're seeing this screen, it means you need to press the `Test` button to initialize the game's backup data.

	Once the game shows ```BACKUP DATA: INITIALIZED```, restart the game.

!!! success "You're all done! The game should load up properly now"

## Help

--8<-- "docs/snippets/common/help.md"
