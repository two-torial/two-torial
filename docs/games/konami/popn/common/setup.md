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
    📂modules
    📂prop
    ```

--8<-- "docs/snippets/konami/common/data_bad.md"

!!! info "If your data is already up-to-date, you can skip ahead to the [Installing spice2x](#installing-spice2x) section"

## Updating data

!!! danger "Make sure you're using the right update for your current game version"

    pop'n music updates have `M39` and one or two datecodes in their archive names.

    **Single datecode:** Contains one update (e.g., `M39_NewDateCode.7z`)  
    **Two datecodes:** Updates from the older to newer version (e.g., `M39_OldDateCode-NewDateCode.rar`)

    A date code should look something like this: `YYYYMMDDXX`

    In the two-datecode example:

    - `OldDateCode` is the older date, the game version required to apply this update
    - `NewDateCode` is the newer date, and is the version you'll arrive at after applying the update

--8<-- "docs/snippets/konami/common/data_update.md"

## Installing spice2x

--8<-- "docs/snippets/konami/common/spice2x32_install.md"

    ``` hl_lines="5-6"
    📂data
    📂dev
    📂modules
    📂prop
    🌶️spice.exe
    🌶️spicecfg.exe
    ```

## Configuring spice2x

--8<-- "docs/snippets/konami/common/spicecfg_preamble.md"

=== "Buttons"

--8<-- "docs/snippets/konami/common/spicecfg_buttons.md"

    !!! tip "Binding your buttons" 

        Click on `Bind` or `Naive` then press the key you want associated with the action.

        With your controller and/or keyboard plugged in, configure your keys for:  

        - **Maintenance**: `Service, Test`
        - **Game buttons**: `1 to 9`
        - **P1 Keypad**: `1 to 9, Keypad Insert Card`

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

    !!! tip "We recommend using [popnhax](https://github.com/CrazyRedMachine/popnhax) instead of spice2x patching"

=== "API"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Advanced"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Options"

--8<-- "docs/snippets/konami/common/spicecfg_options_nvprofile.md"

=== "Development"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

## Connecting to a network

--8<-- "docs/snippets/konami/common/setup_network.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

!!! success "You're all done! The game should load up properly now"

## Help

--8<-- "docs/snippets/common/help.md"