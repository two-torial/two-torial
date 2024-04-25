# Sound Voltex EXCEED GEAR Valkyrie Model Information

<img src="/img/sdvx6/eg.png">

### ea3-config.xml Explanation

!!! tip ""

    The `ea3-config.xml` is located inside the `contents\prop\` folder. You might see a lot of different files but we're only interested in the one that's specifically named `ea3-config.xml`.

    Below is an explanation on what the parameters do.

    ```
    <id>
        <pcbid __type="str">00010203040506070809</pcbid>
        <hardid __type="str">00010203040506070809</hardid>
    </id>
    ```
    

    ```
    <pcbid __type="str">:
    ```
    This option changes the PCBID that your system reports to your e-amusement server. There is ^^**no need to manually change this**^^ as `spice2x` will do it for us when we configure it inside of `spice2x`.

    ```
    <hardid __type="str">:
    ```
    This option changes the Hardware ID that your system reports to your e-amusement server. Changing this isn't required to make the game functional.

    !!! tip ""

    ```
    <soft>
        <model __type="str">KFC</model>
        <dest __type="str">J</dest>
        <spec __type="str">F</spec>
        <rev __type="str">A</rev>
        <ext __type="str">2023042500</ext>
    </soft>
    ```

    ```
    <model __type="str">KFC</model>
    ```

    This option determines what version of the game you are running. You should never changes this. It should always say KFC. 

    ```
    <dest __type="str">:
    ```

    This option determines what region the game is running in. Use ^^`J`^^ for Japanese, ^^`K`^^ for Korean, or ^^`A`^^ for English.

    ```
    <spec __type="str">:
    ```

    This option determines if you are running the game in Nemsys or Valkyrie mode. Use ^^`F`^^ for Nemsys mode or ^^`G`^^ for Valkyrie mode.

    ```
    <ext __type="str">:
    ```

    This option determines your datecode. Always keep it up to date with the datacode you'd like to run.

    !!! tip ""

    ```
    <network>
        <services __type="str">http://localhost:8083</services>
    </network>
    ```

    This option determine what Service URL Server `spice2x` is supposed to connect to. You do not need to manually edit this, as `spice2x` does it for us.

### Setting up Valkyrie Model (Subscreen & 120FPS)

!!! tip ""
	To make use of the Valkyrie Model, which utilizes the subscreen and 120FPS, we need to go into `contents\prop` folder and open the `ea3-config.xml` file.
    I'll be using [Notepad++](https://notepad-plus-plus.org/) for that.

    In there, we're interested in these lines:
    ```    
    <soft>
        <model __type="str">KFC</model>
        <dest __type="str">J</dest>
        <spec __type="str">F</spec>
        <rev __type="str">A</rev>
        <ext __type="str">2023042500</ext>
    </soft>
    ```

    `<spec __type="str">F</spec>` This line actually determines if the game will run in Nemsys (Old, 60FPS) or Valkyrie (New, 120FPS) mode.

    `F` will be Nemsys and `G` will be Valkyrie.

    So your line should look like this:
 
    `<spec __type="str">G</spec>`

<img src="/img/sdvx6/valk_model.png">

!!! tip ""

    Please keep in mind that in order to run Valkyrie Model like intended, you'll need atleast two monitors, one 120Hz and one 60Hz with touchscreen capabilities.

    If you do not meet these requirements but still want to get all the benefits of it, open up your `spicecfg.exe` and enable `Only Use One Monitor`. 
    
<img src="/img/sdvx6/1monitor.png">
    
!!! tip ""

    This will ensure that the subscreen will be accessible with only one monitor, which you can make use of with your mouse as a touchscreen subsitute.

    Next, head over to the `Overlay` tab and configure the key for `Toggle Subscreen`. I've set it to `Prt Scr` but you can use what ever key you'd like.

<img src="/img/sdvx6/toggle_subs.png">

### Changing the games language

!!! tip ""

    Go into `contents\prop` folder and open the `ea3-config.xml` file.
    I'll be using [Notepad++](https://notepad-plus-plus.org/) for that.

    In there, we're interested in these lines:
    ```    
    <soft>
        <model __type="str">KFC</model>
        <dest __type="str">J</dest>
        <spec __type="str">F</spec>
        <rev __type="str">A</rev>
        <ext __type="str">2023042500</ext>
    </soft>
    ```

    `<dest __type="str">J</dest>` This line determines in what language the game is supposed to run.

    Use ^^`J`^^ for Japanese, ^^`K`^^ for Korean, or ^^`A`^^ for English.

    In my case, I'll be using English.

<img src="/img/sdvx6/lang.png">