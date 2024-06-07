# IIDX 14 Common Problems/Tips

<img src="/img/iidx14/gold_logo.png">

### My Game Is Running Crazy Fast!

!!! tip ""
	The most common reason for this is the game is running over its required 59.95hz, the game is hardcoded to run at 59.95hz and this cannot be changed. To solve this, check [this section](setup.md#setting-up-the-games-resolution-locking-fps-and-fixing-stretched-videos) of the guide again.

### I'm getting "NETWORK WARNING" instead of "NETWORK OK"

!!! tip ""
	This can be caused by:

	- Invalid PCBID
	- Firewall blocking connections
	- Invalid eamuse url or port specified
	- Game is not run using the Administrator account 

### My background videos aren't working!

!!! tip ""

	You need to install a codec.
	
	Inside the [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip) archive, navigate to `\iidx.zip\iidx\misc\` where you'll find `CLVSD.ax`.

	Extract `CLVSD.ax` inside a folder that you know won't be moved or renamed.

	Open up the command prompt as ***administrator***. Now type `regsvr32 "<location of the file>\CLVSD.ax"` into the command prompt.

	As an example, it could look like this: `regsvr32 "D:\BEMANI\IIDX\CLVSD.ax"` A prompt should appear telling you that it has been installed successfully.
	This applies for all styles that require this codec.

	If an error occurs, you didn't run the command prompt as administrator or you messed up the location of the file.

	You ***can not*** move or delete `CLVSD.ax` ***at all***, otherwise it will revert the changes and you have to install it again.

### My game crashes immediately!

!!! warning "This can have multiple reasons. This fix shouldn't be needed for GOLD since we're addressing them in the guide. We'll add it anyway just in case."

#### Wrong data structure

!!! tip ""
	Make sure that your unpacked data looks like this:

	- yyyymmddrr (y = year digit, m = month digit, d = day digit, r = revision digit) revision folder containing game binary and libraries
	- data
	- sidcode.txt
	
	Any other files are optional and don't have to be removed as these are not required to run the game.