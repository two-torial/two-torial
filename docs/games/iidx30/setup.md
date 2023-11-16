# beatmania IIDX 30 RESIDENT

<img src="/img/iidx30/resident.png">

!!! note "Author Note:"
	
	For hex edits: Go to [mon's Bemani Patcher](https://mon.im/bemanipatcher/resident.html)

	For lightning mode specifics: they are found [here](lightning.md)

!!! danger "Warning:"
	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.

	If you obtained data from a torrent file, make sure you're not seeding the data before proceeding as well.

	This guide will use [spice2x](https://spice2x.github.io/) which is a fork of SpiceTools that gets regular updates and will be needed to get the game running.

### Getting Started

!!! tip ""
	Before we even touch the game, let's fiddle with our audio settings to minimize any potential crashing on startup. In Windows, go to `Playback Devices` and then right click on your default device and go to `Properties`. From there, hit the `Advanced` tab and set your `Default Format` to `44100 Hz` and check both of the options inside `Exclusive Mode` as pictured.

<img src="/img/gen/441.png">

!!! tip ""
	Once that's done, it's time to work on setting up your data.

	After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, put your `spice2x` **64-bit** tools inside the game's `contents` folder. Pictured below is what your folder should look like.

<img src="/img/iidx31/1.png">

### Configuring for an Online Network

!!! tip ""
	Now that you have your files ready, open up `spicecfg.exe` and head to the `Options` where we'll set our desired parameters.
	
	On the `Service URL: -url` parameter, we're going to input our chosen network URL like so: `http://yoururlhere.com/`

	To go alongside this, we'll also be inputting into the `PCBID: -p` parameter, the PCBID given to us from our network, like so: `XXXXXXXXXXXXXXXXXXXX`

	Lastly, we'll click on the `Windowed Mode: -w` parameter.

	What do these different parameters do?

	- `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
	- `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
	- `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

	Pictured below, the selected options inside the `Options` tab in `spicecfg.exe`.

<img src="/img/iidx31/cfg_on.png">

!!! tip ""
	One final note, since you're playing on a network, you will have one additional step of setting up your card file if you do not already have one.
	For this, simply head to the `Cards` tab and press `Generate`.

	I highly recommend that you copy your `Card Number`, create a `.txt`, paste the `Card Number` and store the `.txt` file somewhere safe where you won't lose it. It doesn't matter how you name it. **For the purpose of this guide, I've chosen the root of my `D:\` drive for easy access and called the text file `guidecard.txt`.**

	Next, click on the three dots (`...`) next to `Card Path` and locate your card text file. Keep in mind that `Player 1` refers to 1P **side** and will log you in on the **left**, Player 2 does the opposite respectively.
	If you have done everything correctly, it should look like this:

<img src="/img/iidx31/card.png">

### Audio & Keybinds

!!! tip ""
	Before we go over the keybinds, we'll change our `IIDX Sound Output Device` to `WASAPI`. This has (from my experience) the highest chance of working. If it doesn't for you, try using `ASIO`. It really comes down to your own hardware setup. 
	
	If you're still having issues, feel free to join our [Discord server](https://discord.gg/yAtdhvee79) and ask away in the troubleshooting section as this could be something very specific. Keep in mind that if you're using `WASAPI`, IIDX will go into WASAPI exclusive mode which means that only IIDX will output it's audio and nothing else [(this can be changed with a hex edit if you'd like).](problems.md#when-i-run-this-game-all-other-background-audio-is-gone-whats-going-on)

	Below is an example of how it looks like using `WASAPI`.

<img src="/img/iidx31/wasapi.png">

!!! tip ""
	The last steps you'll have to do is simply setting up your desired keybinds inside the `Buttons` and `Analogs` tabs. If you'd like an example, I've shown my keybindings below on a Keyboard from the 1P side. Make sure you setup the `Test` keybind as it will be critical for setting up the game. 

<img src="/img/iidx31/iidx_bind.png">

### Disabling Cameras

!!! tip ""
	Go back to the `Options` tab and make sure to enable `IIDX Disable Cameras` or else you will encounter an error and you will be unable to proceed otherwise.

<img src="/img/iidx31/disable_cam.png">

### Setting up the game

!!! tip ""
	Finally we're ready to start the game. Go ahead and start `spice64.exe`.

	If it's your first time running the game, you'll immediately be greeted with this screen.

<img src="/img/iidx31/2.png">

!!! tip ""
	Hit the `Test` keybinding to initialize the backup data, a message will pop up stating it's been initialized.

<img src="/img/iidx31/3.png">

!!! tip ""
	You'll also run into this error message as well. Let the game run for a bit until the monitor check is complete and you should be taken to the service menu pictured below.

<img src="/img/iidx31/4.png">

!!! tip ""
	Start by navigating up to `CLOCK` and entering that menu.

<img src="/img/iidx31/5.png">

!!! tip ""
	Simply hit save and exit and leave, the clock will be saved. Then, back in the service menu head to `NETWORK OPTIONS` from back inside the service menu.

<img src="/img/iidx25/11.png">

!!! tip ""
	The final thing we need to set is here inside `NETWORK OPTIONS`, we will need to set a shop name to play, so select the `SHOP NAME SETTING` option. Once inside, name your shop to whatever you'd like. For the purpose of the guide, we named it `Guide`. Once that's done go to `EXIT` and then `SAVE AND EXIT` inside of `NETWORK OPTIONS` once you've chosen your desired name, as pictured below.

<img src="/img/iidx25/12.png">

<img src="/img/iidx25/13.png">

!!! tip ""
	You're all done! From the service menu select `GAME MODE` and the game should load ready to be played! Have fun!

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section and [Error Code](/errorcodes/) section to resolve any issues not seen in this guide to greater depth.

	Lightning Mode specifics can be found: [here](lightning.md#lightning-specific-troubleshooting)
