<img class="header-logo" src="/img/konami/sdvx/6_exceedgear/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

!!! info "For any issues not covered here, spice2x's [Known issues](https://github.com/spice2x/spice2x.github.io/wiki/Known-issues) page might prove useful"

## Technical problems

### Crashes

!!! info "Riva Tuner Statistics Server (RTSS) and MSI Afterburner are known to cause odd crashes.<br>If you have them installed, close them both before starting any arcade game"

??? tip "`W:BM2D: CreateLayer() 指定したレイヤーは存在しません` then `EXCEPTION_ACCESS_VIOLATION` in logs"

    - Open `log.txt` using an editor that supports `SHIFT-JIS` encoding for Japanese text (like [Notepad++](https://notepad-plus-plus.org/downloads/))
    
    - Look for this error message: `W:BM2D: CreateLayer() 指定したレイヤーは存在しません touch_effect`   
    *Note: While `touch_effect` is common, the missing resource name may vary*

    If you find it, and it's followed by: `W:signal: exception raised: EXCEPTION_ACCESS_VIOLATION`  
    
    Then there's a **problem with your game data**.

    - Make sure there are no DLL files next to the main game directories (`data`, `prop`, etc.)  
    If there are, **move them all** under the `modules` directory 

    For game version `2024-11-05` and newer, check the following files in your `modules` directory:

    - `afp-core.dll` should be 1,015 KB  
    - `afp-utils.dll` should be 179 KB

    If the sizes don't match:

    - Redownload `2024110500` and newer updates  
    - Re-apply all updates in chronological order, always copying **all** DLL files to the `modules` directory

    If the issue isn't resolved by now, **we recommend performing a fresh installation using trusted data sources**.

??? tip "`W:SuperstepSound: Audio device is not available!!!` in logs"

    - Open `log.txt` using an editor that supports `SHIFT-JIS` encoding for Japanese text (like [Notepad++](https://notepad-plus-plus.org/downloads/))

    - Search for `Superstep`

    If you find a line with `Audio device is not available!!!`, it means the game refuses to boot due to a misconfigured or missing audio device.   
    Check the setup guide's [Configuring audio section](setup.md#configuring-audio) as well as our general [Audio guide](/extras/audio.md) to understand the issue better.

??? tip "I'm using a laptop with a hybrid internal+dedicated GPU setup"

    Laptops often have odd issues running data. The game may open on the wrong monitor, run at the wrong resolution or framerate, or simply crashes.  

    There is currently no known fix for this, other than maybe playing in windowed mode, or using a desktop PC instead.

### Performance

!!! info "Check out spice2x's [PC optimization](https://github.com/spice2x/spice2x.github.io/wiki/PC-optimization) guide"

??? tip "Game is running too slow/fast"

    Your game is likely running at an incorrect framerate. The expected framerates are:

    - Nemsys mode: 60 FPS
    - Valkyrie mode: 120 FPS

    Try these steps to resolve framerate issues:

    - Close any software that can affect framerates (like RTSS)
    - Close unnecessary background programs
    - Ensure V-SYNC is not forcefully disabled in your graphics card control panel
    - For NVIDIA users: Enable `NVIDIA profile optimization (-nvprofile)` in spicecfg's `Options` tab

    If issues persist:

    - Double-check that you followed all steps in the [setup guide](setup.md) correctly
    - Your PC hardware might be insufficient to keep a steady 120 FPS, you can try to either:
        - [Patch](/extras/patchsp2x.md) the game with `Valkyrie Mode 60 Hz` to stick in Valkyrie mode but run at 60 FPS
        - [Switch to Nemsys mode](extras.md#nemsys-and-valkyrie-modes)
    - Your data may be corrupt in one way or another, you could try starting from scratch using trusted data sources.

### Audio

!!! info "Check out our [Audio](/extras/audio.md) guide to understand audio modes better"

!!! info "Ensure your default audio device's sample rate is set properly"

    - **44100 Hz** sample rate for **WASAPI Exclusive** and **ASIO**
    - **48000 Hz** if your game is patched with `Shared Mode WASAPI`

??? tip "I can't change my device's sample rate"

    If you're using gaming peripherals (Logitech/Razer/Steelseries) or external audio devices (audio interfaces/sound bars):

    - Check if you can modify the sample rate in the device's software/control panel
    - If not, try uninstalling the device's software. This may restore control over Windows audio settings

    If you still can't change the sample rate:

    - Configure the game's audio mode to match your device's current sample rate instead
    - Try using a different audio device

??? tip "I can't hear anything else than the game"

    Your game's audio is setup to run in WASAPI Exclusive or ASIO modes.

    Check out our [Audio](/extras/audio.md) guide to understand audio modes better.

    If you're using WASAPI Exclusive, you'll want to [patch the game](/extras/patchsp2x.md) with `Shared Mode WASAPI` to hear other applications.

    If you're using ASIO, unless your audio interface mixes WASAPI and ASIO streams when outputting, you'll only be able to hear one application when ASIO is in use.  
    In this case, you'll need to route all audio through software such as [Voicemeeter](https://vb-audio.com/Voicemeeter/banana.htm), and have Voicemeeter output the mix to your ASIO device.

??? tip "Game audio is too quiet/loud"

    - Make sure to not be in a credit as your current progress will be lost
    - Bind and press your `Test` key to enter the Test menu
    - Go to `SOUND OPTIONS` and change the volume at will
    - `SAVE AND EXIT` > `GAME MODE` to return to the game

### Subscreen

!!! info "For more in-depth troubleshooting, refer to the spice2x [Subscreen troubleshooting](https://github.com/spice2x/spice2x.github.io/wiki/Configuring-touch-screens-as-subscreen#troubleshooting) page"

??? tip "Touch input isn't being registered"

    If you're using a physical touch screen, make sure to close **all** spice2x overlays, including the FPS counter.  
    If you're using the virtual subscreen, ensure that the `-sdvxnativetouch` option is not enabled.

## FAQ

??? tip "How to run the game in windowed borderless mode?"

    You'll need to use 3rd party software like [Borderless Gaming](https://github.com/Codeusa/Borderless-Gaming/releases) in order to achieve this.

??? tip "Where are all the navigators? Why am I missing songs?"

    A lot of content is locked behind events and will not show up unless connected to a network that has written support for these events.

    It may also be that the content is only available in specific regions like Japan and your game is configured with another region.

    You can fix this by [patching](/extras/patchsp2x.md) `Fake Region` to `Japan (J)`.
