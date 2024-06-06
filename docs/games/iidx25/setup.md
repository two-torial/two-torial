# beatmania IIDX 25 CANNON BALLERS

<img src="/img/iidx25/cb.png">

!!! danger "Warning:"
	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.

	If you obtained data from a torrent file, make sure you're not seeding the data before proceeding as well.

	Lastly, for demonstrative purposes, this guide uses SpiceTools, you should consult appropriate documentation and requirements of your desired tools as the setup process is likely to be extremely similar.


### Getting Started

!!! tip ""
	Before we even touch the game, let's fiddle with our audio settings to minimize any potential crashing on startup. In Windows, go to `Playback Devices` and then right click on your default device and go to `Properties`. From there, hit the `Advanced` tab and set your `Default Format` to `44100 Hz` and check both of the options inside `Exclusive Mode` as pictured.

<img src="/img/gen/441.png">

!!! tip ""
	Once that's done, it's time to work on setting up your data.
	
	After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, put your desired **64-bit** tools inside the game's `contents` folder, and to create a `.bat` file. Pictured below is what your folder should look like, feel free to name your `.bat` file whatever you desire, for the sake of convenience we've named ours `gamestart.bat`.

<img src="/img/iidx25/1.png">

### Configuring Your Tools

!!! tip ""
	Now that you have your files ready, open up your `.bat` file in your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/)) and edit it with your desired parameters, for the purpose of this guide we will demonstrate both a local network configuration and an online example below with SpiceTools, skip to whichever you're in need of accordingly and please keep in mind you can add whatever additional parameters you desire.

!!! warning "If you're not using SpiceTools:"
	The overall structure of your .bat file will differ from the guide, namely the initialization of SpiceTools won't be present and potential parameters may differ. As stated above, make sure to check the documentation of your tools to ensure you're using the correct parameters for your needs.

### Configuring for a Local Network

!!! tip ""
	For our local network configuration example, on a single line in the `.bat` file we're going to type `spice64.exe -ea -w` and save the file. 

	What do these different parameters do?

	- `-ea` enables an integrated e-amusement server within SpiceTools.
	- `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

	Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/iidx25/2.png">

### Configuring for an Online Network

!!! tip ""
	For our online network example we're simply doing the above but with different parameters! On our single line, we're going to type `spice64.exe -p XXXXXXXXXXXXXXXXXXXX -url http://yoururlhere.com/ -w` and save the file. 

	What do these different parameters do? 

	- `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
	- `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
	- `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

	Pictured below, the contents of our `gamestart.bat` file in Notepad++.

<img src="/img/iidx25/3.png">

!!! tip ""
	One final note, since you're playing on a network, you will have one additional step of setting up your card file within your chosen tools, make sure to check your server's information on how to setup a card file.

### Final Steps and Setting up the Game

!!! tip ""
	The last steps you'll have to do with your chosen tools is simply setting up your desired keybinds! Make sure you setup the `Test` keybind as it will be critical for setting up the game. Once you've done that, launch your game for the first time by double clicking the `.bat` you setup and the game should load.

	If it's your first time running the game, you'll immediately be greeted with this screen, oh no!

<img src="/img/iidx25/4.png">

!!! tip ""
	Ignore this message, simply hit your `Test` keybind and continue onto this.

<img src="/img/iidx25/5.png">

!!! tip ""
	Hit the `Test` keybinding again to initialize the backup data, a message will pop up stating it's been initialized.

<img src="/img/iidx25/6.png">

!!! tip ""
	Lastly, you'll run into this error message as well, let's work on eliminating these messages. Let the game run for a bit until the monitor check is complete and you should be taken to the service menu pictured below.

<img src="/img/iidx25/7.png">

!!! tip ""
	Start by navigating up to `CLOCK` and entering that menu.

<img src="/img/iidx25/8.png">

!!! tip ""
	Simply hit save and exit and leave, the clock will be saved. Then, back in the service menu, go up to `GAME OPTIONS`

<img src="/img/iidx25/9.png">

!!! tip ""
	Once inside that menu, navigate your way up to `DEFINITION TYPE` and choose either `HD` or `HD*` depending on your preferences, both run the game at 720p but have a timing difference addressed on the FAQ page. It might be worth noting that the `HD*` option is no longer present as of beatmania IIDX 26 ROOTAGE.

<img src="/img/iidx25/10.png">

!!! tip ""
	The game will then count down asking you to confirm the selection before reverting, just hit `YES` assuming it loaded just fine on your computer. Then, exit out of that menu and head to `NETWORK OPTIONS` from back inside the service menu.

<img src="/img/iidx25/11.png">

!!! tip ""
	From here, we will need to set a shop name to play, so select the `SHOP NAME SETTING` option. Once inside, name your shop whatever you desire! For the purpose of the guide, we named it `Guide` but highly encourage fun and/or lazy names. Once that's done go to `EXIT` and then `SAVE AND EXIT` inside of `NETWORK OPTIONS` once you've chosen your desired name, as pictured below.

<img src="/img/iidx25/12.png">

<img src="/img/iidx25/13.png">

!!! tip ""
	You're all done! From the service menu select `GAME MODE` and the game should load ready to be played! Have fun!

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section and [Error Code](../../errorcodes.md) section to resolve any issues not seen in this guide to greater depth.
