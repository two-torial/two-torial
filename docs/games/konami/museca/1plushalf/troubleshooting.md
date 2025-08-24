<img class="header-logo" src="/img/konami/museca/logo.webp">
# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

!!! info "For any issues not covered here, spice2x's [Known issues](https://github.com/spice2x/spice2x.github.io/wiki/Known-issues) page might prove useful"

## Technical Problems

??? tip "I'm using a laptop with a hybrid internal+dedicated GPU setup"

    Laptops often have odd issues running data. The game may open on the wrong monitor, run at the wrong resolution or framerate, or simply crashes.  

    There is currently no known fix for this, other than maybe playing in windowed mode, or using a desktop PC instead.

### Performance

!!! info "Check out spice2x's [PC optimization](https://github.com/spice2x/spice2x.github.io/wiki/PC-optimization) guide"

??? tip "Game is running too slow/fast"
    
    Your game is likely running at an incorrect framerate. MÚSECA expects the game to run at 60 fps constantly.
    
    Try these steps to resolve framerate issues:

    - Verify your monitor's refresh ratae is set at exactly 60 Hz.
    - Close any software that can affect framerates (like RTSS)
    - Close unnecessary background programs
    - Ensure V-SYNC is not forcefully disabled in your graphics card control panel
    - For NVIDIA users: Enable `NVIDIA profile optimization (-nvprofile)` in spicecfg's `Options` tab

    If issues persist:

    - Double-check that you followed all steps in the [setup guide](setup.md) correctly
    - Your PC hardware might be insufficient to keep a steady 60 FPS. Make sure your PC meets the requirements of this game.
    - Your data may be corrupt in one way or another, you could try starting from scratch using trusted data sources.

    Your PC may not meet the specifications for MÚSECA. In the arcade, it runs on a Konami PC (ADE-6291):

    - CPU: AMD RX-421BD

    - GPU: Radeon R7

    - RAM: 4 GB

    - OS: Windows 7 Embedded

## Audio

??? tip "I can't hear anything else than the game!"

    Museca only supports [WASAPI exclusive](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) for its audio. This means the game takes exclusive control of your audio device while running, which cannot be changed.

??? tip "I'm not getting any audio/My audio is completely wrecked and I'm using an external DAC!"

    Many external DACs do not work with [WASAPI exclusive mode](https://docs.microsoft.com/en-us/windows/win32/coreaudio/exclusive-mode-streams) and therefore won't function with Museca. Usually, you'll need to use your motherboard's onboard audio or a DAC confirmed to be compatible.

## FAQ

??? tip "How to run the game in windowed borderless mode?"

    You'll need to use 3rd party software like [Borderless Gaming](https://github.com/Codeusa/Borderless-Gaming/releases) in order to achieve this.

??? tip "Can the game be run offline?"

    If your game version is PIX-2018073002, this version supports turning off E-Amusement. In order to do that, change the game code to `J:B:A` (`<spec>B</spec>` in `prop/ea3-config.xml`), disable/disconnect all network adapters and turn set the E-Amusement setting in the game's operator menu to OFF.
