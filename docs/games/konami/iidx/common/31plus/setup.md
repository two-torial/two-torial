# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

--8<-- "docs/snippets/common/cpu_avx2.md"

## Standard and Lightning modes

--8<-- "docs/snippets/konami/iidx/ldj_vs_tdj.md"

## Preparing data

--8<-- "docs/snippets/common/data_readonly.md"

    The **complete game data** should be approximately **100 GB or larger**.  
    If your data is significantly smaller, you likely have an update archive instead of the full game data.

    Here's what the expected data structure should look like: 

    ```
    📂data
    📂dev
    📂modules
    📂prop
    ```

--8<-- "docs/snippets/konami/common/data_bad.md"

!!! info "If your data is already up-to-date, you can skip ahead to the [Installing spice2x](#installing-spice2x) section"

## Updating data

!!! danger "Make sure you're using the right update for your current game version"

    IIDX updates have `LDJ` and one or two datecodes in their archive names.

    **Single datecode:** Contains one update (e.g., `LDJ_NewDateCode.7z`)  
    **Two datecodes:** Updates from the older to newer version (e.g., `LDJ_OldDateCode-NewDateCode.rar`)

    A date code should look something like this: `YYYYMMDDXX`

    In the two-datecode example:

    - `OldDateCode` is the older date, the game version required to apply this update
    - `NewDateCode` is the newer date, and is the version you'll arrive at after applying the update

--8<-- "docs/snippets/konami/common/data_update.md"

## Installing spice2x

--8<-- "docs/snippets/konami/common/spice2x64_install.md"

    ``` hl_lines="5-6"
    📂data
    📂dev
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

--8<-- "docs/snippets/konami/iidx/spicecfg_buttons.md"
  
--8<-- "docs/snippets/konami/common/spicecfg_buttons_additionalinfo.md"

=== "Analogs"

--8<-- "docs/snippets/konami/iidx/spicecfg_analogs.md"

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

--8<-- "docs/snippets/konami/iidx/spicecfg_options_disablecams.md"

--8<-- "docs/snippets/konami/common/spicecfg_options_nvprofile.md"

--8<-- "docs/snippets/konami/iidx/spicecfg_options_tdj.md"

=== "Advanced"

--8<-- "docs/snippets/konami/iidx/spicecfg_advanced_camhook.md"

=== "Development"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

## Configuring audio

--8<-- "docs/snippets/konami/common/setup_audio.md"

## Connecting to a network

--8<-- "docs/snippets/konami/common/setup_network.md"

## Configuring your game

!!! info "Read through the [Extra Information](extras.md) page"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    **First plug your controller if you have one** and run `spice64.exe`, press `Yes` when it asks for elevated privileges.

    If it's your first time running the game, you'll immediately be greeted with this screen.

    <img src="/img/konami/iidx/common/firstlaunch/1.webp">

    Press your `Test` key to initialize the backup data, a message will pop up stating it's been initialized.

    Next, you'll get another error.

    <img src="/img/konami/iidx/common/firstlaunch/2.webp">

    Press your `Test` key again and let the game run for a bit until the monitor check is complete.

    You will now be taken to the service menu.

    <img src="/img/konami/iidx/common/firstlaunch/3.webp">

    Instructions on how to navigate the menu are shown at the bottom of the screen:

    - Press `1` and `2` to go up and down.
    - Press `6` to select/execute.
  
    Start by going up to `CLOCK`.

    <img src="/img/konami/iidx/common/firstlaunch/4.webp">

    Here, simply select `SAVE AND EXIT` and the clock will be set.

    You'll be back in the service menu.

    Go to `NETWORK OPTIONS` then `SHOP NAME SETTING`.

    <img src="/img/konami/iidx/common/firstlaunch/5.webp">
    <img src="/img/konami/iidx/common/firstlaunch/6.webp">

    You will need to set a shop name.
    
    - Name your shop to whatever you'd like. Again, navigation instructions are at the bottom of the screen.
    - Go to `EXIT` then `SAVE AND EXIT`.

    <img src="/img/konami/iidx/common/firstlaunch/7.webp">

    Select `GAME MODE`.

    <img src="/img/konami/iidx/common/firstlaunch/3.webp">
    
!!! success "You're all done! The game should load up properly now"

## Carding in

!!! info "Before carding in, you have the option to change the game's language by pressing your `EFFECT` key"

??? tip "For LDJ (Standard mode)"

    LDJ should accept keypad number binds:

    - Press your `Keypad Insert Card` button.
    - Enter your code using your keypad binds.

??? tip "For TDJ (Lightning mode)"

    TDJ will ignore keypad number binds, you need to:

    - Press your `Keypad Insert Card` button.
    - Press your `Toggle Sub Screen` overlay button *(PgUp by default)* to bring up the sub screen.
    - Enter your code by clicking on the subscreen's keypad.
    - If your code is accepted, you may now close the overlay.

## Help

--8<-- "docs/snippets/common/help.md"