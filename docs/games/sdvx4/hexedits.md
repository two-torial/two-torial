# Sound Voltex IV HEAVENLY HAVEN Hex Edits

<img src="/img/sdvxiv/hh.png">

??? info "Want a quick drag and drop solution?"
	Use _mon's [BemaniPatcher](https://mon.im/bemanipatcher)._ Simply select the game you'd like to edit and drop the corresponding game `.dll` into it and select what changes you'd like!

??? warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](https://guide.fumo.photos/extras/hexguide/) for assistance.

### List of Known Edits For KFC-2019020600

!!! tip ""
	
	Auto Event Mode Toggled (Freeplay (Coin Options) must be "ON" for this to work efficiently)
	
	- soundvoltex.dll: `0x19EAD2: 00 > 01`

	Difficulty Unlock
	
	- soundvoltex.dll: `0x158D42: E8 69 5D 02 -> B8 0D 00 00`

	Song Unlock
	
	- soundvoltex.dll: `0x1BF579: 8B 44 24 20 E8 3E EB FF FF -> B8 03 00 00 00 90 90 90 90`

	2 Song Safe

	- soundvoltex.dll: `0x17A153: 32 C0 -> B0 01`

	Premium Free Hack (Combine with 2 Song Safe Hex above for full effect)

	- soundvoltex.dll: `0x1D6B8F: 00 -> 02`	
	- soundvoltex.dll: `0x1D6D76: 8B 83 64 10 00 00 8D 48 01 83 F9 04 56 57 7F 52 -> B8 01 00 00 00 89 83 64 10 00 00 90 56 57 90 90`

	Safe Banner Removal

	- soundvoltex.dll `0x2FB684: 73 -> 00`

	Prevent Windows volume change on boot

	- soundvoltex.dll: `0x2550CA: E8 21 03 00 00 -> 90 90 90 90 90`

	Disable EVENT MODE/FREE PLAY text

	- soundvoltex.dll: `0xBF9E0: E8 DB -> EB 03`

	Allow ARS (Alternative Rate System) Option (At gauge select, goto excessive and press BT-D to enable)

	- soundvoltex.dll `0x179864: 74 -> EB`

	Non-effective rate gauges start at 0%
	
	- soundvoltex.dll: `0x120730: 10 27 -> 01 00`

	Non-effective rate gauges do not recover
	
	- soundvoltex.dll: `0x120BAA: 01 50 48 -> 90 90 90`

	Enable MUSECA cards in generator start

	- soundvoltex.dll: `0x31F3BA: 6D 75 73 65 63 61 -> 90 90 90 90 90 90`

	Disable chain display
	
	- soundvoltex.dll: `0x128241 8B 45 08 -> 90 90 90`

	Disable gold chain color
	
	- soundvoltex.dll: `0x12822F 00 -> FF`

	Disable UC,PUC fanfare

	- soundvoltex.dll: `0x1285D2 80 -> 81`
	- soundvoltex.dll: `0x128614 00 -> FF`

	Unlock blaster barrier rank 5
	
	- soundvoltex.dll: `0x9DAA6 08 -> 0A`
	- soundvoltex.dll: `0x9DAB7 08 -> 0A`

### List of Known Edits For KFC-2017112800

!!! tip ""

	Auto Event Mode Toggled (Freeplay (Coin Options) must be "ON" for this to work efficiently)

	- soundvoltex.dll: `0x196562 : 00 > 01`

	Song & Difficulty Unlock
	
	- soundvoltex.dll: `0x152142: E8 F9 41 02 -> B8 0D 00 00 (Difficulty Unlock)`
	- soundvoltex.dll: `0x1B4A31: 8B 44 24 20 E8 A6 EC FF FF -> B8 03 00 00 00 90 90 90 90 (Song Unlock)`

	2 Song Safe

	- soundvoltex.dll: `0x171B07: 32 C0 -> B0 01`

	Premium Free Hack (Combine with 2 Song Safe Hex above for full effect)

	- soundvoltex.dll: `0x1CAAFF: 00 -> 02`
	- soundvoltex.dll: `0x1CACC6: 8B 83 64 10 00 00 8D 48 01 83 F9 04 56 57 7F 52 -> B8 01 00 00 00 89 83 64 10 00 00 90 56 57 90 90`

	Safe Banner Removal

	- soundvoltex.dll: `0x2E9C44: 73 -> 00`

	Prevent Windows volume change on boot

	- soundvoltex.dll: `0x2451EA: E8 21 03 00 00 -> 90 90 90 90 90`

	Disable EVENT MODE/FREE PLAY text

	- soundvoltex.dll: `0xBC920: E8 6B -> EB 03`

	Hispeed values from 0.1 to 20.0

	- soundvoltex.dll: `0x12198B: DD 05 F8 87 2D 10 -> D9 05 A0 89 2D 10`
	- soundvoltex.dll: `0x1219A0: DD 05 00 88 2D 10 -> D9 05 E4 86 2D 10`
	- soundvoltex.dll: `0x1211C1: DD 05 F8 87 2D 10 -> D9 05 A0 89 2D 10`
	- soundvoltex.dll: `0x1211BB: DD 05 00 88 2D 10 -> D9 05 E4 86 2D 10`

	Allow ARS (Alternative Rate System) Option (At gauge select, goto excessive and press BT-D to enable)

	- soundvoltex.dll: `0x171274: 74 -> EB`

	Non-effective rate gauges start at 0%

	- soundvoltex.dll: `0x11ACD0: 10 27 -> 01 00`

	Non-effective rate gauges do not recover

	- soundvoltex.dll: `0x11B14A: 01 50 48 -> 90 90 90`

	Remove combo/chain display

	- soundvoltex.dll: `0x1220B1: 8B 45 08 -> 90 90 90`

	Omega Dimension semi-conversion

	- soundvoltex.dll: 0x358B40: DC 5F 30 10 -> 38 54 30 10

	- data/sound/sys_sd_ver04.2dx

	- sys_sd_ver04.2dx: `0x4C: 0A D5 0B 00 -> B6 1D 52 00`
	- sys_sd_ver04.2dx: `0x5C: D2 6B 3D 00 -> 28 10 68 00`
	- sys_sd_ver04.2dx `0x50: 7C 0E 15 00 -> 9A 01 7A 00`

