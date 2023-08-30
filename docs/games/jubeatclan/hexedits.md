# jubeat clan Hex Edits
	
!!! warning "Unsure how to apply hex edits?"

	Check out the [Beginner's Guide to Hex Editing](http://www.bemani.guide/extras/hexguide/) for assistance.

### List of Known Edits For L44-2018070901

!!! tip ""
	
	Disable Tutorial
	
	- jubeat.dll:  `0xCFFC7: 75 4A 57 68 00 -> E9 90 00 00 00`

	Song Select Timer Freeze

	- jubeat.dll: `0xA5A49: 75 -> EB`

	Expert Options Lock (Toggling on expert option keeps it on for every future play)

	- jubeat.dll: `0xD4699: 89 1D -> EB 0B`

	Online Matching Skip

	- jubeat.dll: `0xBCDCE: 7D -> EB`

	Unlock All Songs

	- music_db.dll `0x1B8F: 74 09 -> 90 90`