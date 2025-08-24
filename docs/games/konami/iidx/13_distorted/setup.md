<img class="header-logo" src="/img/konami/iidx/13_distorted/logo.webp">
# Game Setup

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Preparing data

!!! tip ""

    After downloading and extracting your data, we need to make sure your files aren't set to `Read-only`.

    - Right click the folder containing your data, then click on `Properties`.
    - In the `General` tab go down to `Attributes`, untick `Read-only` and click `Apply`.
    - A popup will appear, select `Apply changes to this folder, subfolder and files` and press `OK`.
    - Finally, click `OK` again to exit out of properties.

## Installing Bemanitools

!!! tip ""
    
    - Download :material-package-down:[Bemanitools](https://github.com/djhackersdev/bemanitools/releases/download/5.48/bemanitools-5.48.zip).
  
    - Inside :material-zip-box:`bemanitools-5.48.zip` locate :material-zip-box:`iidx-13.zip`.

    - Extract everything inside the folder that contains the :material-file:`bm2dx.exe` which is located in :material-folder:`\FDD\JAG`.
    
    Pictured below is what your folder should look like. We've removed any files not necessary for **DistorteD**.

<img src="/img/konami/iidx/13_distorted/setup/1.webp">

### Using iidxhook-13.conf & RtEffect.dll

!!! tip ""

    - Download the :material-package-down:[Bemanitools supplements](https://github.com/djhackersdev/bemanitools-supplement/releases/download/1.6/bemanitools-supplement-1.6.zip)

    - Open :material-zip-box:`bemanitools-supplement-v1.6.zip` and navigate inside :material-zip-box:`misc.zip`

    - Inside :material-folder:`misc\d3d8to9`, extract :material-file-cog-outline:`d3d8.dll` to :material-folder:`\FDD\JAG`.

    This enables us to use the graphic options inside :material-file-code:`iidxhook-13.conf` which we will take advantage of.

    - Open :material-zip-box:`bemanitools-supplement-v1.6.zip` and navigate inside :material-zip-box:`iidx.zip`

    - Inside :material-folder:`iidx/misc`, extract :material-file-cog-outline:`RtEffect_stub.dll` to :material-folder:`\FDD\JAG`.
    
    - Delete the already existing :material-file-remove-outline:`RtEffect.dll` and rename :material-file-edit-outline:`RtEffect_stub.dll` to :material-file-cog-outline:`RtEffect.dll`.
  
    This will eliminate any immediate crashes relating to needing specific old hardware.

### Installing CLVSD.ax

!!! tip ""

    We need to install a codec so that background videos will work and won't cause an error.
    
    - Open :material-zip-box:`bemanitools-supplement-v1.6.zip` and navigate to :material-folder:`\iidx.zip\iidx\misc\` where :material-file:`CLVSD.ax` is located.

    - Extract :material-file:`CLVSD.ax` inside a :material-folder: folder that you know won't be moved or renamed.

    - Open the :material-console:command prompt as ***administrator***. Now type `regsvr32 "<location of the file>\CLVSD.ax"` into the command prompt.

    As an example, it could look like this: `regsvr32 "D:\BEMANI\IIDX\CLVSD.ax"`

    A prompt should appear telling you that it has been installed successfully.
    This applies for all styles that require this codec, not just **DistorteD**.

    If an error occurs, you didn't run the command prompt as administrator or you messed up the location of the file.

!!! danger "You **can not** move or delete :material-file:`CLVSD.ax` **at all**, otherwise it will revert the changes and you have to install it again"

## Configuring Bemanitools

!!! info "To configure your keybinds, open your :material-file:`config.bat` file"

### Buttons

!!! tip ""

    Double click on the right on a button that you wish to bind, then press the key you want associated with the action.

    With your controller and/or keyboard plugged in, configure your keys for:  

    - **Maintenance**: `Service, Test`
    - **P1 Game buttons**: `1 to 7, Start, EFFECT, VEFX` 
    - **P1 Keypad**: `Keypad Insert Card` 

    **Only if** you're playing using a keyboard:

    - **Turntable**: `TT+, TT-` **and optionally** `TT+/-` which alternates between `TT+` and `TT-` on each press.

### Analogs (controller/cab only)

!!! tip ""

    With a controller rather than binding buttons to `TT+` and `TT-`, you need to:

    - Head to the `Analogs` tab at the top.
    - In `Device`, pick your controller.
    - In `Control`, pick whichever one corresponds to the turntable.
    - Turn your turntable ensuring that the preview turns along with it.
    - Click `OK`, leaving the rest of the settings alone.

### Lights (controller/cab only)

!!! tip ""

    Your controller might support having its lights controlled by the game through bemanitools.

    If it does, here's how you may link different actions to your lights:

    - In `Device`, pick your controller.
    - In `Game Light`, select the corresponding button that will be used for that light.
    - Repeat for your other lights.

### Configuring Bemanitools for a network

!!! tip "Head over to the `Network` tab"

!!! tip ""
    Now we will set up our PIN pad and card.
    
    - Click on `Keyboard device`
    - You may or may not have more than one option. To figure out which one is your actual keyboard, select a device inside that list and press a button on the numpad.
    - Once you have found your correct device, the `Keyboard status` will change **(the number and location of the number does not matter, it only matters that it changed)**.
    - Grab your card, create a :material-file-document-edit:`.txt` and name it however you like. In this example it's called :material-file-document-edit:`card.txt`
    - Place the file in a location that is easily accessible and you won't forget. In this case it's in a seperate folder.
    
!!! info "If you don't have a numpad, make sure to tick `Use top keyboard row for PIN pad input`. This will also change the `Card In` button to `Backspace`"

<img src="/img/konami/iidx/13_distorted/setup/2.webp">

## Connecting to a network

!!! tip ""
    
    - Locate your :material-file-code:`iidxhook-13.conf`
    
    - Open it with your desired text editor (we're using [Notepad++](https://notepad-plus-plus.org/))

    - Replace the `eamuse.server=localhost:80` with your desired network URL

    - Replace `eamuse.pcbid=XXXXXXXXXXXXXXXXXXXX` **and** `eamuse.eamid=XXXXXXXXXXXXXXXXXXXX` with your PCBID of your network of choice.
    
    ```
    # URL (e.g. http://my.eamuse.server:80/whatever) or IPV4 (e.g. 127.0.0.1:80) of the target eamuse server. The port is optional but defaults to 80.
    eamuse.server=localhost:80

    # PCBID
    eamuse.pcbid=XXXXXXXXXXXXXXXXXXXX

    # EAMID
    eamuse.eamid=XXXXXXXXXXXXXXXXXXXX
    ```

## Game resolution and locking FPS

!!! tip ""
    We'd like to mention that there are two options when it comes to how the game renders. You can choose between `Linear` and `Point`.

    Below is an example of how both look like.

    ??? info "Linear"
        <img src="/img/konami/iidx/13_distorted/iidx13_linear.webp">

    ??? info "Point"
        <img src="/img/konami/iidx/13_distorted/iidx13_point.webp">
        
    It comes down to your own prefrence what you decide on, `Linear` is less sharp but doesn't have pixel perfect edges. `Point` is sharp and is pixel perfect.

!!! tip ""
    Next up, we'll setup borderless window and configure the proper resolution. We're using a `1920x1080` monitor so we will use that.
    
    Repeat the previous step and open your :material-file-code:`iidxhook-12.conf`. We want to find these lines:
    
    ```
    # Software limit the frame rate of the rendering loop in hz, e.g. 60 or 59.95 (0.0 = no software limit)
    gfx.frame_rate_limit=0.0
    
    # Run the game windowed
    gfx.windowed=false

    # Windowed width, 0 for default size
    gfx.window_width=0

    # Windowed height, 0 for default size
    gfx.window_height=0

    # Up-/downscale the back buffer's width. This does not change the game's rendering resolution but scales the final frame. Use this to target the native resolution of your monitor/TV, e.g. to avoid over-/underscan, bad image quality or latency caused by the monitors internal upscaler. 0 to disable this feature. Must be set in combination with the corresponding height parameter.
    gfx.scale_back_buffer_width=0

    # Up-/downscale the back buffer's height. This does not change the game's rendering resolution but scales the final frame. Use this to target the native resolution of your monitor/TV, e.g. to avoid over-/underscan, bad image quality or latency caused by the monitors internal upscaler. 0 to disable this feature. Must be set in combination with the corresponding width parameter.
    gfx.scale_back_buffer_height=0

    # Filter type to use for up-/downscaling the back buffer. Only used if scaling feature was enabled by setting the scaling width and height parameters. Available types: none, linear, point (refer to D3DTEXTUREFILTERTYPE  for explanation).
    gfx.scale_back_buffer_filter=none
    ```
    
    If you can't seem to find them, press `CTRL` + `F` and search for `gfx.frame_rate_limit=0.0`. This will bring you to the first line we want to edit.
    
!!! tip ""
    Listed below are the values we want to change them to.
    
    ```
    gfx.frame_rate_limit=59.95
    gfx.windowed=true
    gfx.window_width=1920
    gfx.window_height=1080
    gfx.scale_back_buffer_width=1920
    gfx.scale_back_buffer_height=1080
    gfx.scale_back_buffer_filter=linear
    ```
    Unless you'd like to have the game properly windowed you can safely ignore `gfx.framed=false`.

    Make sure to decide on whether you want `Linear` or `Point` rendering.

    ```
    gfx.scale_back_buffer_filter=linear
    gfx.scale_back_buffer_filter=point
    ```

## First launch

!!! danger "If you have any issues running the game, refer to the [Troubleshooting](troubleshooting.md) page"

### BACKUP DATA

!!! tip ""

    If you've followed all instructions correctly, you're now finally ready to launch the game!

    **First plug your controller if you have one** and run :material-file:`gamestart.bat`.

    If it's your first time running the game, you'll immediately be greeted with this screen.

<img src="/img/konami/iidx/13_distorted/firstlaunch/1.webp">

<img src="/img/konami/iidx/13_distorted/firstlaunch/2.webp">

!!! tip ""
    Press your `Test` key to confirm to get to the next error message.

### CLOCK ERROR

<img src="/img/konami/iidx/13_distorted/firstlaunch/3.webp">

!!! tip ""
    Press your `Test` key to confirm. This will bring you into it's service menu.
    
<img src="/img/konami/iidx/13_distorted/firstlaunch/4.webp">

!!! tip ""
    Instructions on how to navigate the menu are shown at the bottom of the screen.

    - Press `1` and `2` to go up and down.
    - Press `6` to select/execute.
    
    Navigate to `CLOCK`. You do not need to manually change it. Navigate to `SAVE AND EXIT`.

<img src="/img/konami/iidx/13_distorted/firstlaunch/5.webp">

### Enabling e-AMUSEMENT for Online Play

!!! tip ""
    From the service menu, go to `NETWORK OPTIONS` then `e-AMUSEMENT SETTINGS`.
    
<img src="/img/konami/iidx/13_distorted/firstlaunch/6.webp">

<img src="/img/konami/iidx/13_distorted/firstlaunch/7.webp">

!!! tip ""
    It'll bring you to this screen, change it so that `e-AMUSEMENT` switches to `ON` and it will look like this:
    
<img src="/img/konami/iidx/13_distorted/firstlaunch/8.webp">

<img src="/img/konami/iidx/13_distorted/firstlaunch/9.webp">

!!! tip ""
    We will need to set a `SHOP NAME SETTING` and change our `PREFECTURE` otherwise the game will throw errors at us.
    
<img src="/img/konami/iidx/13_distorted/firstlaunch/10.webp">

!!! tip ""

    - Name your shop to whatever you'd like. Instructions on how to navigate are at the bottom of the screen.
    - Navigate to `EXIT` and select it.
    - Change your prefecture once or how many times you'd like, it doesn't matter as long as it's not the default one.
    
<img src="/img/konami/iidx/13_distorted/firstlaunch/11.webp">

!!! tip ""
    Select `SAVE AND EXIT`. The game will now give you a message, which translated means: 
    
    `e-AMUSEMENT settings have been changed. Please turn the power off and on again.`
    
    So, close the game and open it again.
    
<img src="/img/konami/iidx/13_distorted/firstlaunch/12.webp">
    
## Final Notes

!!! success "You're all done! Make sure to insert two credits by pressing your `SERVICE` key. Have fun!"

!!! warning "Have any other errors?"
    Check out the [Troubleshooting](troubleshooting.md) section.
