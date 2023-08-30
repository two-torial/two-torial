# DDR Ace Common Problems/Tips

### Hardware Specs

!!! tip ""
	Bemani PC Type 4

	CPU: Celeron M 440 1.86GHz

	GPU: ATI Radeon HD 2400

	RAM: 2 GB

	OS: Windows XP Embedded

### My Game Is Running Slow/Lagging

!!! tip ""
	Make sure you at least meet the above hardware requirements, try to eliminate any unnecessary background processes during play as well.

### Ddr a's Video Background Are Missing in the Menus And/Or Some Songs Soft-Lock the Game on the Nth/Final/Extra Stage Screen

!!! tip ""
	DDR's Video backgrounds rely on two DLLs in the game's "com" folder. However, unlike most other Bemani AC Games, these DLLs must be registered (Windows must know that these files exist, and where to point to when they are called). Without these, the game will run, but songs that rely on FMV backgrounds will break and the menu's backgrounds will be blank.


	There are two ways to fix this: You can either install the [K-lite Codec Pack](https://codecguide.com/download_kl.htm) (which gives the added bonus of enabling playback of weird esoteric video formats outside of the game) or register the DLLs for the game manually, if you wish to save space and aren't afraid of the command prompt.


	You can download the K-lite codec pack from here: https://www.codecguide.com/download_kl.htm
	The basic installer is all you need. Simply install the pack and then run DDR A.


	To register the DLLs with Windows:
	
	1. Open an elevated command prompt (Right click Command Prompt -> Run As Administrator)
	
	2. Navigate to your Windows directory (Typically C:/ Windows), then to SysWOW64 (Or System32 if on a 32-bit version of Windows) by typing `cd C:/windows` inside the command prompt
	
	3. Type `regsvr32 [path to one of the two DLLs in your DDR A's "content/com/" folder]`

		Ex: `regsvsr32 D:\MDX-2019042200\contents\com k-clvsd.dll`
	
	4. Repeat the command for the other DLL in the folder, and then close command prompt

		Ex: `regvsr32 D:\MDX-2019042200\contents\com xactengine2_10.dll`
	
	5. If everything went smoothly, run the game again with your desired tools and enjoy a properly working DDR A!

### I Want to Play in 4:3 (SD) Mode!

!!! tip ""
	If you're using SpiceTools, you can add `-ddrsd` to your `gamestart.bat` file and the game will boot into 4:3 mode.

###  Where Is the Option For Dancers/Shading/Measure lines/Fast-Slow/Layering?

!!! tip ""
	These options are locked behind network requirements and they will not show unless connected to a network that has written support for these options. There are some [hex edits](hexedits.md) for some of these options, however
	
###  Why Is My Game Not in English?

!!! tip ""
	English text is built in, change `<dest>J</dest>` in the `eamuse-config.xml` file inside `contents/prop` to `<dest>A</dest>`, then you can change language to English in the service menu's `GAME OPTIONS` (accessed via Spice's `Test` button). If English is not automatically set as pictured below. Make sure the code at the top left upon booting indicates `A:A:A` as desired.

<img src="/img/ddrace/eng.png">