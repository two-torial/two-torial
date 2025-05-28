<img class="header-logo" src="/img/bemani/sdvx/6_exceedgear/logo.png">
# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

## Preparing data

--8<-- "docs/snippets/common/data_readonly.md"

	The **complete game data** should be approximately **20 GB or larger**.  
	If your data is significantly smaller, you likely have an update archive instead of the full game data.

	Here's what the expected data structure should look like: 

	```
	📂data
	📂dev
	📂ext
	📂modules
	📂prop
	```

--8<-- "docs/snippets/bemani/common/data_bad.md"

!!! info "If your data is already up-to-date, you can skip ahead to the [Installing spice2x](#installing-spice2x) section"

## Updating data

!!! info "For a comprehensive list of all game updates in chronological order, visit [BemaniWiki](https://bemaniwiki.com/?SOUND+VOLTEX+EXCEED+GEAR#sdvxegvernew)"

!!! danger "Make sure you're using the right update for your current game version"

	SDVX updates have `KFC` and one or two datecodes in their archive names.

	**Single datecode:** Contains one update (e.g., `KFC_2025021200.7z`)  
	**Two datecodes:** Updates from the older to newer version (e.g., `KFC-2024121000-2025012100.rar`)

	In the two-datecode example:
	- `2024121000` is the older date, the game version required to apply this update
	- `2025012100` is the newer date, and is the version you'll arrive at after applying the update

--8<-- "docs/snippets/bemani/common/data_update.md"

## Installing spice2x

--8<-- "docs/snippets/bemani/common/spice2x64_install.md"

	```
	📂data
	📂dev
	📂ext
	📂modules
	📂prop
	🌶️spice64.exe <---
	🌶️spicecfg.exe <---
	```

--8<-- "docs/snippets/bemani/common/spice2x64_stubs.md"

## Configuring spice2x

!!! info "Following tabs correspond to the ones found in `spicecfg`"

=== "Buttons"

--8<-- "docs/snippets/bemani/sdvx/spicecfg_buttons.md"
  
=== "Analogs"

--8<-- "docs/snippets/bemani/sdvx/spicecfg_analogs.md"

=== "Overlay"

--8<-- "docs/snippets/bemani/common/spicecfg_overlay.md"

=== "Lights"

--8<-- "docs/snippets/bemani/common/spicecfg_lights.md"

=== "Cards"

--8<-- "docs/snippets/bemani/common/spicecfg_cards.md"

=== "Patches"

--8<-- "docs/snippets/bemani/common/spicecfg_patches.md"

=== "API"

--8<-- "docs/snippets/bemani/common/spicecfg_api.md"

=== "Options"

--8<-- "docs/snippets/bemani/common/spicecfg_options.md"

--8<-- "docs/snippets/bemani/common/spicecfg_options_nvprofile.md"

=== "Advanced"

--8<-- "docs/snippets/bemani/common/spicecfg_advanced.md"

=== "Development"

--8<-- "docs/snippets/bemani/common/spicecfg_development.md"

## Configuring Audio

--8<-- "docs/snippets/bemani/common/setup_audio.md"

## Connecting to a network

--8<-- "docs/snippets/bemani/common/setup_network.md"

## Configuring your game

!!! info "Read through the [Extra Information](extras.md) page"

## Monitor Orientation

--8<-- "docs/snippets/bemani/common/display_portraitfirst.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

!!! tip "A few things to remember before each play session"

	- Close of any applications running in the background which could affect performance
	- Double-check your monitor orientation is correct for this game
	- Double-check your sample rate is correct for this game
	- Connect your controller
  
## First launch

!!! tip ""

	If you've followed all instructions correctly, you're finally ready to launch the game!

	Run `spice64.exe`, press `Yes` when it asks for elevated privileges.

	The game will go through a series of checks, let it run, if you've done everything properly they'll pass.

	<img src="/img/bemani/sdvx/6_exceedgear/calibration/1.png">

	If you're seeing this screen, it means you need to calibrate your knobs.

	Press your `Test` key. Here is how you navigate this menu:

	- Press `BT-A` to go up
	- Press `BT-B` to go down
	- Press `Start` to select
  
	Select `I/O CHECK` and press `Start`.

	<img src="/img/bemani/sdvx/6_exceedgear/calibration/2.png">

	Select `CALIBRATION SETTINGS` and press `Start`.

	<img src="/img/bemani/sdvx/6_exceedgear/calibration/3.png">
	<img src="/img/bemani/sdvx/6_exceedgear/calibration/4.png">

	Select `CALIBRATION` and press `Start`.

	First, your left knob (`VOL-L` for keyboard players)

    - **Slowly turn** your **LEFT knob counterclockwise** (`VOL-L Left`) until the line says `COUNT = OK` then press `Start`.
	- **Slowly turn** your **LEFT knob clockwise** (`VOL-L Right`) until the line says `COUNT = OK` then press `Start`.

	Now same thing but for the right knob (`VOL-R` for keyboard players)

    - **Slowly turn** your **RIGHT knob counterclockwise** (`VOL-R Left`) until the line says `COUNT = OK` then press `Start`.
	- **Slowly turn** your **RIGHT knob clockwise** (`VOL-R Right`) until the line says `COUNT = OK` then press `Start`.
	
	<img src="/img/bemani/sdvx/6_exceedgear/calibration/5.png">

	Select `SAVE AND EXIT` and press `Start`.

	<img src="/img/bemani/sdvx/6_exceedgear/calibration/6.png">

	Select `GAME MODE` and press `Start`.
	
	You're all done! The game should load up properly now and you may card in.

# Help

--8<-- "docs/snippets/common/help.md"