# IIDX 9 Common Problems/Tips

<img src="/img/iidx9/9_logo.png">

### My Game Is Running Crazy Fast!

!!! tip ""
	The most common reason for this is the game is running over its required 59.95hz, the game is hardcoded to run at 59.95hz and this cannot be changed. To solve this, check [this section](/games/iidx9/setup/#final-steps-and-setting-up-the-game) of the guide again.

### My game crashes immediately!

!!! warning "This can have multiple reasons. We will provide two possible fixes."
### Fix #1 (Missing codec)

!!! tip ""
	
	You need to install a codec that is missing. Inside the [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip) archive, navigate to `\iidx.zip\iidx\misc\` where you'll find `CLVSD.ax`.

	Extract `CLVSD.ax` inside the folder that contains the bm2dx.exe which should be located in `\C02\D\C02\JAG`

	Open up the command prompt as ***administrator***. Now type `regsvr32 "<location of your game>\CLVSD.ax"` into the command prompt.

	As an example, it could look like this: `regsvr32 "D:\BEMANI\IIDX\9TH-STYLE\C02\JAG\CLVSD.ax"` A prompt should appear telling you that it has been installed successfully. If an error occurs, you didn't run the command prompt as administrator or you messed up the location of the file.

	You ***can not*** move or delete `CLVSD.ax` ***at all***, otherwise it will revert the changes and you have to install it again.

### Fix #2 (Missing file)

!!! tip ""
	If the game still refuses to start, inside the [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip) archive, navigate to `iidx.zip/iidx/misc` and extract `RtEffect_stub.dll` inside the folder that contains the bm2dx.exe which should be located in `\C02\D\C02\JAG`.

	Rename `RtEffect_stub.dll` to `RtEffect.dll`.
