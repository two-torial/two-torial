<img class="header-logo" src="/img/konami/iidx/24_sinobuz/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Preparing data

!!! tip ""

    After downloading and extracting your data, we need to make sure your files aren't set to `Read-only`.

    - Right click the folder containing your data, then click on `Properties`.
    - In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
    - A popup will appear, select `Apply changes to this folder, subfolder and files` and press `OK`.
    - Finally, click `OK` again to exit out of properties.

    You should end up with a file structure with a few folders only, as follows:

<img src="/img/konami/iidx/24_sinobuz/data.webp">

??? warning "If your data doesn't look like this"

    If extra files are present next to your folders, such as executables, scripts, etc., **remove them**.  
    **This also means your data was tampered with and we strongly recommend getting new data from somewhere else.**

## Installing spice2x

!!! info ""

    If you already have spice2x installed, make sure it is up to date!

!!! tip ""

    - Head over to [spice2x.github.io](https://spice2x.github.io) and download the latest release.
    - Extract the `spice.exe` and `spicecfg.exe` files from the archive to your game's directory.
  
    <img src="/img/konami/iidx/24_sinobuz/spice2xdata.webp">

## Configuring spice2x

!!! info "Open `spicecfg.exe`, each following sub-section corresponds to a tab at the top"

#### Buttons

!!! tip ""

    Click on `Bind` then press the key you want associated with the action.

    With your controller and/or keyboard plugged in, configure your keys for:  

    - **Maintenance**: `Service, Test`
    - **P1 Game buttons**: `1 to 7, Start, EFFECT, VEFX` 
    - **P1 Keypad**: `1 to 9, Keypad Insert Card` 

    **Only if** you're playing using a keyboard:

    - **Turntable**: `TT+, TT-` **and optionally** `TT+/-` which alternates between `TT+` and `TT-` on each press.
  
### Analogs (controller/cab only)

!!! tip ""

    With a controller rather than binding buttons to `TT+` and `TT-`, you need to:

    - For Turntable P1, click `Bind`.
    - In `Device`, pick your controller.
    - In `Control`, pick whichever one corresponds to the turntable.
    - Turn your turntable ensuring that the Preview turns along with it.
    - Click `Close`, leaving the rest of the settings alone.

### Overlay

!!! tip ""

    Modifying buttons in this section is not required but you are free to change what you want.

    Click on `Bind` then press the key you want associated with the action.

### Lights (controller/cab only)

!!! tip ""

    Your controller might support having its lights controlled by the game through spice2x.

    If it does, here's how you may link different actions to your lights:

    - Click `Bind`.
    - In `Device`, pick your controller.
    - In `Light Control`, select the corresponding light.
    - Click `Close`.
    - Repeat for your other lights.

### Cards

!!! info "Covered in the [Connecting to a network](#connecting-to-a-network) section"

### Patches

!!! info "Go through the [spice2x Patching](/extras/patchsp2x.md) page to import patches"

!!! danger "To prevent issues, avoid patching things you don't need or understand"

### API

!!! warning "Leave everything at default unless you know what you're doing"

### Options

!!! info "If you don't know what an option does, hover over the its name with your mouse"

    <img src="/img/common/spice2x_option_hover.webp">

!!! danger "Be very careful changing options you don't understand as it may cause issues"

!!! tip "Required"

    | Category         | Option                 | Parameter         | Setting |
    |---------------|-----------------------|-------------------|---------|
    | Network        | EA Service URL        | -url                | Covered in [Connecting to a network](#connecting-to-a-network) |

!!! tip "Highly Recommended for NVIDIA users ONLY"

    | Category             | Option                             | Parameter     | Setting |
    |-------------------|-----------------------------------|---------------|           |
    | Graphics (common)    | NVIDIA profile optimization         | -nvprofile     | ON      |


### Advanced & Development

!!! warning "Leave everything at default unless you know what you're doing"

## Connecting to a network

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

## Pre-launch requirements

!!! info "These steps are required, otherwise your game won't run"

### VCRedist & DirectX

!!! tip ""    

    - Download and install the latest [VCRedist](https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/)  
    - Download and install the [DirectX End-User Runtimes](https://www.microsoft.com/en-us/download/details.aspx?id=8109)

### Audio

!!! tip ""

    - Open `spicecfg.exe`.
    - At the very top, click on `Shortcuts` then `Audio Playback Devices`.
    - In the popup window, right click on your default audio device, and click on `Properties`.
    - Go to the `Advanced` tab.
    - Check both boxes under `Exclusive Mode`.
    - Open the `Default Format` dropdown.
    - Pick the `24 bit, 44100 Hz (CD Quality)` option and click `Apply` then `OK`.

    <img src="/img/common/audio_24_441.webp">

## First launch

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](troubleshooting.md) page"

### BACKUP DATA

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    **First plug your controller if you have one** and run `spice.exe`, press `Yes` when it asks for elevated privileges.

    If it's your first time running the game, you'll immediately be greeted with this screen.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/1.webp">

### CLOCK ERROR

!!! tip "" 

    Press your `Test` key to initialize the backup data, a message will pop up stating it's been initialized.

    Next, you'll get another error.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/2.webp">

!!! tip ""

    Let the game run for a bit until the monitor check is complete and you should be taken to the service menu.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/3.webp">

!!! tip ""

    Instructions on how to navigate the menu are shown at the bottom of the screen.

    - Press `1` and `2` to go up and down.
    - Press `6` to select/execute.
  
    Start by going up to `CLOCK`.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/4.webp">

!!! tip ""

    Here, simply select `SAVE AND EXIT` and the clock will be set.

    You'll be back in the service menu.

### DEFINITION TYPE

!!! tip ""

    Go to `GAME OPTIONS` then `DEFINITION TYPE`.

!!! tip ""

    Choose either `HD` or `HD*` depending on your preferences.

    `HD*` adds `+1.0` offset in-game, while `HD` doesn't.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/5.webp">

!!! tip ""

    Once done selecting, select `YES` then `SAVE AND EXIT`.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/6.webp">

### NETWORK OPTIONS

!!! tip ""

    Go to `NETWORK OPTIONS` then `SHOP NAME SETTING`.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/7.webp">
<img src="/img/konami/iidx/common/oldhd/firstlaunch/8.webp">

!!! tip ""

    We will need to set a shop name.
    
    - Name your shop to whatever you'd like. Instructions on how to navigate are at the bottom of the screen.
    - Go to `EXIT` then `SAVE AND EXIT`.

<img src="/img/konami/iidx/common/oldhd/firstlaunch/9.webp">
<img src="/img/konami/iidx/common/oldhd/firstlaunch/10.webp">

!!! tip ""

    Select `GAME MODE`.
    
    You're all done! The game should load up properly now.

## Carding in

!!! tip ""
    To card into the game:
    
    1. Press your `Keypad Insert Card` button.
    2. Enter your code using your keypad binds.

## Troubleshooting

!!! warning "Have any other issue?"

    Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](/errorcodes/konami.md) pages.

    For any more game-specific information, check out [Extra Information](extras.md).