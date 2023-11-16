# beatmania IIDX 30 Lighting Mode (TDJ) Information

<img src="/img/iidx30/resident.png">
	
### Setting up TDJ (Subscreen & 120FPS)

!!! tip ""
	To mitigate any errors during the process, we'll use a `Bypasss Lightning Monitor Error` hex edit.
	First, locate your `bm2dx.dll` which is located inside the `\modules` folder and make a backup of it in case something goes wrong. Next, head over to [mon's Bemani Patcher](https://mon.im/bemanipatcher/resident.html) and drag & drop your `bm2dx.dll` into the website.

	At the top, you'll see `Bypasss Lightning Monitor Error`. Enable it and press `Save Patched File`. Replace the file inside of `\modules`.

	Next, open up your `spicecfg.exe`, head to the `Options` tab and enable `IIDX TDJ Mode`.

<img src="/img/iidx31/tdj_mode.png">	

!!! warning "Be warned that to make TDJ work as intended, the game requires you to have 2 monitors with one being a touchscreen and the other one being 120Hz. It also disables the Keypad buttons/functionality requiring you to use the subscreen to enter your PIN."

### Setting up Single Monitor TDJ

!!! tip ""
	If you do not have a second monitor but atleast one that is 120Hz, you can set up Single Monitor TDJ mode.
	
	In `spicecfg.exe` under the `Options` tab, head down to `Graphics (Common)` and enable `Only Use One Monitor`. 

<img src="/img/iidx31/tdj_single_monitor.png">	
	
!!! tip ""
	This will enable you to switch (or open) the subscreen with a press of a button which you have to bind first. Inside of the `Buttons` tab, head to the `Overlay Button` section and bind `Toggle Sub Screen` to a button that feels comfortable for you to use. You can also change the subscreen size if you don't like it fullscreen. Simply head back to the `Options` tab and look for `IIDX TDJ Subscreen Size` and change to your preferred size.

### Lightning-specific Troubleshooting

!!! tip ""
	Below is a pretty common issue that has occured for users utilizing this guide and general startup practices.

### Audio Related Crash

!!! tip ""
	If you get a stack trace in your `log.txt` that looks like this...

	`exception raised: EXCEPTION_ACCESS_VIOLATION`

	`[2020/10/22 18:20:21] I:signal: printing callstack`

	`[2020/10/22 18:20:21] I:stackwalker: 000000018026E906 (bm2dx): (unknown): (unknown)`

	For cab type 1 (LDJ), change your audio device to motherboard audio and/or use -audiobackend asio `-asiodriverid ... -audiodummy`

	For cab type 2 (TDJ, with `-iidxtdj` or another means), you have a few options:

	1) Use `-iidxasio "Driver Name Here"` to set the ASIO driver used by IIDX's own ASIO handler. (Does not work with all ASIO drivers, they designed it to work best with a specific revision of the XONAR SOUNCARD(64))

	2) Use `-iidxsounddevice wasapi` to set IIDX to use WASAPI instead of its own ASIO handler.

	3) Use `-iidxsounddevice wasapi` along with `-audiobackend asio ...` to have the game pipe audio through Spice's own ASIO handler which is more compatible with various ASIO drivers