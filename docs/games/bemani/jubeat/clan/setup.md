<img class="header-logo" src="/img/bemani/jubeat/clan/logo.png">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Getting Started

!!! tip ""
	After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, put your desired 32-bit tools inside the game's main folder and to create a `.bat` file. Pictured below is what your folder should look like, feel free to name your `.bat` file whatever you desire, for the sake of convenience we've named ours `gamestart.bat`. 

<img src="/img/bemani/jubeat/clan/1.png">

## Configuring Your Tools

!!! tip ""
	Now that you have your files ready, open up your `.bat` file in your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/)) and edit it with your desired parameters, for the purpose of this guide we will demonstrate both a local network configuration and an online example below with SpiceTools, skip to whichever you're in need of accordingly and please keep in mind you can add whatever additional parameters you desire.

!!! warning "If you're not using SpiceTools:"
	The overall structure of your .bat file will differ from the guide, namely the initialization of SpiceTools won't be present and potential parameters may differ. As stated above, make sure to check the documentation of your tools to ensure you're using the correct parameters for your needs.

## Configuring for a Local Network

!!! tip ""
	For our local network configuration example, on a single line in the `.bat` file we're going to type `spice.exe -ea` and save the file. 

	What do these different parameters do?

	- `-ea` enables an integrated e-amusement server within SpiceTools.

	Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/bemani/jubeat/clan/2.png">

## Configuring for an Online Network

!!! tip ""
	For our online network example we're simply doing the above but with different parameters! On our single line, we're going to type `spice.exe -p XXXXXXXXXXXXXXXXXXXX -url http://yoururlhere.com/` and save the file. 

	What do these different parameters do? 

	- `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
	- `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.

	Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/bemani/jubeat/clan/3.png">

!!! tip ""
	One final note, since you're playing on a network, you will have one additional step of setting up your card file within your chosen tools, make sure to check your server's information on how to setup a card file.

## Final Steps and Setting up the Game

!!! tip ""
	The last steps you'll have to do with your chosen tools is simply setting up your desired keybinds! Make sure you setup the `Test` keybind as it will be critical for setting up the game. Once you've done that, launch your game for the first time by double clicking the `.bat` you setup and the game should load.

	If it's your first time running the game, you'll immediately be greeted with this screen (cropped to save your sanity with scrolling repeatedly on the page), oh no!

<img src="/img/bemani/jubeat/clan/5.png">

!!! tip ""
	This is okay, you can use your mouse or touchscreen to simply hit `TEST` to initialize the backup data, the game will prompt you to reboot, but let's save ourselves some time and instead go into the `GAME OPTIONS` menu instead, as shown below. If you rebooted, you will see a message telling you to set the "Shop Settings" which is what we're going to now do, as shown below.

<img src="/img/bemani/jubeat/clan/7.png">

!!! tip ""
	Enter the `GAME OPTIONS` menu and proceed to the `SHOP SETTINGS` menu.

<img src="/img/bemani/jubeat/clan/8.png">

!!! tip ""
	From here, we will need to set the `SHOP NAME SETTINGS`. This is a simple process, simply navigate using the controls in the menu to set any name you desire! For the purpose of the guide, we named it `Guide` but highly encourage fun and/or lazy names. Lastly, if you're not connected to an online network, you'll need to set the `SHOP AREA` as well, navigate to any option you prefer, they're all predefined so you can't get creative here, pictured below is what we set ours to.

<img src="/img/bemani/jubeat/clan/9.png">

!!! tip ""
	With that, you're all done! Simply exit the service menu or reboot then enjoy the game, have fun!

!!! warning "Have any other errors?"
	Check out the [Troubleshooting](troubleshooting.md) section and [Error Code](/errorcodes/bemani.md) section to resolve any issues not seen in this guide to greater depth.