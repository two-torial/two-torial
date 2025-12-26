<img class="header-logo" src="/img/konami/sdvx/7_nabla/logo.webp">
# Extra Information

--8<-- "docs/snippets/common/data_warning.md"

!!! warning "Starting with Nabla, Nemsys cabs (60 FPS mode) are no longer officially supported"

    However the F spec and BIO2/Valkyrie 60hz patches still seem to work for the time being, though beware things most likely will break in the future.

# Nemsys and Valkyrie modes

!!! warning "Valkyrie mode requires a 120 Hz capable monitor, or to have patched your `.dll` with `Valkyrie Mode 60 Hz`"

!!! tip ""

    To make use of the Valkyrie Mode (Subscreen, 120FPS, S-CRITICAL..) you need to go to the `contents\prop` folder and edit the `ea3-config.xml` file.

    We're interested in these lines:

    ```xml
        <soft>
            <model __type="str">KFC</model>
            <dest __type="str">J</dest>
            <spec __type="str">G</spec>
            <rev __type="str">A</rev>
            <ext __type="str">2025122401</ext>
        </soft>
    ```

    This is the line that determines if the game will run in Nemsys (60 FPS) or Valkyrie (120 FPS) mode.

    ```xml
    <spec __type="str">G</spec>
    ```

    Use:

    - ^^`F`^^ for Nemsys  
    - ^^`G`^^ for Valkyrie
    
## Changing the game's language

!!! tip ""

    Go to the `contents\prop` folder and edit the `ea3-config.xml` file.

    We're interested in these lines:

    ```xml
        <soft>
            <model __type="str">KFC</model>
            <dest __type="str">J</dest>
            <spec __type="str">G</spec>
            <rev __type="str">A</rev>
            <ext __type="str">2025122401</ext>
        </soft>
    ```

    This is the line that determines which region, and therefore which language the game will use.

    ```xml
    <dest __type="str">J</dest>
    ```

    Use:

    - ^^`J`^^ for Japan (Japanese)  
    - ^^`K`^^ for Korea (Korean + some censored jackets)  
    - ^^`A`^^ for Asia/Australia (English)  
    - ^^`U`^^ for America (English + some censoring in recent versions)  
    - ^^`Y`^^ for Indonesia

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
    ^^**You should never change this**^^. It should always say `KFC`.

    ```xml
    <model __type="str">KFC</model>
    ```

    ^^**You should never change this**^^. It should always say `A` for Nabla.

    ```xml
    <rev __type="str">A</rev>
    ```

    The following line determines your datecode.  
    ^^**Always keep it up to date**^^ with your game's current version.

    ```xml
    <ext __type="str">2025122401</ext>
    ```

    The following line determine what remote service URL `spice2x` is supposed to connect to.  
    There is ^^**no need to manually change this**^^ as `spice2x` will do it for us.
    
    ```xml
    <services __type="str">http://localhost:8083</services>
    ```