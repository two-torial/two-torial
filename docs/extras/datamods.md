!!! info "Synopsis"

    This guide will cover how to mod your BEMANI game's data folder in a non-destructive way.  
    No files will be removed or overwritten.

## Pre-requisites

!!! tip ""

    - A fully working and unmodified game
    - The data to mod your game with

!!! danger "ATTENTION"

    - Please make sure the mod you're installing is **compatible with YOUR specific game and game version**
    - If connecting to an **online network**, make sure they **explicitly allow** the mod you're about to install
    - TWO-TORIAL will **NOT** provide support with issues caused by mods besides **Omnimix** for beatmania IIDX

## Preparing data_mods

!!! tip ""

    Let's place your mod files in the right folder.

    - Create a `data_mods` folder next to the others in your game files

    <img src="/img/extras/datamods/1.webp">

    Depending on how your mod is packaged, you may or may not need to create another folder to contain it.  
    Inside that folder, the structure should follow the one in `data/`.

    - Place your files inside that `data_mods/mod_folder/`

    If you're confused, the following may help you understand what this means.

    ```
    📂data
    ┣━📂graphic
    ┣━📂info
    ┣━📂movie
    ┗━📂sound
    📂data_mods 
    ┗━📂mod_folder
       ┣━📂graphic <--- Files that modify data/graphic go here
       ┣━📂info <--- Files that modify data/info go here
       ┣━📂movie <--- Files that modify data/movie go here
       ┗━📂sound <--- Files that modify data/sound go here
    📂dev
    📂modules
    📂prop
    ```

!!! info "Example: Omnimix for beatmania IIDX 31 EPOLIS"

    **Directory**: `contents/data_mods/`
    <img src="/img/extras/datamods/2.webp">
    
    **Directory**: `contents/data_mods/omnimix_31`
    <img src="/img/extras/datamods/3.webp">

## Loading data_mods

### Installing ifs_layeredfs

!!! tip ""

    We now need a way for our game to load our mods.

    - Download the most recent release of [ifs_layeredfs](https://github.com/mon/ifs_layeredfs/releases/)

    <img src="/img/extras/datamods/4.webp">

    - Open the archive

    <img src="/img/extras/datamods/5.webp">

    What we're interested in are the `64bit` and `32bit` folders:
    
    - Your game is 32bit *(spice.exe to launch)*: go in the `32bit` folder
    - Your game is 64bit *(spice64.exe to launch)*: go in the `64bit` folder

    <img src="/img/extras/datamods/6.webp">

    - Copy the `ifs_hook.dll` file to your game's `modules` folder

    <img src="/img/extras/datamods/7.webp">

### Loading ifs_layeredfs

!!! tip ""

    All that should be left to do is tell spice2x to load `ifs_hook.dll`.

    - Open your game's `spicecfg.exe`
    - Head to the `options` tab
    - Find the `Inject DLL Hooks` option under `Common` and type in `ifs_hook.dll` then press Enter

    Note: If you have other DLL hooks, simply add more by having a space in between them..  
    Example: `ifs_hook.dll somehook.dll`

    <img src="/img/extras/datamods/8.webp">

    Assuming your `data_mods` folder has been made properly, that's it!

!!! danger "Extra step for beatmania IIDX Omnimix"

    You also need to patch your game's DLL with the `Omnimix` patch.
    
    For more information on how to patch your game, head over to the [spice2x Patching](/extras/patchsp2x.md) page!