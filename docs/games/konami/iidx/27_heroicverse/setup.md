<img class="header-logo" src="/img/konami/iidx/27_heroicverse/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Getting Started

!!! tip ""
    Before we even touch the game, let's fiddle with our audio settings to minimize any potential crashing on startup. In Windows, go to `Playback Devices` and then right click on your default device and go to `Properties`. From there, hit the `Advanced` tab and set your `Default Format` to `44100 Hz` and check both of the options inside `Exclusive Mode` as pictured.

<img src="/img/common/audio_24_441.webp">

!!! tip ""
    Once that's done, it's time to work on setting up your data.

    After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, put your desired **64-bit** tools inside the game's `contents` folder, Pictured below is what your folder should look like. 

<img src="/img/konami/iidx/27_heroicverse/1.webp">

## Configuring Your Tools

!!! tip ""
    Now that you have your files ready, open up `spicecfg.exe` and head to the `Options` where we'll set our desired parameters. For the purpose of this guide, we will demonstrate both a local network configuration and an online example below with SpiceTools, skip to whichever you're in need of accordingly and please keep in mind you can add whatever additional parameters you desire.

!!! warning "If you're not using SpiceTools:"
    You will have to likely generate a .bat file given your existing tool's documentation. As stated above, make sure to check the documentation of your tools to ensure you're using the correct parameters for your needs and to consult appropriate support if you're unsure how to do this.

## Configuring for a Local Network

!!! tip ""
    For our local network configuration example, inside `Options` tab we're going to click on the following: `E-Amusement Emulation: -ea` and `Windowed Mode: -w` to enable them.

    What do these different parameters do?

    - `-ea` enables an integrated e-amusement server within SpiceTools.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the selected options inside the `Options` tab in `spicecfg.exe`.

<img src="/img/konami/iidx/27_heroicverse/cfg_ea.webp">

## Configuring for an Online Network

!!! tip ""
    For our online network example we're simply doing the above but with different parameters! On the `Service URL: -url` parameter, we're going to input our chosen network URL like so: `http://yoururlhere.com/`

    To go alongside this, we'll also be inputting into the `PCBID: -p` parameter, the PCBID given to us from our network, like so: `XXXXXXXXXXXXXXXXXXXX`

    Lastly, we'll click on the `Windowed Mode: -w` parameter.

    What do these different parameters do?

    - `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
    - `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the selected options inside the `Options` tab in `spicecfg.exe`.

<img src="/img/konami/iidx/27_heroicverse/cfg_on.webp">

!!! tip ""
    One final note, since you're playing on a network, you will have one additional step of setting up your card file within your chosen tools, make sure to check your server's information on how to setup a card file.

## Final Steps and Setting up the Game

!!! tip ""
    The last steps you'll have to do with your chosen tools is simply setting up your desired keybinds inside the `Buttons` and `Analogs` tabs! Make sure you setup the `Test` keybind as it will be critical for setting up the game. 


!!! tip ""
    Once you've done that, launch your game for the first time by double clicking the `spice64.exe` and the game should load with your chosen parameters from `spicecfg.exe`.

    If it's your first time running the game, you'll immediately be greeted with this screen, oh no!

<img src="/img/konami/iidx/25_cannonballers/4.webp">

!!! tip ""
    Ignore this message, simply hit your `Test` keybind and continue onto this.

<img src="/img/konami/iidx/25_cannonballers/5.webp">

!!! tip ""
    Hit the `Test` keybinding to initialize the backup data, a message will pop up stating it's been initialized.

<img src="/img/konami/iidx/25_cannonballers/6.webp">

!!! tip ""
    You'll also run into this error message as well, let's work on eliminating these messages. Let the game run for a bit until the monitor check is complete and you should be taken to the service menu pictured below.

<img src="/img/konami/iidx/25_cannonballers/7.webp">

!!! tip ""
    Start by navigating up to `CLOCK` and entering that menu.

<img src="/img/konami/iidx/25_cannonballers/8.webp">

!!! tip ""
    Simply hit save and exit and leave, the clock will be saved. Then, back in the service menu, go up to `GAME OPTIONS`

<img src="/img/konami/iidx/25_cannonballers/9.webp">

!!! tip ""
    Once inside that menu, navigate your way up to `DEFINITION TYPE` and choose either `SD` or `HD` depending on your preferences.

<img src="/img/konami/iidx/26_rootage/1.webp">

!!! tip ""
    The game will then count down asking you to confirm the selection before reverting, just hit `YES` assuming it loaded just fine on your computer. Then, exit out of that menu and head to `NETWORK OPTIONS` from back inside the service menu.

    If it doesn't transition to HD, after you've saved, you can simply reboot the game and all should be well.

<img src="/img/konami/iidx/25_cannonballers/11.webp">

!!! tip ""
    The final thing we need to set is here inside `NETWORK OPTIONS`, we will need to set a shop name to play, so select the `SHOP NAME SETTING` option. Once inside, name your shop whatever you desire! For the purpose of the guide, we named it `Guide` but highly encourage fun and/or lazy names. Once that's done go to `EXIT` and then `SAVE AND EXIT` inside of `NETWORK OPTIONS` once you've chosen your desired name, as pictured below.

<img src="/img/konami/iidx/25_cannonballers/12.webp">

<img src="/img/konami/iidx/25_cannonballers/13.webp">

!!! tip ""
    You're all done! From the service menu select `GAME MODE` and the game should load ready to be played! Have fun!

!!! warning "Have any other errors?"
    Check out the [Troubleshooting](troubleshooting.md) section and [Error Code](/errorcodes/konami.md) section to resolve any issues not seen in this guide to greater depth.

    Lightning Mode specifics can be found in the [Extra Information](extras.md#lightning-specific-troubleshooting)