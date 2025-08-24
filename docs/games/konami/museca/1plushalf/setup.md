<img class="header-logo" src="/img/konami/museca/logo.webp">
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

--8<-- "docs/snippets/konami/common/data_bad.md"

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

    !!! tip "Binding your buttons" 

        Click on `Bind` or `Naive` then press the key you want associated with the action.

        With your controller and/or keyboard plugged in, configure your keys for:  

        - **Maintenance:** `Service, Test, Start`
        - **Game buttons:** `Disk# Press (1 to 5), Foot Pedal`
        - **P1 Keypad**: `Keypad 0 to 9, Keypad Insert Card` 

        **Only if** you play with a keyboard:

        - **Disks:** `Disk#- (1 to 5), Disk#+ (1 to 5)` (`Disk#-` is counter-clockwise, while `Disk#+` is clockwise.)
  
--8<-- "docs/snippets/konami/common/spicecfg_buttons_additionalinfo.md"
  
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

## Configuring Audio

--8<-- "docs/snippets/konami/common/setup_audio_wasapiexcl_only.md"

## Connecting to a network

--8<-- "docs/snippets/konami/common/setup_network.md"

## Monitor Orientation

--8<-- "docs/snippets/konami/common/display_portraitfirst.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## First launch

!!! tip ""

    If you've followed all instructions correctly, you're finally ready to launch the game!

    Run `spice64.exe`, press `Yes` when it asks for elevated privileges.

    The game will go through a series of checks, let it run, if you've done everything properly they'll pass.

    <img src="/img/konami/museca/backupdata.webp">

    If you're seeing this screen, it means you need to press the `Test` button to initialize the game's backup data.

    Once the game shows `BACKUP DATA: INITIALIZED`, restart the game.

!!! success "You're all done! The game should load up properly now"

## MÚSECA PLUS

!!! info "Since MÚSECA is no longer receiving official updates, community mods like [MÚSECA PLUS](https://museca.plus/) exist to enhance the game with additional content and English translations"

## Help

--8<-- "docs/snippets/common/help.md"