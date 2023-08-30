# Pop'n Usaneko Hex Edits

!!! warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](http://www.bemani.guide/extras/hexguide/) for assistance.

### List of Known Edits For M39-2018082100

!!! tip ""

	E: Drive fix

	- popn22.dll: `0x25A5D0: 65 3A 2F -> 64 65 76`

	HDMI Audio Fix

	- popn22.dll `0x12C26C: 85 C0 75 96 -> 90 90 90 90`

	Prevent Windows volume change on boot

	- popn22.dll: `0x12EE70: 83 -> C3`

	Boot to Event Mode

	- popn22.dll `0x100A10: 8B 00 C3 CC -> 31 C0 40 C3`

	Timer Freeze

	- popn22.dll `0xDB3F2: C7 45 38 09 00 00 00 -> 90 90 90 90 90 90 90`

	Partial Song Unlock (NOTE: This does not unlock all songs, see the notes below.
	
	- popn22.dll `0x1E0524 - 0x1E073F: fill with zeros (00)`

	Unlock Classic 8 EX as a 49

	- popn22.dll `0x2AC1DB: 05 -> 07`
	- popn22.dll `0x2AC1EB: 01 -> 31`

	Network Adapter Fix (for matching online/local)

	- libavs-win32.dll: '0x3A13D: 8B 7C 24 08 8B D5 8B -> BA 01 00 00 00 EB B5'

### Notes

!!! tip ""

	Since we don't have hex edits to unlock songs that are both new and old (eclale songs, SDVX FLOOR INFECTION, etc.) [Here is an unlocked DLL with both the HDMI audio fix and E: drive fix already done.](/files/usaneko-unlock.zip)

	This will unlock all songs in pop'n 24, 23 and the floor infection songs in pop'n 23 and 22. This also takes away the hold note identifier on the menus, so you don't have to have that annoying hold note tutorial if you play without a card or offline.