# MUSECA 1+1/2 Hex Edits

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.

### List of Known Edits for PIX-2018073002

!!! tip ""
	All edits below are for `museca.dll` unless otherwise specified.

	Infinite Final Layer

	- 0x17E587: `FF 83 48 14 00 00 -> 90 90 90 90 90 90`
	- 0x17E4DF: `7F 08 -> 90 90`
	- 0x17E060: `8B 81 48 14 00 00 -> B8 03 00 00 00 90`

	Auto Event Mode Toggled (Freeplay (Coin Options) Must be "ON" for this to Work Efficiently)

	- 0x196431: `89 01 88 41 10 C7 41 14 01 00 00 00 C3 CC CC CC CC -> C7 01 01 00 00 00 88 41 10 C7 41 14 01 00 00 00 C3`