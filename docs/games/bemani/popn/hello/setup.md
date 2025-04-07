# HELLO Pop'n

!!! danger "Warning"
	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.

	If you obtained data from a torrent file, make sure you're not seeding the data before proceeding as well.

	Lastly, for demonstrative purposes, this guide uses SpiceTools, you should consult appropriate documentation and requirements of your desired tools as the setup process is likely to be extremely similar.

### Getting Started

!!! tip ""

    This game still uses DirectSound so we can skip audio related setup needed for other games. After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, put your desired 32-bit tools inside the game's `contents` folder. Pictured below is what your folder should look like.

<img src="/img/popn/hello1.png">


### Configuring Your Tools

!!! tip ""

	Now that you have your files ready, open up `spicecfg.exe` and head to the `Options` tab. Here you can configure all of the various options that SpiceTools has, but for the purpose of this guide we'll demonstrate how to set up a local server and an online server. You can skip over the parts that you don't need, and feel free to set any other options that you might like.

!!! warning "If you're not using SpiceTools:"

	It's most likely that your toolkit doesn't have an options interface, so you'll have to create a `.bat` file. Consult the appropriate documentation for this as this isn't covered in this guide.

### Configuring for a Local Network

!!! tip ""

	For our local network configuration example, in the `Options` tab enable the following options: `E-Amusement Emulation: -ea` and `Windowed Mode: -w`.

	What do these different parameters do?

	- `-ea` enables an integrated e-amusement server within SpiceTools.
	- `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to disable `-w` to run the game fullscreen once you're done setting up!

	Pictured below, the selected options in `spicecfg.exe`.

<img src="/img/popn/hello2.png">

### Configuring for an Online Network

!!! tip ""

	For our online network example we're simply doing the above but with different options! 
    
    We're going to use the option `PCBID: -pcbid` for our PCBID, with `XXXXXXXXXXXXXXXXXXXX` as the value.  
    For the network URL we're going to use the option `Service URL: -url`, with `http://yoururlhere.com/` as the value.  
    We'll also enable windowed mode by enabling the option `Windowed Mode: -w`.

	What do these different parameters do?

	- `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
	- `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
	- `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to disable `-w` to run the game fullscreen once you're done setting up!

	Pictured below, the enabled options in `spicecfg.exe`.

<img src="/img/popn/hello3.png">

!!! tip ""

	One final note, since you're playing on a network, you will have one additional step of setting up your card file within your chosen tools, make sure to check your server's information on how to setup a card file.

### Configuring Keybinds

!!! tip ""
    
    While we're still in `spicecfg.exe`, why not set up the keybinds? To do this you'll have to head on over to the `Buttons` tab. Here you simply click `Bind` and press the button on your controller (or keyboard). Below are my keybinds for a keyboard. Notice that I've also bound the `Service`, `Test` and `Coin Mech` buttons to my keyboard. This might come in handy but shouldn't be necessary to play the game.
    
<img src="/img/popn/hello4.png">

### Final Steps and Setting up the Game

!!! tip ""
	Boot the game by double-clicking `spice.exe`.
    
    The boot sequence may have a very light blue background. Press any overlay hotkey (F12, for example) to make it display normally.

<img src="/img/popn/helloboot1.png">
<img src="/img/popn/helloboot2.png">

!!! tip ""
    Simply follow the on-screen text in the bottom left corner to continue. On the first boot, the game may tell you to press `Test`, and then `Service`.
    
    HELLO Pop'n has the ability to run offline, so the network error can be safely ignored.

	You're all done! The game takes a couple of seconds to load all of the data.

!!! warning "Have any other errors?"
	Check out the [Troubleshooting](troubleshooting.md) section and [Error Code](/errorcodes/bemani.md) section to resolve any issues not seen in this guide to greater depth.
