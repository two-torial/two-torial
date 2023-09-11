# DanceDanceRevolution Ace Hex Edits

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.

### List of Known Edits For MDX-2019042200

!!! tip ""
	All edits below are for `gamemdx.dll` unless otherwise specified.

	Force Enable Fast/Slow
	
	- gamemdx.dll: `0x97C60: 8B 41 44 -> 31 C0 40`

	Force Background Judgement

	- gamemdx.dll: `0x97C50: 8B 41 -> 31 C0`

	Force Darkest Background

	- gamemdx.dll: `0x98A0E: 75 03 33 C0 -> 33 C0 B0 03`

	Song Unlock (Incomplete - Unlocks All the Event Mode Songs but Still Requires Editing the Music Database)

	- gamemdx.dll: `0x846D1: 45 F4 -> 90 E9, 0x8D007: 32 C0 -> B0 01`

	Tutorial Skip

	- gamemdx.dll: `0x49D33: 75 -> EB`

	Timer Freeze

	- gamemdx.dll: `0x275D7: 74 -> EB`

	Unlock Options

	- gamemdx.dll: `0x82733: 75 -> EB`

	Force Cabinet Type 6 (A20 Gold Theme)

	- gamemdx.dll: `0xDE18: FF 24 -> EB 71`

	Force ENDYMION Menu Background

	- gamemdx.dll: `0x1F98D: EC -> F0`

	Skip a20 Menu Background Loading

	- gamemdx.dll: `0x1F944: 75 -> EB`
	
	Make Notes Possible to Read When Using Darkest Setting (Sets to 99%)

	- gamemdx.dll: `0x1C9F6: 33 33 33 3F -> A4 70 7D 3F`



