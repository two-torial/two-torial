<img class="header-logo" src="/img/extras/asphyxia/logo.webp">
# Asphyxia

!!! danger "Existing save data"

    If you have previously used Asphyxia, be sure to backup your **savedata** folder located next to the `plugins` directory.  
    This folder contains important data including your game profiles and scores that you may want to keep.

## What is Asphyxia?

!!! tip ""

    Asphyxia is a tool that handles online services for BEMANI games by simulating an e-amusement network, enabling features like score saving, profile management, game events and other online functionality.

    It consists of two main components:

    - Asphyxia **CORE**: The foundational framework that provides the base functionality but no game support by itself
    - Asphyxia **PLUGINS**: Community-developed modules that implement game-specific features and support

## Downloading Asphyxia

!!! tip ""

    - Head to [Asphyxia CORE's releases](https://github.com/asphyxia-core/asphyxia-core.github.io/releases) page
    - Download the latest `asphyxia-core-win-x64.zip` archive
    - Prepare a permanent place for your Asphyxia files, **preferably an empty folder away from your game data**
    - Extract the archive inside of it

    You should end up with a structure as follows:

    ```
    📂 asphyxia
    ┣━ 📂 plugins
    ┃  ┣━ 📂 _example@identifier
    ┃  ┃  ┗━ ...
    ┃  ┣━ 📄 asphyxia-core.d.ts
    ┃  ┣━ 📄 package.json
    ┃  ┗━ 📄 tsconfig.json
    ┗━ ▶️ asphyxia-core-x64.exe
    ```

!!! info "You can delete the `_example@identifier` folder, it serves as an example plugin layout for developers"

## Installing Plugins

!!! info "Asphyxia requires a specific plugin for each game you want to use it with"

!!! tip ""

    To get started with Asphyxia for your specific game(s), you'll need to install the appropriate plugin(s).

    While **we maintain a collection of plugins in our Discord server, we may not have support for every game and version**.  
    In such cases, **you will need to search for community-developed plugins online yourself**.

    To install plugins from our Discord:

    - Join our Discord server using the logo in the bottom right of the page
    - Navigate to your game's channel
    - Check the pinned `Resources` message for potential plugin links
    - Download and extract the plugin
    - Place the extracted folders (like `sdvx@asphyxia`) into your `plugins` directory

    If plugin files are scattered across multiple files/folders, create a single directory for them and move everything inside, following the `game@asphyxia` naming scheme.

    ```
    📂 asphyxia
    ┣━ 📂 plugins
    ┃  ┣━ 📂 sdvx@asphyxia
    ┃  ┣━ 📂 iidx@asphyxia
    ┃  ┣━ 📂 etc.
    ┃  ┣━ 📄 asphyxia-core.d.ts
    ┃  ┣━ 📄 package.json
    ┃  ┗━ 📄 tsconfig.json
    ┗━ ▶️ asphyxia-core-x64.exe
    ```

## Starting and Configuring Asphyxia

!!! tip ""

    Launch `asphyxia-core-x64.exe` to start the server.  
    A browser window will automatically open with the Asphyxia WebUI interface.

### Configuring Service URL

!!! tip ""

    To configure the service URL for your BEMANI game:

    - Open `spicecfg.exe`
    - Navigate to the `Options` tab
    - Locate the `EA Service URL` field
    - Enter the URL shown in Asphyxia WebUI's Dashboard (typically `localhost:8083`)

### Game-specific configuration

!!! info "Each tab corresponds to steps you need to follow for various games"

=== "SDVX"

    !!! tip "Settings and WebUI Assets"

        - In the WebUI, select `SDVX` in the left sidebar
        - Under `Plugin Settings`, find `Exceed Gear Data Directory`
        - Enter the full path to your game's data folder (the folder containing `data`, `modules`, `prop`, etc.)
        - (Optional) Toggle all four `Unlock` switches to unlock all game content by default
        - Click `Apply` to save your changes
        - Close Asphyxia by selecting `Process` > `Shutdown CORE` in the top-right corner of the WebUI

        Next, update the WebUI assets:

        - Launch `asphyxia-core-x64.exe` again
        - Click `Update Webui Assets` in the left sidebar
        - Click `Update` and confirm the datacode update in `ea3-config.xml`
        - Wait for the console to show "Done" at the top

    !!! warning "About expected errors"

        While importing WebUI assets you may see errors like:  
        `- [ifs] MD5 mismatch - /data/graphics/ver06/psd_level.ifs`  
        
        If you're using the correct plugin and game data, these can usually be ignored.

    !!! tip "Final setup"

        - Launch SDVX and create a new profile
        - Close the game
        - In the WebUI, navigate to `SDVX` → `Profiles` making sure your new profile appears
        - Customize additional settings through the WebUI interface and make sure everything works as intended

=== "IIDX"

    !!! tip ""

        IIDX setup is straightforward:

        - Launch the game with Asphyxia running
        - Create a new profile in-game
        - The profile will automatically appear in the WebUI
        - You can customize additional settings through the WebUI interface and make sure everything works as intended

## Final words

!!! success "Setup Complete!"

    Remember to always make sure Asphyxia is running **before** starting your game!

    If you were following a guide, you can now return to it and proceed with the next steps.

## Help

--8<-- "docs/snippets/common/help.md"