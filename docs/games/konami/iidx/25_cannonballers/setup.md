<img class="header-logo" src="/img/konami/iidx/25_cannonballers/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Getting Started

!!! tip ""
    Before we even touch the game, let's fiddle with our audio settings to minimize any potential crashing on startup. In Windows, go to `Playback Devices` and then right click on your default device and go to `Properties`. From there, hit the `Advanced` tab and set your `Default Format` to `44100 Hz` and check both of the options inside `Exclusive Mode` as pictured.

<img src="/img/common/audio_24_441.webp">

!!! tip ""
    Once that's done, it's time to work on setting up your data.
    
    After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, put your desired **64-bit** tools inside the game's `contents` folder, and to create a `.bat` file. Pictured below is what your folder should look like, feel free to name your `.bat` file whatever you desire, for the sake of convenience we've named ours `gamestart.bat`.

<img src="/img/konami/iidx/25_cannonballers/1.webp">

## Configuring Your Tools

!!! tip ""
    Now that you have your files ready, open up your `.bat` file in your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/)) and edit it with your desired parameters, for the purpose of this guide we will demonstrate both a local network configuration and an online example below with SpiceTools, skip to whichever you're in need of accordingly and please keep in mind you can add whatever additional parameters you desire.

!!! warning "If you're not using SpiceTools:"
    The overall structure of your .bat file will differ from the guide, namely the initialization of SpiceTools won't be present and potential parameters may differ. As stated above, make sure to check the documentation of your tools to ensure you're using the correct parameters for your needs.

## Configuring for a Local Network

!!! tip ""
    For our local network configuration example, on a single line in the `.bat` file we're going to type `spice64.exe -ea -w` and save the file. 

    What do these different parameters do?

    - `-ea` enables an integrated e-amusement server within SpiceTools.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/konami/iidx/25_cannonballers/2.webp">

## Configuring for an Online Network

!!! tip ""
    For our online network example we're simply doing the above but with different parameters! On our single line, we're going to type `spice64.exe -p XXXXXXXXXXXXXXXXXXXX -url http://yoururlhere.com/ -w` and save the file. 

    What do these different parameters do? 

    - `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
    - `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/konami/iidx/25_cannonballers/3.webp">

!!! tip ""
    One final note, since you're playing on a network, you will have one additional step of setting up your card file within your chosen tools, make sure to check your server's information on how to setup a card file.

## Final Steps and Setting up the Game

!!! tip ""
    The last steps you'll have to do with your chosen tools is simply setting up your desired keybinds! Make sure you setup the `Test` keybind as it will be critical for setting up the game. Once you've done that, launch your game for the first time by double clicking the `.bat` you setup and the game should load.

    If it's your first time running the game, you'll immediately be greeted with this screen, oh no!

<img src="/img/konami/iidx/25_cannonballers/4.webp">

!!! tip ""
    Ignore this message, simply hit your `Test` keybind and continue onto this.

<img src="/img/konami/iidx/25_cannonballers/5.webp">

!!! tip ""
    Hit the `Test` keybinding again to initialize the backup data, a message will pop up stating it's been initialized.

<img src="/img/konami/iidx/25_cannonballers/6.webp">

!!! tip ""
    Lastly, you'll run into this error message as well, let's work on eliminating these messages. Let the game run for a bit until the monitor check is complete and you should be taken to the service menu pictured below.

<img src="/img/konami/iidx/25_cannonballers/7.webp">

!!! tip ""
    Start by navigating up to `CLOCK` and entering that menu.

<img src="/img/konami/iidx/25_cannonballers/8.webp">

!!! tip ""
    Simply hit save and exit and leave, the clock will be saved. Then, back in the service menu, go up to `GAME OPTIONS`

<img src="/img/konami/iidx/25_cannonballers/9.webp">

!!! tip ""
    Once inside that menu, navigate your way up to `DEFINITION TYPE` and choose either `HD` or `HD*` depending on your preferences, both run the game at 720p but have a timing difference addressed on the FAQ page. It might be worth noting that the `HD*` option is no longer present as of beatmania IIDX 26 ROOTAGE.

<img src="/img/konami/iidx/25_cannonballers/10.webp">

!!! tip ""
    The game will then count down asking you to confirm the selection before reverting, just hit `YES` assuming it loaded just fine on your computer. Then, exit out of that menu and head to `NETWORK OPTIONS` from back inside the service menu.

<img src="/img/konami/iidx/25_cannonballers/11.webp">

!!! tip ""
    From here, we will need to set a shop name to play, so select the `SHOP NAME SETTING` option. Once inside, name your shop whatever you desire! For the purpose of the guide, we named it `Guide` but highly encourage fun and/or lazy names. Once that's done go to `EXIT` and then `SAVE AND EXIT` inside of `NETWORK OPTIONS` once you've chosen your desired name, as pictured below.

<img src="/img/konami/iidx/25_cannonballers/12.webp">

<img src="/img/konami/iidx/25_cannonballers/13.webp">

!!! tip ""
    You're all done! From the service menu select `GAME MODE` and the game should load ready to be played! Have fun!

!!! warning "Have any other errors?"
    Check out the [Troubleshooting](troubleshooting.md) section and [Error Code](/errorcodes/konami.md) section to resolve any issues not seen in this guide to greater depth.