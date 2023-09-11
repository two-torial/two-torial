# GITADORA Matixx Hex Edits

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.

###List of Known Edits For M32-2018071700

!!! tip ""
	Timer Freeze

	- game.dll: `0xBC37: 0F 85 AA 01 00 00 -> E9 AB 01 00 00 90`

	Stage Freeze **(NOT compatible with usage on networks due to how the game saves user plays)**

	- game.dll: `0x1595E1 0F 85 FB 01 00 00 -> E9 FC 01 00 00 90`

	Unlock all music

	- game.dll: `0x1EAEFA: 71 00 -> 4D 01`
	- game.dll: `0x1EAF12: 73 00 -> 4D 01`
	- game.dll: `0x162FF4: 75 16 -> EB 23`

	Enable Long music

	- game.dll: `0x163134: 75 03 -> 90 90`

	Fix IP change error

	- libshare-pj.dll: `0x23375: 74 -> EB`