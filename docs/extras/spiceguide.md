# SpiceTools Usage, Parameters, and Functionality

- **Last Update: March 14th, 2020.**

- **Version Covered: March 3rd, 2020.**

!!! warning "Before reading:"
	This section contains a myriad of information regarding SpiceTools including the games supported, various parameters, and its functionality. Feel free to consult this section anytime you are confused or simply want to learn more. However, SpiceTools is consistently updated and updates to this section may fall behind, to combat this, the above information in bold will cover the latest revision of SpiceTools this guide covers and along the latest update to this section.

### What is SpiceTools?

!!! tip ""
	SpiceTools is a toolkit allowing users to play several Konami games on their PC, typically of the arcade variety with the focus being on BEMANI games. The idea behind SpiceTools is to provide a simple to use toolkit that consists of just the executable and its configuration, allowing users to have minimal interaction with game files and thus minimizing user error.

### Why SpiceTools

!!! tip ""
	The reason this guide utilizes SpiceTools exclusively is because it's capable of running games without the user ever touching a single file, minimizes any potential user error. On top of this, SpiceTools has a few exclusive features that benefit new and experienced players alike. The combination of simplicity and advanced features makes it an ideal choice.

### SpiceOverlay

!!! tip ""
	One of the newest features SpiceTools has is an included overlay called SpiceOverlay, it contains a number of useful options such as a patch manager to enable/disable hex edits on the fly, and virtual keypads, its keybinds are as follows below:

	``F5 - Keypad P1``
	``F6 - Keypad P2``
	``F7 - Card Manager``
	``F8 - Log``
	``F9 - Control``
	``F10 - Patch Manager``
	``F12 - Overlay/FPS toggle``

### SpiceOptions

!!! tip ""
	SpiceTools now features an options tab that allows you to set parameters inside the game with the ability to restart the game after you make your desired changes.

	<img src="/img/spice/options.png">

	Note that the purple highlighted options are tied to the specific game you are running, you do not need to check them in most cases as oftentimes they are loaded automatically for most setups.

### SpiceCompanion

!!! tip ""
	SpiceTools also has a companion app on android called [SpiceCompanion](https://play.google.com/store/apps/details?id=spicedev.spicecompanion) this guide won't go over all of its features and functionalities, perhaps a separate page would be more appropriate. Just note it shares many similarities with SpiceOverlay and is yet another powerful tool to aid in playing these arcade games. One fan favorite feature is the ability to utilize your phone as a card reader, allowing friends to easily card-in and play alongside you.

### Supported Games

!!! tip ""
	SpiceTools at the time of writing supports the following games, if no specific denotation is listed, assume all recent versions of said game):

	- beatmania IIDX (Tricoro and newer)
	- Sound Voltex 
	- jubeat (knit and newer)
	- Reflec Beat
	- Dance Evolution Arcade
	- DanceDanceRevolution
	- Beatstream
	- Road Fighters 3D
	- Pop'n Music
	- MÚSECA
	- Metal Gear Arcade
	- GITADORA (XG3 and newer)
	- NOSTALGIA
	- BISHI BASHI CHANNEL
	- QUIZ MAGIC ACADEMY
	- MAHJONG FIGHT CLUB
	- FutureTomTom
	- SCOTTO
	- HELLO! Pop'n Music
	- LovePlus
	- DANCERUSH STARDOM
	- Steel Chronicle
	- Tenkaichi Shogikai
	- Otoca D'or
	- Winning Eleven 2012

### Coins

!!! tip ""
	There's a coin emulation working for most games, simply press F1 to insert a single coin.

	Some games have an additional/different coin key.

### Readers

!!! tip ""
	If you have an original Wavepass reader and have it connected to a COM port on your computer, SpiceTools should be able to use it. It was being created and tested with the newer readers also used in the newer Pop'n Music games.
	Example for one reader on COM3: -reader COM3
	Example for two readers for P1/2 on COM3 and COM4: -reader COM3 -reader COM4
	Example for one reader with P1/2 toggle on NumLock: -togglereader COM3

### SpiceTools API

!!! tip ""
	SpiceTools has its own API with a custom protocol. The main goals were simplicity, portability and extensibility, so TCP/JSON was chosen, allowing fast access over network.

	It optionally supports passwords/encryption and its response time on LAN was tested to be below 1ms (as long as extended API logging isn't enabled manually).

	For details and how to use it, check out README.md in the included source. Additionally, python and dart libraries are provided for easy communication.

	Key features are card/coin insertions, read/write access for keypads/analogs/buttons/lights, status information and memory read/write via raw addresses and signatures.

### Bemanitools 5 API Compatibility

!!! tip ""
	There is basic BT5 API integration as of 03/13/2018.

	This feature can be enabled with `-bt5api` and currently makes use of eamio.dll only.
	Currently, this can be used for applications such as the popular NFCeamuse app which can be found elsewhere.

### Keybindings/Analogs

!!! tip ""
	As of beta, buttons can be bound via either RawInput (the default) or "Naive" (GetAsyncKeyState).

	RawInput supports all kinds of HID controllers (your FP7 is one, your XBOX360 Controller as well), however it's bound to a device.

	If you plug your controller into another USB slot, SpiceTools does not have a way to detect it and will report the device as "missing", until you plug it back into where you originally configured it.

	Using the "naive" approach, only keyboard buttons can be detected, however this will then work with any keyboard attached, it's not bound to a device.

	Since May 2018 you can also bind MIDI devices for "one-shot" types like drums and hold types like piano keys and launchpads.



### Usage

!!! tip ""
	Utilizing SpiceTools is very straightforward, it typically involves simply dropping SpiceTools 32-bit or 64-bit (depending on game requirements) into your chosen game's content folder, creating a `.bat` file that initializes SpiceTools and desired parameters. For the grand majority of user installations, I've documented how to best utilize SpiceTools in the first time setup section of your respective game, so please read over it. One of the easiest and classic examples of a `.bat` file's contents would be along the lines of `spice64.exe -ea -w` which would boot SpiceTools with the `-ea` and `-w` parameters, more on parameters below.

### Parameters

!!! tip ""
	SpiceTools consists of several dozen parameters for users to utilize to fill their needs. Ideally, these parameters are initialized using a user created `.bat` file as described above. If you open up `spicecfg.exe` and head on over to the options tab, you can hover over the far left `?` with your mouse to get an idea as to what a parameter does!

	The grand majority of parameters are for advanced users, but don't be scared if you don't understand what most do.

&nbsp;

## Notes on Functionality for Several Games

### beatmania IIDX

!!! tip ""
	For using your own cameras in IIDX 25 or newer, just plug them in (and hopefully your camera isn't incompatible with the game) and they shall work.

	It's also possible to use one camera only instead of the two the game wants, just dismiss the camera error on game boot as you would with no cameras connected, and your camera should be registered in-game as CAMERA A. If you're not happy with the order of the automatic camera detection, just use -iidxflipcams and CAMERA B will be CAMERA A, etc.

	You can bind the effectors as analog inputs if you want, this is especially interesting for IIDX 25 and newer, where the effects are software based and not tied to specific sound cards anymore. When not bound, they will stay on the maximum value.

### Sound Voltex

!!! tip ""
	Printer fully supported as of 03/13/2018, can save prints in PNG/BMP/TGA to a customizable output path.

	Optionally able to clean up saved images on game boot time.

	Keyboard play should be perfectly working. If you don't want to use the mouse for the knobs, you can make use of native knob emulation, which works just as it works in Keyshoot-Mania.

### jubeat

!!! tip ""
	This makes use of the SpiceTools touch module, which makes you able to play any version of the game just fine with both mouse and HID compliant touch devices on Windows 7 or newer.

	The Dell ST2240T touch screen seems to work well, especially the new 2017 revision.

	Card insert button available and enabled by default.

	Touch the area to insert a card in attract mode.

### GITADORA

!!! tip ""
	To switch between Guitar/Drum you need to specify the specific eamuse config to load. By default, SpiceTools first tries to load ea3-config.xml, then eamuse-config.xml.

	Since the latter one is the default for the drums, for the guitar you have to override the path setting like so: `spice64.exe -e prop\eamuse-config2.xml`

	Additionally, since GitaDora uses 4 channels by default, you can specify -2ch to run it with 2 channel audio instead. If you don't and have a normal 2 channel setup, the game will refuse to play sound/tracks.

### Reflec Beat

!!! tip ""
	Including emulation of the real IR touch screen device so the game should just act like the real one.

	This makes use of the SpiceTools Touch module, which makes you able to play any version of the game just fine with both mouse and HID compliant touch devices.

	Card insert button available and enabled by default.

	For this game it's not visible in fullscreen but still works just as fine.

	Touch the area to insert a card in attract mode.

### NOSTALGIA

!!! tip ""
	Spicetools will auto-detect whether or not a compatible touch device is present. If a touch device is detected, the mouse cursor will disappear. If no touch device is detected, the mouse cursor will be visible in-game. During boot-up process, do not click or else the game may pre-maturely crash. You may safely click after the monitor check is completed. It's been found that Virtual HID Touch devices commonly found with remote access software may cause detection issues, take note of that.

	Some people have had issues with crashing on startup while having multiple monitors while using windowed mode, consider disabling the other monitors to see if this alleviates the issue.
