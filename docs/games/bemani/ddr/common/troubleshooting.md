# Troubleshooting

--8<-- "docs/snippets/common/data_warning.md"

!!! info "For any issues not covered here, spice2x's [Known issues](https://github.com/spice2x/spice2x.github.io/wiki/Known-issues) page might prove useful"

## Technical problems

### Crashes

??? tip "Game crashes on startup or when starting a song / No background and no music video"

    This is likely caused by missing or incorrectly registered codecs. Make sure to follow the DDR section on the [spice2x wiki](https://github.com/spice2x/spice2x.github.io/wiki/DLL-Dependencies#ddr).

### Performance

!!! info "Check out spice2x's [PC optimization](https://github.com/spice2x/spice2x.github.io/wiki/PC-optimization) guide"

??? tip "Game is running too slow/fast"

    Try to eliminate any unnecessary background processes during play and ensure your screen's framerate is set to 60 FPS.

## Other

??? tip "Where are the option for Dancers/Shading/Measure lines/Fast-Slow/Layering?"

    These options are locked behind network requirements and will not be displayed unless you are connected to a network that has written support for these options. Patches are available to mitigate this, see our [spice2x Patching guide](/extras/patchsp2x.md).