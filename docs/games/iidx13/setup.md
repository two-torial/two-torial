# beatmania IIDX 13 DistorteD

<img src="/img/iidx13/distorted_logo.png">

!!! tip "This guide wouldn't exist without the help of sync (Discord: `sync_plus`)."

!!! warning "Before reading:"
	This game ***will*** require you to touch and edit files manually. This guide tries to make everything as clear as possible. **[Bemanitools](https://github.com/djhackersdev/bemanitools/releases/download/5.44/bemanitools-5.44.zip) & [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip)** will be used in this guide.

!!! danger "Warning:"
	Please make sure your data is from an appropriate source and unmodified before proceeding, this guide is unable to troubleshoot any problems related to bad or poorly managed data.
	
	If you encounter any issues or errors regarding this guide or come across issues that aren't listed, feel free to open up a [GitHub Issue!](https://github.com/yxrei/bemani-guide/issues)


### Getting Started

!!! tip ""
	
	After downloading your data, the first thing to do is make sure your files aren't set to READ ONLY, make sure to uncheck it from the main folder in the Windows Properties tab if so. Then, locate `iidx-13.zip` inside the `bemanitools-5.44.zip`. Extract it inside the folder that contains the `bm2dx.exe` which should be located in `\FDD\JAG`. Pictured below is what your folder should look like, we've removed any files not necessary for **DistorteD**. Feel free to name your `gamestart.bat` file whatever you desire, for the sake of convenience we've kept it as it.

<img src="/img/iidx13/bt1.png">

<img src="/img/iidx13/bt2.png">

<img src="/img/iidx13/1.png">

!!! tip ""

	Next up, open the `bemanitools-supplement-v1.6.zip` or any version higher than that and navigate inside the `misc.zip`. Now navigate into `misc\d3d8to9` and extract `d3d8.dll` into the same folder as we previously have done. This enables us to use the graphic options inside `iidxhook-13.conf` which we will take advantage of. It should look like this:

<img src="/img/iidx10/btsup1.png">

<img src="/img/iidx13/2.png">

!!! tip ""

	Now, open up `bemanitools-supplement-v1.6.zip` again and navigate into `iidx.zip`. Next, navigate into `iidx/misc` and extract `RtEffect_stub.dll` into the same folder as we previously have done. 
	
	Delete the already existing `RtEffect.dll` and rename `RtEffect_stub.dll` to `RtEffect.dll`. This will eliminate any immediate crashes relating to needing specific old hardware.

<img src="/img/iidx10/btsup2.png">

<img src="/img/iidx13/3.png">

<img src="/img/iidx13/4.png">

!!! tip ""

	Lastly, we need to install a codec so that background videos will work and won't cause an error. 
	
	Inside the [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip) archive, navigate to `\iidx.zip\iidx\misc\` where you'll find `CLVSD.ax`.

	Extract `CLVSD.ax` inside a folder that you know won't be moved or renamed.

	Open up the command prompt as ***administrator***. Now type `regsvr32 "<location of the file>\CLVSD.ax"` into the command prompt.

	As an example, it could look like this: `regsvr32 "D:\BEMANI\IIDX\CLVSD.ax"` A prompt should appear telling you that it has been installed successfully.
	This applies for all styles that require this codec, not just **DistorteD**.

	If an error occurs, you didn't run the command prompt as administrator or you messed up the location of the file.

	You ***can not*** move or delete `CLVSD.ax` ***at all***, otherwise it will revert the changes and you have to install it again.

### Configuring Your Tools

!!! tip ""
	To configure your keybinds, open up your `config.bat` file. You'll be greeted by this screen:

<img src="/img/iidx10/5.png">

!!! tip ""
	It works similarly to Spice but not entirely. Make sure to also bind `Test` and `Service` since we will need it later. `Service` will also be used to **insert coins** to start the game. When you're done setting up your keybinds and analogs, it should look something like this:
	
<img src="/img/iidx10/6.png">

!!! info "If you'd like to play offline, you can head straight to [Setting up the games resolution](setup.md#setting-up-the-games-resolution)"

### Configuring Bemanitools for an Online Network

!!! tip ""
	After setting the keybinds and analogs, we can head over to the `Network` tab, which will look like this:

<img src="/img/iidx10/7.png">

!!! tip ""
	Now we will set up our PIN pad and card.
	Click on `Keyboard device`, you may or may not have more than one option. This is normal. To figure out which one is your actual keyboard, select a device inside that list and press a button on the numpad.
	
!!! info "If you don't have a numpad, make sure to tick `Use top keyboard row for PIN pad input`. This will also change the `Card In` button to `Backspace`."

!!! tip ""
	If you have found your correct device, the `Keyboard status` will change **(the number and location of the number does not matter, it only matters that it changed)**. It should look similiar to this:
	
<img src="/img/iidx10/8.png">

!!! tip ""
	Next, grab your card, create a `.txt`, name it however you like, in this example it's called `card.txt` and place the file in a location that is easily accessible and you won't forget. In this case it's in a seperate folder. It should look like this:
	
<img src="/img/iidx10/9.png">

### Configuring the game for an Online Network

!!!tip ""
	Locate your `iidxhook-13.conf` and edit it in your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/)). It may seem overwhelming at first but it's actually fairly simple. All we really care about are these lines:
	
	```
	# URL (e.g. http://my.eamuse.server:80/whatever) or IPV4 (e.g. 127.0.0.1:80) of the target eamuse server. The port is optional but defaults to 80.
	eamuse.server=localhost:80

	# PCBID
	eamuse.pcbid=XXXXXXXXXXXXXXXXXXXX

	# EAMID
	eamuse.eamid=XXXXXXXXXXXXXXXXXXXX
	```
	
	Replace the `eamuse.server=localhost:80` with your desired network URL
	
	Replace `eamuse.pcbid=XXXXXXXXXXXXXXXXXXXX` **and** `eamuse.eamid=XXXXXXXXXXXXXXXXXXXX` with your PCBID of your network of choice.

### Setting up the games resolution, locking FPS & fix stretched videos

!!! tip ""
	Before we begin, we'd like to mention that you have two options when it comes to how the game renders. You can choose between `Linear` and `Point`.

	Below is an example of how both look like.

??? info "Linear"
	<img src="/img/iidx13/iidx13_linear.png">

??? info "Point"
	<img src="/img/iidx13/iidx13_point.png">

!!! tip ""
	It comes down to your own prefrence what you decide on, `Linear` is less sharp but doesn't have pixel perfect edges. `Point` is sharp and is pixel perfect.

!!! tip ""
	Next up, we'll setup borderless window, configure the proper resolution and fix stretched background videos. We're using a `1920x1080` monitor so we will use that.
	
	Repeat the previous step and open your `iidxhook-13.conf`. We want to find these lines:
	
	```
	# Fix stretched BG videos on newer GPUs. Might appear on Red and newer
	gfx.bgvideo_uv_fix=false
	
	# Software limit the frame rate of the rendering loop in hz, e.g. 60 or 59.95 (0.0 = no software limit)
	gfx.frame_rate_limit=0.0
	
	# Run the game windowed
	gfx.windowed=false

	# Windowed width, 0 for default size
	gfx.window_width=0

	# Windowed height, 0 for default size
	gfx.window_height=0

	# Up-/downscale the back buffer's width. This does not change the game's rendering resolution but scales the final frame. Use this to target the native resolution of your monitor/TV, e.g. to avoid over-/underscan, bad image quality or latency caused by the monitors internal upscaler. 0 to disable this feature. Must be set in combination with the corresponding height parameter.
	gfx.scale_back_buffer_width=0

	# Up-/downscale the back buffer's height. This does not change the game's rendering resolution but scales the final frame. Use this to target the native resolution of your monitor/TV, e.g. to avoid over-/underscan, bad image quality or latency caused by the monitors internal upscaler. 0 to disable this feature. Must be set in combination with the corresponding width parameter.
	gfx.scale_back_buffer_height=0

	# Filter type to use for up-/downscaling the back buffer. Only used if scaling feature was enabled by setting the scaling width and height parameters. Available types: none, linear, point (refer to D3DTEXTUREFILTERTYPE  for explanation).
	gfx.scale_back_buffer_filter=none
	```
	
	If you can't seem to find them, simply press `CTRL` + `F` and search for each argument. It will highlight them for you.
	
<img src="/img/iidx9/8.png">
	
!!! tip ""
	Listed below are the values we want to change them to.
	
	```
	gfx.bgvideo_uv_fix=true
	gfx.frame_rate_limit=59.95
	gfx.windowed=true
	gfx.window_width=1920
	gfx.window_height=1080
	gfx.scale_back_buffer_width=1920
	gfx.scale_back_buffer_height=1080
	gfx.scale_back_buffer_filter=linear
	```
	Unless you'd like to have the game properly windowed you can safely ignore `gfx.framed=false`. Under normal circumstances there shouldn't be a need for you to fiddle with `gfx.monitor_check=1.000000` so we are also going to ignore it.

	Make sure to adjust for if you want either `Linear` or `Point` rendering.

	```
	gfx.scale_back_buffer_filter=linear
	gfx.scale_back_buffer_filter=point
	```
	
	When you're done, it should look like this:
	
<img src="/img/iidx11/config_args.png">

### Final Steps and Setting up the Game

!!! tip ""
	We can now focus on starting the game and getting it running. Open `gamestart.bat` (if you kept the name as is)
	
	You will be greeted by the initialization screen and shortly after this screen:

<img src="/img/iidx13/5.png">

<img src="/img/iidx13/6.png">

!!! tip ""
	Hit your `Start` button to confirm to get to this screen:

<img src="/img/iidx13/7.png">

!!! tip ""
	Hit your `Start` button again to confirm. This will bring you into the games settings menu. From there, navigate to `CLOCK SETUP`. You can leave the date, no need to manually change it. Simply navigate to `SAVE AND EXIT`.
	
<img src="/img/iidx13/8.png">

<img src="/img/iidx13/9.png">

!!! info "If you'd like to play offline, you can head straight to [Final Notes](setup.md#final-notes)"

### Enabling e-AMUSEMENT for Online Play

!!! tip ""
	From the games settings menu, naviate to `e-AMUSEMENT OPTIONS` and select it. This will bring you to `e-AMUSEMENT SETTINGS`. Select it aswell.
	
<img src="/img/iidx13/10.png">

<img src="/img/iidx13/11.png">

!!! tip ""
	It'll bring you to this next screen, select it so that `e-AMUSEMENT` switches to `ON` and it will look like this:
	
<img src="/img/iidx13/12.png">

<img src="/img/iidx11/12.png">

!!! tip ""
	We now have to change our `SHOP NAME SETTING` and `PREFECTURE` otherwise the game will throw errors at us.
	
	Start with the shop name, select it and change them to what ever you like. When you're done editing your shop name, navigate to `EXIT` and select it.
	
<img src="/img/iidx11/13.png">

!!! tip ""
	For the prefecture change it once or how many times you'd like, it doesn't matter as long as it's not the default one.
	
<img src="/img/iidx11/14.png">

!!! tip ""
	Once that is done, hit `SAVE AND EXIT`. The game will now give you a message, which translated means: 
	
	`e-AMUSEMENT settings have been changed. Please turn the power off and on again.`
	
	So, close the game and open it up again.
	
<img src="/img/iidx11/15.png">
	
### Final Notes

!!! success "You're all done! From the service menu select `GAMEMODE` and the game should load ready to be played! Make sure to insert two credits by pressing your `SERVICE` key! Have fun!"

!!! warning "Have any other errors?"
	Check out the [Common Problems/Tips](problems.md) section to resolve any issues not seen in this guide to greater depth.
