<img class="header-logo" src="/img/konami/iidx/30_resident/logo.webp">
# Extra Information

## Standard and Lightning modes

!!! warning "Lightning mode requires a 120 Hz capable monitor"

!!! tip ""

    To make use of the Lightning Mode, which unlocks the subscreen and 120FPS, we need to go to the `contents\prop` folder and edit the `ea3-config.xml` file.

    We're interested in these lines:

    ```xml
        <soft>
            <model __type="str">LDJ</model>
            <dest __type="str">J</dest>
            <spec __type="str">A</spec>
            <rev __type="str">A</rev>
            <ext __type="str">2023090500</ext>
        </soft>
    ```

    This is the line that determines if the game will run in Standard (60 FPS) or Lightning (120 FPS) mode.

    ```xml
    <spec __type="str">A</spec>
    ```

    - ^^`A`^^ for Standard (LDJ-003, LDJ, 60 Hz)
    - ^^`E`^^ for Standard (LDJ-012, LDJ, 60 Hz)
    - ^^`D`^^ for Lightning (LDJ-010, TDJ, 120 Hz)
    
## Changing the game's language

!!! tip ""

    This is done in-game before card-in by pressing your `EFFECT` key.

## More about ea3-config.xml

!!! tip ""

    The `ea3-config.xml` file is located inside the `prop` folder. 

    Below is an explanation on what different sections of this file do.

    The following lines change the PCBID and HARDID that your system reports to your e-amusement server.  
    There is ^^**no need to manually change this**^^ as `spice2x` will do it for us.
    
    ```xml
    <pcbid __type="str">00010203040506070809</pcbid>
    <hardid __type="str">00010203040506070809</hardid>
    ```

    The following line determines what version of the game you are running.  
    ^^**You should never change this**^^. It should always say `LDJ`.

    ```xml
    <model __type="str">LDJ</model>
    ```

    The following line determines the game's region.
    ^^**You should never change this**^^. As you can change the language in-game.

    ```xml
    <dest __type="str">J</dest>
    ```

    ^^**You should never change this**^^. It should always say `A` for Resident.

    ```xml
    <rev __type="str">A</rev>
    ```

    The following line determines your datecode.  
    ^^**Always keep it up to date**^^ with your game's current version.

    ```xml
    <ext __type="str">2023090500</ext>
    ```

    The following line determine what remote service URL `spice2x` is supposed to connect to.  
    There is ^^**no need to manually change this**^^ as `spice2x` will do it for us.

    ```xml
    <services __type="str">http://localhost:8083</services>
    ```