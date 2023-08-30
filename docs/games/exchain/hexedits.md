# GITADORA EXCHAIN Hex Edits

!!! warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](http://www.bemani.guide/extras/hexguide/) for assistance.

###List of Known Edits For M32-2019092400

!!! tip ""
	Timer Freeze

	- game.dll: `0xBC27: 0F 85 AA 01 00 00 -> E9 AB 01 00 00 90`

	Fix IP change error

	- libshare-pj.dll: `0x23305: 74 -> EB`