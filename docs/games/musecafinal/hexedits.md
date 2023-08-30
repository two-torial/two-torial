# MUSECA 1+1/2 Hex Edits

!!! warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](http://www.bemani.guide/extras/hexguide/) for assistance.

### List of Known Edits for PIX-2018073002

!!! tip ""
	All edits below are for `museca.dll` unless otherwise specified.

	Infinite Final Layer

	- 0x17E587: `FF 83 48 14 00 00 -> 90 90 90 90 90 90`
	- 0x17E4DF: `7F 08 -> 90 90`
	- 0x17E060: `8B 81 48 14 00 00 -> B8 03 00 00 00 90`

	Auto Event Mode Toggled (Freeplay (Coin Options) Must be "ON" for this to Work Efficiently)

	- 0x196431: `89 01 88 41 10 C7 41 14 01 00 00 00 C3 CC CC CC CC -> C7 01 01 00 00 00 88 41 10 C7 41 14 01 00 00 00 C3`