<img class="header-logo" src="/img/konami/mfg/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/data_warning.md"

## Preparing Data

--8<-- "docs/snippets/common/data_readonly.md"

    The **complete game data** should be approximately **5 GB or larger**

    Here's what the expected data structure should look like: 

    ```
    📂prop
    📂modules
    📂game
    📄game.inf
    ```

--8<-- "docs/snippets/konami/common/data_bad.md"

## Installing spice2x

--8<-- "docs/snippets/konami/common/spice2x64_install.md"
    
    ``` hl_lines="5-6"
    📂prop
    📂modules
    📂game
    📄game.inf
    🌶️spice64.exe
    🌶️spicecfg.exe
    ```

## Configuring spice2x

--8<-- "docs/snippets/konami/common/spicecfg_preamble.md"

=== "Buttons"

--8<-- "docs/snippets/konami/common/spicecfg_buttons.md"

    !!! tip "Binding your buttons" 

        Click on `Bind` or `Naive` then press the key you want associated with the action.

        With your keyboard plugged in, configure your keys for P1 and/or P2:  

        - **Maintenance**: `Service, Test`

        Mahjong Fight Girl is a touchscreen game, so it does not need any extra button configuration beyond the above.

--8<-- "docs/snippets/konami/common/spicecfg_buttons_additionalinfo.md"
  
=== "Analogs"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Overlay"

--8<-- "docs/snippets/konami/common/spicecfg_overlay.md"

=== "Lights"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Cards"

--8<-- "docs/snippets/konami/common/spicecfg_cards.md"

=== "Patches"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "API"

--8<-- "docs/snippets/konami/common/spicecfg_nochange.md"

=== "Options"

--8<-- "docs/snippets/konami/common/spicecfg_options.md"

    !!! tip "Choose Cab Type"
        
        Mahjong Fight Girl has multiple cab types. **HG** is currently the only supported cab type.

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
