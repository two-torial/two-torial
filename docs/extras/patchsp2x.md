# Spice2x DLL Patching

!!! info "Last updated: June 3rd, 2024<br>Known spice2x patchers: [External resources](/externalresources#spice2x-patchers)"

!!! warning "Compatibility"

	This patching method only is for [spice2x supported games](https://github.com/spice2x/spice2x.github.io/wiki/List-of-supported-games).

	Please make sure you're using the latest release for [spice2x](https://spice2x.github.io/).  
	**Note: As of writing, you need to use the latest beta release as the feature has not yet been pushed to stable.**

!!! danger "Before proceeding"

	**It is highly recommended to use an unpatched DLL as your base!**
	
	If you've already patched your game through other methods *([web patching](/extras/patchweb) or [hex editing](/extras/hexguide))*,  
	**Please replace your game's DLL with the original**.

---
### Getting Started

!!! tip ""

	**The following guide works the same regardless of which spice2x compatible game you're using.**

	In this case we will be using a clean SDVX installation as a reference, with the following folder structure.

<img src="/img/patchsp2x/1.png">

#### Importing Patches from URL

!!! tip ""

	Open `spicecfg.exe` and head to the `Patches` tab.

<img src="/img/patchsp2x/2.png">

!!! tip ""

	By default no patches will be available, we need to import some. 

	Click on `Import from URL`.

	A new popup will appear, in which you should paste your preferred patcher's URL.  
	At time of writing `https://p.eagate.turksigara.net/resources/` is the most up-to-date for SDVX.

	After pasting your URL in, click on `Import`.  
	If patching fails, it most likely is because the URL you provided doesn't support your game's version.

<img src="/img/patchsp2x/3.png">

#### Picking Patches

!!! danger "Important"

	**As a general rule of thumb, if you're not sure what a patch does or you're not absolutely certain you need it, leave it alone**.

!!! tip ""

	After a successful import, your patches should now show up inside spice2x.
	
	A new `Patches` folder has also been created, containing a `.json` file with your available patches for offline use.

<img src="/img/patchsp2x/4.png">

!!! tip ""

	Now you may pick and choose desired patches!

	For game-specific instructions, refer to their respective dedicated pages.

#### Auto apply / Overwrite game files

!!! tip "Auto apply (recommended)"

	After picking your patches, it is **strongly recommended** to tick the `Auto apply patches on game start` box.

	Doing so will keep your game files intact until you start it, at which point your selected patches will apply.  
	Upon closing the game your game's files will be restored.

!!! warning "Overwrite game files"

	You also have the option to `Overwrite game files`, which will **permanently modify your game files**.

	This is **NOT** recommended unless you have a good reason to do so.  
	A backup of your original dll will be created, however it is recommended to make your own!