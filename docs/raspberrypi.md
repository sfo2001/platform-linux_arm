::: wy-grid-for-nav
::: wy-side-scroll
::: wy-side-nav-search
[](../index.html)

::: {role="search"}
:::
:::

::: {.wy-menu .wy-menu-vertical spy="affix" role="navigation" aria-label="Navigation menu"}
-   [What is PlatformIO?](../what-is-platformio.html){.reference
    .internal}

[Getting Started]{.caption-text}

-   [PlatformIO IDE](../integration/ide/pioide.html){.reference
    .internal}
-   [PlatformIO Core (CLI)](../core/index.html){.reference .internal}
-   [PlatformIO Home](../home/index.html){.reference .internal}
-   [PlatformIO Account](../plus/pio-account.html){.reference .internal}
-   [Tutorials and Examples](../tutorials/index.html){.reference
    .internal}

[Configuration]{.caption-text}

-   [platformio.ini](../projectconf/index.html){.reference .internal}
-   [Build
    Configurations](../projectconf/build_configurations.html){.reference
    .internal}
-   [Environment Variables](../envvars.html){.reference .internal}

[Instruments]{.caption-text}

-   [Library Management](../librarymanager/index.html){.reference
    .internal}
-   [Platforms](index.html){.reference .internal}
    -   [Embedded](index.html#embedded){.reference .internal}
        -   [Aceinna IMU](aceinna_imu.html){.reference .internal}
        -   [Atmel AVR](atmelavr.html){.reference .internal}
        -   [Atmel megaAVR](atmelmegaavr.html){.reference .internal}
        -   [Atmel SAM](atmelsam.html){.reference .internal}
        -   [CHIPS Alliance](chipsalliance.html){.reference .internal}
        -   [Espressif 32](espressif32.html){.reference .internal}
        -   [Espressif 8266](espressif8266.html){.reference .internal}
        -   [Freescale Kinetis](freescalekinetis.html){.reference
            .internal}
        -   [Heltec CubeCell](heltec-cubecell.html){.reference
            .internal}
        -   [Intel ARC32](intel_arc32.html){.reference .internal}
        -   [Intel MCS-51 (8051)](intel_mcs51.html){.reference
            .internal}
        -   [Lattice iCE40](lattice_ice40.html){.reference .internal}
        -   [Maxim 32](maxim32.html){.reference .internal}
        -   [Microchip PIC32](microchippic32.html){.reference .internal}
        -   [Nordic nRF51](nordicnrf51.html){.reference .internal}
        -   [Nordic nRF52](nordicnrf52.html){.reference .internal}
        -   [NXP i.MX RT](nxpimxrt.html){.reference .internal}
        -   [NXP LPC](nxplpc.html){.reference .internal}
        -   [OpenHW Group](openhw.html){.reference .internal}
        -   [Raspberry Pi RP2040](#){.current .reference .internal}
            -   [Examples](#examples){.reference .internal}
            -   [Debugging](#debugging){.reference .internal}
            -   [Stable and upstream
                versions](#stable-and-upstream-versions){.reference
                .internal}
            -   [Packages](#packages){.reference .internal}
            -   [Frameworks](#frameworks){.reference .internal}
            -   [Boards](#boards){.reference .internal}
        -   [Renesas RA](renesas-ra.html){.reference .internal}
        -   [RISC-V GAP](riscv_gap.html){.reference .internal}
        -   [Shakti](shakti.html){.reference .internal}
        -   [SiFive](sifive.html){.reference .internal}
        -   [Silicon Labs EFM32](siliconlabsefm32.html){.reference
            .internal}
        -   [ST STM32](ststm32.html){.reference .internal}
        -   [ST STM8](ststm8.html){.reference .internal}
        -   [Teensy](teensy.html){.reference .internal}
        -   [TI MSP430](timsp430.html){.reference .internal}
        -   [TI TIVA](titiva.html){.reference .internal}
    -   [Desktop](index.html#desktop){.reference .internal}
-   [Frameworks](../frameworks/index.html){.reference .internal}
-   [Boards](../boards/index.html){.reference .internal}
-   [Custom Platform & Board](custom_platform_and_board.html){.reference
    .internal}

[Advanced]{.caption-text}

-   [Scripting](../scripting/index.html){.reference .internal}
-   [Debugging](../plus/debugging.html){.reference .internal}
-   [Unit Testing](../advanced/unit-testing/index.html){.reference
    .internal}
-   [Static Code
    Analysis](../advanced/static-code-analysis/index.html){.reference
    .internal}
-   [Remote Development](../plus/pio-remote.html){.reference .internal}

[Integration]{.caption-text}

-   [Cloud & Desktop IDEs](../integration/ide/index.html){.reference
    .internal}
-   [Continuous Integration](../integration/ci/index.html){.reference
    .internal}
-   [Compilation database [`compile_commands.json`{.docutils .literal
    .notranslate}]{.pre}](../integration/compile_commands.html){.reference
    .internal}

[Miscellaneous]{.caption-text}

-   [FAQ](../faq/index.html){.reference .internal}
-   [Release Notes](../core/history.html){.reference .internal}
-   [Migrating from 5.x to 6.0](../core/migration.html){.reference
    .internal}
:::
:::

::: {.section .wy-nav-content-wrap toggle="wy-nav-shift"}
[PlatformIO](../index.html)

::: wy-nav-content

::: rst-content
::: {role="navigation" aria-label="Page navigation"}
-   [](../index.html){.icon .icon-home aria-label="Home"}
-   [Development Platforms](index.html)
-   Raspberry Pi RP2040
-   [Edit on
    GitHub](https://github.com/platformio/platformio-docs/blob/develop/platforms/raspberrypi.rst){.fa
    .fa-github}

------------------------------------------------------------------------
:::

::: {.document role="main" itemscope="itemscope" itemtype="http://schema.org/Article"}
::: {itemprop="articleBody"}
::: {#raspberry-pi-rp2040 .section}
[]{#platform-raspberrypi}

# Raspberry Pi RP2040[](#raspberry-pi-rp2040 "Link to this heading"){.headerlink}

Registry[:]{.colon}

:   [https://registry.platformio.org/platforms/platformio/raspberrypi](https://registry.platformio.org/platforms/platformio/raspberrypi){.reference
    .external}

Configuration[:]{.colon}

:   [[platform]{.std
    .std-ref}](../projectconf/sections/env/options/platform/platform.html#projectconf-env-platform){.reference
    .internal} = [`platformio/raspberrypi`{.docutils .literal
    .notranslate}]{.pre}

RP2040 is a low-cost, high-performance microcontroller device with a
large on-chip memory, symmetric dual-core processor complex, and rich
peripheral.

For more detailed information please visit [vendor
site](https://www.raspberrypi.org/documentation/rp2040/getting-started/?utm_source=platformio.org&utm_medium=docs){.reference
.external}.

Contents

-   [Examples](#examples){#id2 .reference .internal}

-   [Debugging](#debugging){#id3 .reference .internal}

-   [Stable and upstream versions](#stable-and-upstream-versions){#id4
    .reference .internal}

-   [Packages](#packages){#id5 .reference .internal}

-   [Frameworks](#frameworks){#id6 .reference .internal}

-   [Boards](#boards){#id7 .reference .internal}

::: {#examples .section}
## [Examples](#id2){.toc-backref role="doc-backlink"}[](#examples "Link to this heading"){.headerlink}

Examples are listed from [Raspberry Pi RP2040 development platform
repository](https://github.com/platformio/platform-raspberrypi/tree/master/examples?utm_source=platformio.org&utm_medium=docs){.reference
.external}:

-   [arduino-blink](https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-external-libs](https://github.com/platformio/platform-raspberrypi/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs){.reference
    .external}
:::

::: {#debugging .section}
## [Debugging](#id3){.toc-backref role="doc-backlink"}[](#debugging "Link to this heading"){.headerlink}

[[Debugging]{.std .std-ref}](../plus/debugging.html#piodebug){.reference
.internal} - "1-click" solution for debugging with a zero configuration.

-   [Tools & Debug Probes](#tools-debug-probes){#id8 .reference
    .internal}

    -   [External Debug Tools](#external-debug-tools){#id9 .reference
        .internal}

::: {#tools-debug-probes .section}
### [Tools & Debug Probes](#id8){.toc-backref role="doc-backlink"}[](#tools-debug-probes "Link to this heading"){.headerlink}

Supported debugging tools are listed in "Debug" column. For more
detailed information, please scroll table by horizontal. You can switch
between debugging [[Tools & Debug Probes]{.std
.std-ref}](../plus/debugging.html#debugging-tools){.reference .internal}
using [[debug_tool]{.std
.std-ref}](../projectconf/sections/env/options/debug/debug_tool.html#projectconf-debug-tool){.reference
.internal} option in [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}.

::: {.admonition .warning}
Warning

You will need to install debug tool drivers depending on your system.
Please click on compatible debug tool below for the further
instructions.
:::

::: {#external-debug-tools .section}
#### [External Debug Tools](#id9){.toc-backref role="doc-backlink"}[](#external-debug-tools "Link to this heading"){.headerlink}

Boards listed below are compatible with [[Debugging]{.std
.std-ref}](../plus/debugging.html#piodebug){.reference .internal} but
**DEPEND ON** external debug probe. They **ARE NOT READY** for
debugging. Please click on board name for the further details.

  Name                                                                                                                                                     MCU      Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ----------- ------- -------
  [[Arduino Nano RP2040 Connect]{.std .std-ref}](../boards/raspberrypi/nanorp2040connect.html#board-raspberrypi-nanorp2040connect){.reference .internal}   RP2040   133MHz      2MB     264KB
  [[Raspberry Pi Pico]{.std .std-ref}](../boards/raspberrypi/pico.html#board-raspberrypi-pico){.reference .internal}                                       RP2040   133MHz      2MB     264KB
:::
:::
:::

::: {#stable-and-upstream-versions .section}
## [Stable and upstream versions](#id4){.toc-backref role="doc-backlink"}[](#stable-and-upstream-versions "Link to this heading"){.headerlink}

You can switch between [stable
releases](https://github.com/platformio/platform-raspberrypi/releases){.reference
.external} of Raspberry Pi RP2040 development platform and the latest
upstream version using [[platform]{.std
.std-ref}](../projectconf/sections/env/options/platform/platform.html#projectconf-env-platform){.reference
.internal} option in [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal} as described below.

::: {#stable .section}
### Stable[](#stable "Link to this heading"){.headerlink}

::: {.highlight-ini .notranslate}
::: highlight
    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = raspberrypi
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = raspberrypi@x.y.z
    board = ...
:::
:::
:::

::: {#upstream .section}
### Upstream[](#upstream "Link to this heading"){.headerlink}

::: {.highlight-ini .notranslate}
::: highlight
    [env:upstream_develop]
    platform = https://github.com/platformio/platform-raspberrypi.git
    board = ...
:::
:::
:::
:::

::: {#packages .section}
## [Packages](#id5){.toc-backref role="doc-backlink"}[](#packages "Link to this heading"){.headerlink}

  Name                                                                                                                          Description
  ----------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------
  [framework-arduino-mbed](https://registry.platformio.org/tools/platformio/framework-arduino-mbed){.reference .external}       Arduino framework supporting mbed-enabled boards
  [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink){.reference .external}                               Software and Documentation Pack for SEGGER J-Link debug probes
  [tool-openocd-raspberrypi](https://registry.platformio.org/tools/platformio/tool-openocd-raspberrypi){.reference .external}   Open On-Chip Debugger for Raspberry Pi MCUs
  [tool-rp2040tools](https://registry.platformio.org/tools/platformio/tool-rp2040tools){.reference .external}                   Tools for interacting with a RP2040 device in BOOTSEL mode or with a RP2040 binary
  [toolchain-gccarmnoneeabi](https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi){.reference .external}   GNU toolchain for Arm Cortex-M and Cortex-R processors

::: {.admonition .warning}
Warning

**Linux Users**:

> <div>
>
> -   Install "udev" rules [[99-platformio-udev.rules]{.std
>     .std-ref}](../core/installation/udev-rules.html#platformio-udev-rules){.reference
>     .internal}
>
> -   Raspberry Pi users, please read this article [Enable serial port
>     on Raspberry
>     Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/){.reference
>     .external}.
>
> </div>

**Windows Users:**

> <div>
>
> Please check that you have a correctly installed USB driver from board
> manufacturer
>
> </div>
:::
:::

::: {#frameworks .section}
## [Frameworks](#id6){.toc-backref role="doc-backlink"}[](#frameworks "Link to this heading"){.headerlink}

  Name                                                                                             Description
  ------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[Arduino]{.std .std-ref}](../frameworks/arduino.html#framework-arduino){.reference .internal}   Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.
:::

::: {#boards .section}
## [Boards](#id7){.toc-backref role="doc-backlink"}[](#boards "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

-   You can list pre-configured boards by [[pio boards]{.std
    .std-ref}](../core/userguide/cmd_boards.html#cmd-boards){.reference
    .internal} command

-   For more detailed [`board`{.docutils .literal .notranslate}]{.pre}
    information please scroll the tables below by horizontally.
:::

::: {#arduino .section}
### Arduino[](#arduino "Link to this heading"){.headerlink}

  Name                                                                                                                                                     Debug      MCU      Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- -------- ----------- ------- -------
  [[Arduino Nano RP2040 Connect]{.std .std-ref}](../boards/raspberrypi/nanorp2040connect.html#board-raspberrypi-nanorp2040connect){.reference .internal}   External   RP2040   133MHz      2MB     264KB
:::

::: {#raspberry-pi .section}
### Raspberry Pi[](#raspberry-pi "Link to this heading"){.headerlink}

  Name                                                                                                                 Debug      MCU      Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------- ---------- -------- ----------- ------- -------
  [[Raspberry Pi Pico]{.std .std-ref}](../boards/raspberrypi/pico.html#board-raspberrypi-pico){.reference .internal}   External   RP2040   133MHz      2MB     264KB
:::
:::
:::
:::
:::

::: {.rst-footer-buttons role="navigation" aria-label="Footer"}
[[]{.fa .fa-arrow-circle-left aria-hidden="true"}
Previous](openhw.html "OpenHW Group"){.btn .btn-neutral .float-left
accesskey="p" rel="prev"} [Next []{.fa .fa-arrow-circle-right
aria-hidden="true"}](renesas-ra.html "Renesas RA"){.btn .btn-neutral
.float-right accesskey="n" rel="next"}
:::

------------------------------------------------------------------------

::: {role="contentinfo"}
© Copyright 2014-present, PlatformIO.
:::
:::
:::
:::
:::

::: {.rst-versions toggle="rst-versions" role="note" aria-label="Versions"}
[ [ Documentation]{.fa .fa-book} v6.1.19a2 (latest) []{.fa
.fa-caret-down} ]{.rst-current-version toggle="rst-current-version"}

::: rst-other-versions

Versions
:   [latest](/en/)
:   [stable](/en/stable/)

```{=html}
<!-- -->
```

On Github
:   [View](https://github.com/platformio/platformio-docs/blob/develop/platforms/raspberrypi.rst)
:   [Edit](https://github.com/platformio/platformio-docs/edit/develop/platforms/raspberrypi.rst)

```{=html}
<!-- -->
```

Search

:   ::: {role="search"}
    :::
:::
:::
