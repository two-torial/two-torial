!!! info "Synopsis"

    Konami arcade games and associated community tooling are built to run on Windows.  
    This guide will document the best currently known ways to get games working on Linux systems.

!!! warning "Compatibility"

    **ONLY** the following game and versions are confirmed to work with the process described in this guide.

    | Game | Version(s) | Caveats (if any) |
    |------|:----------:|:----------------:|
    | Sound Voltex | `Exceed Gear` | Subscreen clicks don't work |
    | DanceDanceRevolution | `World` | |
    | Mahjong Fight Girl | | |

    This guide was primarily written targetting arch-based systems running KDE and pipewire.  
    **Instructions should still be distro and DE agnostic, but your mileage may vary.**

## Pre-requisites

!!! tip ""

    - A Linux system with:
        - `pipewire` as an audio backend
        - `wine` with wow64 included (default on arch since June 2025) 
        - `winetricks curl unzip` installed
        - `gstreamer gst-plugins-good gst-plugins-ugly gst-libav` for codecs (package names may vary)
    - Compatible game data placed inside a `📂contents` directory
    - Your game's regular setup guide opened in another tab

??? tip "Extra requirements for NixOS"

    `spice2x` requires an optional wine feature which NixOS does not enable by default.
    Apart from that, a patch for `winetricks` is needed due to [weirdness with winetricks on NixOS with WoW64 wine](https://github.com/NixOS/nixpkgs/issues/338367).

    To fix this, copy this to your confiuration:
    ```nix
    environment.systemPackages = [
      (
        pkgs.wine-with-pcsclite.override {
          wineBuild = "wineWow64";
        }
      )
    ];

    nixpkgs.overlays = [
      (
        final: prev: {
          wine-with-pcsclite = prev.wine.overrideAttrs (old: {
            buildInputs = old.buildInputs ++ [final.pcsclite];
            configureFlags = old.configureFlags ++ ["--with-pcsclite"];
          });
          winetricks = prev.winetricks.overrideAttrs (old: {
            patches = [
              (final.fetchpatch {
                # make WINE_BIN and WINESERVER_BIN overridable
                # see https://github.com/NixOS/nixpkgs/issues/338367
                url = "https://github.com/Winetricks/winetricks/commit/1d441b422d9a9cc8b0a53fa203557957ca1adc44.patch";
                hash = "sha256-AYXV2qLHlxuyHC5VqUjDu4qi1TcAl2pMSAi8TEp8db4=";
              })
            ];
            postInstall =
              old.postInstall
              + ''
                sed -i \
                  -e '2i : "''${WINESERVER_BIN:=/run/current-system/sw/bin/wineserver}"' \
                  -e '2i : "''${WINE_BIN:=/run/current-system/sw/bin/.wine}"' \
                  "$out/bin/winetricks"
              '';
          });
        }
      )
    ];
    ```

## Automated setup (for spice2x compatible games)

!!! tip ""

    - Download the `sp2x-linux-setup.sh` script from [NotAkitake/sp2x-linux-setup](https://github.com/NotAkitake/sp2x-linux-setup/)
    - Place it next to your `📂contents` directory contaning compatible game files
    - Make the script executable `chmod +x sp2x-linux-setup.sh`
    - Run the script and follow instructions

## Manual setup

!!! info "This section will mostly describe what the automated process above achieves"

### Installing spice2x

!!! tip ""

    This process is largely the **same as windows** and can be found in your game's setup guide.  
    Simply place the `spice.exe` or `spice64.exe` executable inside `📂contents`.

    We won't need `spicecfg.exe` however.  
    Instead we will later pass `-cfg` as a launch argument to the main spice2x executable later.

!!! warning "NVIDIA Stubs"

    **For ALL graphics cards:** If your game's setup guide has a `Additional steps for AMD and Intel graphics cards` warning in its **Installing spice2x** section, **do what it says**.

### Wine prefix

!!! danger "Double check commands"

    We provide ready-made command for simplicity, however **don't blindy copy and execute them**.  
    **ALWAYS** double check command before running them, and substitute `REPLACE_THIS_PATH` with your own location.

#### Initializing

!!! tip ""

    - Create an empty `📂prefix` directory in the location of your choosing  
    **We advise creating a new prefix for every game and placing it next to `📂contents`**.

    - Run the following command to initialize a new wine prefix without being prompted for mono or gecko.

    ```sh
    WINEARCH=win64 WINEPREFIX=REPLACE_THIS_PATH/prefix WINEDLLOVERRIDES="mscoree=d;mshtml=d" wineboot --init
    ```

#### Common dependencies

!!! tip ""

    Some dependencies are required across most games, install them to your prefix using winetricks as follows:

    ```sh
    WINEARCH=win64 WINEPREFIX=REPLACE_THIS_PATH/prefix winetricks -q dxvk d3dcompiler_42 d3dcompiler_43 d3dcompiler_46 d3dcompiler_47
    ```

#### Game-specific dependencies

!!! info "If there is no tab for your game, you may skip this step"

!!! tip ""

    === "Default (none)"

    === "DDR"

        Install these to your prefix for background movies to play, otherwise the game will crash.

        ```sh
        WINEARCH=win64 WINEPREFIX=REPLACE_THIS_PATH/prefix winetricks -q quartz devenum amstream windowscodecs
        ```

### (optional) PipeWire audio sink

!!! info "You can create an audio device games will accept that routes audio to your desired hardware"

    It **may not be necessary** for all games as it depends on your specific setup and game.  
    You could try following the rest of the guide without this virtual sink first to see whether you need it or not.

!!! tip ""

    - Create the `.config/pipewire/pipewire.conf.d` directory in your home directory if it doesn't already exist

    ```sh
    mkdir -p "$HOME/.config/pipewire/pipewire.conf.d"
    ```

    - Create a `spice2x-sink.conf` file in that directory containing:

    ```sh
    context.modules = [
      {
        name = libpipewire-module-loopback
        args = {
          audio.position = [ FL FR ]
          capture.props = {
            media.class = Audio/Sink
            audio.format = S16LE
            audio.rate = 44100
            audio.channels = 2
            node.name = spice2x41
            node.description = "spice2x @ 44100Hz"
          }
          playback.props = {
            node.passive = true
            node.name = spice2x41.output
            node.description = "SPICE2X 44100Hz OUTPUT"
            target.object = "alsa_output.pci-0000_04_00.6.HiFi__hw_Generic_1__sink"
            audio.format = S16LE
          }
        }
      }
    ]
    ```

    The `audio.rate` may need to be set to 48000 on a per game-basis, but for the games covered here, 44100 is fine.

    The `target.object` set above means audio will be routed the first audio device it finds.  
    If you have multiple audio devices available and want to make sure it outputs to a specific one, run:

    ```sh
    pw-cli list-objects | awk '/node.name/ {name=$0} /media.class/ && /Audio\/Sink/ {gsub(/.*= "|"/,"",name); print name}'
    ```

    Replace the `target.object` device with the output line corresponding to your desired output device.  
    For example:

    ```sh
    target.object = "alsa_output.usb-Focusrite_Scarlett_Solo_4th_Gen_S1APY0Z3611B4E-00.HiFi__Line1__sink"
    ```

    - **Finally**, save and exit then restart pipewire. On systemd distros you may do it by running:

    ```sh
    systemctl --user restart pipewire.service pipewire-pulse.socket
    ```

### (optional) Launcher scripts

!!! info "This section will help you create two bash scripts you may use to start and configure your game"

    They are not mandatory but very handy to have, rather than remembering commands to run spice executables with the right prefix, paths, arguments, etc..

!!! tip "Game start"

    Let's create the main launch script first, which will also be used by our second script.

    - Next to your contents directory, create a `launch.sh` file containing:

    ```bash hl_lines="6 19"
    #!/usr/bin/env bash
    # Game Launcher

    SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
    export WINEARCH=win64
    export WINEPREFIX="REPLACE_THIS_PATH/prefix"

    # Default arguments
    ARGS=""

    # Optional: Add arguments per line
    # ARGS="$ARGS -url localhost:8083"     # Network URL
    # ARGS="$ARGS -p 01FXXXXXXXXXXXXXXXXX" # PCBID

    # Append args to this script
    ARGS="$ARGS $*"

    cd "$SCRIPT_DIR/contents" || exit
    wine "spice64.exe" $ARGS
    ```

    - On the first highlighted line: make sure `WINEPREFIX` points to your game prefix created earlier

    - On the second highlighted line: replace `spice64.exe` with `spice.exe` if necessary

    - Make the script executable by running `chmod +x launch.sh`

!!! tip "Game config"

    To get a graphical interface replicating what `spicecfg.exe` does, we can simply call our previous script and pass `-cfg` as an argument.

    - Next to your previous script, create a `config.sh` file containing:

    ```bash
    #!/usr/bin/env bash
    # Config Launcher

    SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
    "$SCRIPT_DIR/launch.sh" -cfg
    ```

    - On the last line, make sure the file name matches the previous script

    - Make the script executable by running `chmod +x config.sh`

!!! warning "Try executing `config.sh`"

    The spice2x configuration window for your game should appear.  
    Your game should also be detected and show in the top right!

    If your game isn't detected, it's highly likely paths are wrong somewhere in your scripts.

### Game-specific last steps

!!! info "If there is no tab for your game, you may skip this step"

!!! tip ""

    === "Default (none)"

    === "SDVX"

        - You need to patch `Shared Mode WASAPI` to ensure audio comes through wine.  
        Either use the previously created `config.sh` to start spicecfg, or use the command in the next section.  
        If you don't know how patches work, follow instructions in our [spice2x patching](./patchsp2x.md) guide.

        ---

        - You need to set your monitor orientation to portait before playing

        - **OR** If you want to play the game windowed and keep your display in landscape orientation:
 
            - Create a `wine_desktop.reg` file containing:

            ```reg
            Windows Registry Editor Version 5.00

            [HKEY_CURRENT_USER\Software\Wine\Explorer]
            "Desktop"="Default"

            [HKEY_CURRENT_USER\Software\Wine\Explorer\Desktops]
            "Default"="1080x1920"
            ```

            - Fix the paths in the command below and run it. Then feel free to delete the `.reg` file:

            ```sh
            WINEARCH=win64 WINEPREFIX=REPLACE_THIS_PATH/prefix wine regedit REPLACE_THIS_PATH/wine_desktop.reg
            ```

### What's next?

!!! success "Linux-specific instructions are over"

    Head to your game's setup guide, straight to the "Configuring spice2x" section.  

    - **IF** you opted to use the PipeWire audio sink, set it as your default audio device before starting the game
    - Skip the `Configuring audio` section 
    - Skip any section asking you to install VCRedist and/or DirectX, our prefix takes care of that
    - Use the previously created `config.sh` instead of spicecfg, and `launch.sh` to start the game  
        **OR** If you opted not to create scripts, instead use this, fixing the paths and spice executable name:

        ```sh
        cd REPLACE_THIS_PATH/contents && WINEARCH=win64 WINEPREFIX=REPLACE_THIS_PATH/prefix wine "spice64.exe" -cfg
        ```

        And use the same command without the `-cfg` argument to start the game.
