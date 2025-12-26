<img class="header-logo" src="/img/konami/sdvx/7_nabla/logo.webp">
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

--8<-- "docs/snippets/konami/common/data_bad.md"

!!! info "If your data is already up-to-date, you can skip ahead to the [Installing spice2x](#installing-spice2x) section"

## Updating data

!!! info "For a comprehensive list of all game updates in chronological order, visit [BemaniWiki](https://bemaniwiki.com/?SOUND+VOLTEX+%A2%E0#sdvxnblvernew)"

!!! danger "Make sure you're using the right update for your current game version"

    SDVX updates have `KFC` and one or two datecodes in their archive names.

    **Single datecode:** Contains one update (e.g., `KFC_NewDateCode.7z`)  
    **Two datecodes:** Updates from the older to newer version (e.g., `KFC-OldDateCode-NewDateCode.rar`)

    In the two-datecode example:
 
    - `OldDateCode` is the older date, the game version required to apply this update
    - `NewDateCode` is the newer date, and is the version you'll arrive at after applying the update

--8<-- "docs/snippets/konami/common/data_update.md"

## Installing spice2x

--8<-- "docs/snippets/konami/common/spice2x64_install.md"

    ``` hl_lines="6-7"
    📂data
    📂dev
    📂ext
    📂modules
    📂prop
    🌶️spice64.exe
    🌶️spicecfg.exe
    ```

--8<-- "docs/snippets/konami/common/spice2x64_stubs.md"

## Configuring spice2x

--8<-- "docs/snippets/konami/common/spicecfg_preamble.md"

=== "Buttons"

--8<-- "docs/snippets/konami/common/spicecfg_buttons.md"

--8<-- "docs/snippets/konami/sdvx/spicecfg_buttons.md"
  
--8<-- "docs/snippets/konami/common/spicecfg_buttons_additionalinfo.md"
  
=== "Analogs"

--8<-- "docs/snippets/konami/sdvx/spicecfg_analogs.md"

=== "Overlay"

--8<-- "docs/snippets/konami/common/spicecfg_overlay.md"

=== "Lights"

--8<-- "docs/snippets/konami/common/spicecfg_lights.md"

=== "Cards"

--8<-- "docs/snippets/konami/common/spicecfg_cards.md"

=== "Patches"

--8<-- "docs/snippets/konami/common/spicecfg_patches.md"

=== "API"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Options"

--8<-- "docs/snippets/konami/common/spicecfg_options.md"

--8<-- "docs/snippets/konami/common/spicecfg_options_nvprofile.md"

=== "Advanced"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Development"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

## Configuring audio

--8<-- "docs/snippets/konami/common/setup_audio.md"

## Connecting to a network

--8<-- "docs/snippets/konami/common/setup_network.md"

## Configuring your game

!!! info "Read through the [Extra Information](extras.md) page"

## Monitor Orientation

--8<-- "docs/snippets/konami/common/display_portraitfirst.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"
  
## First launch

!!! tip ""

    If you've followed all instructions correctly, you're finally ready to launch the game!

    Run `spice64.exe`, press `Yes` when it asks for elevated privileges.

    The game will go through a series of checks, let it run, if you've done everything properly they'll pass.

    <img src="/img/konami/sdvx/6_exceedgear/calibration/1.webp">

    If you're seeing this screen, it means you need to calibrate your knobs.

    Press your `Test` key to go to the service menu.
    
    Instructions on how to navigate the menu are shown at the bottom of the screen:

    - Press `BT-A` to go up
    - Press `BT-B` to go down
    - Press `Start` to select
  
    Select `I/O CHECK` and press `Start`.

    <img src="/img/konami/sdvx/6_exceedgear/calibration/2.webp">

    Select `CALIBRATION SETTINGS` and press `Start`.

    <img src="/img/konami/sdvx/6_exceedgear/calibration/3.webp">
    <img src="/img/konami/sdvx/6_exceedgear/calibration/4.webp">

    Select `CALIBRATION` and press `Start`.

    First, your left knob (`VOL-L` for keyboard players)

    - **Slowly turn** your **LEFT knob counterclockwise** (`VOL-L Left`) until the line says `COUNT = OK` then press `Start`.
    - **Slowly turn** your **LEFT knob clockwise** (`VOL-L Right`) until the line says `COUNT = OK` then press `Start`.

    Now same thing but for the right knob (`VOL-R` for keyboard players)

    - **Slowly turn** your **RIGHT knob counterclockwise** (`VOL-R Left`) until the line says `COUNT = OK` then press `Start`.
    - **Slowly turn** your **RIGHT knob clockwise** (`VOL-R Right`) until the line says `COUNT = OK` then press `Start`.
    
    <img src="/img/konami/sdvx/6_exceedgear/calibration/5.webp">

    Select `SAVE AND EXIT` and press `Start`.

    <img src="/img/konami/sdvx/6_exceedgear/calibration/6.webp">

    Select `GAME MODE` and press `Start`.
    
!!! success "You're all done! The game should load up properly now"

## Help

--8<-- "docs/snippets/common/help.md"
