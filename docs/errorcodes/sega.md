# SEGA Error Codes

!!! info "Synopsis"

    This section contains various SEGA games error codes you might run across and potential steps to resolve them.

## Universal

### 0000

!!! tip "Unexpected Error Occured"

    Data is corrupt, incomplete, or incorrectly modified.  
    Redownload data from trusted source.

### 0032

!!! tip "Unexpected Error Occured"

    Generic network error with multiple symptoms, the most typical of which being enabling DHCP in Windows while the game expects a static IP.
    
    Try adding this to `config_hook.json`:

    ```json
    {
        "network": {
            "property": {
                "dhcp": true
            }
        }
    }
    ```

    If you're copying into an existing `config_hook.json`, remove the outer braces and add a comma to the previous item, like so:
    
    ```json
    {
        "emoney": {
            "enable": false
        },
        "network": {
            "property": {
                "dhcp": true
            }
        }
    }
    ```

    If your game files does not include `config_hook.json`, it is OK to create a new file.  
    Then edit the launch script (usually `launch.bat`) to tell the game about it:
    
    ```
    amdaemon.exe -f -c config_common.json config_server.json config_client.json {++config_hook.json++}
    ```

### 0800

!!! tip "Unknown Error"

    Generic network error usually thrown because the game is not able to connect to a server.

    Make sure that you have correctly entered your network's address in `segatools.ini` under the `[dns]` section:

    ```ini
    [dns]
    ; Can also be an IP address:
    ; default=192.168.34.23
    default=example.com
    ```

### 0919

!!! tip "DVD Drive Remain Error"

    This error occurs if the game detects an enabled DVD drive on the system.  
    To resolve, either disable your computer's DVD drive, or enable DVD drive emulation in `segatools.ini`:

    ```ini hl_lines="2"
    [dvd]
    enable=1
    ```

### 0949

!!! tip "Keychip Not Found"

    Enable keychip emulation in `segatools.ini`:

    ```ini hl_lines="2"
    [keychip]
    enable=1
    ```

    If on a real cabinet using a real keychip, confirm that the keychip is connected properly and working.

### 4104

!!! tip "Unexpected Error Occured"

    Make sure that the game files are not on the `E:` or `Y:` drive.  
    If that is already the case, check if the config files passed to AM Daemon exists and are valid JSON files:

    ```hl_lines="5"
    Runtime exception occurred.
    File: D:\Jenkins\workspace\amdaemon_all_build\libs\amdproc\src\ConfigFileLoader.cpp
    Line: 79
    Function: enum amdaemon::process::ConfigFileLoader::Result __cdecl `anonymous-namespace'::parse(const class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > &,class picojson::value &)
    Message: Cannot open "config_nonexistent.json".
    ```

    ```hl_lines="5 6"
    Runtime exception occurred.
    File: D:\Jenkins\workspace\amdaemon_all_build\libs\amdproc\src\ConfigFileLoader.cpp
    Line: 89
    Function: enum amdaemon::process::ConfigFileLoader::Result __cdecl `anonymous-namespace'::parse(const class std::basic_string<wchar_t,struct std::char_traits<wchar_t>,class std::allocator<wchar_t> > &,class picojson::value &)
    Message: Cannot parse ".\config_hook.json".
    syntax error at line 6 near: }
    ```

### 4105

!!! tip "Unexpected Error Occured"

    Check the AM Daemon window for any "runtime exception" messages, such as:

    ```hl_lines="6"
    amsGfetcherThreadContextInit: Line1345  Error: load Icf failed.
    Runtime exception occurred.
    File: D:\Jenkins\workspace\amdaemon_all_build\libs\libamw\src\amw_netdeliver_context.cpp
    Line: 91
    Function: enum am::util::ModuleContext<3>::Status __cdecl am::netdeliver::Context::initialize(void)
    Message: amGfetcherInit(). ErrCode -1.
    ```

    Then continue by checking [AMDaemon error codes](#amdaemon).

### 6401

!!! tip "I/O board is not connected to main board"

    This error occurs when the game times out trying to communicate with the I/O board.

    When using segatools, this happens because I/O emulation took too long, which is usually caused by long-running background tasks (e.g. Windows Defender, Windows Update, file-syncing software).   
    Try to see if this can be fixed by setting the game process and/or `amdaemon.exe` to high/realtime priority.

### 6501

!!! tip "Aime Card Reader Not Found"

    This error occurs when an Aime card reader is not found.  
    Make sure you enabled Aime card reader emulation in `segatools.ini` if you don't have a physical reader connected:

    ```ini
    [aime]
    enable=1
    ```

### 6503

!!! tip "Failed to read Aime card"

    This error occurs when the Aime card cannot be read.  
    Make sure your connection to the ALL.Net server is good (the network icon in the bottom corner is green).

### 8114

!!! tip "ALL.Net System error (RTC)"

    Make sure you're connected to an ALL.Net server for the first boot, or disable accounting by editing `config_hook.json`:

    ```json
    {
        "allnet_accounting": {
            "enable": false
        }
    }
    ```

    If you're copying into an existing `config_hook.json`, remove the outer braces and add a comma to the previous item, like so:
    
    ```json
    {
        "emoney": {
            "enable": false
        },
        "allnet_accounting": {
            "enable": false
        }
    }
    ```

    If your game files does not include `config_hook.json`, it is OK to create a new file.  
    Then edit the launch script (usually `launch.bat`) to tell the game about it:
    
    ```
    amdaemon.exe -f -c config_common.json config_server.json config_client.json {++config_hook.json++}
    ```

## CHUNITHM

### 3101, 3102

!!! tip "An unexpected error has occurred with the main device<br>Initialization failure with the main device"

    This error occurs when the game fails to communicate with the controller.  
    Check if your controller is connected properly and if ChuniIO DLLs are working.

### 3201, 3202, 3203, 3204, 3205, 3206

!!! tip "Cannot confirm the connection with the side device sensor 1/2/3/4/5/6"

    This error occurs if the air sensors are not functional or blocked during system test.  
    To resolve this, enter and exit Test mode by pressing the F1 key (or 1 on older segatools) then stay clear of your controller.  
    If the error still happens, your air sensors may be faulty.

### 3300

!!! tip "Duplicate servers in the same network"

    If multiple CHUNITHM machines are on the same LAN network, only one of them can be the server (dip switch 1 ON). Set all other machines to dip switch 1 OFF:

    ```ini hl_lines="2"
    [system]
    dipsw1=0
    ```

!!! warning "As of 2024-08-20, the [gpio] section in segatools has been renamed to [system]"

### 3301

!!! tip "Duplicate STANDARD in the same group"

    If multiple CHUNITHM machines are on the same LAN network and cabinet group (A/B/C/D), one of them should set reference machine settings to STANDARD and the rest to FOLLOW THE STANDARD.
    
    Change this by going to Test menu > Game Settings (4th option) > Reference machine settings (2nd option).

### 3400

!!! tip "Monitor Not Supported 120fps"

    This error occurs if your monitor is not set to `1920x1080@120 Hz` at 32-bit color mode.  
    Adjust display settings and try again.

### 3401

!!! tip "Machine Not Supported 120fps"

    This error occurs if you're running the game in CVT mode at 120fps.  
    Use SP mode (dip switch 3 OFF) to run the game in 120fps.  
    In `segatools.ini` this would be:

    ```ini
    [system]
    dipsw3=0
    ```

!!! warning "As of 2024-08-20, the [gpio] section in segatools has been renamed to [system]"

## AMDaemon

### ampdGd1232a01aInit(). ErrCode -4

!!! tip ""

    This error occurs because of a VFD port number mismatch.  

    Update segatools, or if you're using a real VFD, confirm that the VFD uses the same port as specified in `config_common.json` or `config_sp.json` (CHUNITHM) under `emoney.display_port`:
    
    ```json
    "emoney" :
    {        
        "display_port" : 2
    }
    ```

    The value should match the COM port that your real VFD is connected to.

### amAppImageInit(). ErrCode -5

!!! tip ""

    Path to the configured AMFS directory is too long.  
    Ensure that the path is shorter than 16 characters (32 bytes).

### RegCreateKeyExW(). ErrorCode -5

!!! tip ""

    This error occurs because the Windows registry cannot be written to as a normal user.  
    Start the game as administrator **once**, or update segatools.

### amSysFileInitEx(). ErrCode -5

!!! tip ""

    The AMFS folder is read only.  
    Uncheck the read only property in file explorer for the AMFS folder.

### amGfetcherInit(). ErrCode -1

!!! tip ""

    ICF1 is missing in the configured AMFS directory.  
    Get the correct ICF for your game (the game ID in the ICF must be correct).