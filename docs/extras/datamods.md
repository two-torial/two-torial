!!! info "Synopsis"

    This guide will cover how to mod your KONAMI game's data folder in a non-destructive way.  
    No files will be removed or overwritten.

## Pre-requisites

!!! tip ""

    - A fully working and unmodified game
    - The data to mod your game with

!!! danger "ATTENTION"

    - Please make sure the mod you're installing is **compatible with YOUR specific game and game version**
    - If connecting to an **online network**, make sure they **explicitly allow** the mod you're about to install

## Installing mod files

!!! tip ""

    - Create a `data_mods` folder next to the others in your game files if it doesn't exist

    <img src="/img/extras/datamods/1.webp">

    - Place your mod files inside data_mods in a way that respects the following structure   
        `data_mods/mod_folder/<data folders/<data_files>`

    You can think of the mod folder coming to overwrite your game's data folder at runtime.  
    If you're confused, the following may help you understand what we mean.

    ``` hl_lines="6-11"
    📂data
    ┣━📂graphic
    ┣━📂info
    ┣━📂movie
    ┗━📂sound
    📂data_mods 
    ┗━📂mod_folder
       ┣━📂graphic - Files that modify data/graphic go here
       ┣━📂info    - Files that modify data/info go here
       ┣━📂movie   - Files that modify data/movie go here
       ┗━📂sound   - Files that modify data/sound go here
    📂dev
    📂modules
    📂prop
    ```

!!! info "Example: Omnimix for beatmania IIDX 31 EPOLIS"

    **Directory**: `contents/data_mods/`
    <img src="/img/extras/datamods/2.webp">
    
    **Directory**: `contents/data_mods/omnimix_31`
    <img src="/img/extras/datamods/3.webp">

## Loading mods data files (ifs_layeredfs)

!!! tip ""

    Overwriting game files with mods is heavily discouraged, as there is no clean way of undoing that.
    This is where ifs_layeredfs comes in, to load modded data files without permanently modifying your game data.

    - Download the most recent release of [ifs_layeredfs](https://github.com/mon/ifs_layeredfs/releases/)

    <img src="/img/extras/datamods/4.webp">

    - Open the archive

    <img src="/img/extras/datamods/5.webp">

    - Your game is 32bit *(spice.exe to launch)*: go in the `32bit` folder
    - Your game is 64bit *(spice64.exe to launch)*: go in the `64bit` folder

    <img src="/img/extras/datamods/6.webp">

    - Copy the `ifs_hook.dll` file to your game's `modules` folder

    <img src="/img/extras/datamods/7.webp">

    Follow the [Injecting DLL Hooks](#injecting-dll-hooks) section to load this DLL.

## Installing Omnifix (for IIDX Omnimix only)

!!! info "Compatibility"

    [Supported game versions](https://github.com/aixxe/omnifix?tab=readme-ov-file#compatibility)  
    For unsupported game versions, you'll have to patch Omnimix with [spice2x](patchsp2x.md) or [web](patchweb.md) patching.

!!! tip ""

    Omnimix files require modification of your game DLL which can't be handled by ifs_layeredfs.  
    This is where Omnifix comes in, as a commonly agreed upon way of loading Omnimix for beatmania IIDX. 

    - Download the latest release archive for [omnifix](https://github.com/aixxe/omnifix/releases/) much like you did with ifs_layeredfs
    - Extract the `omnifix.dll` file contained in the archive to your game's `modules` folder

    Follow the [Injecting DLL Hooks](#injecting-dll-hooks) section to load this DLL.

    Note that Omnifix also offers optional [launch parameters](https://github.com/aixxe/omnifix?tab=readme-ov-file#options) you may want to consider.

## Injecting DLL Hooks

!!! tip ""

    Adding DLL files to your modules folder won't necessarily make them load automatically.  
    You sometimes need to tell spice2x to load each file individually, like with the DLLs mentioned in this guide.

    - Open your game's `spicecfg.exe`
    - Head to the `options` tab
    - Find the `Inject DLL Hooks` option under `Common`
    - Add the name of the DLL file(s) you want to load inside the text box

    Example: `ifs_hook.dll omnifix.dll`  
    
    You may list one or multiple DLL files separated by a space.  
    The order does matter, as it dictates in which order the DLL files are loaded.  
    **We recommend loading `ifs_hook.dll` before all else**.

    <img src="/img/extras/datamods/8.webp">
