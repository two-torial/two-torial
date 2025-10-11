<img class="header-logo" src="/img/konami/reflecbeat/reflesia/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Getting Started

!!! tip ""

    This game still uses DirectSound so we can skip audio related setup needed for other games. After downloading your data, the first thing to do is put your desired 32-bit tools inside the game's `contents` folder, and to create a `.bat` file. Pictured below is what your folder should look like, feel free to name your `.bat` file anything you desire, for the sake of convenience we've named ours `gamestart.bat`.

<img src="/img/konami/reflecbeat/reflesia/data.webp">


## Configuring Your Tools

!!! tip ""

    Now that you have your files ready, open up your `.bat` file in your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/)) and edit it with your desired parameters, for the purpose of this guide we will demonstrate both a local network configuration and an online example below with SpiceTools, skip to whichever you're in need of accordingly and please keep in mind you can add whatever additional parameters you desire.

!!! warning "If you're not using SpiceTools:"

    The overall structure of your .bat file will differ from the guide, namely the initialization of SpiceTools won't be present and potential parameters may differ. As stated above, make sure to check the documentation of your tools to ensure you're using the correct parameters for your needs.

## Configuring for a Local Network

!!! tip ""

    For our local network configuration example, on a single line in the `.bat` file we're going to type `spice.exe -ea -w` and save the file. 

    What do these different parameters do?

    - `-ea` enables an integrated e-amusement server within SpiceTools.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

## Configuring for an Online Network

!!! tip ""

    For our online network example we're simply doing the above but with different parameters! On our single line, we're going to type `spice.exe -p XXXXXXXXXXXXXXXXXXXX -url http://yoururlhere.com/ -w` and save the file. 

    What do these different parameters do? 

    - `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
    - `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

!!! tip ""

    One final note, since you're playing on a network, you will have one additional step of setting up your card file within your chosen tools, make sure to check your server's information on how to setup a card file.

## Final Steps and Setting up the Game

!!! tip ""

    It's important to note before booting the game that Reflec Beat uses portrait mode and attempting to boot the game fullscreen in most landscape environments will result in a crash. To alleviate this, we must set our *main* monitor to portrait mode and be ready to rotate it! To do so, right click on your desktop and go into `Display Settings`, then simply set the orientation to `Portrait`.

    In the event that you do not have the means to run the game in portrait mode and cannot rotate your monitor, it is recommended you boot the game in windowed mode. In SpiceTools, simply add the windowed mode parameter, this parameter is `-w` and can be placed right after any other desired parameters chosen in our `gamestart.bat`

    As for the touch stuff, by default SpiceTools should detect your mouse just fine, you can use the `-s` parameter to have your cursor show at all times above the game window. For touchscreen monitors, it's a bit tricky to write something encompassing them all. Many should be detected automatically, however some may require adding the `-wintouch` parameter for support.

    With that, you're all done! The final step you'll have to do with your chosen tools is simply setting up your desired keybinds! Once you've done that, Boot the game with your `gamestart.bat` and the game should load and be ready to be enjoyed! Have fun!

## Troubleshooting

!!! warning "Have any other errors?"

    Check out the [Troubleshooting](troubleshooting.md) and [Error Code](/errorcodes/konami.md) sections to resolve any issues not seen in this guide.
