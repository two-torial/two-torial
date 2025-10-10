!!! tip ""

    For background movies to work, you need to install and register a codec.

    This also applies for IIDX 12 to 18, if you'd done it before you shouldn't need to again and may skip this step.

    - Inside `bemanitools-supplement-vx.x.zip` locate and open `iidx.zip`

    - Inside `iidx\misc\`, extract `CLVSD.ax` to any directory where the file can stay long term  
    As an example we will be using your Documents folder, but it really could be anywhere you prefer.

    - Open a command prompt as ***administrator***, and run `regsvr32 "CHOSEN_PATH\CLVSD.ax"`  
    For the Documents folder, the command would be `regsvr32 "C:\Users\YOUR_USERNAME\Documents\CLVSD.ax"`

    You should get confirmation that the file has been registered successfully.

    If an error occurs, you most likely didn't start your command prompt as administrator, or the location to CLVSD.ax was incorrect.

