# Sound Voltex EXCEED GEAR Valkyrie Model Information

<img src="/img/sdvx6/eg.png">

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