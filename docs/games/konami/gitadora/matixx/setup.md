<img class="header-logo" src="/img/konami/gitadora/matixx/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

### Getting Started.

!!! tip ""
    Before we even touch the game, let's fiddle with our audio settings to minimize any potential audio issues on startup. In Windows, go to `Playback Devices` and then right click on your default device and go to `Properties`. From there, hit the `Advanced` tab and set your `Default Format` to `44100 Hz` and check both of the options inside `Exclusive Mode` as pictured.

<img src="/img/common/audio_24_441.webp">

!!! tip ""
    Once that's done, it's time to work on setting up your data.

    After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, the first thing to do is put your desired 64-bit tools inside the game's `contents` folder, and to create a `.bat` file. Pictured below is what your folder should look like, feel free to name your `.bat` file whatever you desire, for the sake of convenience we've named ours `gamestart.bat`.

<img src="/img/konami/gitadora/matixx/1.webp">

### Configuring Your Tools

!!! tip ""
    Now that you have your files ready, open up your `.bat` file in your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/)) and edit it with your desired parameters, for the purpose of this guide we will demonstrate both a local network configuration and an online example below for both launching the guitar version and drum version using SpiceTools, skip to whichever you're in need of accordingly and please keep in mind you can add whatever additional parameters you desire.

!!! warning "If you're not using SpiceTools:"
    The overall structure of your .bat file will differ from the guide, namely the initialization of SpiceTools won't be present and potential parameters may differ. As stated above, make sure to check the documentation of your tools to ensure you're using the correct parameters for your needs.

### Configuring for a Local Network

!!! tip ""
    **FOR GUITAR**

    For our guitar local network configuration example, on a single line in the `.bat` file we're going to type `spice64.exe -e prop\eamuse-config2.xml -2ch -ea -w` and save the file. 

    What do these different parameters do?
    - `-e` sets a custom path for the eamuse config to boot the proper one (in this case, guitar via `prop\eamuse-config2.xml`)
    - `-2ch` enables 2-channel audio for GITADORA
    - `-ea` enables an integrated e-amusement server within SpiceTools.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/konami/gitadora/matixx/2g.webp">

!!! tip ""
    **FOR DRUM**

    For our drum local network configuration example, on a single line in the `.bat` file we're going to type `spice64.exe -2ch -ea -w` and save the file. 

    What do these different parameters do?
    - `-2ch` enables 2-channel audio for GITADORA
    - `-ea` enables an integrated e-amusement server within SpiceTools.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/konami/gitadora/matixx/2d.webp">

### Configuring for an Online Network

!!! tip ""
    **FOR GUITAR**

    For our guitar online network example we're simply doing the above but with different parameters! On our single line, we're going to type `spice64.exe -e prop\eamuse-config2.xml -2ch -p XXXXXXXXXXXXXXXXXXXX -url http://yoururlhere.com/ -w` and save the file. 

    What do these different parameters do? 

    - `-e` sets a custom path for the eamuse config to boot the proper one (in this case, guitar via `prop\eamuse-config2.xml`)
    - `-2ch` enables 2-channel audio for GITADORA
    - `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
    - `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/konami/gitadora/matixx/3g.webp">

!!! tip ""
    **FOR DRUM**

    For our drum online network example we're simply doing the above but with different parameters! On our single line, we're going to type `spice64.exe -2ch -p XXXXXXXXXXXXXXXXXXXX -url http://yoururlhere.com/ -w` and save the file. 

    What do these different parameters do? 

    - `-2ch` enables 2-channel audio for GITADORA
    - `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
    - `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
    - `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

    Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/konami/gitadora/matixx/3d.webp">

!!! tip ""
    One final note, since you're playing on a network, you will have one additional step of setting up your card file within your chosen tools, make sure to check your server's information on how to setup a card file.

### Final Steps and Setting up the Game

!!! tip ""
    The last steps you'll have to do with your chosen tools is simply setting up your desired keybinds! Make sure you setup the `Test` keybind as it will be critical for setting up the game. Once you've done that, launch your game for the first time by double clicking the `.bat` you setup and the game should load.

    If it's your first time running the game, you'll immediately be greeted with this screen, oh no!

<img src="/img/konami/gitadora/matixx/4.webp">

!!! tip ""
    This is normal, simply hit your `Test` keybind and continue on to this.

<img src="/img/konami/gitadora/matixx/5.webp">

!!! tip ""
    From here, we will need to set a shop name to play, so select the `GAME OPTIONS` option.

<img src="/img/konami/gitadora/matixx/6.webp">

!!! tip "" 
    Then, select `SHOP SETTINGS`.

<img src="/img/konami/gitadora/matixx/7.webp">

!!! tip "" 
    Once inside, select `SHOP NAME SETTINGS` and name your shop whatever you desire! For the purpose of the guide, we named it `Guide` but highly encourage fun and/or lazy names. Once that's done, go down to `PREFECTURE` and set it to whatever you desire as well. Finally, go to `SAVE AND EXIT` to get back to the main menu.

<img src="/img/konami/gitadora/matixx/8.webp">

!!! tip ""
    The last menu we'll go inside from the service menu is the clock menu. Go inside `CLOCK` and simply set the clock by hitting `SAVE AND EXIT` as pictured below.

<img src="/img/konami/gitadora/matixx/9.webp">

!!! tip ""
    You're all done! From the service menu select `GAME MODE` and the game should load ready to be played! Have fun!

!!! warning "Have any other errors?"
    Check out the [Troubleshooting](troubleshooting.md) section and [Error Code](/errorcodes/konami.md) section to resolve any issues not seen in this guide to greater depth.
