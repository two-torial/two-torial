# NOSTALGIA OP.2 Hex Edits

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.

### List of Known Edits For PAN-20191002/PAN-2019112700

!!! tip ""
	
	Menu Timer Freeze
	
	- nostalgia.dll: `0x303D33: 41 FF C8 -> 90 90 90`

	Shorter Monitor Check
	
	- nostalgia.dll: `0x21A6FA: 1E -> 00`

	Hide "EXTRA PASELI: %d"
	
	- nostalgia.dll: `0x307BD2: CA 2F 2A -> 04 72 26`
	- nostalgia.dll: `0x307BEE: 7E 2F 2A -> E8 71 26`

	Hide "PASELI: *****"

	- nostalgia.dll: `0x307A6E: FF 15 14 42 09 00 -> E9 A0 01 00 00 90`

	Hide Credit Count

	- nostalgia.dll: `0x307E31: BB 2B 2A -> A5 6F 26`
	- nostalgia.dll: `0x307E4D: 7F 2B 2A -> 89 6F 26`

	