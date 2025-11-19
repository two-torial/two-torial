<img class="header-logo" src="/img/konami/gitadora/fuzzup/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Installing spice2x

!!! info ""

    If you already have spice2x installed, make sure it is up to date!

!!! tip ""

    - Head over to [spice2x.github.io](https://spice2x.github.io) and download the latest release.
    - Extract the `spice64.exe` and `spicecfg.exe` files from the archive to your game's directory.
  
    <img src="/img/konami/gitadora/fuzzup/spice.webp">

## General Configuration

!!! info ""

    Since GITADORA has a separate mode for both Guitar and Drums, the configuration will be split into three sections.<br>This section will cover the general configuration that is not specific to either mode.

!!! info "Open `spicecfg.exe`, each following sub-section corresponds to a tab at the top"

### Buttons

!!! tip ""

    Click on `Bind` then press the key you want associated with the action.

    With your keyboard, configure your keys for:  

    - **Maintenance:** `Test`
    - **P1 Keypad**: `Keypad 0 to 9, Keypad Insert Card`

### Cards

!!! info "Covered in the [Connecting to a Network](#connecting-to-a-network) section"

### Patches

!!! info "Go through the [spice2x Patching](/extras/patchsp2x.md) page to import patches"

!!! danger "To prevent issues, avoid patching things you don't need or understand"

### Options

!!! danger "Be very careful changing options you don't understand as it may cause issues"

!!! tip "Required"

    | Category           | Option                                | Parameter   | Setting |
    |---------------|-----------------------------|-------------|---------|
    | Game Options    | GitaDora Two Channel Audio     | -2ch           | ON        |
    | Network            | EA Service URL                  | -url                | Covered in [Connecting to a Network](#connecting-to-a-network) |

!!! tip "Highly Recommended for NVIDIA users ONLY"

    | Category                 | Option                                           | Parameter       | Setting |
    |-------------------|-----------------------------------|---------------|---------|
    | Graphics (Common)    | NVIDIA profile optimization            | -nvprofile       | ON        |

## GuitarFreaks Configuration

!!! info ""

    This section will cover the configuration specific to the **Guitar** mode.<br>If you are wanting to configure drums, skip to the [DrumMania Configuration](#drummania-configuration) section.

#### Buttons

!!! tip "Set up your guitar as right-handed. Lefty mode is software-based"

!!! tip ""

    Click on `Bind` then press the key you want associated with the action.

    With your keyboard and controller plugged in, configure your keys for:

    - **Guitar P1 IO Panel:** `Guitar P1 Start, Up, Down, Left, Right, Help`
    - **Guitar P1 Controls:** `Guitar P1 Pick Up, Pick Down, R, G, B, Y, P`

### Analogs

!!! tip ""

    Rather than setting your Wail to buttons, you should:

    - Find the Guitar P1 Wail X, Y, and Z analogs.
    - Click `Bind`.
    - In `Device`, pick your guitar.
    - In `Control`, pick the corresponding axis.
    - Move your guitar and ensure the Preview visualizer shows movement.
    - Repeat for other applicable axes your guitar has.

### Advanced

!!! warning "Not setting these values will cause the game to not boot into either mode"

!!! tip "Required"

    | Category           | Option                                | Parameter   | Setting |
    |---------------|-----------------------------|-------------|---------|
    | Paths                    | Path to ea3-config.xml         | -e             | `prop/ea3-config2.xml`     |
    | Paths            | Path to avs-config.xml                 |    -v              | `prop/avs-config-jb.xml` |

## DrumMania Configuration

!!! info ""

    This section will cover the configuration specific to the **Drums** mode.<br>If you are wanting to configure guitar, refer to the [GuitarFreaks Configuration](#guitarfreaks-configuration) section.

### Buttons

!!! tip ""

    Click on `Bind` then press the key you want associated with the action.

    With your keyboard and controller plugged in, configure your keys for:

    - **Drum IO Panel:** `Drum Start, Up, Down, Left, Right, Help`
    - **Drum Controls:** `Drum Hi-Hat, Snare, Hi-Tom, Low-Tom, Right Cymbal, Bass Pedal, Left Cytmbal, Left Pedal, Floor Tom`

### Advanced

!!! warning "Not setting these values will cause the game to not boot into either mode"

!!! tip "Required"

    | Category           | Option                         | Parameter   | Setting |
    |---------------|-------------------------|-------------|---------|
    | Paths                    | Path to ea3-config.xml     | -e                  | `prop/ea3-config.xml`       |
    | Paths                | Path to avs-config.xml  | -v                    | `prop/avs-config-ja.xml` |

## Connecting to a Network

!!! danger "Please choose one of the two solutions, not both!"

??? tip "Remote (Online Network)"

    Open `spicecfg.exe` and head to the `Options` tab.
  
    In the `Network` category, set the following settings: 
    
    - `EA Service URL` to the URL provided by your network.
    - `PCBID` to the PCBID provided by your network.
    
    <img src="/img/common/spice2x_network.webp">

    Next you need a card number.  
    If you don't already have one, generate one in the `Cards` tab.  
    To keep your card number safe, create a new `.txt` file with ONLY it inside.

    Once that's done, head to the `Cards` tab, for `Player 1` click `Open...` and point to your text file.

    <img src="/img/common/spice2x_cards.webp">

??? tip "Local e-amuse Emulator (Asphyxia)"

    This is covered in the [Asphyxia CORE](/extras/asphyxia.md) page.

## Pre-launch Requirements

!!! info "These steps are required, otherwise your game won't run"

### VCRedist & DirectX

!!! tip ""    

    - Download and install the latest [VCRedist](https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/)
    - Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

### Audio

!!! info "GITADORA FUZZ-UP currently only supports WASAPI exclusive mode"

!!! tip ""

    - Open `spicecfg.exe`.
    - At the very top, click on `Shortcuts` then `Audio Playback Devices`.
    - In the popup window, right click on your default audio device, and click on `Properties`.
    - Go to the `Advanced` tab.
    - Check both boxes under `Exclusive Mode`.
    - Open the `Default Format` dropdown.
    - Pick the `24 bit, 44100 Hz (Studio Quality)` option and click `Apply` then `OK`.

    <img src="/img/common/audio_24_441.webp">

## First Launch

!!! danger "If you have any issues running the game at this point, refer to the [Troubleshooting](troubleshooting.md) page"

!!! tip ""

    If you've followed all instructions correctly, you're finally ready to launch the game!

    First, ensure your guitar or drumkit is connected and run `spice64.exe`. Press `Yes` when it asks for elevated privileges.

    Upon launching your game, you will be greeted with this `BACKUP DATA ERROR` screen.

<img src="/img/konami/gitadora/matixx/4.webp">

!!! tip ""

    This is normal, simply hit your `Test` keybind to enter test mode.

<img src="/img/konami/gitadora/matixx/5.webp">

!!! tip ""

    From here, we will need to set a shop name to play, so select the `GAME OPTIONS` option.

<img src="/img/konami/gitadora/matixx/6.webp">

!!! tip "" 

    Then, select `SHOP SETTINGS`.

<img src="/img/konami/gitadora/matixx/7.webp">

!!! tip "" 

    Once inside, select `SHOP NAME SETTINGS` and name your shop whatever you desire! Once that's done, go down to `PREFECTURE` and set it to whatever you desire as well. Finally, go to `SAVE AND EXIT` to get back to the test menu.

<img src="/img/konami/gitadora/matixx/8.webp">

!!! tip ""

    The last menu we'll go inside from the test menu is the clock menu. Go inside `CLOCK` and simply set the clock by hitting `SAVE AND EXIT` as pictured below.

<img src="/img/konami/gitadora/matixx/9.webp">

!!! tip ""

    You're all done! From the test menu, select `GAME MODE` and the game should boot up!

## Carding In

!!! tip "" 

    Once the game is done loading, you need to card in.

    - Press your `Keypad Insert Card` button.
    - Enter your code using your keypad binds.

## Troubleshooting

!!! warning "Have any other issue?"

    Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](/errorcodes/konami.md) pages.
