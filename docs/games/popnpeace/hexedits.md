# Pop'n Peace Hex Edits

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.

### List of Known Edits For M39-2020092800

!!! tip ""

	E: Drive fix

	- popn22.dll: `0x286AA8: 65 3A 2F -> 64 65 76`

	HDMI Audio Fix

	- popn22.dll `0x13442C: 85 C0 75 96 -> 90 90 90 90`

	Prevent Windows volume change on boot

	- popn22.dll: `0x137030: 83 -> C3`

	Boot to Event Mode

	- popn22.dll `0x108DC0: 8B 00 C3 CC -> 31 C0 40 C3`

	Timer Freeze

	- popn22.dll `0xE294C: 0F 85 -> 0x90 E9`

	Skip Menu and Long Note Tutorials
	
	- popn22.dll `0x28E0B: 74 -> EB`
	- popn22.dll `0x28DE7: 75 -> EB`
	- popn22.dll `0x8AE71: 75 -> EB`

	Unlock All Songs

    - popn22.dll `0x10D2E2: 74 -> EB`
    - popn22.dll `0x10D2FB: 75 46 -> 90 90`
    - popn22.dll `0x10D318: 74 3A -> 90 90`
    - popn22.dll `0x10D33B: 84 C0 -> B0 01`