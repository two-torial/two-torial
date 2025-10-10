<img class="header-logo" src="/img/konami/iidx/16_empress/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

!!! warning "If you get any error codes that weren't listed in the guides here, check out the [Bemanitools docs](https://github.com/djhackersdev/bemanitools/blob/master/doc/game-error-codes.md)"

## Technical problems

### Crashes

!!! info "Riva Tuner Statistics Server (RTSS) and MSI Afterburner are known to cause odd crashes.<br>If you have them installed, close them both before starting any arcade game"

??? tip "I'm using a laptop with a hybrid internal+dedicated GPU setup"

    Laptops often have odd issues running data. The game may open on the wrong monitor, run at the wrong resolution or framerate, or simply crashes.  

    There is currently no known fix for this, other than maybe playing in windowed mode, or using a desktop PC instead. 

### Performance

??? tip "Game is running too slow/fast"

    Your game is likely running at an incorrect framerate. The expected framerates is 59.95fps for S-VIDEO output mode, and 60.05fps for VGA output mode.
    !!! info "For more information regarding output modes, check out the [Extra Information](extras.md) page"
    Try these steps to resolve framerate issues:

    - Double-check that your selected output mode in the service menu matches the refresh rate in your `iidxhook-xx.conf` file.
    - Close any software that can affect framerates (like RTSS)
    - Close unnecessary background programs
    - Ensure V-SYNC is not forcefully disabled in your graphics card control panel

    If issues persist:

    - Double-check that you followed all steps in the setup guide correctly
    - Your data may be corrupt in one way or another, you could try starting from scratch using trusted data sources

!!! info "For issues with desync, check out the [Bemanitools IIDX syncbook](https://github.com/djhackersdev/bemanitools/blob/master/doc/iidxhook/iidx-syncbook.md)"

### Other

??? tip "Background videos not working"

    The CLVSD codec is not registered. Follow the instructions in the [setup guide](setup.md#installing-bemanitools).
    
