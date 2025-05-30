# Game Patching (hex editing)

!!! danger "Before proceeding"

    **This guide should ONLY be used as a last resort if all other methods fail.**  
    **It has a high chance of breaking your game, make backups.**

## Preamble

!!! tip ""

    We're going to patch Beatmania IIDX 25 CANNON BALLERS, however the process is similar for other BEMANI games.

    Here's what you'll need:

    - Your favorite hex editor, here we'll be using [HxD](https://mh-nexus.de/en/hxd/).
    - A clean copy of your desired BEMANI game.
    - A backup of your original `.dll` before editing.

## Getting Started

!!! tip ""

    Decide on what hex edits you want to apply, you may find that information from the community or our [Resources](/resources.md).
    
    It's time to open our hex editor. If you're using HxD, you'll be greeted with the screen below.

<img src="/img/extras/hexguide/1.webp">

!!! tip ""

    Open your game's `.dll` file in the hex editor.
    
    For the grand majority of hex edits, this is the main game file, such as `bm2dx.dll`, `soundvoltex.dll`, etc.
    
    Pictured below, we've opened up `bm2dx.dll` inside HxD.

<img src="/img/extras/hexguide/2.webp">

!!! danger "Attention"

    The edit we'll be applying is **EXCLUSIVE to this version of the game** and serves as an example.
    
    This means it will not work on any other version of the game, nor any other game!  
    Hex edits modify specific memory addresses that only apply to very specific game versions.

!!! tip ""

    We'll be editing our game to `Unlock All Songs` and its edit is:
    
    - **Offset**: `0xB60B2`
    - **Original**: `74 10`
    - **Modified**: `90 90`
    
    In HxD we're going to hit `Ctrl+G` to open the `Goto` window. 
    
    From here, we'll input the offset `B60B2` in the `Offset` section as shown below, and hit `OK`.

<img src="/img/extras/hexguide/3.webp">

!!! tip ""

    Our cursor should be taken to the offset at the exact location you want to edit.
    
    As you can see, the numbers in front of the cursor are `74` and `10` which corresponds to what we need to replace.
    
    **If there's a mismatch, it's likely the offset you've put in was wrong, so be sure to double check!**

<img src="/img/extras/hexguide/4.webp">

!!! tip ""

    Now all we need to do is select `74 10` and replace it with `90 90`.

    You can do this by either manually typing `90 90` or by copy and pasting.
    
    It should now look as shown below.

<img src="/img/extras/hexguide/5.webp">

!!! tip ""

    Lastly, simply save your file and repeat these steps for any other edits you want to apply!

    If at any point your game has issues due to your edits, restore your backup.