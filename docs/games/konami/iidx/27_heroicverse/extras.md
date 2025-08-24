<img class="header-logo" src="/img/konami/iidx/27_heroicverse/logo.webp">
# Extra Information

--8<-- "docs/snippets/common/old_guide.md"

--8<-- "docs/snippets/common/data_warning.md"

## Notes

!!! tip ""
    Booting the game in Lightning Mode requires a few things. To start off with, you will need to enable the `-iidxtdj` option in SpiceTools and you will also need to enable the `Enable Lightning Mode` patch.

    In doing so, and subsequently every time you choose to switch between the two modes, you will want to delete everything inside your `dev/nvram` folder, and redo the setup process again with initializing the backup date, setting the clock, shop name, and the definition type.

    SpiceTools as of 10/26/2020 has some updated features to work with this as well. Namely, the ability to toggle the Lightning Model subscreen via the `Toggle Subscreen` option in the Buttons tab. You can use your mouse to navigate the touchscreen as desired. Enter your pin, toggle buttons, etc.

    SpiceCompanion has also as of 10/26/2020 added a brand new Screen feature as well. Using SpiceCompanion, you can receive the subscreen on your phone/tablet/etc and then use your device as a touch device for the subscreen. Do note that at this time it will not work while the game is running in windowed mode. If you run into performance issues, go to the settings tab to adjust things like the Screen Quality, Screen Threads, and Screen Divide, this feature is heavily dependent on connection and you will notice as you bump up the quality that the ping will increase as well. It may take some fiddling to find the most ideal settings for your setup.

## Lightning-specific Troubleshooting

!!! tip ""
    Below are the two main issues that have arisen for users utilizing this guide and general startup practices.

## Hardware Specs

!!! tip ""

    Bemani PC Type 11 (ARESPEAR C300)

    Konami (2019)

    Based on KONAMI ARESPEAR C300 gaming PC.

    CPU: Intel i5-9400F 2.9Ghz

    GPU: GIGABYTE GeForce GTX 1650 1530Mhz 4GB

    RAM: 8 GB DDR4

    STORAGE: Innodisk 2.5" 3ME3 SATA SSD 256GB

    AUDIO: ASUS Xonar AE

    OS: Windows 10 IoT Enterprise

## Enabling Lighting Mode Patch

!!! tip ""
    If you get a stack trace in your `log.txt` with the following line...

    `I:stackwalker: 00000001805FC970 (bm2dx): (unknown): dll_entry_main`

    Please enable the lightning mode patch in SpiceTool's patch manager.

## Audio Related Crash

!!! tip ""
    If you get a stack trace in your `log.txt` that looks like this:..

    `exception raised: EXCEPTION_ACCESS_VIOLATION`

    `[2020/10/22 18:20:21] I:signal: printing callstack`

    `[2020/10/22 18:20:21] I:stackwalker: 000000018026E906 (bm2dx): (unknown): (unknown)`

    For cab type 1 (LDJ), change your audio device to motherboard audio and/or use -audiobackend asio `-asiodriverid ... -audiodummy`

    For cab type 2 (TDJ, with `-iidxtdj` or another means), you have a few options:

    1) Use `-iidxasio "Driver Name Here"` to set the ASIO driver used by IIDX's own ASIO handler. (Does not work with all ASIO drivers, they designed it to work best with a specific revision of the XONAR SOUNCARD(64))

    2) Use `-iidxsounddevice wasapi` to set IIDX to use WASAPI instead of its own ASIO handler.

    3) Use `-iidxsounddevice wasapi` along with `-audiobackend asio ...` to have the game pipe audio through Spice's own ASIO handler which is more compatible with various ASIO drivers