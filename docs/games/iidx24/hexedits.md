# beatmania IIDX 24 Hex Edits

<img src="/img/iidx24/sinobuz.png">

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.
	


### List of Known Edits For LDJ-2017082800

!!! tip ""

	All below edits are for `bm2dx.dll` unless otherwise specified. 

	Timer Freeze

	- 0x9BAEE: `74 → EB`
	
	90 Sec Music Select Timer (Make sure your Select Time option is set to **"45 SEC"** in the Game Options for this to work!)
	
	- 0x350B4: `2D → 5A`
	
	Premium Free
	
	- 0x60A1B: `75 → EB`
	
	Premium Free (2 player mode)
	
	- 0x60B94: `74 2f → 90 90`
	- 0x60BA5: `0f 85 3b → e9 3c ff`
	- 0x60BAA: `ff → 90`
	
	Premium Free Timer Freeze
	
	- 0x5DEAD: `48 → 90`
	
	Level 12 Unlocked
	
	- 0x5BB35: `83 FF 02 74 0B 83 FF 05 74 06 B0 01 → 90 90 90 90 90 90 90 90 90 90`
	
	Unlock All Songs
	
	- 0x5C005: `74 15 → 90 90`
	
	Unlock All Daily Bonuses
	
	- 0x5E180: `56 8B F1 E8 58 57 FD FF → B8 01 00 00 00 C2 04 00`
	
	Cursor lock
	
	- 0x6C8E5: `74 23 → 90 90`
	
	CS-Style Song Start Delay
	
	- 0x78D52: `7C → EB`
	
	Dark Mode
	
	- 0x71cb7: `74 3b → 90 90`
	
	Disable Bar Lines
	
	- 0x3d540: `75 → EB`
	
	Remove Rainbow Banners
	
	- 0x12C34D: `5F → 00`
	
	Volume Bug Fix [If your volume gets forced to max, turn this on]
	
	- 0xda249: `00 → 01`
	
	Free play text to LED ticker
	
	- 0x150EA: `E0 8F 12 10 → 64 99 6A 11`
	
	Free play text to LED ticker (Upper left)
	
	- 0xA4615: `74 32 → 90 90`
	- 0xA4630: `54 1D 16 10 → 64, 99, 6A, 11`
	
	Debug mode (disables score saving!) [Press F1 in-game to open menu]
	
	- 0x579B0: `32 C0 → 0C 01`
	
	Skip Card Entry
	
	- 0x63E34: `32 → 20`
	
	Quick Retry [Hold VEFX and Effect during a song to restart]
	
	- 0x4e284: `8A C3 → B0 01`
	
	Shorter monitor check [Runs for 300 frames (5 seconds) instead of 1200 (20 seconds), recommended only if you have a very stable framerate]
	
	- 0x81A5A: `B0 04 → 2C 01`
	
	6 digits in monitor check [Purely visual, does not affect anything besides the FPS display]
	
	- 0x15ADF9: `34 → 36`
