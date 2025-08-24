<img class="header-logo" src="/img/konami/iidx/13_distorted/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

### My Game Is Running Crazy Fast!

!!! tip ""
    The most common reason for this is the game is running over its required 59.95hz, the game is hardcoded to run at 59.95hz and this cannot be changed. To solve this, check [Game resolution and locking FPS](setup.md#game-resolution-and-locking-fps) of the guide again.

### I'm getting "NETWORK WARNING" instead of "NETWORK OK"

!!! tip ""
    This can be caused by:

    - Invalid PCBID
    - Firewall blocking connections
    - Invalid eamuse url or port specified
    - Game is not run using the Administrator account 

### My background videos aren't working!

!!! tip ""

    You need to install a codec.
    
    - Open :material-zip-box:`bemanitools-supplement-v1.6.zip` and navigate to :material-folder:`\iidx.zip\iidx\misc\` where :material-file:`CLVSD.ax` is located.

    - Extract :material-file:`CLVSD.ax` inside a :material-folder: folder that you know won't be moved or renamed.

    - Open the :material-console:command prompt as ***administrator***. Now type `regsvr32 "<location of the file>\CLVSD.ax"` into the command prompt.

    As an example, it could look like this: `regsvr32 "D:\BEMANI\IIDX\CLVSD.ax"`

    A prompt should appear telling you that it has been installed successfully.
    This applies for all styles that require this codec, not just **DistorteD**.

    If an error occurs, you didn't run the command prompt as administrator or you messed up the location of the file.

!!! danger "You **can not** move or delete :material-file:`CLVSD.ax` **at all**, otherwise it will revert the changes and you have to install it again"

### My game crashes immediately!

!!! warning "This can have multiple reasons. These fixes shouldn't be needed for DistorteD since we're addressing them in the guide. We'll add them anyway just in case"

#### Fix #1 (Wrong data structure)

!!! tip ""
    Make sure that your unpacked data looks like this:

    - JAx (Game binary revision folder where 'x' can be A, B, C, D, E, F, G)
    - data
    - sidcode.txt
    
    Any other files are optional and don't have to be removed as these are not required to run the game.

#### Fix #2 (RtEffects.dll didn't get replaced)

!!! tip ""
    Refer to [Using iidxhook-13.conf & RtEffect.dll](setup.md#using-iidxhook-13conf-rteffectdll) again and check if you have followed all the instructions explained in it.