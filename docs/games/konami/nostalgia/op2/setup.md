<img class="header-logo" src="/img/konami/nostalgia/op2/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Getting Started

!!! tip ""
    Before we even touch the game, let's fiddle with our audio settings to minimize any potential audio issues on startup. In Windows, go to `Playback Devices` and then right click on your default device and go to `Properties`. From there, hit the `Advanced` tab and set your `Default Format` to `44100 Hz` and check both of the options inside `Exclusive Mode` as pictured.

<img src="/img/common/audio_24_441.webp">

!!! tip ""
    Once that's done, it's time to work on setting up your data.

    After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, put your desired 64-bit tools inside the game's main folder and to create a `.bat` file. Pictured below is what your folder should look like, feel free to name your `.bat` file whatever you desire, for the sake of convenience we've named ours `gamestart.bat`.

<img src="/img/konami/nostalgia/common/8.webp">

## Configuring Your Tools

!!! tip ""
    Now that you have your files ready, open up your `.bat` file in your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/)) and edit it with your desired parameters, for the purpose of this guide we will demonstrate ONLY a local network configuration with SpiceTools. Why only local? Because none of the most typical places currently support Nostalgia. Regardless, please keep in mind you can add whatever additional parameters you desire.

!!! warning "If you're not using SpiceTools:"
    The overall structure of your .bat file will differ from the guide, namely the initialization of SpiceTools won't be present and potential parameters may differ. As stated above, make sure to check the documentation of your tools to ensure you're using the correct parameters for your needs.

## Configuring for a Local Network

!!! tip ""
    For our local network configuration example, on a single line in the `.bat` file we're going to type `spice64.exe -ea -w` and save the file. 

    What do these different parameters do?

    - `-ea` enables an integrated e-amusement server within SpiceTools.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

## Configuring for an Online Network

!!! tip ""
    For our online network example we're simply doing the above but with different parameters! On our single line, we're going to type `spice64.exe -p XXXXXXXXXXXXXXXXXXXX -url http://yoururlhere.com/ -w` and save the file. 

    What do these different parameters do? 

    - `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
    - `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

## Final Steps and Setting up the Game

!!! tip ""
    The last steps you'll have to do with your chosen tools is simply setting up your desired keybinds! Make sure you setup the `Test` keybind as it will be critical for setting up the game. Once you've done that, launch your game for the first time by double clicking the `.bat` you setup and the game should load.

    If it's your first time running the game, you should be automatically forced into the service menu with lots of scary flashing notifications as pictured below, let's work through them.

<img src="/img/konami/nostalgia/common/2.webp">

!!! tip ""
    Interestingly, only the red flashing ones really take any effort to deal with. You can start by entering and exiting the following menus: `SOUND OPTIONS`, `GAME OPTIONS`, `COIN OPTIONS`, `ECOMODE OPTIONS`, and `NETWORK OPTIONS`. 

    Once you've done that, enter `CLOCK` and set the clock by hitting `SAVE AND EXIT` as pictured below.

<img src="/img/konami/nostalgia/common/3.webp">

!!! tip ""
    The final menu we must deal with is `VIRTUAL COIN`, enter the menu and select `OPERATION SETTINGS` as seen below.

<img src="/img/konami/nostalgia/common/4.webp">

!!! tip ""
    Once inside this menu, we'll need to deal with all 4 blinking options, let's start by entering the `TAX RATE SETTING` menu, shown below.

<img src="/img/konami/nostalgia/common/5.webp">

!!! tip ""
    Set the tax rate by simply selecting `SAVE AND EXIT` while will take us back into the `OPERATING SETTINGS`. Pictured below is the `TAX RATE SETTING` menu.

<img src="/img/konami/nostalgia/common/6.webp">

!!! tip ""
    Once back inside the `TAX RATE SETTING` menu, we must deal with the three blinking `PATTERN` options. Doing so is effortless, simply enter all three menus one by one and hit `SAVE AND EXIT` just as we did for the `TAX RATE SETTING` in the previous step. Pictured below is the inside of `PATTERN 1`. 

<img src="/img/konami/nostalgia/common/6.webp">

!!! tip ""
    After saving and exiting all three `PATTERN` options, you're all done! From the service menu select `GAME MODE` and the game should load ready to be played! Have fun!

!!! warning "Have any other errors?"
    Check out the [Troubleshooting](troubleshooting.md) section and [Error Code](/errorcodes/konami.md) section to resolve any issues not seen in this guide to greater depth.