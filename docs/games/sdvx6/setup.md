# SOUND VOLTEX EXCEED GEAR

<img src="/img/sdvx6/eg.png">

!!! note "Author Note:"

	Last updated: February 9th, 2024 (Currently using `2023042500`)
	
	For hex edits: Go to the [Türksigara Patcher](https://p.eagate.turksigara.net/)

	For Valkyrie Model specifics: they are found [here](valk.md)

!!! danger "Warning"

	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.

	This guide will use [spice2x](https://spice2x.github.io/) which is a fork of SpiceTools that gets regular updates and will be needed to get the game running.

	This guide will try to accommodate for both an Upgrade Kit and a whole file set.

### Getting Started

!!! tip ""

	Before we even touch the game, let's fiddle with our audio settings to minimize crashes on start up. In Windows, go to Playback Devices and then right click on your default device and go to Properties. From there, hit the Advanced tab and set your Default Format to 44100 Hz and check both of the options inside Exclusive Mode as pictured.

<img src="/img/gen/441.png">

!!! tip ""
	Once that's done, it's time to work on setting up your data.

	After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, if that's the case, uncheck it from the main folder in the Windows Properties tab if so. Then, put your spice2x 64-bit tools inside the game's contents folder. Pictured below is what your folder should look like.

<img src="/img/sdvx6/1.png">

!!! tip ""
	Why does this look different than the usual? This installation includes a `modules` folder that Spice automatically detects, keeping things clean and simple. If your version of the game doesn't have this, it probably has the `contents` folder populated with many different dll files such as the main `soundvoltex.dll`. Below is an example with the populated `contents` folder.

<img src="/img/sdvx6/1a.png">

!!! info "If you have gotten a complete data set, you are done and can head over to [Configuring for a Network](setup.md#configuring-for-a-network)"

### Merging Current Data with New Data

!!! tip ""
	In this case, I'll be using `KFC-2021083100` as my old data and `KFC-2023042500` as my new data. Both can be replaced with what ever you have at hand or would like to update to. Just make sure that it is compatible with your current version, for example in my case, it's conveniently named `KFC-2021083100-to-KFC-2023042500`.

!!! tip ""
	Next, unpack the contents of the archive and drag & drop all files into your `contents` folder of `KFC-2021083100`. Make sure to confirm if it prompts you to replace files in the destination, this is normal. The folders in which files are getting replaced should look like this:

<img src="/img/sdvx6/2.png">

!!! tip ""
	Lastly, head over to `\contents\prop` and open up `ea3-config.xml` with a text editor of your choice. I'll be using [Notepad++](https://notepad-plus-plus.org/) for that. In this example, I'll use `2023101800`.

	Look for these lines which should be at the top:
	```
    <soft>
        <model __type="str">KFC</model>
        <dest __type="str">J</dest>
        <spec __type="str">F</spec>
        <rev __type="str">A</rev>
        <ext __type="str">2023042500</ext>
    </soft>
	```
	If `<ext __type="str">2023042500</ext>` already has `2023042500` then you're good to go. If it has anything other than that, change it to `2023042500`.
	This is the games datacode, basically telling the game what version it is on.

!!! info "If you'd like to enable the Valkyrie Model mode, which is `off` by default or want to change the game language to English, head over to [Valkyrie Model](valk.md#setting-up-valkyrie-model-subscreen-120fps)"

### Configuring for a Network

!!! danger "You can decide between the two, whether you want to play on an online network or use a local e-amuse emulator. ***Do not*** use both. Only choose one."

??? tip "Online Network"
	Now that you have your files ready, open up `spicecfg.exe` and head to the `Options` where we'll set our desired parameters.
	
	On the `Service URL: -url` parameter, we're going to input our chosen network URL like so: `http://yoururlhere.com/`

	To go alongside this, we'll also be inputting into the `PCBID: -p` parameter, the PCBID given to us from our network, like so: `XXXXXXXXXXXXXXXXXXXX`

	Lastly, we'll click on the `Windowed Mode: -w` parameter.

	What do these different parameters do?

	- `-url` allows you to specify a custom service URL to connect with, simply replace `http://yoururlhere.com/` with your chosen network's URL.
	- `-p` takes your PCBID on your network of choice, simply replace `XXXXXXXXXXXXXXXXXXXX` with your PCBID.
	- `-w` will boot the game in windowed mode which will ease our initial setup and testing later, make sure to remove `-w` to run the game fullscreen once you're done setting up!

	Pictured below, the selected options inside the `Options` tab in `spicecfg.exe`.

	<img src="/img/sdvx6/cfg_on.png">

	One final note, since you're playing on a network, you will have one additional step of setting up your card file if you do not already have one.
	For this, simply head to the `Cards` tab and press `Generate`.

	I highly recommend that you copy your `Card Number`, create a `.txt`, paste the `Card Number` and store the `.txt` file somewhere safe where you won't lose it. It doesn't matter what you name it. **For the purpose of this guide, I've chosen the root of my `D:\` drive for easy access and called the text file `guidecard.txt`.**

	Next, click on the three dots (`...`) next to `Card Path` and locate your card text file. If you have done everything correctly, it should look like this:

	<img src="/img/sdvx6/card.png">

??? tip "e-amuse Emulator (Asphyxia CORE)"
	We've written a guide on how to setup ```Asphyxia CORE``` [which you can access here.](/extras/asphyxia)

	When you're done setting up ```Asphyxia CORE``` come back here and continue with the guide.

### Audio & Keybinds

!!! note "This guide will utilize ```WASAPI Shared``` because it is the easiest to set up in most cases. There are more methods to use which you can read about [here.](/extras/audio/) The next best method we recommend is using ```FlexASIO```. You can read more about it on what it does and how to set it up [here.](/extras/streamaudio/#option-4-flexasio)"

!!! tip ""
	Before we go over the keybinds, I'd like to mention that Sound Voltex Exceed Gear by default, uses `WASAPI`. This has (from my experience) the highest chance of working.

	If you're having issues, feel free to join our [Discord server](https://discord.gg/yAtdhvee79) and ask away in the troubleshooting section as this could be something very specific. Keep in mind that if you're using `WASAPI`, SDVX will go into WASAPI exclusive mode which means that only SDVX will output it's audio and nothing else [(this can be changed with a hex edit if you'd like).](problems.md#when-i-run-this-game-all-other-background-audio-is-gone-whats-going-on)

!!! tip ""
	The last steps you'll have to do is simply setting up your desired keybinds inside the `Buttons` and `Analogs` tabs. If you'd like an example, I've shown my keybindings below on a Keyboard. Make sure you setup the `Test` keybind as it will be critical for setting up the game. 

<img src="/img/sdvx6/sdvx_bind.png">

### Disabling Cameras

!!! tip ""
	Go back to the `Options` tab and make sure to enable `SDVX Disable Cameras` or else you will encounter an error (or potentially a crash) and you will be unable to proceed otherwise.

<img src="/img/sdvx6/sdvx_disable_cam.png">

### Setting up the game

!!! tip ""
	It's important to note before booting the game that Sound Voltex uses portrait mode and attempting to boot the game fullscreen in most landscape environments will result in a crash. To alleviate this, we must set our *main* monitor to portrait mode and be ready to rotate it. To do so, right click on your desktop and go into `Display Settings`, then simply set the orientation to `Portrait` as pictured.

<img src="/img/sdvx6/port_mode.png">

!!! tip ""
	In the event that you do not have the means to run the game in portrait mode and cannot rotate your monitor, it is recommended you boot the game in windowed mode.

!!! tip ""
	Finally we're ready to start the game. Go ahead and start `spice64.exe`.

	To not clutter everything with a lot of blackscreens, I've cut the images to only show what is important.

	If it's your first time running the game, you'll immediately be greeted with this screen.

<img src="/img/sdvx6/3.png">

!!! tip ""
	Hit the `Test` keybinding to start calibrating your analogs. You'll be instructed by the game on where to navigate inside the menu.

<img src="/img/sdvx6/4.png">

!!! tip ""
	Select `I/O CHECK` and hit your `Start` button.

<img src="/img/sdvx6/5.png">

!!! tip ""
	Navigate to `CALIBRATION SETTINGS` with your designated A and B buttons and hit `Start`

<img src="/img/sdvx6/6.png">

!!! tip ""
	In here, you're instructed to turn your left knob **3 whole rotations to the *left.*** If you're on keyboard simply hold your `VOL-L Left` button.

<img src="/img/sdvx6/7.png">

!!! tip ""
	When you have done that, the `COUNT = X` (X being the value at which the knob stopped) should turn to `COUNT = OK`. Press your `Start` button.

	Now repeat the same steps but with your right knob. Once you're finished, select `SAVE AND EXIT`.

!!! tip ""
	You're all done! From the service menu select `GAME MODE` and the game should load ready to be played! Have fun!

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section and [Error Code](/errorcodes/) section to resolve any issues not seen in this guide to greater depth.

	Valkyrie Model specifics can be found: [here](valk.md)