# BEMANI Error Codes

!!! warning "Before reading:"
	This section contains various gamecode errors that a user may run across. There is an innumerable amount of these and I sometimes wonder if it's truly possible to have them all listed. 
	Nonetheless, dozens, if not hundreds are currently missing. This list is a massive work in progress and will be updated with time.

	Furthermore, not every solution listed can be the definitive solution to your error, sometimes various odd software and hardware nuances occur to create yet unseen issues. 
	I encourage you to be vocal about your solutions so that they can be added to the guide by [contacting me.](/about/#contact)


## Universal Error Codes

### 5-0000-0000

!!! tip ""
	This error can appear across any game, it's a generic critical error with several possible solutions.

	It is usually caused by network adapters that are enabled, other than the primary one used for network service. Try to disable some network adapters in Windows Device Manager, including hidden adapters.

	It can also be caused by game files being set to read only, especially the dev folder. Uncheck read only property in file explorer for all game files.

### 5-2000-0000

!!! tip ""
	This error can appear across any game, it's a standard network error with several possible solutions.

	First, make sure you have correctly entered your network service's URL properly with the `-url` parameter, that your internet connection is fine, and that the service is not down. 
	Also make sure you have correctly entered your PCBID with the ``-p`` parameter. 

	One other thing to check is that the data is supported by the service, and that the datecode used by the game
	is not invalid. Don't modify things if you don't need to! If the data is from a clean, trusted source, then this is extremely unlikely to be the cause.

### 5-2002-0915

!!! tip ""
	This error can appear across any game, it's a standard network error with several possible solutions.

	First, make sure you have correctly entered your network service's URL properly with the `-url` parameter, that your internet connection is fine, and that the service is not down. 
	Also make sure you have correctly entered your PCBID with the ``-p`` parameter. 

	One other thing to check is that the data is supported by the service, and that the datecode used by the game
	is not invalid. Don't modify things if you don't need to! If the data is from a clean, trusted source, then this is extremely unlikely to be the cause.

### 5-2600-0000

!!! tip ""
	This error can appear across any game, it's a standard network error with several possible solutions.

	First, make sure you have correctly entered your network service's URL properly with the `-url` parameter, that your internet connection is fine, and that the service is not down. 
	Also make sure you have correctly entered your PCBID with the ``-p`` parameter. 

	One other thing to check is that the data is supported by the service, and that the datecode used by the game
	is not invalid. Don't modify things if you don't need to! If the data is from a clean, trusted source, then this is extremely unlikely to be the cause.

&nbsp;
## IIDX Error Codes

### 5-1500-0002

!!! tip "SOUND DATA CREATE ERROR"
	This error occured from a corrupted installation. If your data came from a trusted source and you're having this issue, consider redownloading the files and making sure your installation was done properly. Or, perhaps your hard drive is failing.

### 5-1503-0004

!!! tip "USBIO ERROR (NO ANSWER...)"
	This error occurs when the game times out trying to communicate with the I/O board.
	
	When using tools, this typically happens because I/O emulation in tools takes too long, which can be caused by long-running background services on your computer. Usual offenders are: file-syncing software (GDrive, OneDrive, back up service, etc), anti-virus / malware scans, Windows Updates, or possibly bad hardware. Try to see if you can run tools at elevated process priority (SpiceTools already does this, but you can also try -realtime as last resort).
	
	On a real cabinet this would typically be a hardware error with the I/O board. Check cable connection and the power supply to the I/O board.

### 5-1505-0001

!!! tip "SSD DATA ERROR"
	This error occurs when the data is horribly corrupt, incomplete, or modified incorrectly. Please redownload your data from a reliable source.

### 5-1503-0042

!!! tip "CAMERA DEVICE ERROR"
	This error occurs when camera devices are missing/not functional. To resolve either have two cameras connected to your machine or apply a [hex edit](/extras/hexguide/) for your game's specific version and date code to simply not have this error occur on startup. It can be bypassed by hitting the `Test` button so it is not a critical error.

### 5-1506-0001

!!! tip "CLOCK ERROR"
	This error occurs when the clock is not set. To resolve, set the `CLOCK` in the service menu by hitting `SAVE AND EXIT` inside of the menu.

&nbsp;
## Sound Voltex Error Codes

### 5-1506-0000

!!! tip "ACIO ERROR"
	A user had this error when they downloaded the game from an unreliable source, they redownloaded `libacio.dll` from a clean, trusted source and had no issues. If the error persists, consider redownloading the data from a reliable source entirely.

### 5-2009-0000

!!! tip ""
	This error was seen on Sound Voltex Booth, a user had messed up their dll files. Thus, the solution would be to leave files unmodified and do not needlessly tamper. If your data came from a trusted source and you're having this issue, consider redownloading the files and making sure your installation was done properly.

&nbsp;
## Pop&apos;n Error Codes

### 5-1509-0000
!!! tip ""
	A user experienced this error every few minutes or so during play. If this issue occurs, make sure you have correctly inputted your chosen network's service URL and your PCBID correctly. 

### 5-2002-2400

!!! tip ""
	This error was seen on Pop&apos;n Usaneko due to improper setup and bad parameter usage in SpiceTools, make sure to follow [the first time setup](/games/popnusaneko/setup/) and utilize the `-url` and `-p` parameters in SpiceTools 
	so that you're not needlessly risking making mistakes in modifying the game's files. 

&nbsp;
## Jubeat Error Codes
	
### 5-2500-0000

!!! tip "BACKUP DATA ERROR"
	Follow the steps listed [here](/games/jubeatclan/setup/#final-steps-and-setting-up-the-game)

&nbsp;
## GITADORA Error Codes

### 5-1698-0000

!!! tip ""
	This was seen in GITADORA Tri-Boost Re:EVOLVE. To resolve, uncheck the `Read Only` attribute on the following `contents` folders.

		- \contents\data\product\aep_x64\
		- \contents\data\product\aep\

	Also, remove the following files from these folders.

		- battle_matching_3.bin
		- beargarden_3.bin
		- common_3.bin
		- custom_3.bin
		- entry_3.bin
		- game_combo_3.bin
		- game_common_3.bin
		- game_dm_3.bin
		- game_gf_3.bin
		- game_session.bin
		- home.bin
		- mission_result.bin
		- record_3.bin
		- select_music_3.bin
		- tab_3.bin
		- title_3.bin
		- warning_3.bin

### 5-1506-0000

!!! tip ""
	Disable all the unused network adapters inside device manager (make sure to view the hidden ones as well and disable those too!)

### 5-2500-0001

!!! tip "BACKUP DATA ERROR"
	Follow the steps listed [here](/games/gitamatixx/setup/#final-steps-and-setting-up-the-game)

### 5-2501-0000

!!! tip "GROUP ID ERROR"
	The Group ID Error is caused when it finds another cab of the same kind (GF or DM) with the same Group ID on the network. In most cases for users, this means the computer is connected to BOTH Ethernet and Wi-fi so the game sees 2 instances of itself. Thus to resolve, make sure you do not have 2 devices on the same subnet like this by checking your connections accordingly.

&nbsp;
## NOSTALGIA Error Codes

### 5-1501-0000

!!! tip ""
	This error was seen in NOSTALGIA Op. 2 when a user had a bad AVS config, make sure your data is from a reliable source and consider redownloading or replacing the file.