# IIDX 9 Common Problems/Tips

<img src="/img/iidx9/9_logo.png">

### My Game Is Running Crazy Fast!

!!! tip ""
	The most common reason for this is the game is running over its required 59.95hz, the game is hardcoded to run at 59.95hz and this cannot be changed. To solve this, check [this section](/games/iidx9/setup/#final-steps-and-setting-up-the-game) of the guide again.

### I'm getting "NETWORK WARNING" instead of "NETWORK OK"

!!! tip ""
	This can be caused by:

	- Invalid PCBID
	- Firewall blocking connections
	- Invalid eamuse url or port specified
	- Game is not run using the Administrator account 

### My game crashes immediately!

!!! warning "This can have multiple reasons. These fixes shouldn't be needed for 9th style to run properly, but will be mandatory for other styles. We'll add them to 9th style anyway just in case."

#### Fix #1 (Wrong data structure)

!!! tip ""
	Make sure that your unpacked data looks like this:

	- JAx (Game binary revision folder where 'x' can be A, B, C, D, E, F, G)
	- data
	- sidcode.txt
	
	Any other files are optional and don't have to be removed as these are not required to run the game.

#### Fix #2 (Missing codec)

!!! tip ""

	You need to install a codec that is missing. Inside the [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip) archive, navigate to `\iidx.zip\iidx\misc\` where you'll find `CLVSD.ax`.

	Extract `CLVSD.ax` inside the folder that contains the bm2dx.exe which should be located in `\C02\D\C02\JAG`

	Open up the command prompt as ***administrator***. Now type `regsvr32 "<location of your game>\CLVSD.ax"` into the command prompt.

	As an example, it could look like this: `regsvr32 "D:\BEMANI\IIDX\9TH-STYLE\C02\JAG\CLVSD.ax"` A prompt should appear telling you that it has been installed successfully. If an error occurs, you didn't run the command prompt as administrator or you messed up the location of the file.

	You ***can not*** move or delete `CLVSD.ax` ***at all***, otherwise it will revert the changes and you have to install it again.

#### Fix #3 (Missing file)

!!! tip ""
	
	If the game still refuses to start, inside the [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip) archive, navigate to `iidx.zip/iidx/misc` and extract `RtEffect_stub.dll` inside the folder that contains the bm2dx.exe which should be located in `\C02\D\C02\JAG`.

	Rename `RtEffect_stub.dll` to `RtEffect.dll`.