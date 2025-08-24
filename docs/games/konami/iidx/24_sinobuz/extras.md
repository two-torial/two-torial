<img class="header-logo" src="/img/konami/iidx/24_sinobuz/logo.webp">
# Extra Information

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

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

    ^^**You should never change this**^^. It should always say `A` for SINOBUZ.

    ```xml
    <rev __type="str">A</rev>
    ```

    The following line determines your datecode.  
    ^^**Always keep it up to date**^^ with your game's current version.

    ```xml
    <ext __type="str">2017082800</ext>
    ```

    The following line determine what remote service URL `spice2x` is supposed to connect to.  
    There is ^^**no need to manually change this**^^ as `spice2x` will do it for us.

    ```xml
    <services __type="str">http://localhost:8083</services>
    ```