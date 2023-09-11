# Sound Voltex V: Vivid Wave

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.

### List of Known Edits For KFC-2020122200

!!! tip ""

	These are included inside of SpiceTools now by default! Check the `Patches` tab inside of the overlay and apply whichever you desire by clicking the check boxes and hitting apply.

### List of Known Edits For KFC-2020011500

!!! tip ""
	
	Boot Into Event Mode (Not compatible with premium free mode)
	
	- soundvoltex.dll: `0x4C4830: 33 C0 C7 41 08 64 05 00 00 48 89 01 C3 CC CC CC CC -> 31 C0 67 8D 40 01 C7 41 08 64 05 00 00 48 89 01 C3`

	All Songs/Difficulties Unlocked (Do not use when connected to online servers, will break automation paradise favoriting)
	
	- soundvoltex.dll: `0x4D2D75: 8B 4C 24 34 E8 C2 09 00 00 -> B8 03 00 00 00 90 90 90 90`
	- soundvoltex.dll: `0x55F4A2: E8 C9 A2 08 00 -> B8 0D 00 00 00`

	Infinite Premium Time

	- soundvoltex.dll: `0x2F4A15: FF 15 6D 5B 38 00 48 8B 44 24 30 -> 48 C7 C0 01 00 00 00 90 90 90 90`

	All Songs SAFE (You will not be forced out of your session for failing a song)

	- soundvoltex.dll: `0x5E2424: 06 -> 13`
	- soundvoltex.dll: `0x5E2433: A4 -> 00` 

	No Safe Banner on Jackets

	- soundvoltex.dll: `0x4FFF2B: 07 -> 45`

	Enable ARS (Alternative Rate System) Globally

	- soundvoltex.dll: `0x5E2A3D: 85 C9 74 08 -> B1 01 75 08`

	Freeze Non-Premium Timer

	- soundvoltex.dll: `0x406C8D: 8B 53 68 -> 90 90 90`

	Non-Effective Rate Gauges Start At 0%
	
	- soundvoltex.dll: `0x52E535: 10 27 -> 01 00`

	Non-Effective Rate Gauges Do Not Recover

	- soundvoltex.dll `0x52F003: 41 01 41 6C -> 90 90 90 90`

	Skip Global Matching Screen

	- soundvoltex.dll: `0x726A30: 4D -> 4E`

	All Appeal Cards Unlocked

	- soundvoltex.dll: `0x4D7E22: 16 -> 00`

	All Crew Unlocked

	- soundvoltex.dll `0x4D890B: 95 -> 91`

	SSE4.2 Fix (Allows the game to run on processors which do not support the SSE4.2 instruction set. If you can successfully boot the game already, DO NOT USE THIS EDIT!)
	
	- soundvoltex.dll: `0x25280D: F3 45 0F B8 C8 -> 67 45 8D 48 FF`
	- soundvoltex.dll: `0x26CCC6: F3 45 0F B8 CA -> 44 8D 4E 02 90`

	Bypass Camera Error

	- soundvoltex.dll: `0x61FBF0: 74 24 -> 90 90`

	Shared Mode WASAPI (Replaces the first audio device initilization attempt)
	
	- soundvoltex.dll: `0x638EC5: BA 03 00 00 00 -> BA 00 00 00 00`