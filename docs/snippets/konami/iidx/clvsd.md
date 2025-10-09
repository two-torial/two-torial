!!! tip ""

    In order to have background videos work, we need to install a codec.

    - Inside `bemanitools-supplement-vx.x.zip` that you downloaded locate `iidx.zip`

    - From inside `iidx\misc\`, extract `CLVSD.ax` into any folder on your computer that won't get moved or renamed
        - An example to this can be your Documents folder

    - Open the command prompt as ***administrator***, and type `regsvr32 "[File location]\CLVSD.ax"`
        - In the case of the documents folder, the command will be `regsvr32 "C:\Users\YourUsername\Documents\CLVSD.ax"`

    A prompt should appear telling you that it has been installed successfully.
    This applies for game styles between 12 and 18, if you did it once you don't have to again.

    If an error occurs, you didn't run the command prompt as administrator or you messed up the location of the file.