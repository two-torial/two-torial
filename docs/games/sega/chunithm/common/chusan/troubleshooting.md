# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

### My game crashes on launch!

!!! tip ""

    Could be due to **many** things, the most common of which are:
    
    - `amdaemon` crashing in the background. Make sure that the `config_*.json` files
    have valid syntax, your ICF files are correct.
    - Using the incorrect dipswitch settings for your refresh rate (e.g. `dipsw3=0` on
    a 60 Hz screen). Refer to the game setup guide to fix it.
    - Enabling 120FPS on a monitor that is not **exactly 120 Hz** or **exactly 1080p**.
    If you cannot set your monitor's refresh rate to 120 Hz, apply the "Bypass 120 Hz
    monitor check"/"Bypass 1080p monitor check" on a CHUNITHM web patcher (see [Resources](/resources.md#web-patchers)).
    
??? info "Capturing logs from `amdaemon` for troubleshooting"

    To assist with troubleshooting, a script can be used to capture logs from `amdaemon`. Create a file named
    `amdaemontest.bat` in `App\bin`, then paste the code block below into the file.

    ```batch
    @echo off
    cls
    echo Attempting to run AM Daemon ...
    echo Window should close after 30 seconds
    echo Log will be generated at amdaemontest.txt
    call :sub >amdaemontest.txt
    exit /b

    :sub
    pushd %~dp0
    start /b "AM Daemon" /min inject_x64 -d -k chusanhook_x64.dll amdaemon.exe -c config_common.json config_server.json config_client.json config_cvt.json config_sp.json config_hook.json
    ping 127.0.0.1 -n 31 > nul && taskkill /im amdaemon.exe
    ```

    Double-click it to run. The script should run for 30 seconds, and you will get a file
    named `amdaemontest.txt` in `App\bin`, which you can send to help people troubleshoot your issue.

### My game takes a long time to boot!

!!! tip ""

    CHUNITHM game files consist of thousands of small XML files, which Windows Defender
    takes a long time to scan through. Add your game folder to the Windows Defender
    exclusion list.

!!! danger

    Doing this will prevent Windows Defender from scanning your game folder for viruses.
    Only do this if you trust the source of the data.

### My game is running too slow/fast

!!! tip ""

    The game could be running under or over its required refresh rate.
    
    - Make sure V-Sync isn't disabled in your graphics settings (called "Vertical sync"
    in NVIDIA Control Panel and "Wait for Vertical Refresh" in AMD Control Panel.)
    - Make sure your monitor's refresh rate is set to 60 Hz or 120 Hz.

    It could also be that your computer's performance isn't good enough to keep
    a steady framerate.

### My game is stuttering

!!! tip ""

    For NVIDIA users, create an override for `chusanApp.exe` in NVIDIA Control Panel
    and change "Power management mode" to "**Prefer maximum performance**".

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

### When I run the game all other audio is gone!

!!! tip ""

    CHUNITHM uses [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams)
    for audio to get better latency.

    You can apply the "Shared Audio" patch on a CHUNITHM web patcher (see [Resources](/resources.md#web-patchers))
    to hear audio outside of the game at the cost of audio latency.

### Cabinet-to-Cabinet(c2c) Fixes

!!! tip ""

    c2c can have many problems but you can fix most of them by applying the "Patch for head-to-head play" and disabling "Set all timers to 999" on a CHUNITHM web patcher (see [Resources](/resources.md#web-patchers)).

    If the above does not work then please ensure both machines have the exact same data and can communicate with each other if they cannot then you can try disabling firewalls or changing the c2c group.

    If clicking the c2c button does nothing, you can fix it by resetting the network settings in Windows.
