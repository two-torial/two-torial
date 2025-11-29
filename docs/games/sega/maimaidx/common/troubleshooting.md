# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

### My game crashes on launch/stuck on "Starting System Process"

!!! tip ""

    Could be due to **many** things, the most common of which are:

    - `amdaemon` crashing in the background. Make sure that the `config_*.json` files
    have valid syntax, your ICF files are correct.

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
    start /b "AM Daemon" /min inject -d -k mai2hook.dll amdaemon.exe -f -c config_common.json config_server.json
    ping 127.0.0.1 -n 31 > nul && taskkill /F /im amdaemon.exe
    ```

    Double-click it to run. The script should run for 30 seconds, and you will get a file
    named `amdaemontest.txt` in `App\bin`, which you can send to help people troubleshoot your issue.

### My game is stuck on a black screen at launch!

!!! tip ""

    This could also be due to **many** things, the most common of which are:

    - You have one or more incorrect/broken DLL(s) in `App\Package\Sinmai_Data\Managed`

        This is likely to be `Assembly-CSharp.dll`, `Assembly-CSharp-firstpass.dll`, and/or `AMDaemon.NET.dll`.
        You can try replacing the DLLs or re-downloading data from elsewhere.

    - An ill-formed keychip is defined in `segatools.ini`

### My game is stuck on a blue and black screen!

!!! tip ""
    You need to run the data using unprotected/unpacked files. Please refer to the setup guide to find which ones you need and obtain them.

    If you believe you've already done this. You might be missing a try installing the latest [vcredist](https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/)

### My game is running too slow/fast or the notes are out of sync!

!!! tip ""

    The game could be running under or over its required refresh rate.

    - Make sure V-Sync isn't disabled in your graphics settings (called "Vertical sync"
    in NVIDIA Control Panel and "Wait for Vertical Refresh" in AMD Control Panel.)
    - Limit `Sinmai.exe` to run at 60 FPS using a tool like [RivaTuner](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download) or a patch.

    It could also be that your computer's performance isn't good enough to keep
    a steady framerate.
