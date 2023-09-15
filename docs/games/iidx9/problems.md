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
	
	We have [provided a `.bat` file](/files/install-CLVSD.bat). Right click the link and select `Save link as`, save it into `\C02\D\C02\JAG` again.
	
	When you have both files in that directory, right click `install-CLVSD.bat` and select `Run as administrator`. This will install the codec for you.
	
	You may want to delete `install-CLVSD.bat` now but you **can not** move or delete `CLVSD.ax` **at all**

### Fix #2 (Missing file)

!!! tip ""
	If the game still refuses to start, inside the [Bemanitools Supplement](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip) archive, navigate to `iidx.zip/iidx/misc` and extract `RtEffect_stub.dll` inside the folder that contains the bm2dx.exe which should be located in `\C02\D\C02\JAG`.
	
	Rename `RtEffect_stub.dll` to `RtEffect.dll`.

