!!! danger "Please make sure you downloaded your data from an appropriate source.<br>This guide is unable to troubleshoot any problems related to bad or poorly managed data."

---

### My game takes a long time to boot!

!!! tip ""

    CHUNITHM game files consist of thousands of small XML files, which Windows Defender
    takes a long time to scan through. Add your game folder to the Windows Defender
    exclusion list.

!!! danger

    Doing this will prevent Windows Defender from scanning your game folder for viruses.
    Only do this if you trust the source of the data.

---

### My game is running too slow/fast

!!! tip ""

    The game could be running under or over its required refresh rate.
    
    - Make sure V-Sync isn't disabled in your graphics settings (called "Vertical sync"
    in NVIDIA Control Panel and "Wait for Vertical Refresh" in AMD Control Panel.)
    - Make sure your monitor's refresh rate is set to 60Hz.

    It could also be that your computer's performance isn't good enough to keep
    a steady framerate.

---

### My game is stuttering

!!! tip ""

    For NVIDIA users, create an override for `chuniApp.exe` in NVIDIA Control Panel
    and change "Power management mode" to "**Prefer maximum performance**".

---

### My game crashes when I tab out of fullscreen!

!!! tip ""

    As the game is intended to run on arcade hardware, it doesn't like being minimized.
    
    One workaround for this is to use DXVK. Download the latest version from [releases](https://github.com/doitsujin/dxvk/releases/latest).
    This will be a `dxvk-x.y.z.tar.gz` file, which you can open using [7zip](https://www.7-zip.org/).
    Navigate to the `x32` folder, and copy the `d3d9.dll` file to your game's `App\bin` folder, agreeing
    to overwrite when asked.

    You should now be able to tab out of fullscreen without crashing the game.

!!! warning

    The game will not ignore inputs when out of focus.
    
    This means any controller inputs will still be accepted, so try not to lean onto
    your slider whilst tabbed out!

    This also means that you can accidentally enter the service menu by hitting your
    `Test` key even if the game is minimised. If you were in the middle of a credit,
    **your scores will be lost.**

---

### When I run the game all other audio is gone!

!!! tip ""

    CHUNITHM uses [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams)
    for audio to get better latency.

    You can apply the "Shared Audio" patch on a CHUNITHM web patcher (see [Resources](/resources.md#web-patchers))
    to hear audio outside of the game at the cost of audio latency.

---

### Cabinet-to-Cabinet(c2c) Fixes

!!! tip ""

    c2c can have many problems but you can fix most of them by applying the "Patch for head-to-head play" and disabling "Set all timers to 999" on a CHUNITHM web patcher (see [Resources](/resources.md#web-patchers)).

    If the above does not work then please ensure both machines have the exact same data and can communicate with each other if they cannot then you can try disabling firewalls or changing the c2c group.

    If clicking the c2c button does nothing, you can fix it by resetting the network settings in Windows.
