!!! info "Check out our general [Audio](/extras/audio.md) guide to understand audio modes better, at least the TL;DR"

!!! tip ""

    - Open `spicecfg.exe`
    - At the very top, click on `Shortcuts` then `Audio Playback Devices`
    - In the popup window, right click on your default audio device, and click on `Properties`
    - Go to the `Advanced` tab

    Then, depending follow instructions for your desired audio mode:

??? tip "Setup for WASAPI Exclusive (default)"

    - Check both boxes under `Exclusive Mode`
    - Open the `Default Format` dropdown
    - Pick the `16 bit, 44100 Hz (CD Quality)` option, click `Apply` then `OK`

??? tip "Setup for WASAPI Shared"

    - Open the `Default Format` dropdown
    - Pick the `16 bit, 48000 Hz (DVD Quality)` option, click `Apply` then `OK`
    - Return to `spicecfg`, go to the `Patches` tab
    - Following the [patching guide](/extras/patchsp2x.md) and patch `Shared Mode WASAPI`

    Optionally: go to the `Options` tab, and at the very bottom enable `Low Latency Shared Audio` to help mitigate the latency penalty from using Shared audio.

??? tip "Setup for ASIO (requires specialized hardware)"

    - Check both boxes under `Exclusive Mode`
    - Open the `Default Format` dropdown
    - Pick the `16 bit, 44100 Hz (CD Quality)` option, click `Apply` then `OK`