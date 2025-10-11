# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

## About data

!!! note ""

    Please keep the following in mind as you're going through this guide.  

    DDR's codename is `MDX`. Starting with `DDR A20` this would be either:

    - `MDX-001` *(Other cabs, 32 bits)*
    - `MDX-003` *(Gold cab, 64 bits)*

    The gold cab version contains more features, such as exclusive songs or the "GOLDEN LEAGUE" mode.

## Preparing data

--8<-- "docs/snippets/common/data_readonly.md"

    The **complete game data** should be approximately **20 GB or larger**.  
    If your data is significantly smaller, you likely have an update archive instead of the full game data.

    Here's what the expected data structure should look like: 

    ```
    📂arkdata
    📂com
    📂data
    📂modules
    📂prop
    ```

--8<-- "docs/snippets/konami/common/data_bad.md"

!!! info "If your data is already up-to-date, you can skip ahead to the [Installing spice2x](#installing-spice2x) section"

## Updating data

!!! danger "Please make sure you're using the right update for your current data."

    DDR updates have `MDX` and one or two datecodes in their archive names.

    **Single datecode:** Contains one update (e.g., `MDX_NewDateCode.7z`)  
    **Two datecodes:** Updates from the older to newer version (e.g., `MDX_OldDateCode-NewDateCode.rar`)

    A date code should look something like this: `YYYYMMDDXX`

    In the two-datecode example:

    - `OldDateCode` is the older date, the game version required to apply this update
    - `NewDateCode` is the newer date, and is the version you'll arrive at after applying the update

--8<-- "docs/snippets/konami/common/data_update.md"

## Installing spice2x

!!! info "If you already have spice2x installed, ensure you're using the latest version"

??? tip "For MDX-001 (32 bits)"

    - Visit [spice2x.github.io](https://spice2x.github.io) to download the latest release
    - Extract both `spice.exe` and `spicecfg.exe` from the archive into your game's directory
  
    ``` hl_lines="6-7"
    📂arkdata
    📂com
    📂data
    📂modules
    📂prop
    🌶️spice.exe
    🌶️spicecfg.exe
    ```

??? tip "For MDX-003 (64 bits)"

    - Visit [spice2x.github.io](https://spice2x.github.io) to download the latest release
    - Extract both `spice64.exe` and `spicecfg.exe` from the archive into your game's directory
  
    ``` hl_lines="6-7"
    📂arkdata
    📂com
    📂data
    📂modules
    📂prop
    🌶️spice64.exe
    🌶️spicecfg.exe
    ```

## Configuring spice2x

--8<-- "docs/snippets/konami/common/spicecfg_preamble.md"

=== "Buttons"

--8<-- "docs/snippets/konami/common/spicecfg_buttons.md"

    !!! tip "Binding your buttons" 

        Click on `Bind` or `Naive` then press the key you want associated with the action.

        With your controller and/or keyboard plugged in, configure your keys for P1 and/or P2:  

        - **Maintenance**: `Service, Test`
        - **Game buttons**: `Up, Down, Left, Right`
        - **Menu buttons**: ` Start, Up, Down, Left, Right`
        - **Keypad**: `Keypad Insert Card`, `1 to 9`

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

## Connecting to a network

--8<-- "docs/snippets/konami/common/setup_network.md"

## Installing VCRedist & DirectX

--8<-- "docs/snippets/common/setup_vcredist_directx.md"

## Before playing

--8<-- "docs/snippets/common/before_playing.md"

## Help

--8<-- "docs/snippets/common/help.md"