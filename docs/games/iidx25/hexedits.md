# beatmania IIDX 25 Hex Edits
	
!!! warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](http://www.bemani.guide/extras/hexguide/) for assistance.

### List of Known Edits For LDJ-2019100700

!!! tip ""

	All below edits are for `bm2dx.dll` unless otherwise specified. 

	SSE4.2 Fix (Allows the game to run on processors which do not support the SSE4.2 instruction set. If you can successfully boot the game already, DO NOT USE THIS EDIT!)

	- 0x3F8CF7: `F3 45 0F → 90 90 90` 

	Unlock All Songs

	- 0x16D7B2: `74 10 → 90 90`

	Unlock All 12s

	- 0x16D660: `83 FF 02 74 05 83 FF 05 → 90 90 90 90 90 90 90 90`

	Skip CAMERA DEVICE ERROR prompt

	- 0x36F3FB: `84 → 81`

	1P Premium Free

	- 0x32F5C7: `75 → EB`

	2P Premium Free

	- 0x32F765: `74 55 → 90 90`
	- 0x32F77B: `74 3F → 90 90`

	Premium Free Timer Freeze

	- 0x16FCAD: `FF C8 → 90 90`

	Standard/Menu Timer Freeze

	- 0x387F37: `74 → EB`

	Cursor lock

	- 0x334914: `74 1D → 90 90`

	CS-Style Song Start Delay

	- 0x3539EA: `7D 25 → 90 90`

	Play video preview on all songs (Normally only some beginner songs do this)

	- 0x11CA4C: `0F B6 → EB 2F`
	- 0x11FDFE: `74 0E → 90 90`

	Hide INSERT COIN[S] text

	- 0x107279: `3B → 3A`

	Hide CREDIT %d text

	- 0x106DF8: `0C → 0B`

	Hide CREDIT %d COIN %d / %d text

	- 0x106DCD: `17 → 16`

	Hide EXTRA PASELI: %d text

	- 0x106EE9: `43 → 42`

	Hide PASELI: %d text

	- 0x1070B8: `A4 → A3`

	Hide PASELI: NO ACCOUNT text

	- 0x10717B: `21 → 20`

	Hide PASELI: ****** text

	- 0x1070DD: `9F → 9E`

	Free play text to LED ticker (Bottom Right)

	- 0x106F9F: `35 2F 35 00 → D9 68 44 02`

	LED Ticker (Top Left)

	- 0x36D780: `FC B9 1C 00 → 98 01 3A 02`
	- 0x36D958 `74 3C → 90 90`

	Quick Retry (Guest and non-VIP card players can hold VEFX and Effect during a song to quickly restart)

	- 0x1583BF: `32 C0 → B0 01`

	Expert Course Force Open (In offline or local mode)

	- 0x32F711: `75 → EB`

	Shorter monitor check (Runs for 2 seconds instead of 20, only use if your framerate is extremely stable or you will have issues)

	- 0x366E6C: `B0 04 → 78 00`


