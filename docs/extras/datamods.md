# Data Mods and Omnimix

!!! info "This guide will cover how to mod your BEMANI game's data folder in a non-destructive way.<br>No files will be removed or overwritten."

---
### Pre-requisites

!!! tip ""

	- A fully working and unmodified game.
	- The data to mod your game with.

!!! danger "ATTENTION"

	- Please make sure the mod you're installing is **compatible with YOUR specific game and game version**.
	- If connecting to an **online network**, make sure they **explicitly allow** the mod you're about to install.
	- TWO-TORIAL will **NOT** provide support with issues caused by mods besides **Omnimix** for beatmania IIDX.

---
### Preparing data_mods

!!! tip ""

	Let's place your mod files in the right folder.

	- Create a `data_mods` folder next to the others in your game files.

	<img src="/img/datamods/1.png">

	Depending on how your mod is packaged, you may or may not need to create another folder to contain it.  
	Inside that folder, the structure should follow the one in `data/`.

	- Place your files inside that `data_mods/folder/`.

	If you're confused, the following may help you understand what this means.

	```
	├─ data/
	├─── graphic/
	├─── info/
	├─── movie/
	├─── sound/
	├─── etc...
	├─ data_mods/  
	├─── folder_name/
	├───── graphic/ <- files that mod the /data/graphic/ folder go here
	├───── info/ <- files that mod the /data/info/ folder go here
	├───── movie/ <- files that mod the /data/movie/ folder go here
	├───── sound/ <- files that mod the /data/sound/ folder go here
	├───── etc...
	├─ dev/ 
	├─ modules/  
	├─ prop/  
	```

!!! info "Example: Omnimix for beatmania IIDX 31 EPOLIS"

	**Directory**: `contents/data_mods/`
	<img src="/img/datamods/2.png">
	
	**Directory**: `contents/data_mods/omnimix_31`
	<img src="/img/datamods/3.png">

---
### Loading data_mods

#### Installing ifs_layeredfs

!!! tip ""

	We now need a way for our game to load our mods.

	- Download the most recent release of [ifs_layeredfs](https://github.com/mon/ifs_layeredfs/releases/).

	<img src="/img/datamods/4.png">

	- Open the archive.

	<img src="/img/datamods/5.png">

	What we're interested in are the `64bit` and `32bit` folders:
	
	- Your game is 32bit *(spice.exe to launch)*: go in the `32bit` folder.
	- Your game is 64bit *(spice64.exe to launch)*: go in the `64bit` folder.

	<img src="/img/datamods/6.png">

	- Copy the `ifs_hook.dll` file to your game's `modules` folder.

	- Back to the archive, go inside the `automatic_injector_dlls` folder.

	<img src="/img/datamods/7.png">

	- Copy the `d3d9.dll` file to your game's `modules` folder.

	<img src="/img/datamods/8.png">

#### Loading ifs_layeredfs

!!! tip ""

	All that should be left to do is tell spice2x to load `ifs_hook.dll`.

	- Open your game's `spicecfg.exe`.
	- Head to the `options` tab.
	- Find the `Inject DLL Hooks` option under `Common` and type in `ifs_hook.dll` then press Enter.

	Note: If you have other DLL hooks, simply add more by having a space in between them..  
	Example: `ifs_hook.dll somehook.dll`

	<img src="/img/datamods/9.png">

	Assuming your `data_mods` folder has been made properly, that's it!

!!! danger "Extra step for beatmania IIDX Omnimix"

	You also need to patch your game's DLL with the `Omnimix` patch.
	
	For more information on how to patch your game, head over to the [Spice2x Patching](../extras/patchsp2x.md) page!