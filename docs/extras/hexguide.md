# Beginner's Guide to Hex Editing

!!! warning "Before reading:"
	This section is for users that have never hex edited their game before, if you already know how to do this, nothing here will be of any use to you.


### Before Beginning

!!! tip ""
	There's several ways to apply hex edits to games, for the sake of this guide we'll demonstrate the manual way of doing edits to games in the event that the sites/services that simplify the process ever go down.

	We'll be using HxD to edit beatmania IIDX 25 CANNON BALLERS, the process is the same for any other game so this guide can work universally.

	Here's what you'll need:

	- Your favorite hex editor, such as [HxD](https://mh-nexus.de/en/hxd/).
	- A clean copy of your desired BEMANI game.
	- A backup of your original `.dll` before editing in the event of any mistakes.

### Getting Started

!!! tip ""
	So after downloading HxD or your preferred editor and deciding on what hex edits you want to apply, it's time to load it up for the first time. If you're using HxD, you'll be greeted with the screen below.

<img src="/img/hexguide/1.png">

!!! tip ""
	Open up the appropriate `.dll` file inside HxD that you wish to edit, for the grand majority of hex edits, this is the main game file, such as `bm2dx.dll`, `soundvoltex.dll`, and so on. Pictured below, I've opened up `bm2dx.dll` inside of HxD.

<img src="/img/hexguide/2.png">

!!! warning "Please note:"
	For demonstrative purposes, we're going to apply 1 edit to the game. The edit we'll be applying is EXCLUSIVE to this version of the game, meaning that it will not work on any other version of the game, nor any other games, because it's modifying specific addresses in memory that only apply to this specific version of the game.

!!! tip ""
	The edit we've chosen to apply is `Unlock All Songs` and its edit is `0xB60B2: 74 10 -> 90 90` so to start in HxD we're going to hit `Ctrl+G` to open the `Goto` window. From here, we'll input the offset `B60B2` inside the `Offset` section, as pictured, and hit OK.

<img src="/img/hexguide/3.png">

!!! tip ""
	Your cursor should be taken to the offset at the exact location you're ready to edit. As you can see, the numbers in front of you are `74` and `10` the same exact ones we need to replace! If they're not, it's likely you put in the wrong offset so be sure to double check.

<img src="/img/hexguide/4.png">

!!! tip ""
	From here, all we need to do is mouse over `74 10` and replace it with `90 90` you can do this by either manually typing `90 90` or by copy and pasting, it should look as it does below.

<img src="/img/hexguide/5.png">

!!! tip ""
	Once that's done, all you need to do is save the changes and repeat for every additional edit you want to do! The whole process is merely repeating by going to whichever offsets an edit requires and replacing the values in each location just as we did! Simple, right?
	