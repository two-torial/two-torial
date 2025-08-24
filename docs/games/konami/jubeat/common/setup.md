# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

## Preparing data

--8<-- "docs/snippets/common/data_readonly.md"

    The **complete game data** should be approximately **10 GB or larger**.  
    If your data is significantly smaller, you likely have an update archive instead of the full game data.

    Here's what the expected data structure should look like: 

    ```
    📂data
    📂modules
    📂prop
    ⚙️msvcr100.dll
    ```

!!! danger "If your data does not look like this"

    If you have **other** `.dll` files next to your `data`, `prop`, etc., folders:

    - Create a `modules` folder if it does not exist already
    - Move all `.dll` files into it

    If extra directories or files are still present (executables, scripts, etc.), **remove them**.

    **This also indicates tampered data, we strongly recommend obtaining clean data from elsewhere.**

!!! info "If your data is already up-to-date, you can skip ahead to the [Installing spice2x](#installing-spice2x) section"

## Updating data

!!! danger "Make sure you're using the right update for your current game version"

    jubeat updates have `L44` and one or two datecodes in their archive names.

    **Single datecode:** Contains one update (e.g., `L44_NewDateCode.7z`)  
    **Two datecodes:** Updates from the older to newer version (e.g., `L44_OldDateCode-NewDateCode.rar`)

    A date code should look something like this: `YYYYMMDDXX`

    In the two-datecode example:

    - `OldDateCode` is the older date, the game version required to apply this update
    - `NewDateCode` is the newer date, and is the version you'll arrive at after applying the update

--8<-- "docs/snippets/konami/common/data_update.md"

## Installing spice2x

--8<-- "docs/snippets/konami/common/spice2x32_install.md"

    ``` hl_lines="5-6"
    📂data
    📂modules
    📂prop
    ⚙️msvcr100.dll
    🌶️spice.exe
    🌶️spicecfg.exe
    ```

--8<-- "docs/snippets/konami/common/spice2x32_stubs.md"

## Configuring spice2x

--8<-- "docs/snippets/konami/common/spicecfg_preamble.md"

=== "Buttons"

--8<-- "docs/snippets/konami/common/spicecfg_buttons.md"

    !!! tip "Binding your buttons"

        Click on `Bind` or `Naive` then press the key you want associated with the action.

        With your controller and/or keyboard plugged in, configure your keys for:  

        - **Maintenance**: `Service, Test`
        - **Game buttons**: `Button 1 to Button 16`
        - **Keypad**: `Keypad Insert Card`

    !!! tip "Using a touch screen" 

        spice2x supports using a touch screen instead of the 16 game buttons. In that case, you don't need to bind these buttons.
  
--8<-- "docs/snippets/konami/common/spicecfg_buttons_additionalinfo.md"

=== "Analogs"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

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

--8<-- "docs/snippets/konami/common/spicecfg_options_nvprofile.md"

=== "Advanced"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Development"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

## Configuring audio

!!! tip ""

    - Open `spicecfg.exe`
    - At the very top, click on `Shortcuts` then `Audio Playback Devices`
    - In the popup window, right click on your default audio device, and click on `Properties`
    - Go to the `Advanced` tab
    - Open the `Default Format` dropdown
    - Pick the `16 bit, 48000 Hz (DVD Quality)` option, click `Apply` then `OK`

    Optionally: go to the `Options` tab in `spicecfg.exe`, and at the very bottom enable `Low Latency Shared Audio` to help mitigate audio latency.

## Connecting to a network

--8<-- "docs/snippets/konami/common/setup_network.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## First launch

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    **First plug your controller if you have one** and run `spice.exe`, press `Yes` when it asks for elevated privileges.

    If it's your first time running the game, you'll immediately be greeted with this screen.

    <img src="/img/konami/jubeat/common/firstlaunch/backup_data_error.webp">

    Press your `Test` key to initialize the backup data, another message with the same error will pop up.  
    Press your `Test` key again to open the service menu.

    You will be greeted by a warning asking you to reboot the game, you can safely ignore it for the moment.

    *Instructions on how to navigate the menu are shown on the screen.*
  
    Go to `GAME OPTIONS`, then `SHOP SETTINGS`.

    <img src="/img/konami/jubeat/common/firstlaunch/shop_settings.webp">

    You will need to set a shop name.
    
    - Name your shop to whatever you'd like. Again, navigation instructions are on the screen.
    - Press the `EXIT` button.

    Then, set the shop area to whatever region you'd like.

    Select `SAVE AND EXIT` then `EXIT`.

    Finally, restart the game.
    
!!! success "You're all done! The game should load up properly now"

## Help

--8<-- "docs/snippets/common/help.md"
