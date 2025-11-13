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
        -   [Raspberry Pi RP2040](raspberrypi.html){.reference
            .internal}
        -   [Renesas RA](renesas-ra.html){.reference .internal}
        -   [RISC-V GAP](riscv_gap.html){.reference .internal}
        -   [Shakti](shakti.html){.reference .internal}
        -   [SiFive](sifive.html){.reference .internal}
        -   [Silicon Labs EFM32](siliconlabsefm32.html){.reference
            .internal}
        -   [ST STM32](#){.current .reference .internal}
            -   [Tutorials](#tutorials){.reference .internal}
            -   [Configuration](#configuration){.reference .internal}
            -   [Examples](#examples){.reference .internal}
            -   [Debugging](#debugging){.reference .internal}
            -   [Stable and upstream
                versions](#stable-and-upstream-versions){.reference
                .internal}
            -   [Packages](#packages){.reference .internal}
            -   [Frameworks](#frameworks){.reference .internal}
            -   [Boards](#boards){.reference .internal}
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
-   ST STM32
-   [Edit on
    GitHub](https://github.com/platformio/platformio-docs/blob/develop/platforms/ststm32.rst){.fa
    .fa-github}

------------------------------------------------------------------------
:::

::: {.document role="main" itemscope="itemscope" itemtype="http://schema.org/Article"}
::: {itemprop="articleBody"}
::: {#st-stm32 .section}
[]{#platform-ststm32}

# ST STM32[](#st-stm32 "Link to this heading"){.headerlink}

Registry[:]{.colon}

:   [https://registry.platformio.org/platforms/platformio/ststm32](https://registry.platformio.org/platforms/platformio/ststm32){.reference
    .external}

Configuration[:]{.colon}

:   [[platform]{.std
    .std-ref}](../projectconf/sections/env/options/platform/platform.html#projectconf-env-platform){.reference
    .internal} = [`platformio/ststm32`{.docutils .literal
    .notranslate}]{.pre}

The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M
processor is designed to offer new degrees of freedom to MCU users. It
offers a 32-bit product range that combines very high performance,
real-time capabilities, digital signal processing, and low-power,
low-voltage operation, while maintaining full integration and ease of
development.

For more detailed information please visit [vendor
site](http://www.st.com/web/en/catalog/mmc/FM141/SC1169?sc=stm32&utm_source=platformio.org&utm_medium=docs){.reference
.external}.

Contents

-   [Tutorials](#tutorials){#id10 .reference .internal}

-   [Configuration](#configuration){#id11 .reference .internal}

-   [Examples](#examples){#id12 .reference .internal}

-   [Debugging](#debugging){#id13 .reference .internal}

-   [Stable and upstream versions](#stable-and-upstream-versions){#id14
    .reference .internal}

-   [Packages](#packages){#id15 .reference .internal}

-   [Frameworks](#frameworks){#id16 .reference .internal}

-   [Boards](#boards){#id17 .reference .internal}

::: {#tutorials .section}
## [Tutorials](#id10){.toc-backref role="doc-backlink"}[](#tutorials "Link to this heading"){.headerlink}

-   [[STM32Cube HAL and Nucleo-F401RE: debugging and unit testing]{.std
    .std-ref}](../tutorials/ststm32/stm32cube_debugging_unit_testing.html#tutorial-stm32cube-debugging-unit-testing){.reference
    .internal}
:::

::: {#configuration .section}
## [Configuration](#id11){.toc-backref role="doc-backlink"}[](#configuration "Link to this heading"){.headerlink}

::: {#switching-between-arduino-cores .section}
### Switching between Arduino cores[](#switching-between-arduino-cores "Link to this heading"){.headerlink}

There are three different Arduino cores for STM32 microcontrollers:
STM32Duino, Arduino STM32 (maple) and STM32L0. All of them have been
developed independently, therefore, have different functionality and set
of internal libraries. By default, official STM32Duino core is used
(except cases when a board supports only one specific core). Some of the
boards support all three cores. To change the core you can use a
[`board_build.core`{.docutils .literal .notranslate}]{.pre} option that
needs be added to [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal}:

An example of [["platformio.ini" (Project Configuration File)]{.std
.std-ref}](../projectconf/index.html#projectconf){.reference .internal}
with [`maple`{.docutils .literal .notranslate}]{.pre} core

::: {.highlight-ini .notranslate}
::: highlight
    [env:hy_tinystm103tb]
    platform = ststm32
    framework = arduino
    board = hy_tinystm103tb
    board_build.core = maple
:::
:::
:::

::: {#stm32duino-configuration-system .section}
### STM32Duino configuration system[](#stm32duino-configuration-system "Link to this heading"){.headerlink}

STM32Duino core has several options that can be configured using the
next configuration flags in [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} section of [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}:

  Name                                                                                    Description
  --------------------------------------------------------------------------------------- ------------------------------------
  [`PIO_FRAMEWORK_ARDUINO_STANDARD_LIB`{.docutils .literal .notranslate}]{.pre}           Disable Newlib Nano library
  [`PIO_FRAMEWORK_ARDUINO_NANOLIB_FLOAT_PRINTF`{.docutils .literal .notranslate}]{.pre}   Newlib Nano + float printf support
  [`PIO_FRAMEWORK_ARDUINO_NANOLIB_FLOAT_SCANF`{.docutils .literal .notranslate}]{.pre}    Newlib Nano + float scanf support

  : [C/C++ standard library
  configuration]{.caption-text}[](#id3 "Link to this table"){.headerlink}

  Name                                                                                      Description
  ----------------------------------------------------------------------------------------- ------------------------------
  [`PIO_FRAMEWORK_ARDUINO_SERIAL_WITHOUT_GENERIC`{.docutils .literal .notranslate}]{.pre}   Enabled (no generic Serial)
  [`PIO_FRAMEWORK_ARDUINO_SERIAL_DISABLED`{.docutils .literal .notranslate}]{.pre}          Disabled (no Serial support)

  : [USART
  Configuration]{.caption-text}[](#id4 "Link to this table"){.headerlink}

  Name                                                                                         Description
  -------------------------------------------------------------------------------------------- ----------------------------------------
  [`PIO_FRAMEWORK_ARDUINO_ENABLE_CDC`{.docutils .literal .notranslate}]{.pre}                  CDC (generic Serial supersede U(S)ART)
  [`PIO_FRAMEWORK_ARDUINO_ENABLE_CDC_WITHOUT_SERIAL`{.docutils .literal .notranslate}]{.pre}   CDC (no generic Serial)
  [`PIO_FRAMEWORK_ARDUINO_ENABLE_HID`{.docutils .literal .notranslate}]{.pre}                  HID (keyboard and mouse)

  : [USB
  Configuration]{.caption-text}[](#id5 "Link to this table"){.headerlink}

  Name                                                                                      Description
  ----------------------------------------------------------------------------------------- -------------------------------
  [`PIO_FRAMEWORK_ARDUINO_USB_HIGHSPEED`{.docutils .literal .notranslate}]{.pre}            High Speed mode
  [`PIO_FRAMEWORK_ARDUINO_USB_HIGHSPEED_FULLMODE`{.docutils .literal .notranslate}]{.pre}   High Speed in Full Speed mode

  : [USB Speed
  Configuration]{.caption-text}[](#id6 "Link to this table"){.headerlink}

Example:

::: {.highlight-ini .notranslate}
::: highlight
    [env:nucleo_f401re]
    platform = ststm32
    framework = arduino
    board = nucleo_f401re
    build_flags =
      -D PIO_FRAMEWORK_ARDUINO_ENABLE_CDC
      -D PIO_FRAMEWORK_ARDUINO_NANOLIB_FLOAT_PRINTF
      -D PIO_FRAMEWORK_ARDUINO_USB_HIGHSPEED_FULLMODE
:::
:::
:::

::: {#maple-stm32-configuration-system .section}
### Maple STM32 configuration system[](#maple-stm32-configuration-system "Link to this heading"){.headerlink}

In this core the USB peripheral (STM32F4 boards only) can be configured
using the next configuration flags in [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} section of [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}:

  Name                                                                 Description
  -------------------------------------------------------------------- ------------------------
  [`ENABLE_USB_SERIAL`{.docutils .literal .notranslate}]{.pre}         USB serial (CDC)
  [`ENABLE_USB_MASS_STORAGE`{.docutils .literal .notranslate}]{.pre}   USB Mass Storage (MSC)

  : [USB Configuration for STM32F4
  boards]{.caption-text}[](#id7 "Link to this table"){.headerlink}

Example:

::: {.highlight-ini .notranslate}
::: highlight
    [env:disco_f407vg]
    platform = ststm32
    framework = arduino
    board = disco_f407vg
    board_build.core = maple
    build_flags = -D ENABLE_USB_MASS_STORAGE
:::
:::
:::

::: {#arduino-stm32l0-configuration-system .section}
### Arduino STM32L0 configuration system[](#arduino-stm32l0-configuration-system "Link to this heading"){.headerlink}

Arduino STM32L0 core has several options that can be configured using
the next configuration flags in [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} section of [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}:

  Name                                                                                       Description
  ------------------------------------------------------------------------------------------ ------------------------------------------
  [`PIO_FRAMEWORK_ARDUINO_ENABLE_MASS_STORAGE`{.docutils .literal .notranslate}]{.pre}       Serial + Mass Storage
  [`PIO_FRAMEWORK_ARDUINO_ENABLE_HID`{.docutils .literal .notranslate}]{.pre}                Serial + Keyboard + Mouse
  [`PIO_FRAMEWORK_ARDUINO_ENABLE_MASS_STORAGE_HID`{.docutils .literal .notranslate}]{.pre}   Serial + Mass Storage + Keyboard + Mouse
  [`PIO_FRAMEWORK_ARDUINO_NO_USB`{.docutils .literal .notranslate}]{.pre}                    No USB

  : [USB
  Configuration]{.caption-text}[](#id8 "Link to this table"){.headerlink}

  Name                                                                         Description
  ---------------------------------------------------------------------------- --------------
  [`PIO_FRAMEWORK_ARDUINO_FS_SDCARD`{.docutils .literal .notranslate}]{.pre}   SDCARD (SPI)
  [`PIO_FRAMEWORK_ARDUINO_FS_SFLASH`{.docutils .literal .notranslate}]{.pre}   SFLASH (SPI)

  : [FS
  Configuration]{.caption-text}[](#id9 "Link to this table"){.headerlink}

Example:

::: {.highlight-ini .notranslate}
::: highlight
    [env:cricket_l082cz]
    platform = ststm32
    framework = arduino
    board = cricket_l082cz
    build_flags =
      -D PIO_FRAMEWORK_ARDUINO_ENABLE_MASS_STORAGE
:::
:::
:::
:::

::: {#examples .section}
## [Examples](#id12){.toc-backref role="doc-backlink"}[](#examples "Link to this heading"){.headerlink}

Examples are listed from [ST STM32 development platform
repository](https://github.com/platformio/platform-ststm32/tree/master/examples?utm_source=platformio.org&utm_medium=docs){.reference
.external}:

-   [zephyr-blink](https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-ll-blink](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-ll-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [libopencm3-blink](https://github.com/platformio/platform-ststm32/tree/master/examples/libopencm3-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-mbed-doom](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mbed-doom?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-mbed-rpc](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mbed-rpc?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [libopencm3-usb-cdcacm](https://github.com/platformio/platform-ststm32/tree/master/examples/libopencm3-usb-cdcacm?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [cmsis-blink](https://github.com/platformio/platform-ststm32/tree/master/examples/cmsis-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-hal-iap](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-iap?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-blink](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-hal-extmem-boot](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-extmem-boot?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [spl-blink](https://github.com/platformio/platform-ststm32/tree/master/examples/spl-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-hal-lcd](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-lcd?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-mesh-minimal](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-mesh-minimal?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-mxchip-sensors](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-sensors?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [zephyr-cpp-synchronization](https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-cpp-synchronization?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [zephyr-net-https-client](https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-net-https-client?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-blink-baremetal](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-blink-baremetal?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-filesystem](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-filesystem?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-sockets](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-sockets?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-hal-wifi-client](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-wifi-client?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-usb-keyboard](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-usb-keyboard?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-ethernet-tls](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-ethernet-tls?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-hal-blink](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [zephyr-drivers-can](https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-drivers-can?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-mxchip-azureiot](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-azureiot?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-mxchip-filesystem](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-filesystem?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-hal-usb-device-dfu](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-usb-device-dfu?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-internal-libs](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-internal-libs?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-external-libs](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-external-libs?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-mxchip-wifiscan](https://github.com/platformio/platform-ststm32/tree/master/examples/arduino-mxchip-wifiscan?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-events](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-events?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [libopencm3-1bitsy](https://github.com/platformio/platform-ststm32/tree/master/examples/libopencm3-1bitsy?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [zephyr-subsys-usb-hid-mouse](https://github.com/platformio/platform-ststm32/tree/master/examples/zephyr-subsys-usb-hid-mouse?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-serial](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-serial?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [mbed-rtos-custom-target](https://github.com/platformio/platform-ststm32/tree/master/examples/mbed-rtos-custom-target?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [stm32cube-hal-eeprom-emulation](https://github.com/platformio/platform-ststm32/tree/master/examples/stm32cube-hal-eeprom-emulation?utm_source=platformio.org&utm_medium=docs){.reference
    .external}
:::

::: {#debugging .section}
## [Debugging](#id13){.toc-backref role="doc-backlink"}[](#debugging "Link to this heading"){.headerlink}

[[Debugging]{.std .std-ref}](../plus/debugging.html#piodebug){.reference
.internal} - "1-click" solution for debugging with a zero configuration.

-   [Tools & Debug Probes](#tools-debug-probes){#id18 .reference
    .internal}

    -   [On-Board Debug Tools](#on-board-debug-tools){#id19 .reference
        .internal}

    -   [External Debug Tools](#external-debug-tools){#id20 .reference
        .internal}

::: {#tools-debug-probes .section}
### [Tools & Debug Probes](#id18){.toc-backref role="doc-backlink"}[](#tools-debug-probes "Link to this heading"){.headerlink}

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

::: {#on-board-debug-tools .section}
#### [On-Board Debug Tools](#id19){.toc-backref role="doc-backlink"}[](#on-board-debug-tools "Link to this heading"){.headerlink}

Boards listed below have on-board debug probe and **ARE READY** for
debugging! You do not need to use/buy external debug probe.

  Name                                                                                                                                                             MCU              Frequency   Flash    RAM
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------- ----------- -------- -------
  [[32F412GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f412zg.html#board-ststm32-disco-f412zg){.reference .internal}                                        STM32F412ZGT6    100MHz      1MB      256KB
  [[32F723EDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f723ie.html#board-ststm32-disco-f723ie){.reference .internal}                                        STM32F723IEK6    216MHz      512KB    192KB
  [[3D printer controller]{.std .std-ref}](../boards/ststm32/remram_v1.html#board-ststm32-remram-v1){.reference .internal}                                         STM32F765VIT6    216MHz      2MB      512KB
  [[3DP001V1 Evaluation board for 3D printer]{.std .std-ref}](../boards/ststm32/st3dp001_eval.html#board-ststm32-st3dp001-eval){.reference .internal}              STM32F401VET6    84MHz       512KB    96KB
  [[96Boards B96B-F446VE]{.std .std-ref}](../boards/ststm32/b96b_f446ve.html#board-ststm32-b96b-f446ve){.reference .internal}                                      STM32F446VET6    168MHz      512KB    128KB
  [[Armstrap Eagle 1024]{.std .std-ref}](../boards/ststm32/armstrap_eagle1024.html#board-ststm32-armstrap-eagle1024){.reference .internal}                         STM32F417VGT6    168MHz      1MB      192KB
  [[Armstrap Eagle 2048]{.std .std-ref}](../boards/ststm32/armstrap_eagle2048.html#board-ststm32-armstrap-eagle2048){.reference .internal}                         STM32F427VIT6    168MHz      1.99MB   256KB
  [[Armstrap Eagle 512]{.std .std-ref}](../boards/ststm32/armstrap_eagle512.html#board-ststm32-armstrap-eagle512){.reference .internal}                            STM32F407VET6    168MHz      512KB    192KB
  [[Big Tree Tech EBB42 V1.1]{.std .std-ref}](../boards/ststm32/btt_ebb42_v1_1.html#board-ststm32-btt-ebb42-v1-1){.reference .internal}                            STM32G0B1RET6    64MHz       128KB    144KB
  [[L476DMW1K]{.std .std-ref}](../boards/ststm32/rhombio_l476dmw1k.html#board-ststm32-rhombio-l476dmw1k){.reference .internal}                                     STM32L476VGT6    80MHz       1MB      128KB
  [[Leafony Systems AP03]{.std .std-ref}](../boards/ststm32/leafony_ap03.html#board-ststm32-leafony-ap03){.reference .internal}                                    STM32L452RET6    80MHz       512KB    160KB
  [[Mbed Connect Cloud]{.std .std-ref}](../boards/ststm32/mbed_connect_odin.html#board-ststm32-mbed-connect-odin){.reference .internal}                            STM32F439ZIY6    168MHz      2MB      256KB
  [[Microsoft Azure IoT Development Kit (MXChip AZ3166)]{.std .std-ref}](../boards/ststm32/mxchip_az3166.html#board-ststm32-mxchip-az3166){.reference .internal}   STM32F412ZGT6    100MHz      1MB      256KB
  [[Nucleo G070RB]{.std .std-ref}](../boards/ststm32/nucleo_g070rb.html#board-ststm32-nucleo-g070rb){.reference .internal}                                         STM32G070RBT6    64MHz       128KB    36KB
  [[Nucleo G071RB]{.std .std-ref}](../boards/ststm32/nucleo_g071rb.html#board-ststm32-nucleo-g071rb){.reference .internal}                                         STM32G071RBT6    64MHz       128KB    36KB
  [[Nucleo G431KB]{.std .std-ref}](../boards/ststm32/nucleo_g431kb.html#board-ststm32-nucleo-g431kb){.reference .internal}                                         STM32G431KBT6    170MHz      128KB    32KB
  [[Nucleo G431RB]{.std .std-ref}](../boards/ststm32/nucleo_g431rb.html#board-ststm32-nucleo-g431rb){.reference .internal}                                         STM32G431RBT6    170MHz      128KB    32KB
  [[Nucleo G474RE]{.std .std-ref}](../boards/ststm32/nucleo_g474re.html#board-ststm32-nucleo-g474re){.reference .internal}                                         STM32G474RET6    170MHz      512KB    128KB
  [[P-Nucleo WB55RG]{.std .std-ref}](../boards/ststm32/nucleo_wb55rg_p.html#board-ststm32-nucleo-wb55rg-p){.reference .internal}                                   STM32WB55RG      64MHz       512KB    192KB
  [[RushUp Cloud-JAM]{.std .std-ref}](../boards/ststm32/cloud_jam.html#board-ststm32-cloud-jam){.reference .internal}                                              STM32F401RET6    84MHz       512KB    96KB
  [[RushUp Cloud-JAM L4]{.std .std-ref}](../boards/ststm32/cloud_jam_l4.html#board-ststm32-cloud-jam-l4){.reference .internal}                                     STM32L476RGT6    80MHz       1MB      128KB
  [[ST 32F3348DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f334c8.html#board-ststm32-disco-f334c8){.reference .internal}                                     STM32F334C8T6    72MHz       64KB     12KB
  [[ST 32F401CDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f401vc.html#board-ststm32-disco-f401vc){.reference .internal}                                     STM32F401VCT6    84MHz       256KB    64KB
  [[ST 32F411EDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f411ve.html#board-ststm32-disco-f411ve){.reference .internal}                                     STM32F411VET6    100MHz      512KB    128KB
  [[ST 32F413HDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f413zh.html#board-ststm32-disco-f413zh){.reference .internal}                                     STM32F413ZHT6    100MHz      1.50MB   320KB
  [[ST 32F429IDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f429zi.html#board-ststm32-disco-f429zi){.reference .internal}                                     STM32F429ZIT6    180MHz      2MB      256KB
  [[ST 32F469IDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f469ni.html#board-ststm32-disco-f469ni){.reference .internal}                                     STM32F469NIH6    180MHz      2MB      384KB
  [[ST 32F746GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f746ng.html#board-ststm32-disco-f746ng){.reference .internal}                                     STM32F746NGH6    216MHz      1MB      320KB
  [[ST 32F769IDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f769ni.html#board-ststm32-disco-f769ni){.reference .internal}                                     STM32F769NIH6    216MHz      2MB      512KB
  [[ST 32L0538DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l053c8.html#board-ststm32-disco-l053c8){.reference .internal}                                     STM32L053C8T6    32MHz       64KB     8KB
  [[ST 32L100DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l100rc.html#board-ststm32-disco-l100rc){.reference .internal}                                      STM32L100RCT6    32MHz       256KB    16KB
  [[ST 32L476GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l476vg.html#board-ststm32-disco-l476vg){.reference .internal}                                     STM32L476VGT6    80MHz       1MB      128KB
  [[ST 32L496GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l496ag.html#board-ststm32-disco-l496ag){.reference .internal}                                     STM32L496AGI6    80MHz       1MB      320KB
  [[ST B-G431B-ESC1 Discovery]{.std .std-ref}](../boards/ststm32/disco_b_g431b_esc1.html#board-ststm32-disco-b-g431b-esc1){.reference .internal}                   STM32G431CBU6    170MHz      128KB    32KB
  [[ST B-L475E-IOT01A Discovery kit]{.std .std-ref}](../boards/ststm32/disco_l475vg_iot01a.html#board-ststm32-disco-l475vg-iot01a){.reference .internal}           STM32L475VGT6    80MHz       1MB      96KB
  [[ST B-U585I-IOT02A Discovery]{.std .std-ref}](../boards/ststm32/disco_b_u585i_iot02a.html#board-ststm32-disco-b-u585i-iot02a){.reference .internal}             STM32U585AII6Q   160MHz      2MB      256KB
  [[ST DISCO-L072CZ-LRWAN1]{.std .std-ref}](../boards/ststm32/disco_l072cz_lrwan1.html#board-ststm32-disco-l072cz-lrwan1){.reference .internal}                    STM32L072CZ      32MHz       192KB    20KB
  [[ST Discovery F072RB]{.std .std-ref}](../boards/ststm32/disco_f072rb.html#board-ststm32-disco-f072rb){.reference .internal}                                     STM32F072RBT6    48MHz       128KB    16KB
  [[ST NUCLEO-G031K8]{.std .std-ref}](../boards/ststm32/nucleo_g031k8.html#board-ststm32-nucleo-g031k8){.reference .internal}                                      STM32G031K8      64MHz       64KB     8KB
  [[ST Nucleo F030R8]{.std .std-ref}](../boards/ststm32/nucleo_f030r8.html#board-ststm32-nucleo-f030r8){.reference .internal}                                      STM32F030R8T6    48MHz       64KB     8KB
  [[ST Nucleo F031K6]{.std .std-ref}](../boards/ststm32/nucleo_f031k6.html#board-ststm32-nucleo-f031k6){.reference .internal}                                      STM32F031K6T6    48MHz       32KB     4KB
  [[ST Nucleo F042K6]{.std .std-ref}](../boards/ststm32/nucleo_f042k6.html#board-ststm32-nucleo-f042k6){.reference .internal}                                      STM32F042K6T6    48MHz       32KB     6KB
  [[ST Nucleo F070RB]{.std .std-ref}](../boards/ststm32/nucleo_f070rb.html#board-ststm32-nucleo-f070rb){.reference .internal}                                      STM32F070RBT6    48MHz       128KB    16KB
  [[ST Nucleo F072RB]{.std .std-ref}](../boards/ststm32/nucleo_f072rb.html#board-ststm32-nucleo-f072rb){.reference .internal}                                      STM32F072RBT6    48MHz       128KB    16KB
  [[ST Nucleo F091RC]{.std .std-ref}](../boards/ststm32/nucleo_f091rc.html#board-ststm32-nucleo-f091rc){.reference .internal}                                      STM32F091RCT6    48MHz       256KB    32KB
  [[ST Nucleo F103RB]{.std .std-ref}](../boards/ststm32/nucleo_f103rb.html#board-ststm32-nucleo-f103rb){.reference .internal}                                      STM32F103RBT6    72MHz       128KB    20KB
  [[ST Nucleo F207ZG]{.std .std-ref}](../boards/ststm32/nucleo_f207zg.html#board-ststm32-nucleo-f207zg){.reference .internal}                                      STM32F207ZGT6    120MHz      1MB      128KB
  [[ST Nucleo F302R8]{.std .std-ref}](../boards/ststm32/nucleo_f302r8.html#board-ststm32-nucleo-f302r8){.reference .internal}                                      STM32F302R8T6    72MHz       64KB     16KB
  [[ST Nucleo F303K8]{.std .std-ref}](../boards/ststm32/nucleo_f303k8.html#board-ststm32-nucleo-f303k8){.reference .internal}                                      STM32F303K8T6    72MHz       64KB     12KB
  [[ST Nucleo F303RE]{.std .std-ref}](../boards/ststm32/nucleo_f303re.html#board-ststm32-nucleo-f303re){.reference .internal}                                      STM32F303RET6    72MHz       512KB    64KB
  [[ST Nucleo F303ZE]{.std .std-ref}](../boards/ststm32/nucleo_f303ze.html#board-ststm32-nucleo-f303ze){.reference .internal}                                      STM32F303ZET6    72MHz       512KB    64KB
  [[ST Nucleo F334R8]{.std .std-ref}](../boards/ststm32/nucleo_f334r8.html#board-ststm32-nucleo-f334r8){.reference .internal}                                      STM32F334R8T6    72MHz       64KB     16KB
  [[ST Nucleo F401RE]{.std .std-ref}](../boards/ststm32/nucleo_f401re.html#board-ststm32-nucleo-f401re){.reference .internal}                                      STM32F401RET6    84MHz       512KB    96KB
  [[ST Nucleo F410RB]{.std .std-ref}](../boards/ststm32/nucleo_f410rb.html#board-ststm32-nucleo-f410rb){.reference .internal}                                      STM32F410RBT6    100MHz      128KB    32KB
  [[ST Nucleo F411RE]{.std .std-ref}](../boards/ststm32/nucleo_f411re.html#board-ststm32-nucleo-f411re){.reference .internal}                                      STM32F411RET6    100MHz      512KB    128KB
  [[ST Nucleo F412ZG]{.std .std-ref}](../boards/ststm32/nucleo_f412zg.html#board-ststm32-nucleo-f412zg){.reference .internal}                                      STM32F412ZGT6    100MHz      1MB      256KB
  [[ST Nucleo F413ZH]{.std .std-ref}](../boards/ststm32/nucleo_f413zh.html#board-ststm32-nucleo-f413zh){.reference .internal}                                      STM32F413ZHT6    100MHz      1.50MB   320KB
  [[ST Nucleo F429ZI]{.std .std-ref}](../boards/ststm32/nucleo_f429zi.html#board-ststm32-nucleo-f429zi){.reference .internal}                                      STM32F429ZIT6    180MHz      2MB      192KB
  [[ST Nucleo F439ZI]{.std .std-ref}](../boards/ststm32/nucleo_f439zi.html#board-ststm32-nucleo-f439zi){.reference .internal}                                      STM32F439ZIT6    180MHz      2MB      192KB
  [[ST Nucleo F446RE]{.std .std-ref}](../boards/ststm32/nucleo_f446re.html#board-ststm32-nucleo-f446re){.reference .internal}                                      STM32F446RET6    180MHz      512KB    128KB
  [[ST Nucleo F446ZE]{.std .std-ref}](../boards/ststm32/nucleo_f446ze.html#board-ststm32-nucleo-f446ze){.reference .internal}                                      STM32F446ZET6    180MHz      512KB    128KB
  [[ST Nucleo F722ZE]{.std .std-ref}](../boards/ststm32/nucleo_f722ze.html#board-ststm32-nucleo-f722ze){.reference .internal}                                      STM32F722ZET6    216MHz      512KB    256KB
  [[ST Nucleo F746ZG]{.std .std-ref}](../boards/ststm32/nucleo_f746zg.html#board-ststm32-nucleo-f746zg){.reference .internal}                                      STM32F746ZGT6    216MHz      1MB      320KB
  [[ST Nucleo F756ZG]{.std .std-ref}](../boards/ststm32/nucleo_f756zg.html#board-ststm32-nucleo-f756zg){.reference .internal}                                      STM32F756ZG      216MHz      1MB      320KB
  [[ST Nucleo F767ZI]{.std .std-ref}](../boards/ststm32/nucleo_f767zi.html#board-ststm32-nucleo-f767zi){.reference .internal}                                      STM32F767ZIT6    216MHz      2MB      512KB
  [[ST Nucleo G0B1RE]{.std .std-ref}](../boards/ststm32/nucleo_g0b1re.html#board-ststm32-nucleo-g0b1re){.reference .internal}                                      STM32G0B1RET6    64MHz       512KB    144KB
  [[ST Nucleo H723ZG]{.std .std-ref}](../boards/ststm32/nucleo_h723zg.html#board-ststm32-nucleo-h723zg){.reference .internal}                                      STM32H723ZGT6    550MHz      1MB      320KB
  [[ST Nucleo H743ZI]{.std .std-ref}](../boards/ststm32/nucleo_h743zi.html#board-ststm32-nucleo-h743zi){.reference .internal}                                      STM32H743ZIT6    400MHz      2MB      512KB
  [[ST Nucleo H745ZI-Q]{.std .std-ref}](../boards/ststm32/nucleo_h745zi_q.html#board-ststm32-nucleo-h745zi-q){.reference .internal}                                STM32H745ZIT6    480MHz      1MB      512KB
  [[ST Nucleo H753ZI]{.std .std-ref}](../boards/ststm32/nucleo_h753zi.html#board-ststm32-nucleo-h753zi){.reference .internal}                                      STM32H753ZIT6    400MHz      2MB      512KB
  [[ST Nucleo L010RB]{.std .std-ref}](../boards/ststm32/nucleo_l010rb.html#board-ststm32-nucleo-l010rb){.reference .internal}                                      STM32L010RBT6    32MHz       128KB    20KB
  [[ST Nucleo L011K4]{.std .std-ref}](../boards/ststm32/nucleo_l011k4.html#board-ststm32-nucleo-l011k4){.reference .internal}                                      STM32L011K4T6    32MHz       16KB     2KB
  [[ST Nucleo L031K6]{.std .std-ref}](../boards/ststm32/nucleo_l031k6.html#board-ststm32-nucleo-l031k6){.reference .internal}                                      STM32L031K6T6    32MHz       32KB     8KB
  [[ST Nucleo L053R8]{.std .std-ref}](../boards/ststm32/nucleo_l053r8.html#board-ststm32-nucleo-l053r8){.reference .internal}                                      STM32L053R8T6    32MHz       64KB     8KB
  [[ST Nucleo L073RZ]{.std .std-ref}](../boards/ststm32/nucleo_l073rz.html#board-ststm32-nucleo-l073rz){.reference .internal}                                      STM32L073RZ      32MHz       192KB    20KB
  [[ST Nucleo L152RE]{.std .std-ref}](../boards/ststm32/nucleo_l152re.html#board-ststm32-nucleo-l152re){.reference .internal}                                      STM32L152RET6    32MHz       512KB    80KB
  [[ST Nucleo L412KB]{.std .std-ref}](../boards/ststm32/nucleo_l412kb.html#board-ststm32-nucleo-l412kb){.reference .internal}                                      STM32L412KBU6    80MHz       128KB    40KB
  [[ST Nucleo L412RB-P]{.std .std-ref}](../boards/ststm32/nucleo_l412rb_p.html#board-ststm32-nucleo-l412rb-p){.reference .internal}                                STM32L412RBT6P   80MHz       128KB    40KB
  [[ST Nucleo L432KC]{.std .std-ref}](../boards/ststm32/nucleo_l432kc.html#board-ststm32-nucleo-l432kc){.reference .internal}                                      STM32L432KCU6    80MHz       256KB    64KB
  [[ST Nucleo L433RC-P]{.std .std-ref}](../boards/ststm32/nucleo_l433rc_p.html#board-ststm32-nucleo-l433rc-p){.reference .internal}                                STM32L433RC      80MHz       256KB    64KB
  [[ST Nucleo L452RE]{.std .std-ref}](../boards/ststm32/nucleo_l452re.html#board-ststm32-nucleo-l452re){.reference .internal}                                      STM32L452RET6    80MHz       512KB    160KB
  [[ST Nucleo L476RG]{.std .std-ref}](../boards/ststm32/nucleo_l476rg.html#board-ststm32-nucleo-l476rg){.reference .internal}                                      STM32L476RGT6    80MHz       1MB      96KB
  [[ST Nucleo L486RG]{.std .std-ref}](../boards/ststm32/nucleo_l486rg.html#board-ststm32-nucleo-l486rg){.reference .internal}                                      STM32L486RGT6    80MHz       1MB      128KB
  [[ST Nucleo L496ZG]{.std .std-ref}](../boards/ststm32/nucleo_l496zg.html#board-ststm32-nucleo-l496zg){.reference .internal}                                      STM32L496ZGT6    80MHz       1MB      320KB
  [[ST Nucleo L496ZG-P]{.std .std-ref}](../boards/ststm32/nucleo_l496zg_p.html#board-ststm32-nucleo-l496zg-p){.reference .internal}                                STM32L496ZGT6P   80MHz       1MB      320KB
  [[ST Nucleo L4R5ZI]{.std .std-ref}](../boards/ststm32/nucleo_l4r5zi.html#board-ststm32-nucleo-l4r5zi){.reference .internal}                                      STM32L4R5ZIT6    120MHz      2MB      640KB
  [[ST Nucleo L552ZE-Q]{.std .std-ref}](../boards/ststm32/nucleo_l552ze_q.html#board-ststm32-nucleo-l552ze-q){.reference .internal}                                STM32L552ZET6    80MHz       512KB    192KB
  [[ST Nucleo U575ZI-Q]{.std .std-ref}](../boards/ststm32/nucleo_u575zi_q.html#board-ststm32-nucleo-u575zi-q){.reference .internal}                                STM32U575ZIT6Q   160MHz      2MB      256KB
  [[ST Nucleo WL55JC]{.std .std-ref}](../boards/ststm32/nucleo_wl55jc.html#board-ststm32-nucleo-wl55jc){.reference .internal}                                      STM32WL55JC      48MHz       256KB    64KB
  [[ST STM32F0308DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f030r8.html#board-ststm32-disco-f030r8){.reference .internal}                                  STM32F030R8T6    48MHz       64KB     8KB
  [[ST STM32F0DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f051r8.html#board-ststm32-disco-f051r8){.reference .internal}                                     STM32F051R8T6    48MHz       64KB     8KB
  [[ST STM32F3DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f303vc.html#board-ststm32-disco-f303vc){.reference .internal}                                     STM32F303VCT6    72MHz       256KB    40KB
  [[ST STM32F4DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f407vg.html#board-ststm32-disco-f407vg){.reference .internal}                                     STM32F407VGT6    168MHz      1MB      128KB
  [[ST STM32G071B Discovery]{.std .std-ref}](../boards/ststm32/disco_g071rb.html#board-ststm32-disco-g071rb){.reference .internal}                                 STM32G071RBT6    64MHz       128KB    36KB
  [[ST STM32L073Z-EVAL]{.std .std-ref}](../boards/ststm32/eval_l073z.html#board-ststm32-eval-l073z){.reference .internal}                                          STM32L073VZT6    32MHz       192KB    20KB
  [[ST STM32L4+ Discovery kit IoT node]{.std .std-ref}](../boards/ststm32/disco_l4s5i_iot01a.html#board-ststm32-disco-l4s5i-iot01a){.reference .internal}          STM32L4S5VIT6    80MHz       2MB      640KB
  [[ST STM32LDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l152rb.html#board-ststm32-disco-l152rb){.reference .internal}                                      STM32L152RBT6    32MHz       128KB    16KB
  [[ST STM32VLDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f100rb.html#board-ststm32-disco-f100rb){.reference .internal}                                     STM32F100RBT6    24MHz       128KB    8KB
  [[ST Sensor Node]{.std .std-ref}](../boards/ststm32/silica_sensor_node.html#board-ststm32-silica-sensor-node){.reference .internal}                              STM32L476JG      80MHz       1MB      128KB
  [[STM32F7508-DK]{.std .std-ref}](../boards/ststm32/disco_f750n8.html#board-ststm32-disco-f750n8){.reference .internal}                                           STM32F750N8H6    216MHz      64KB     340KB
  [[STM32H735G-DK Discovery kit]{.std .std-ref}](../boards/ststm32/disco_h735ig.html#board-ststm32-disco-h735ig){.reference .internal}                             STM32H735IGK6    550MHz      1MB      432KB
  [[STM32H747I-DISCO]{.std .std-ref}](../boards/ststm32/disco_h747xi.html#board-ststm32-disco-h747xi){.reference .internal}                                        STM32H747XIH6    400MHz      2MB      512KB
  [[Seeed Arch Max]{.std .std-ref}](../boards/ststm32/seeedArchMax.html#board-ststm32-seeedarchmax){.reference .internal}                                          STM32F407VET6    168MHz      512KB    192KB
  [[Seeed Wio 3G]{.std .std-ref}](../boards/ststm32/wio_3g.html#board-ststm32-wio-3g){.reference .internal}                                                        STM32F439VI      180MHz      2MB      256KB
  [[sakura.io Evaluation Board]{.std .std-ref}](../boards/ststm32/sakuraio_evb_01.html#board-ststm32-sakuraio-evb-01){.reference .internal}                        STM32F411RET6    100MHz      1MB      128KB
  [[u-blox C030-R410M IoT]{.std .std-ref}](../boards/ststm32/ublox_c030_r410m.html#board-ststm32-ublox-c030-r410m){.reference .internal}                           STM32F437VG      180MHz      1MB      256KB
  [[u-blox ODIN-W2]{.std .std-ref}](../boards/ststm32/mtb_ublox_odin_w2.html#board-ststm32-mtb-ublox-odin-w2){.reference .internal}                                STM32F439ZIY6    168MHz      2MB      256KB
:::

::: {#external-debug-tools .section}
#### [External Debug Tools](#id20){.toc-backref role="doc-backlink"}[](#external-debug-tools "Link to this heading"){.headerlink}

Boards listed below are compatible with [[Debugging]{.std
.std-ref}](../plus/debugging.html#piodebug){.reference .internal} but
**DEPEND ON** external debug probe. They **ARE NOT READY** for
debugging. Please click on board name for the further details.

  Name                                                                                                                                                                      MCU             Frequency   Flash      RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ----------- ---------- ----------
  [[1Bitsy]{.std .std-ref}](../boards/ststm32/1bitsy_stm32f415rgt.html#board-ststm32-1bitsy-stm32f415rgt){.reference .internal}                                             STM32F415RGT    168MHz      1MB        128KB
  [[3D Printer Controller]{.std .std-ref}](../boards/ststm32/armed_v1.html#board-ststm32-armed-v1){.reference .internal}                                                    STM32F407VET6   168MHz      512KB      128KB
  [[3D Printer control board]{.std .std-ref}](../boards/ststm32/rumba32_f446ve.html#board-ststm32-rumba32-f446ve){.reference .internal}                                     STM32F446RET6   180MHz      512KB      128KB
  [[96Boards Argonkey (STEVAL-MKI187V1)]{.std .std-ref}](../boards/ststm32/b96b_argonkey.html#board-ststm32-b96b-argonkey){.reference .internal}                            STM32F412CG     100MHz      1MB        256KB
  [[96Boards Neonkey]{.std .std-ref}](../boards/ststm32/b96b_aerocore2.html#board-ststm32-b96b-aerocore2){.reference .internal}                                             STM32F427VIT6   168MHz      1.99MB     256KB
  [[96Boards Neonkey]{.std .std-ref}](../boards/ststm32/b96b_neonkey.html#board-ststm32-b96b-neonkey){.reference .internal}                                                 STM32F411CE     100MHz      512KB      128KB
  [[ACSIP S76S]{.std .std-ref}](../boards/ststm32/acsip_s76s.html#board-ststm32-acsip-s76s){.reference .internal}                                                           STM32L073RZ     32MHz       192KB      20KB
  [[Adafruit Feather STM32F405]{.std .std-ref}](../boards/ststm32/adafruit_feather_f405.html#board-ststm32-adafruit-feather-f405){.reference .internal}                     STM32F405RGT6   168MHz      1MB        128KB
  [[AfroFlight Rev5 (8MHz)]{.std .std-ref}](../boards/ststm32/afroflight_f103cb.html#board-ststm32-afroflight-f103cb){.reference .internal}                                 STM32F103CBT6   72MHz       128KB      20KB
  [[Arduino Giga R1 (M4 core)]{.std .std-ref}](../boards/ststm32/giga_r1_m4.html#board-ststm32-giga-r1-m4){.reference .internal}                                            STM32H747XIH6   480MHz      1MB        287.35KB
  [[Arduino Giga R1 (M7 core)]{.std .std-ref}](../boards/ststm32/giga_r1_m7.html#board-ststm32-giga-r1-m7){.reference .internal}                                            STM32H747XIH6   480MHz      768KB      511.35KB
  [[Arduino Nicla Vision]{.std .std-ref}](../boards/ststm32/nicla_vision.html#board-ststm32-nicla-vision){.reference .internal}                                             STM32H747XIH6   480MHz      768KB      511.35KB
  [[Arduino Nicla Vision (M4 core)]{.std .std-ref}](../boards/ststm32/nicla_vision_m4.html#board-ststm32-nicla-vision-m4){.reference .internal}                             STM32H747XIH6   480MHz      1MB        287.35KB
  [[Arduino Opta]{.std .std-ref}](../boards/ststm32/opta.html#board-ststm32-opta){.reference .internal}                                                                     STM32H747XIH6   480MHz      768KB      511.35KB
  [[Arduino Opta (M4 core)]{.std .std-ref}](../boards/ststm32/opta_m4.html#board-ststm32-opta-m4){.reference .internal}                                                     STM32H747XIH6   480MHz      1MB        287.35KB
  [[Arduino Portenta H7 (M4 core)]{.std .std-ref}](../boards/ststm32/portenta_h7_m4.html#board-ststm32-portenta-h7-m4){.reference .internal}                                STM32H747XIH6   480MHz      1MB        287.35KB
  [[Arduino Portenta H7 (M7 core)]{.std .std-ref}](../boards/ststm32/portenta_h7_m7.html#board-ststm32-portenta-h7-m7){.reference .internal}                                STM32H747XIH6   480MHz      768KB      511.35KB
  [[Black STM32F407VE]{.std .std-ref}](../boards/ststm32/black_f407ve.html#board-ststm32-black-f407ve){.reference .internal}                                                STM32F407VET6   168MHz      512KB      128KB
  [[Black STM32F407VG]{.std .std-ref}](../boards/ststm32/black_f407vg.html#board-ststm32-black-f407vg){.reference .internal}                                                STM32F407VGT6   168MHz      512KB      128KB
  [[Black STM32F407ZE]{.std .std-ref}](../boards/ststm32/black_f407ze.html#board-ststm32-black-f407ze){.reference .internal}                                                STM32F407ZET6   168MHz      512KB      128KB
  [[Black STM32F407ZG]{.std .std-ref}](../boards/ststm32/black_f407zg.html#board-ststm32-black-f407zg){.reference .internal}                                                STM32F407ZGT6   168MHz      1MB        128KB
  [[BlackPill F103C8]{.std .std-ref}](../boards/ststm32/blackpill_f103c8.html#board-ststm32-blackpill-f103c8){.reference .internal}                                         STM32F103C8T6   72MHz       64KB       20KB
  [[BlackPill F103C8 (128k)]{.std .std-ref}](../boards/ststm32/blackpill_f103c8_128.html#board-ststm32-blackpill-f103c8-128){.reference .internal}                          STM32F103C8T6   72MHz       128KB      20KB
  [[BlackPill F303CC]{.std .std-ref}](../boards/ststm32/robotdyn_blackpill_f303cc.html#board-ststm32-robotdyn-blackpill-f303cc){.reference .internal}                       STM32F303CCT6   72MHz       256KB      40KB
  [[Blue STM32F407VE Mini]{.std .std-ref}](../boards/ststm32/blue_f407ve_mini.html#board-ststm32-blue-f407ve-mini){.reference .internal}                                    STM32F407VET6   168MHz      512KB      128KB
  [[BluePill F103C6]{.std .std-ref}](../boards/ststm32/bluepill_f103c6.html#board-ststm32-bluepill-f103c6){.reference .internal}                                            STM32F103C6T6   72MHz       32KB       10KB
  [[BluePill F103C8]{.std .std-ref}](../boards/ststm32/bluepill_f103c8.html#board-ststm32-bluepill-f103c8){.reference .internal}                                            STM32F103C8T6   72MHz       64KB       20KB
  [[BluePill F103C8 (128k)]{.std .std-ref}](../boards/ststm32/bluepill_f103c8_128k.html#board-ststm32-bluepill-f103c8-128k){.reference .internal}                           STM32F103C8T6   72MHz       128KB      20KB
  [[Blues Cygnet]{.std .std-ref}](../boards/ststm32/blues_cygnet.html#board-ststm32-blues-cygnet){.reference .internal}                                                     STM32L433CCT6   80MHz       256KB      64KB
  [[Blues Swan R5]{.std .std-ref}](../boards/ststm32/blues_swan_r5.html#board-ststm32-blues-swan-r5){.reference .internal}                                                  STM32L4R5ZIY6   120MHz      2MB        640KB
  [[BluesWireless Swan R5]{.std .std-ref}](../boards/ststm32/bw_swan_r5.html#board-ststm32-bw-swan-r5){.reference .internal}                                                STM32L4R5ZIY6   120MHz      2MB        640KB
  [[Cicada-L082CZ]{.std .std-ref}](../boards/ststm32/cicada_l082cz.html#board-ststm32-cicada-l082cz){.reference .internal}                                                  STM32L082CZY6   32MHz       192KB      20KB
  [[Core board F401RCT6]{.std .std-ref}](../boards/ststm32/coreboard_f401rc.html#board-ststm32-coreboard-f401rc){.reference .internal}                                      STM32F401RCT6   84MHz       256KB      64KB
  [[Cricket-L082CZ]{.std .std-ref}](../boards/ststm32/cricket_l082cz.html#board-ststm32-cricket-l082cz){.reference .internal}                                               STM32L082CZY6   32MHz       192KB      20KB
  [[Demo F030F4]{.std .std-ref}](../boards/ststm32/demo_f030f4.html#board-ststm32-demo-f030f4){.reference .internal}                                                        STM32F030F4P6   48MHz       16KB       4KB
  [[DevEBox H743VITX]{.std .std-ref}](../boards/ststm32/devebox_h743vitx.html#board-ststm32-devebox-h743vitx){.reference .internal}                                         STM32H743VIT6   480MHz      2MB        512KB
  [[DevEBox H750VBTX]{.std .std-ref}](../boards/ststm32/devebox_h750vbtx.html#board-ststm32-devebox-h750vbtx){.reference .internal}                                         STM32H750VBT6   480MHz      512KB      128KB
  [[Econode-L082CZ]{.std .std-ref}](../boards/ststm32/econode_l082cz.html#board-ststm32-econode-l082cz){.reference .internal}                                               STM32L082CZY6   32MHz       192KB      20KB
  [[Electrosmith Daisy]{.std .std-ref}](../boards/ststm32/electrosmith_daisy.html#board-ststm32-electrosmith-daisy){.reference .internal}                                   STM32H750IBK6   400MHz      128KB      512KB
  [[Electrosmith Daisy Patch SM]{.std .std-ref}](../boards/ststm32/electrosmith_daisy_patch_sm.html#board-ststm32-electrosmith-daisy-patch-sm){.reference .internal}        STM32H750IBK6   400MHz      128KB      512KB
  [[Electrosmith Daisy Petal SM]{.std .std-ref}](../boards/ststm32/electrosmith_daisy_petal_sm.html#board-ststm32-electrosmith-daisy-petal-sm){.reference .internal}        STM32H750IBK6   400MHz      128KB      512KB
  [[Elektor LoRa Node Core F072C8 (128 kB)]{.std .std-ref}](../boards/ststm32/elektor_f072cb.html#board-ststm32-elektor-f072cb){.reference .internal}                       STM32F072C8T6   48MHz       128KB      16KB
  [[Elektor LoRa Node Core F072C8 (64 kB)]{.std .std-ref}](../boards/ststm32/elektor_f072c8.html#board-ststm32-elektor-f072c8){.reference .internal}                        STM32F072C8T6   48MHz       64KB       16KB
  [[Espotel LoRa Module]{.std .std-ref}](../boards/ststm32/elmo_f411re.html#board-ststm32-elmo-f411re){.reference .internal}                                                STM32F411RET6   100MHz      512KB      128KB
  [[F407VG]{.std .std-ref}](../boards/ststm32/diymore_f407vgt.html#board-ststm32-diymore-f407vgt){.reference .internal}                                                     STM32F407VGT6   168MHz      1MB        128KB
  [[FK407M1]{.std .std-ref}](../boards/ststm32/fk407m1.html#board-ststm32-fk407m1){.reference .internal}                                                                    STM32F407VET6   168MHz      512KB      128KB
  [[FYSETC S6]{.std .std-ref}](../boards/ststm32/fysetc_s6.html#board-ststm32-fysetc-s6){.reference .internal}                                                              STM32F446VET6   168MHz      512KB      128KB
  [[Gnat-L082CZ]{.std .std-ref}](../boards/ststm32/gnat_l082cz.html#board-ststm32-gnat-l082cz){.reference .internal}                                                        STM32L082CZY6   32MHz       192KB      20KB
  [[Grasshopper-L082CZ]{.std .std-ref}](../boards/ststm32/grasshopper_l082cz.html#board-ststm32-grasshopper-l082cz){.reference .internal}                                   STM32L082CZY6   32MHz       192KB      20KB
  [[M200 V2]{.std .std-ref}](../boards/ststm32/malyanm200_f070cb.html#board-ststm32-malyanm200-f070cb){.reference .internal}                                                STM32F070CBT6   48MHz       120KB      14.81KB
  [[M300]{.std .std-ref}](../boards/ststm32/malyanm300_f070cb.html#board-ststm32-malyanm300-f070cb){.reference .internal}                                                   STM32F070CBT6   48MHz       120KB      14.81KB
  [[MKR Sharky]{.std .std-ref}](../boards/ststm32/mkr_sharky.html#board-ststm32-mkr-sharky){.reference .internal}                                                           STM32WB55CG     64MHz       512KB      192KB
  [[MTS Dragonfly]{.std .std-ref}](../boards/ststm32/mts_dragonfly_f411re.html#board-ststm32-mts-dragonfly-f411re){.reference .internal}                                    STM32F411RET6   100MHz      512KB      128KB
  [[Malyan M200 V1]{.std .std-ref}](../boards/ststm32/malyanm200_f103cb.html#board-ststm32-malyanm200-f103cb){.reference .internal}                                         STM32F103CBT6   72MHz       120KB      20KB
  [[Maple]{.std .std-ref}](../boards/ststm32/maple.html#board-ststm32-maple){.reference .internal}                                                                          STM32F103RBT6   72MHz       108KB      17KB
  [[Maple (RET6)]{.std .std-ref}](../boards/ststm32/maple_ret6.html#board-ststm32-maple-ret6){.reference .internal}                                                         STM32F103RET6   72MHz       256KB      48KB
  [[Maple Mini Bootloader 2.0]{.std .std-ref}](../boards/ststm32/maple_mini_b20.html#board-ststm32-maple-mini-b20){.reference .internal}                                    STM32F103CBT6   72MHz       120KB      20KB
  [[Maple Mini Original]{.std .std-ref}](../boards/ststm32/maple_mini_origin.html#board-ststm32-maple-mini-origin){.reference .internal}                                    STM32F103CBT6   72MHz       108KB      20KB
  [[Microduino Core STM32 to Flash]{.std .std-ref}](../boards/ststm32/microduino32_flash.html#board-ststm32-microduino32-flash){.reference .internal}                       STM32F103CBT6   72MHz       105.47KB   20KB
  [[MultiTech mDot]{.std .std-ref}](../boards/ststm32/mts_mdot_f405rg.html#board-ststm32-mts-mdot-f405rg){.reference .internal}                                             STM32F411RET6   100MHz      512KB      128KB
  [[MultiTech mDot F411]{.std .std-ref}](../boards/ststm32/mts_mdot_f411re.html#board-ststm32-mts-mdot-f411re){.reference .internal}                                        STM32F411RET6   100MHz      512KB      128KB
  [[MultiTech xDot]{.std .std-ref}](../boards/ststm32/xdot_l151cc.html#board-ststm32-xdot-l151cc){.reference .internal}                                                     STM32L151CCU6   32MHz       256KB      32KB
  [[N2+]{.std .std-ref}](../boards/ststm32/netduino2plus.html#board-ststm32-netduino2plus){.reference .internal}                                                            STM32F405RGT6   168MHz      1MB        128KB
  [[NAMote72]{.std .std-ref}](../boards/ststm32/mote_l152rc.html#board-ststm32-mote-l152rc){.reference .internal}                                                           STM32L152RC     32MHz       256KB      32KB
  [[OLIMEXINO-STM32]{.std .std-ref}](../boards/ststm32/olimexino.html#board-ststm32-olimexino){.reference .internal}                                                        STM32F103RBT6   72MHz       128KB      20KB
  [[Olimex OLIMEXINO-STM32F3]{.std .std-ref}](../boards/ststm32/olimexino_stm32f3.html#board-ststm32-olimexino-stm32f3){.reference .internal}                               STM32F303RCT6   72MHz       256KB      40KB
  [[Olimex STM32-H103]{.std .std-ref}](../boards/ststm32/olimex_f103.html#board-ststm32-olimex-f103){.reference .internal}                                                  STM32F103RBT6   72MHz       128KB      20KB
  [[Olimex STM32-P405]{.std .std-ref}](../boards/ststm32/olimex_p405.html#board-ststm32-olimex-p405){.reference .internal}                                                  STM32F405RGT6   168MHz      1MB        128KB
  [[PYBSTICK26 Duino]{.std .std-ref}](../boards/ststm32/pybstick26_duino.html#board-ststm32-pybstick26-duino){.reference .internal}                                         STM32F072RB     48MHz       128KB      16KB
  [[PYBStick 26 Pro]{.std .std-ref}](../boards/ststm32/pybstick26_pro.html#board-ststm32-pybstick26-pro){.reference .internal}                                              STM32F412RE     100MHz      512KB      256KB
  [[PYBStick Lite 26]{.std .std-ref}](../boards/ststm32/pybstick26_lite.html#board-ststm32-pybstick26-lite){.reference .internal}                                           STM32F401CEU6   84MHz       512KB      96KB
  [[PYBStick Standard 26]{.std .std-ref}](../boards/ststm32/pybstick26_std.html#board-ststm32-pybstick26-std){.reference .internal}                                         STM32F411CEU6   100MHz      512KB      128KB
  [[Piconomix PX-HER0]{.std .std-ref}](../boards/ststm32/piconomix_px_her0.html#board-ststm32-piconomix-px-her0){.reference .internal}                                      STM32L072RB     32MHz       128KB      20KB
  [[PrntrBoard V2]{.std .std-ref}](../boards/ststm32/prntr_v2.html#board-ststm32-prntr-v2){.reference .internal}                                                            STM32F407VET6   168MHz      512KB      128KB
  [[RAK811 LoRa Tracker]{.std .std-ref}](../boards/ststm32/rak811_tracker.html#board-ststm32-rak811-tracker){.reference .internal}                                          STM32L151RBT6   32MHz       128KB      16KB
  [[RAK811 LoRa Tracker]{.std .std-ref}](../boards/ststm32/rak811_tracker_32.html#board-ststm32-rak811-tracker-32){.reference .internal}                                    STM32L151RBT6   32MHz       128KB      32KB
  [[RHF76 052]{.std .std-ref}](../boards/ststm32/rhf76_052.html#board-ststm32-rhf76-052){.reference .internal}                                                              STM32L051C8T6   32MHz       64KB       8KB
  [[RYMCU Nebula Pi F103VE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/rymcu_nebulapi_f103ve.html#board-ststm32-rymcu-nebulapi-f103ve){.reference .internal}   STM32F103VET6   72MHz       512KB      64KB
  [[RYMCU STM32F407VE (192k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/rymcu_f407ve.html#board-ststm32-rymcu-f407ve){.reference .internal}                         STM32F407VET6   168MHz      502.23KB   128KB
  [[ST STM32G0316-DISCO]{.std .std-ref}](../boards/ststm32/disco_g031j6.html#board-ststm32-disco-g031j6){.reference .internal}                                              STM32G031J6     64MHz       32KB       8KB
  [[STEVAL-FCU001V1 Flight controller unit evaluation board]{.std .std-ref}](../boards/ststm32/steval_fcu001v1.html#board-ststm32-steval-fcu001v1){.reference .internal}    STM32F401CCU6   84MHz       256KB      64KB
  [[STM32-E407]{.std .std-ref}](../boards/ststm32/olimex_e407.html#board-ststm32-olimex-e407){.reference .internal}                                                         STM32F407ZGT6   168MHz      1MB        128KB
  [[STM32-H407]{.std .std-ref}](../boards/ststm32/olimex_h407.html#board-ststm32-olimex-h407){.reference .internal}                                                         STM32F407ZGT6   168MHz      1MB        128KB
  [[STM3210C-EVAL]{.std .std-ref}](../boards/ststm32/eval_f107vc.html#board-ststm32-eval-f107vc){.reference .internal}                                                      STM32F107VCT6   72MHz       256KB      64KB
  [[STM32373C-EVAL]{.std .std-ref}](../boards/ststm32/eval_f373vc.html#board-ststm32-eval-f373vc){.reference .internal}                                                     STM32F373VCT6   72MHz       256KB      32KB
  [[STM32F072-EVAL]{.std .std-ref}](../boards/ststm32/eval_f072vb.html#board-ststm32-eval-f072vb){.reference .internal}                                                     STM32F072VBT6   48MHz       128KB      16KB
  [[STM32F103C4 (6k RAM. 16k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103C4.html#board-ststm32-genericstm32f103c4){.reference .internal}                      STM32F103C4T6   72MHz       16KB       6KB
  [[STM32F103C6 (10k RAM. 32k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103C6.html#board-ststm32-genericstm32f103c6){.reference .internal}                     STM32F103C6T6   72MHz       32KB       10KB
  [[STM32F103C8 (20k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103C8.html#board-ststm32-genericstm32f103c8){.reference .internal}                     STM32F103C8T6   72MHz       64KB       20KB
  [[STM32F103CB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103CB.html#board-ststm32-genericstm32f103cb){.reference .internal}                    STM32F103CBT6   72MHz       128KB      20KB
  [[STM32F103R4 (6k RAM. 16k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103R4.html#board-ststm32-genericstm32f103r4){.reference .internal}                      STM32F103R4T6   72MHz       16KB       6KB
  [[STM32F103R6 (10k RAM. 32k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103R6.html#board-ststm32-genericstm32f103r6){.reference .internal}                     STM32F103R6T6   72MHz       32KB       10KB
  [[STM32F103R8 (20k RAM. 64 Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103R8.html#board-ststm32-genericstm32f103r8){.reference .internal}                      STM32F103R8T6   72MHz       64KB       20KB
  [[STM32F103RB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RB.html#board-ststm32-genericstm32f103rb){.reference .internal}                    STM32F103RBT6   72MHz       128KB      20KB
  [[STM32F103RC (48k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RC.html#board-ststm32-genericstm32f103rc){.reference .internal}                    STM32F103RCT6   72MHz       256KB      48KB
  [[STM32F103RD (64k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RD.html#board-ststm32-genericstm32f103rd){.reference .internal}                    STM32F103RDT6   72MHz       384KB      64KB
  [[STM32F103RE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RE.html#board-ststm32-genericstm32f103re){.reference .internal}                    STM32F103RET6   72MHz       512KB      64KB
  [[STM32F103RF (96k RAM. 768k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RF.html#board-ststm32-genericstm32f103rf){.reference .internal}                    STM32F103RFT6   72MHz       768KB      96KB
  [[STM32F103RG (96k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RG.html#board-ststm32-genericstm32f103rg){.reference .internal}                   STM32F103RGT6   72MHz       1MB        96KB
  [[STM32F103T4 (6k RAM. 16k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103T4.html#board-ststm32-genericstm32f103t4){.reference .internal}                      STM32F103T4U6   72MHz       16KB       6KB
  [[STM32F103T6 (10k RAM. 32k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103T6.html#board-ststm32-genericstm32f103t6){.reference .internal}                     STM32F103T6U6   72MHz       32KB       10KB
  [[STM32F103T8 (20k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103T8.html#board-ststm32-genericstm32f103t8){.reference .internal}                     STM32F103T8U6   72MHz       64KB       20KB
  [[STM32F103TB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103TB.html#board-ststm32-genericstm32f103tb){.reference .internal}                    STM32F103TBU6   72MHz       128KB      20KB
  [[STM32F103V8 (20k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103V8.html#board-ststm32-genericstm32f103v8){.reference .internal}                     STM32F103V8T6   72MHz       64KB       20KB
  [[STM32F103VB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VB.html#board-ststm32-genericstm32f103vb){.reference .internal}                    STM32F103VBT6   72MHz       128KB      20KB
  [[STM32F103VC (48k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VC.html#board-ststm32-genericstm32f103vc){.reference .internal}                    STM32F103VCT6   72MHz       256KB      48KB
  [[STM32F103VD (64k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VD.html#board-ststm32-genericstm32f103vd){.reference .internal}                    STM32F103VDT6   72MHz       384KB      64KB
  [[STM32F103VE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VE.html#board-ststm32-genericstm32f103ve){.reference .internal}                    STM32F103VET6   72MHz       512KB      64KB
  [[STM32F103VF (96k RAM. 768k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VF.html#board-ststm32-genericstm32f103vf){.reference .internal}                    STM32F103VFT6   72MHz       768KB      96KB
  [[STM32F103VG (96k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VG.html#board-ststm32-genericstm32f103vg){.reference .internal}                   STM32F103VGT6   72MHz       1MB        96KB
  [[STM32F103ZC (48k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZC.html#board-ststm32-genericstm32f103zc){.reference .internal}                    STM32F103ZCT6   72MHz       256KB      48KB
  [[STM32F103ZD (64k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZD.html#board-ststm32-genericstm32f103zd){.reference .internal}                    STM32F103ZDT6   72MHz       384KB      64KB
  [[STM32F103ZE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZE.html#board-ststm32-genericstm32f103ze){.reference .internal}                    STM32F103ZET6   72MHz       512KB      64KB
  [[STM32F103ZF (96k RAM. 768k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZF.html#board-ststm32-genericstm32f103zf){.reference .internal}                    STM32F103ZFT6   72MHz       768KB      96KB
  [[STM32F103ZG (96k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZG.html#board-ststm32-genericstm32f103zg){.reference .internal}                   STM32F103ZGT6   72MHz       1MB        96KB
  [[STM32F303CB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F303CB.html#board-ststm32-genericstm32f303cb){.reference .internal}                    STM32F303CBT6   72MHz       128KB      32KB
  [[STM32F373RC (32k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F373RC.html#board-ststm32-genericstm32f373rc){.reference .internal}                    STM32F373RCT6   72MHz       256KB      32KB
  [[STM32F401CB (64k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CB.html#board-ststm32-genericstm32f401cb){.reference .internal}                    STM32F401CBU6   84MHz       128KB      64KB
  [[STM32F401CC (64k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CC.html#board-ststm32-genericstm32f401cc){.reference .internal}                    STM32F401CCU6   84MHz       256KB      64KB
  [[STM32F401CD (96k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CD.html#board-ststm32-genericstm32f401cd){.reference .internal}                    STM32F401CDU6   84MHz       384KB      96KB
  [[STM32F401CE (96k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CE.html#board-ststm32-genericstm32f401ce){.reference .internal}                    STM32F401CEU6   84MHz       512KB      96KB
  [[STM32F401RB (64k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RB.html#board-ststm32-genericstm32f401rb){.reference .internal}                    STM32F401RBT6   84MHz       128KB      64KB
  [[STM32F401RC (64k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RC.html#board-ststm32-genericstm32f401rc){.reference .internal}                    STM32F401RCT6   84MHz       256KB      64KB
  [[STM32F401RD (96k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RD.html#board-ststm32-genericstm32f401rd){.reference .internal}                    STM32F401RDT6   84MHz       384KB      96KB
  [[STM32F401RE (96k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RE.html#board-ststm32-genericstm32f401re){.reference .internal}                    STM32F401RET6   84MHz       512KB      96KB
  [[STM32F405RG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F405RG.html#board-ststm32-genericstm32f405rg){.reference .internal}                  STM32F405RGT6   168MHz      1MB        128KB
  [[STM32F407IG (192k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F407IGT6.html#board-ststm32-genericstm32f407igt6){.reference .internal}              STM32F407IGT6   168MHz      1MB        192KB
  [[STM32F407VE (192k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F407VET6.html#board-ststm32-genericstm32f407vet6){.reference .internal}               STM32F407VET6   168MHz      502.23KB   128KB
  [[STM32F407VG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F407VGT6.html#board-ststm32-genericstm32f407vgt6){.reference .internal}              STM32F407VGT6   168MHz      1MB        128KB
  [[STM32F410C8 (32k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410C8.html#board-ststm32-genericstm32f410c8){.reference .internal}                     STM32F410C8T6   100MHz      64KB       32KB
  [[STM32F410CB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410CB.html#board-ststm32-genericstm32f410cb){.reference .internal}                    STM32F410CBT6   100MHz      128KB      32KB
  [[STM32F410R8 (32k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410R8.html#board-ststm32-genericstm32f410r8){.reference .internal}                     STM32F410R8T6   100MHz      64KB       32KB
  [[STM32F410RB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410RB.html#board-ststm32-genericstm32f410rb){.reference .internal}                    STM32F410RBT6   100MHz      128KB      32KB
  [[STM32F411CC (128k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411CC.html#board-ststm32-genericstm32f411cc){.reference .internal}                   STM32F411CCU6   100MHz      256KB      128KB
  [[STM32F411CE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411CE.html#board-ststm32-genericstm32f411ce){.reference .internal}                   STM32F411CEU6   100MHz      512KB      128KB
  [[STM32F411RC (128k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411RC.html#board-ststm32-genericstm32f411rc){.reference .internal}                   STM32F411RCT6   100MHz      256KB      128KB
  [[STM32F411RE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411RE.html#board-ststm32-genericstm32f411re){.reference .internal}                   STM32F411RET6   100MHz      512KB      128KB
  [[STM32F412CE (256k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412CE.html#board-ststm32-genericstm32f412ce){.reference .internal}                   STM32F412CEU6   100MHz      512KB      256KB
  [[STM32F412CG (256k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412CG.html#board-ststm32-genericstm32f412cg){.reference .internal}                  STM32F412CGU6   100MHz      1MB        256KB
  [[STM32F412RE (256k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412RE.html#board-ststm32-genericstm32f412re){.reference .internal}                   STM32F412RET6   100MHz      512KB      256KB
  [[STM32F412RG (256k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412RG.html#board-ststm32-genericstm32f412rg){.reference .internal}                  STM32F412RGT6   100MHz      1MB        256KB
  [[STM32F413CG (320k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413CG.html#board-ststm32-genericstm32f413cg){.reference .internal}                  STM32F413CGU6   100MHz      1MB        320KB
  [[STM32F413CH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413CH.html#board-ststm32-genericstm32f413ch){.reference .internal}                  STM32F413CHU6   100MHz      1.50MB     320KB
  [[STM32F413RG (320k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413RG.html#board-ststm32-genericstm32f413rg){.reference .internal}                  STM32F413RGT6   100MHz      1MB        320KB
  [[STM32F413RH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413RH.html#board-ststm32-genericstm32f413rh){.reference .internal}                  STM32F413RHT6   100MHz      1.50MB     320KB
  [[STM32F415RG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F415RG.html#board-ststm32-genericstm32f415rg){.reference .internal}                  STM32F415RGT6   168MHz      1MB        128KB
  [[STM32F417VE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F417VE.html#board-ststm32-genericstm32f417ve){.reference .internal}                   STM32F417VET6   168MHz      512KB      128KB
  [[STM32F417VG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F417VG.html#board-ststm32-genericstm32f417vg){.reference .internal}                  STM32F417VGT6   168MHz      1MB        128KB
  [[STM32F423CH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F423CH.html#board-ststm32-genericstm32f423ch){.reference .internal}                  STM32F423CHU6   100MHz      1.50MB     320KB
  [[STM32F423RH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F423RH.html#board-ststm32-genericstm32f423rh){.reference .internal}                  STM32F423RHT6   100MHz      1.50MB     320KB
  [[STM32F446RC (128k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F446RC.html#board-ststm32-genericstm32f446rc){.reference .internal}                   STM32F446RCT6   180MHz      256KB      128KB
  [[STM32F446RE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F446RE.html#board-ststm32-genericstm32f446re){.reference .internal}                   STM32F446RET6   180MHz      512KB      128KB
  [[STM32F4Stamp F405]{.std .std-ref}](../boards/ststm32/stm32f4stamp.html#board-ststm32-stm32f4stamp){.reference .internal}                                                STM32F405RGT6   168MHz      1MB        128KB
  [[STM32G431CB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32G431CB.html#board-ststm32-genericstm32g431cb){.reference .internal}                    STM32G431CBU6   170MHz      128KB      32KB
  [[STM32H750VBT6 (1024k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32H750VB.html#board-ststm32-genericstm32h750vb){.reference .internal}                STM32H750VBT6   480MHz      128KB      1MB
  [[STorM32 BGC v1.31 RC]{.std .std-ref}](../boards/ststm32/storm32_v1_31_rc.html#board-ststm32-storm32-v1-31-rc){.reference .internal}                                     STM32F103RCT6   72MHz       256KB      48KB
  [[SeeedStudio LoRa E5 Dev Board]{.std .std-ref}](../boards/ststm32/lora_e5_dev_board.html#board-ststm32-lora-e5-dev-board){.reference .internal}                          STM32WLE5JC     48MHz       256KB      64KB
  [[SeeedStudio LoRa-E5 mini]{.std .std-ref}](../boards/ststm32/lora_e5_mini.html#board-ststm32-lora-e5-mini){.reference .internal}                                         STM32WLE5JC     48MHz       256KB      64KB
  [[SensorTile.box]{.std .std-ref}](../boards/ststm32/steval_mksboxv1.html#board-ststm32-steval-mksboxv1){.reference .internal}                                             STM32L4R9ZI     120MHz      2MB        640KB
  [[Sigma IC AGAFIA SG0]{.std .std-ref}](../boards/ststm32/agafia_sg0.html#board-ststm32-agafia-sg0){.reference .internal}                                                  STM32G071RBT6   64MHz       128KB      36KB
  [[SparkFun MicroMod STM32F405]{.std .std-ref}](../boards/ststm32/sparkfun_micromod_f405.html#board-ststm32-sparkfun-micromod-f405){.reference .internal}                  STM32F405RGT6   168MHz      1MB        128KB
  [[Sparky V1 F303]{.std .std-ref}](../boards/ststm32/sparky_v1.html#board-ststm32-sparky-v1){.reference .internal}                                                         STM32F303CCT6   72MHz       256KB      40KB
  [[ThunderPack v1.0]{.std .std-ref}](../boards/ststm32/thunder_pack.html#board-ststm32-thunder-pack){.reference .internal}                                                 STM32L072KZ     32MHz       192KB      20KB
  [[ThunderPack v1.1+]{.std .std-ref}](../boards/ststm32/thunder_pack_f411.html#board-ststm32-thunder-pack-f411){.reference .internal}                                      STM32F411CEU6   100MHz      512KB      128KB
  [[Tiny STM103T]{.std .std-ref}](../boards/ststm32/hy_tinystm103tb.html#board-ststm32-hy-tinystm103tb){.reference .internal}                                               STM32F103TBU6   72MHz       128KB      20KB
  [[VAkE v1.0]{.std .std-ref}](../boards/ststm32/vake_v1.html#board-ststm32-vake-v1){.reference .internal}                                                                  STM32F446RET6   180MHz      512KB      128KB
  [[VCCGND F103ZET6 Mini]{.std .std-ref}](../boards/ststm32/vccgnd_f103zet6.html#board-ststm32-vccgnd-f103zet6){.reference .internal}                                       STM32F103ZET6   72MHz       512KB      64KB
  [[VCCGND F407ZGT6 Mini]{.std .std-ref}](../boards/ststm32/vccgnd_f407zg_mini.html#board-ststm32-vccgnd-f407zg-mini){.reference .internal}                                 STM32F407ZGT6   168MHz      1MB        128KB
  [[Waveshare Open103Z]{.std .std-ref}](../boards/ststm32/waveshare_open103z.html#board-ststm32-waveshare-open103z){.reference .internal}                                   STM32F103ZET6   72MHz       512KB      64KB
  [[WeAct Studio BlackPill V2.0 (STM32F401CC)]{.std .std-ref}](../boards/ststm32/blackpill_f401cc.html#board-ststm32-blackpill-f401cc){.reference .internal}                STM32F401CCU6   84MHz       256KB      64KB
  [[WeAct Studio BlackPill V2.0 (STM32F411CE)]{.std .std-ref}](../boards/ststm32/blackpill_f411ce.html#board-ststm32-blackpill-f411ce){.reference .internal}                STM32F411CEU6   100MHz      512KB      128KB
  [[WeAct Studio BlackPill V3.0 (STM32F401CE)]{.std .std-ref}](../boards/ststm32/blackpill_f401ce.html#board-ststm32-blackpill-f401ce){.reference .internal}                STM32F401CEU6   84MHz       512KB      96KB
  [[WeAct Studio MiniSTM32H743VITX]{.std .std-ref}](../boards/ststm32/weact_mini_h743vitx.html#board-ststm32-weact-mini-h743vitx){.reference .internal}                     STM32H743VIT6   480MHz      2MB        512KB
  [[WeAct Studio MiniSTM32H750VBTX]{.std .std-ref}](../boards/ststm32/weact_mini_h750vbtx.html#board-ststm32-weact-mini-h750vbtx){.reference .internal}                     STM32H750VBT6   480MHz      512KB      128KB
  [[Wraith V1 ESC]{.std .std-ref}](../boards/ststm32/wraith32_v1.html#board-ststm32-wraith32-v1){.reference .internal}                                                      STM32F051K6     48MHz       32KB       7.75KB
  [[u-blox C030-N211 IoT Starter Kit]{.std .std-ref}](../boards/ststm32/ublox_c030_n211.html#board-ststm32-ublox-c030-n211){.reference .internal}                           STM32F437VG     180MHz      1MB        256KB
  [[u-blox C030-U201 IoT Starter Kit]{.std .std-ref}](../boards/ststm32/ublox_c030_u201.html#board-ststm32-ublox-c030-u201){.reference .internal}                           STM32F437VG     180MHz      1MB        256KB
  [[u-blox EVK-ODIN-W2]{.std .std-ref}](../boards/ststm32/ublox_evk_odin_w2.html#board-ststm32-ublox-evk-odin-w2){.reference .internal}                                     STM32F439ZIY6   168MHz      2MB        256KB
:::
:::
:::

::: {#stable-and-upstream-versions .section}
## [Stable and upstream versions](#id14){.toc-backref role="doc-backlink"}[](#stable-and-upstream-versions "Link to this heading"){.headerlink}

You can switch between [stable
releases](https://github.com/platformio/platform-ststm32/releases){.reference
.external} of ST STM32 development platform and the latest upstream
version using [[platform]{.std
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
    platform = ststm32
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = ststm32@x.y.z
    board = ...
:::
:::
:::

::: {#upstream .section}
### Upstream[](#upstream "Link to this heading"){.headerlink}

::: {.highlight-ini .notranslate}
::: highlight
    [env:upstream_develop]
    platform = https://github.com/platformio/platform-ststm32.git
    board = ...
:::
:::
:::
:::

::: {#packages .section}
## [Packages](#id15){.toc-backref role="doc-backlink"}[](#packages "Link to this heading"){.headerlink}

  Name                                                                                                                                      Description
  ----------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [framework-arduino-mbed](https://registry.platformio.org/tools/platformio/framework-arduino-mbed){.reference .external}                   Arduino framework supporting mbed-enabled boards
  [framework-arduinostm32mxchip](https://registry.platformio.org/tools/platformio/framework-arduinostm32mxchip){.reference .external}       Arduino Wiring-based Framework for the Azure MXChip IoT DevKit
  [framework-arduinoststm32](https://registry.platformio.org/tools/platformio/framework-arduinoststm32){.reference .external}               Arduino Wiring-based Framework for ST STM32 microcontrollers
  [framework-arduinoststm32-maple](https://registry.platformio.org/tools/platformio/framework-arduinoststm32-maple){.reference .external}   Arduino Wiring-based Framework for ST STM32 microcontrollers (Maple Core)
  [framework-arduinoststm32l0](https://registry.platformio.org/tools/platformio/framework-arduinoststm32l0){.reference .external}           Arduino Wiring-based Framework for ST STM32 microcontrollers (ST STM32L0 Core)
  [framework-cmsis](https://registry.platformio.org/tools/platformio/framework-cmsis){.reference .external}                                 Vendor-independent hardware abstraction layer for the Cortex-M processor series
  [framework-cmsis-stm32f0](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32f0){.reference .external}                 CMSIS component for the STMicroelectronics STM32F0 series
  [framework-cmsis-stm32f1](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32f1){.reference .external}                 CMSIS component for the STMicroelectronics STM32F1 series
  [framework-cmsis-stm32f2](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32f2){.reference .external}                 CMSIS component for the STMicroelectronics STM32F2 series
  [framework-cmsis-stm32f3](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32f3){.reference .external}                 CMSIS component for the STMicroelectronics STM32F3 series
  [framework-cmsis-stm32f4](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32f4){.reference .external}                 CMSIS component for the STMicroelectronics STM32F4 series
  [framework-cmsis-stm32f7](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32f7){.reference .external}                 CMSIS component for the STMicroelectronics STM32F7 series
  [framework-cmsis-stm32g0](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32g0){.reference .external}                 CMSIS component for the STMicroelectronics STM32G0 series
  [framework-cmsis-stm32g4](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32g4){.reference .external}                 CMSIS component for the STMicroelectronics STM32G4 series
  [framework-cmsis-stm32h7](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32h7){.reference .external}                 CMSIS component for the STMicroelectronics STM32H7 series
  [framework-cmsis-stm32l0](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32l0){.reference .external}                 CMSIS component for the STMicroelectronics STM32L0 series
  [framework-cmsis-stm32l1](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32l1){.reference .external}                 CMSIS component for the STMicroelectronics STM32L1 series
  [framework-cmsis-stm32l4](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32l4){.reference .external}                 CMSIS component for the STMicroelectronics STM32L4 series
  [framework-cmsis-stm32l5](https://registry.platformio.org/tools/platformio/framework-cmsis-stm32l5){.reference .external}                 CMSIS component for the STMicroelectronics STM32L5 series
  [framework-libopencm3](https://registry.platformio.org/tools/platformio/framework-libopencm3){.reference .external}                       The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers.
  [framework-mbed](https://registry.platformio.org/tools/platformio/framework-mbed){.reference .external}                                   Arm Mbed OS is a platform operating system designed for the internet of things
  [framework-spl](https://registry.platformio.org/tools/platformio/framework-spl){.reference .external}                                     Standard Peripheral Library for ST STM32 microcontrollers
  [framework-stm32cubef0](https://registry.platformio.org/tools/platformio/framework-stm32cubef0){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF0 MCU Firmware Package)
  [framework-stm32cubef1](https://registry.platformio.org/tools/platformio/framework-stm32cubef1){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF1 MCU Firmware Package)
  [framework-stm32cubef2](https://registry.platformio.org/tools/platformio/framework-stm32cubef2){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF2 MCU Firmware Package)
  [framework-stm32cubef3](https://registry.platformio.org/tools/platformio/framework-stm32cubef3){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF3 MCU Firmware Package)
  [framework-stm32cubef4](https://registry.platformio.org/tools/platformio/framework-stm32cubef4){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF4 MCU Firmware Package)
  [framework-stm32cubef7](https://registry.platformio.org/tools/platformio/framework-stm32cubef7){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeF7 MCU Firmware Package)
  [framework-stm32cubeg0](https://registry.platformio.org/tools/platformio/framework-stm32cubeg0){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeG0 MCU Firmware Package)
  [framework-stm32cubeg4](https://registry.platformio.org/tools/platformio/framework-stm32cubeg4){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeG4 MCU Firmware Package)
  [framework-stm32cubeh7](https://registry.platformio.org/tools/platformio/framework-stm32cubeh7){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeH7 MCU Firmware Package)
  [framework-stm32cubel0](https://registry.platformio.org/tools/platformio/framework-stm32cubel0){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeL0 MCU Firmware Package)
  [framework-stm32cubel1](https://registry.platformio.org/tools/platformio/framework-stm32cubel1){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeL1 MCU Firmware Package)
  [framework-stm32cubel4](https://registry.platformio.org/tools/platformio/framework-stm32cubel4){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeL4 MCU Firmware Package)
  [framework-stm32cubel5](https://registry.platformio.org/tools/platformio/framework-stm32cubel5){.reference .external}                     STM32Cube is a set of tools and embedded software bricks available free of charge to enable fast and easy development on the STM32 platform (STM32CubeL5 MCU Firmware Package)
  [framework-zephyr](https://registry.platformio.org/tools/platformio/framework-zephyr){.reference .external}                               Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures
  [tool-cmake](https://registry.platformio.org/tools/platformio/tool-cmake){.reference .external}                                           CMake is an open-source, cross-platform family of tools designed to build, test and package software
  [tool-dfuutil](https://registry.platformio.org/tools/platformio/tool-dfuutil){.reference .external}                                       Device Firmware Upgrade Utilities
  [tool-dfuutil-arduino](https://registry.platformio.org/tools/platformio/tool-dfuutil-arduino){.reference .external}                       Device Firmware Upgrade Utilities
  [tool-dtc](https://registry.platformio.org/tools/platformio/tool-dtc){.reference .external}                                               Device tree compiler
  [tool-gperf](https://registry.platformio.org/tools/platformio/tool-gperf){.reference .external}                                           GNU gperf is a perfect hash function generator
  [tool-jlink](https://registry.platformio.org/tools/platformio/tool-jlink){.reference .external}                                           Software and Documentation Pack for SEGGER J-Link debug probes
  [tool-ldscripts-ststm32](https://registry.platformio.org/tools/platformio/tool-ldscripts-ststm32){.reference .external}                   Linker scripts pack for STMicroelectronics STM32 platform
  [tool-ninja](https://registry.platformio.org/tools/platformio/tool-ninja){.reference .external}                                           Ninja is a small build system with a focus on speed
  [tool-openocd](https://registry.platformio.org/tools/platformio/tool-openocd){.reference .external}                                       Open On-Chip Debugger. Free and Open On-Chip Debugging, In-System Programming and Boundary-Scan Testing
  [tool-stm32duino](https://registry.platformio.org/tools/platformio/tool-stm32duino){.reference .external}                                 STM32Duino Tools
  [toolchain-gccarmnoneeabi](https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi){.reference .external}               GNU toolchain for Arm Cortex-M and Cortex-R processors

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
## [Frameworks](#id16){.toc-backref role="doc-backlink"}[](#frameworks "Link to this heading"){.headerlink}

  Name                                                                                                         Description
  ------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[Arduino]{.std .std-ref}](../frameworks/arduino.html#framework-arduino){.reference .internal}               Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.
  [[CMSIS]{.std .std-ref}](../frameworks/cmsis.html#framework-cmsis){.reference .internal}                     Vendor-independent hardware abstraction layer for the Cortex-M processor series
  [[LibOpenCM3]{.std .std-ref}](../frameworks/libopencm3.html#framework-libopencm3){.reference .internal}      The libopencm3 project aims to create an open-source firmware library for various ARM Cortex-M microcontrollers.
  [[Mbed]{.std .std-ref}](../frameworks/mbed.html#framework-mbed){.reference .internal}                        Arm Mbed OS is a platform operating system designed for the internet of things
  [[Standard Peripheral Library]{.std .std-ref}](../frameworks/spl.html#framework-spl){.reference .internal}   Standard Peripheral Library for ST STM32 microcontrollers
  [[STM32Cube]{.std .std-ref}](../frameworks/stm32cube.html#framework-stm32cube){.reference .internal}         STM32Cube embedded software libraries, including: The HAL hardware abstraction layer, enabling portability between different STM32 devices via standardized API calls; The Low-Layer (LL) APIs, a light-weight, optimized, expert oriented set of APIs designed for both performance and runtime efficiency
  [[Zephyr]{.std .std-ref}](../frameworks/zephyr.html#framework-zephyr){.reference .internal}                  Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures
:::

::: {#boards .section}
## [Boards](#id17){.toc-backref role="doc-backlink"}[](#boards "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

-   You can list pre-configured boards by [[pio boards]{.std
    .std-ref}](../core/userguide/cmd_boards.html#cmd-boards){.reference
    .internal} command

-   For more detailed [`board`{.docutils .literal .notranslate}]{.pre}
    information please scroll the tables below by horizontally.
:::

::: {#bitsquared .section}
### 1BitSquared[](#bitsquared "Link to this heading"){.headerlink}

  Name                                                                                                                            Debug      MCU            Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------- ---------- -------------- ----------- ------- -------
  [[1Bitsy]{.std .std-ref}](../boards/ststm32/1bitsy_stm32f415rgt.html#board-ststm32-1bitsy-stm32f415rgt){.reference .internal}   External   STM32F415RGT   168MHz      1MB     128KB
:::

::: {#id2 .section}
### 96Boards[](#id2 "Link to this heading"){.headerlink}

  Name                                                                                                                                             Debug      MCU             Frequency   Flash    RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------ ---------- --------------- ----------- -------- -------
  [[96Boards Argonkey (STEVAL-MKI187V1)]{.std .std-ref}](../boards/ststm32/b96b_argonkey.html#board-ststm32-b96b-argonkey){.reference .internal}   External   STM32F412CG     100MHz      1MB      256KB
  [[96Boards B96B-F446VE]{.std .std-ref}](../boards/ststm32/b96b_f446ve.html#board-ststm32-b96b-f446ve){.reference .internal}                      On-board   STM32F446VET6   168MHz      512KB    128KB
  [[96Boards Neonkey]{.std .std-ref}](../boards/ststm32/b96b_aerocore2.html#board-ststm32-b96b-aerocore2){.reference .internal}                    External   STM32F427VIT6   168MHz      1.99MB   256KB
  [[96Boards Neonkey]{.std .std-ref}](../boards/ststm32/b96b_neonkey.html#board-ststm32-b96b-neonkey){.reference .internal}                        External   STM32F411CE     100MHz      512KB    128KB
:::

::: {#acsip .section}
### ACSIP[](#acsip "Link to this heading"){.headerlink}

  Name                                                                                                              Debug      MCU           Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------- ---------- ------------- ----------- ------- ------
  [[ACSIP S76S]{.std .std-ref}](../boards/ststm32/acsip_s76s.html#board-ststm32-acsip-s76s){.reference .internal}   External   STM32L073RZ   32MHz       192KB   20KB
:::

::: {#adafruit .section}
### Adafruit[](#adafruit "Link to this heading"){.headerlink}

  Name                                                                                                                                                    Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Adafruit Feather STM32F405]{.std .std-ref}](../boards/ststm32/adafruit_feather_f405.html#board-ststm32-adafruit-feather-f405){.reference .internal}   External   STM32F405RGT6   168MHz      1MB     128KB
:::

::: {#afroflight .section}
### AfroFlight[](#afroflight "Link to this heading"){.headerlink}

  Name                                                                                                                                        Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[AfroFlight Rev5 (8MHz)]{.std .std-ref}](../boards/ststm32/afroflight_f103cb.html#board-ststm32-afroflight-f103cb){.reference .internal}   External   STM32F103CBT6   72MHz       128KB   20KB
:::

::: {#airbot .section}
### Airbot[](#airbot "Link to this heading"){.headerlink}

  Name                                                                                                                   Debug      MCU           Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------- ---------- ------------- ----------- ------- --------
  [[Wraith V1 ESC]{.std .std-ref}](../boards/ststm32/wraith32_v1.html#board-ststm32-wraith32-v1){.reference .internal}   External   STM32F051K6   48MHz       32KB    7.75KB
:::

::: {#arduino .section}
### Arduino[](#arduino "Link to this heading"){.headerlink}

  Name                                                                                                                                            Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ----------
  [[Arduino Giga R1 (M4 core)]{.std .std-ref}](../boards/ststm32/giga_r1_m4.html#board-ststm32-giga-r1-m4){.reference .internal}                  External   STM32H747XIH6   480MHz      1MB     287.35KB
  [[Arduino Giga R1 (M7 core)]{.std .std-ref}](../boards/ststm32/giga_r1_m7.html#board-ststm32-giga-r1-m7){.reference .internal}                  External   STM32H747XIH6   480MHz      768KB   511.35KB
  [[Arduino Nicla Vision]{.std .std-ref}](../boards/ststm32/nicla_vision.html#board-ststm32-nicla-vision){.reference .internal}                   External   STM32H747XIH6   480MHz      768KB   511.35KB
  [[Arduino Nicla Vision (M4 core)]{.std .std-ref}](../boards/ststm32/nicla_vision_m4.html#board-ststm32-nicla-vision-m4){.reference .internal}   External   STM32H747XIH6   480MHz      1MB     287.35KB
  [[Arduino Opta]{.std .std-ref}](../boards/ststm32/opta.html#board-ststm32-opta){.reference .internal}                                           External   STM32H747XIH6   480MHz      768KB   511.35KB
  [[Arduino Opta (M4 core)]{.std .std-ref}](../boards/ststm32/opta_m4.html#board-ststm32-opta-m4){.reference .internal}                           External   STM32H747XIH6   480MHz      1MB     287.35KB
  [[Arduino Portenta H7 (M4 core)]{.std .std-ref}](../boards/ststm32/portenta_h7_m4.html#board-ststm32-portenta-h7-m4){.reference .internal}      External   STM32H747XIH6   480MHz      1MB     287.35KB
  [[Arduino Portenta H7 (M7 core)]{.std .std-ref}](../boards/ststm32/portenta_h7_m7.html#board-ststm32-portenta-h7-m7){.reference .internal}      External   STM32H747XIH6   480MHz      768KB   511.35KB
:::

::: {#armed .section}
### Armed[](#armed "Link to this heading"){.headerlink}

  Name                                                                                                                     Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------ ---------- --------------- ----------- ------- -------
  [[3D Printer Controller]{.std .std-ref}](../boards/ststm32/armed_v1.html#board-ststm32-armed-v1){.reference .internal}   External   STM32F407VET6   168MHz      512KB   128KB
:::

::: {#armstrap .section}
### Armstrap[](#armstrap "Link to this heading"){.headerlink}

  Name                                                                                                                                       Debug      MCU             Frequency   Flash    RAM
  ------------------------------------------------------------------------------------------------------------------------------------------ ---------- --------------- ----------- -------- -------
  [[Armstrap Eagle 1024]{.std .std-ref}](../boards/ststm32/armstrap_eagle1024.html#board-ststm32-armstrap-eagle1024){.reference .internal}   On-board   STM32F417VGT6   168MHz      1MB      192KB
  [[Armstrap Eagle 2048]{.std .std-ref}](../boards/ststm32/armstrap_eagle2048.html#board-ststm32-armstrap-eagle2048){.reference .internal}   On-board   STM32F427VIT6   168MHz      1.99MB   256KB
  [[Armstrap Eagle 512]{.std .std-ref}](../boards/ststm32/armstrap_eagle512.html#board-ststm32-armstrap-eagle512){.reference .internal}      On-board   STM32F407VET6   168MHz      512KB    192KB
:::

::: {#avnet-silica .section}
### Avnet Silica[](#avnet-silica "Link to this heading"){.headerlink}

  Name                                                                                                                                  Debug      MCU           Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------- ---------- ------------- ----------- ------- -------
  [[ST Sensor Node]{.std .std-ref}](../boards/ststm32/silica_sensor_node.html#board-ststm32-silica-sensor-node){.reference .internal}   On-board   STM32L476JG   80MHz       1MB     128KB
:::

::: {#big-tree-tech .section}
### Big Tree Tech[](#big-tree-tech "Link to this heading"){.headerlink}

  Name                                                                                                                                    Debug      MCU             Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Big Tree Tech EBB42 V1.1]{.std .std-ref}](../boards/ststm32/btt_ebb42_v1_1.html#board-ststm32-btt-ebb42-v1-1){.reference .internal}   On-board   STM32G0B1RET6   64MHz       128KB   144KB
:::

::: {#blues .section}
### Blues[](#blues "Link to this heading"){.headerlink}

  Name                                                                                                                       Debug      MCU             Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Blues Cygnet]{.std .std-ref}](../boards/ststm32/blues_cygnet.html#board-ststm32-blues-cygnet){.reference .internal}      External   STM32L433CCT6   80MHz       256KB   64KB
  [[Blues Swan R5]{.std .std-ref}](../boards/ststm32/blues_swan_r5.html#board-ststm32-blues-swan-r5){.reference .internal}   External   STM32L4R5ZIY6   120MHz      2MB     640KB
:::

::: {#blueswireless .section}
### BluesWireless[](#blueswireless "Link to this heading"){.headerlink}

  Name                                                                                                                         Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[BluesWireless Swan R5]{.std .std-ref}](../boards/ststm32/bw_swan_r5.html#board-ststm32-bw-swan-r5){.reference .internal}   External   STM32L4R5ZIY6   120MHz      2MB     640KB
:::

::: {#devebox .section}
### DevEBox[](#devebox "Link to this heading"){.headerlink}

  Name                                                                                                                                Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[DevEBox H743VITX]{.std .std-ref}](../boards/ststm32/devebox_h743vitx.html#board-ststm32-devebox-h743vitx){.reference .internal}   External   STM32H743VIT6   480MHz      2MB     512KB
  [[DevEBox H750VBTX]{.std .std-ref}](../boards/ststm32/devebox_h750vbtx.html#board-ststm32-devebox-h750vbtx){.reference .internal}   External   STM32H750VBT6   480MHz      512KB   128KB
:::

::: {#diymore .section}
### Diymore[](#diymore "Link to this heading"){.headerlink}

  Name                                                                                                                    Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[F407VG]{.std .std-ref}](../boards/ststm32/diymore_f407vgt.html#board-ststm32-diymore-f407vgt){.reference .internal}   External   STM32F407VGT6   168MHz      1MB     128KB
:::

::: {#econode .section}
### Econode[](#econode "Link to this heading"){.headerlink}

  Name                                                                                                                          Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Econode-L082CZ]{.std .std-ref}](../boards/ststm32/econode_l082cz.html#board-ststm32-econode-l082cz){.reference .internal}   External   STM32L082CZY6   32MHz       192KB   20KB
:::

::: {#electrosmith .section}
### Electrosmith[](#electrosmith "Link to this heading"){.headerlink}

  Name                                                                                                                                                                 Debug      MCU             Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Electrosmith Daisy]{.std .std-ref}](../boards/ststm32/electrosmith_daisy.html#board-ststm32-electrosmith-daisy){.reference .internal}                              External   STM32H750IBK6   400MHz      128KB   512KB
  [[Electrosmith Daisy Patch SM]{.std .std-ref}](../boards/ststm32/electrosmith_daisy_patch_sm.html#board-ststm32-electrosmith-daisy-patch-sm){.reference .internal}   External   STM32H750IBK6   400MHz      128KB   512KB
  [[Electrosmith Daisy Petal SM]{.std .std-ref}](../boards/ststm32/electrosmith_daisy_petal_sm.html#board-ststm32-electrosmith-daisy-petal-sm){.reference .internal}   External   STM32H750IBK6   400MHz      128KB   512KB
:::

::: {#elektor .section}
### Elektor[](#elektor "Link to this heading"){.headerlink}

  Name                                                                                                                                                  Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Elektor LoRa Node Core F072C8 (128 kB)]{.std .std-ref}](../boards/ststm32/elektor_f072cb.html#board-ststm32-elektor-f072cb){.reference .internal}   External   STM32F072C8T6   48MHz       128KB   16KB
  [[Elektor LoRa Node Core F072C8 (64 kB)]{.std .std-ref}](../boards/ststm32/elektor_f072c8.html#board-ststm32-elektor-f072c8){.reference .internal}    External   STM32F072C8T6   48MHz       64KB    16KB
:::

::: {#espotel .section}
### Espotel[](#espotel "Link to this heading"){.headerlink}

  Name                                                                                                                         Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Espotel LoRa Module]{.std .std-ref}](../boards/ststm32/elmo_f411re.html#board-ststm32-elmo-f411re){.reference .internal}   External   STM32F411RET6   100MHz      512KB   128KB
:::

::: {#fysetc .section}
### FYSETC[](#fysetc "Link to this heading"){.headerlink}

  Name                                                                                                           Debug      MCU             Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[FYSETC S6]{.std .std-ref}](../boards/ststm32/fysetc_s6.html#board-ststm32-fysetc-s6){.reference .internal}   External   STM32F446VET6   168MHz      512KB   128KB
:::

::: {#generic .section}
### Generic[](#generic "Link to this heading"){.headerlink}

  Name                                                                                                                                                           Debug      MCU             Frequency   Flash      RAM
  -------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ---------- -------
  [[BlackPill F103C8]{.std .std-ref}](../boards/ststm32/blackpill_f103c8.html#board-ststm32-blackpill-f103c8){.reference .internal}                              External   STM32F103C8T6   72MHz       64KB       20KB
  [[BlackPill F103C8 (128k)]{.std .std-ref}](../boards/ststm32/blackpill_f103c8_128.html#board-ststm32-blackpill-f103c8-128){.reference .internal}               External   STM32F103C8T6   72MHz       128KB      20KB
  [[BluePill F103C6]{.std .std-ref}](../boards/ststm32/bluepill_f103c6.html#board-ststm32-bluepill-f103c6){.reference .internal}                                 External   STM32F103C6T6   72MHz       32KB       10KB
  [[BluePill F103C8]{.std .std-ref}](../boards/ststm32/bluepill_f103c8.html#board-ststm32-bluepill-f103c8){.reference .internal}                                 External   STM32F103C8T6   72MHz       64KB       20KB
  [[BluePill F103C8 (128k)]{.std .std-ref}](../boards/ststm32/bluepill_f103c8_128k.html#board-ststm32-bluepill-f103c8-128k){.reference .internal}                External   STM32F103C8T6   72MHz       128KB      20KB
  [[Demo F030F4]{.std .std-ref}](../boards/ststm32/demo_f030f4.html#board-ststm32-demo-f030f4){.reference .internal}                                             External   STM32F030F4P6   48MHz       16KB       4KB
  [[FK407M1]{.std .std-ref}](../boards/ststm32/fk407m1.html#board-ststm32-fk407m1){.reference .internal}                                                         External   STM32F407VET6   168MHz      512KB      128KB
  [[STM32F103C4 (6k RAM. 16k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103C4.html#board-ststm32-genericstm32f103c4){.reference .internal}           External   STM32F103C4T6   72MHz       16KB       6KB
  [[STM32F103C6 (10k RAM. 32k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103C6.html#board-ststm32-genericstm32f103c6){.reference .internal}          External   STM32F103C6T6   72MHz       32KB       10KB
  [[STM32F103C8 (20k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103C8.html#board-ststm32-genericstm32f103c8){.reference .internal}          External   STM32F103C8T6   72MHz       64KB       20KB
  [[STM32F103CB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103CB.html#board-ststm32-genericstm32f103cb){.reference .internal}         External   STM32F103CBT6   72MHz       128KB      20KB
  [[STM32F103R4 (6k RAM. 16k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103R4.html#board-ststm32-genericstm32f103r4){.reference .internal}           External   STM32F103R4T6   72MHz       16KB       6KB
  [[STM32F103R6 (10k RAM. 32k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103R6.html#board-ststm32-genericstm32f103r6){.reference .internal}          External   STM32F103R6T6   72MHz       32KB       10KB
  [[STM32F103R8 (20k RAM. 64 Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103R8.html#board-ststm32-genericstm32f103r8){.reference .internal}           External   STM32F103R8T6   72MHz       64KB       20KB
  [[STM32F103RB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RB.html#board-ststm32-genericstm32f103rb){.reference .internal}         External   STM32F103RBT6   72MHz       128KB      20KB
  [[STM32F103RC (48k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RC.html#board-ststm32-genericstm32f103rc){.reference .internal}         External   STM32F103RCT6   72MHz       256KB      48KB
  [[STM32F103RD (64k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RD.html#board-ststm32-genericstm32f103rd){.reference .internal}         External   STM32F103RDT6   72MHz       384KB      64KB
  [[STM32F103RE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RE.html#board-ststm32-genericstm32f103re){.reference .internal}         External   STM32F103RET6   72MHz       512KB      64KB
  [[STM32F103RF (96k RAM. 768k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RF.html#board-ststm32-genericstm32f103rf){.reference .internal}         External   STM32F103RFT6   72MHz       768KB      96KB
  [[STM32F103RG (96k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103RG.html#board-ststm32-genericstm32f103rg){.reference .internal}        External   STM32F103RGT6   72MHz       1MB        96KB
  [[STM32F103T4 (6k RAM. 16k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103T4.html#board-ststm32-genericstm32f103t4){.reference .internal}           External   STM32F103T4U6   72MHz       16KB       6KB
  [[STM32F103T6 (10k RAM. 32k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103T6.html#board-ststm32-genericstm32f103t6){.reference .internal}          External   STM32F103T6U6   72MHz       32KB       10KB
  [[STM32F103T8 (20k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103T8.html#board-ststm32-genericstm32f103t8){.reference .internal}          External   STM32F103T8U6   72MHz       64KB       20KB
  [[STM32F103TB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103TB.html#board-ststm32-genericstm32f103tb){.reference .internal}         External   STM32F103TBU6   72MHz       128KB      20KB
  [[STM32F103V8 (20k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103V8.html#board-ststm32-genericstm32f103v8){.reference .internal}          External   STM32F103V8T6   72MHz       64KB       20KB
  [[STM32F103VB (20k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VB.html#board-ststm32-genericstm32f103vb){.reference .internal}         External   STM32F103VBT6   72MHz       128KB      20KB
  [[STM32F103VC (48k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VC.html#board-ststm32-genericstm32f103vc){.reference .internal}         External   STM32F103VCT6   72MHz       256KB      48KB
  [[STM32F103VD (64k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VD.html#board-ststm32-genericstm32f103vd){.reference .internal}         External   STM32F103VDT6   72MHz       384KB      64KB
  [[STM32F103VE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VE.html#board-ststm32-genericstm32f103ve){.reference .internal}         External   STM32F103VET6   72MHz       512KB      64KB
  [[STM32F103VF (96k RAM. 768k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VF.html#board-ststm32-genericstm32f103vf){.reference .internal}         External   STM32F103VFT6   72MHz       768KB      96KB
  [[STM32F103VG (96k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103VG.html#board-ststm32-genericstm32f103vg){.reference .internal}        External   STM32F103VGT6   72MHz       1MB        96KB
  [[STM32F103ZC (48k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZC.html#board-ststm32-genericstm32f103zc){.reference .internal}         External   STM32F103ZCT6   72MHz       256KB      48KB
  [[STM32F103ZD (64k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZD.html#board-ststm32-genericstm32f103zd){.reference .internal}         External   STM32F103ZDT6   72MHz       384KB      64KB
  [[STM32F103ZE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZE.html#board-ststm32-genericstm32f103ze){.reference .internal}         External   STM32F103ZET6   72MHz       512KB      64KB
  [[STM32F103ZF (96k RAM. 768k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZF.html#board-ststm32-genericstm32f103zf){.reference .internal}         External   STM32F103ZFT6   72MHz       768KB      96KB
  [[STM32F103ZG (96k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F103ZG.html#board-ststm32-genericstm32f103zg){.reference .internal}        External   STM32F103ZGT6   72MHz       1MB        96KB
  [[STM32F303CB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F303CB.html#board-ststm32-genericstm32f303cb){.reference .internal}         External   STM32F303CBT6   72MHz       128KB      32KB
  [[STM32F373RC (32k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F373RC.html#board-ststm32-genericstm32f373rc){.reference .internal}         External   STM32F373RCT6   72MHz       256KB      32KB
  [[STM32F401CB (64k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CB.html#board-ststm32-genericstm32f401cb){.reference .internal}         External   STM32F401CBU6   84MHz       128KB      64KB
  [[STM32F401CC (64k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CC.html#board-ststm32-genericstm32f401cc){.reference .internal}         External   STM32F401CCU6   84MHz       256KB      64KB
  [[STM32F401CD (96k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CD.html#board-ststm32-genericstm32f401cd){.reference .internal}         External   STM32F401CDU6   84MHz       384KB      96KB
  [[STM32F401CE (96k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401CE.html#board-ststm32-genericstm32f401ce){.reference .internal}         External   STM32F401CEU6   84MHz       512KB      96KB
  [[STM32F401RB (64k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RB.html#board-ststm32-genericstm32f401rb){.reference .internal}         External   STM32F401RBT6   84MHz       128KB      64KB
  [[STM32F401RC (64k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RC.html#board-ststm32-genericstm32f401rc){.reference .internal}         External   STM32F401RCT6   84MHz       256KB      64KB
  [[STM32F401RD (96k RAM. 384k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RD.html#board-ststm32-genericstm32f401rd){.reference .internal}         External   STM32F401RDT6   84MHz       384KB      96KB
  [[STM32F401RE (96k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F401RE.html#board-ststm32-genericstm32f401re){.reference .internal}         External   STM32F401RET6   84MHz       512KB      96KB
  [[STM32F405RG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F405RG.html#board-ststm32-genericstm32f405rg){.reference .internal}       External   STM32F405RGT6   168MHz      1MB        128KB
  [[STM32F407IG (192k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F407IGT6.html#board-ststm32-genericstm32f407igt6){.reference .internal}   External   STM32F407IGT6   168MHz      1MB        192KB
  [[STM32F407VE (192k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F407VET6.html#board-ststm32-genericstm32f407vet6){.reference .internal}    External   STM32F407VET6   168MHz      502.23KB   128KB
  [[STM32F407VG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F407VGT6.html#board-ststm32-genericstm32f407vgt6){.reference .internal}   External   STM32F407VGT6   168MHz      1MB        128KB
  [[STM32F410C8 (32k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410C8.html#board-ststm32-genericstm32f410c8){.reference .internal}          External   STM32F410C8T6   100MHz      64KB       32KB
  [[STM32F410CB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410CB.html#board-ststm32-genericstm32f410cb){.reference .internal}         External   STM32F410CBT6   100MHz      128KB      32KB
  [[STM32F410R8 (32k RAM. 64k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410R8.html#board-ststm32-genericstm32f410r8){.reference .internal}          External   STM32F410R8T6   100MHz      64KB       32KB
  [[STM32F410RB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F410RB.html#board-ststm32-genericstm32f410rb){.reference .internal}         External   STM32F410RBT6   100MHz      128KB      32KB
  [[STM32F411CC (128k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411CC.html#board-ststm32-genericstm32f411cc){.reference .internal}        External   STM32F411CCU6   100MHz      256KB      128KB
  [[STM32F411CE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411CE.html#board-ststm32-genericstm32f411ce){.reference .internal}        External   STM32F411CEU6   100MHz      512KB      128KB
  [[STM32F411RC (128k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411RC.html#board-ststm32-genericstm32f411rc){.reference .internal}        External   STM32F411RCT6   100MHz      256KB      128KB
  [[STM32F411RE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F411RE.html#board-ststm32-genericstm32f411re){.reference .internal}        External   STM32F411RET6   100MHz      512KB      128KB
  [[STM32F412CE (256k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412CE.html#board-ststm32-genericstm32f412ce){.reference .internal}        External   STM32F412CEU6   100MHz      512KB      256KB
  [[STM32F412CG (256k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412CG.html#board-ststm32-genericstm32f412cg){.reference .internal}       External   STM32F412CGU6   100MHz      1MB        256KB
  [[STM32F412RE (256k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412RE.html#board-ststm32-genericstm32f412re){.reference .internal}        External   STM32F412RET6   100MHz      512KB      256KB
  [[STM32F412RG (256k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F412RG.html#board-ststm32-genericstm32f412rg){.reference .internal}       External   STM32F412RGT6   100MHz      1MB        256KB
  [[STM32F413CG (320k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413CG.html#board-ststm32-genericstm32f413cg){.reference .internal}       External   STM32F413CGU6   100MHz      1MB        320KB
  [[STM32F413CH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413CH.html#board-ststm32-genericstm32f413ch){.reference .internal}       External   STM32F413CHU6   100MHz      1.50MB     320KB
  [[STM32F413RG (320k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413RG.html#board-ststm32-genericstm32f413rg){.reference .internal}       External   STM32F413RGT6   100MHz      1MB        320KB
  [[STM32F413RH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F413RH.html#board-ststm32-genericstm32f413rh){.reference .internal}       External   STM32F413RHT6   100MHz      1.50MB     320KB
  [[STM32F415RG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F415RG.html#board-ststm32-genericstm32f415rg){.reference .internal}       External   STM32F415RGT6   168MHz      1MB        128KB
  [[STM32F417VE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F417VE.html#board-ststm32-genericstm32f417ve){.reference .internal}        External   STM32F417VET6   168MHz      512KB      128KB
  [[STM32F417VG (128k RAM. 1024k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F417VG.html#board-ststm32-genericstm32f417vg){.reference .internal}       External   STM32F417VGT6   168MHz      1MB        128KB
  [[STM32F423CH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F423CH.html#board-ststm32-genericstm32f423ch){.reference .internal}       External   STM32F423CHU6   100MHz      1.50MB     320KB
  [[STM32F423RH (320k RAM. 1536k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F423RH.html#board-ststm32-genericstm32f423rh){.reference .internal}       External   STM32F423RHT6   100MHz      1.50MB     320KB
  [[STM32F446RC (128k RAM. 256k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F446RC.html#board-ststm32-genericstm32f446rc){.reference .internal}        External   STM32F446RCT6   180MHz      256KB      128KB
  [[STM32F446RE (128k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32F446RE.html#board-ststm32-genericstm32f446re){.reference .internal}        External   STM32F446RET6   180MHz      512KB      128KB
  [[STM32F4Stamp F405]{.std .std-ref}](../boards/ststm32/stm32f4stamp.html#board-ststm32-stm32f4stamp){.reference .internal}                                     External   STM32F405RGT6   168MHz      1MB        128KB
  [[STM32H750VBT6 (1024k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32H750VB.html#board-ststm32-genericstm32h750vb){.reference .internal}     External   STM32H750VBT6   480MHz      128KB      1MB
:::

::: {#hy .section}
### HY[](#hy "Link to this heading"){.headerlink}

  Name                                                                                                                          Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Tiny STM103T]{.std .std-ref}](../boards/ststm32/hy_tinystm103tb.html#board-ststm32-hy-tinystm103tb){.reference .internal}   External   STM32F103TBU6   72MHz       128KB   20KB
:::

::: {#leaflabs .section}
### LeafLabs[](#leaflabs "Link to this heading"){.headerlink}

  Name                                                                                                                                     Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Maple]{.std .std-ref}](../boards/ststm32/maple.html#board-ststm32-maple){.reference .internal}                                         External   STM32F103RBT6   72MHz       108KB   17KB
  [[Maple (RET6)]{.std .std-ref}](../boards/ststm32/maple_ret6.html#board-ststm32-maple-ret6){.reference .internal}                        External   STM32F103RET6   72MHz       256KB   48KB
  [[Maple Mini Bootloader 2.0]{.std .std-ref}](../boards/ststm32/maple_mini_b20.html#board-ststm32-maple-mini-b20){.reference .internal}   External   STM32F103CBT6   72MHz       120KB   20KB
  [[Maple Mini Original]{.std .std-ref}](../boards/ststm32/maple_mini_origin.html#board-ststm32-maple-mini-origin){.reference .internal}   External   STM32F103CBT6   72MHz       108KB   20KB
:::

::: {#leafony-systems .section}
### Leafony Systems[](#leafony-systems "Link to this heading"){.headerlink}

  Name                                                                                                                            Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Leafony Systems AP03]{.std .std-ref}](../boards/ststm32/leafony_ap03.html#board-ststm32-leafony-ap03){.reference .internal}   On-board   STM32L452RET6   80MHz       512KB   160KB
:::

::: {#mxchip .section}
### MXChip[](#mxchip "Link to this heading"){.headerlink}

  Name                                                                                                                                                             Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Microsoft Azure IoT Development Kit (MXChip AZ3166)]{.std .std-ref}](../boards/ststm32/mxchip_az3166.html#board-ststm32-mxchip-az3166){.reference .internal}   On-board   STM32F412ZGT6   100MHz      1MB     256KB
:::

::: {#malyan .section}
### Malyan[](#malyan "Link to this heading"){.headerlink}

  Name                                                                                                                                Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ---------
  [[M200 V2]{.std .std-ref}](../boards/ststm32/malyanm200_f070cb.html#board-ststm32-malyanm200-f070cb){.reference .internal}          External   STM32F070CBT6   48MHz       120KB   14.81KB
  [[M300]{.std .std-ref}](../boards/ststm32/malyanm300_f070cb.html#board-ststm32-malyanm300-f070cb){.reference .internal}             External   STM32F070CBT6   48MHz       120KB   14.81KB
  [[Malyan M200 V1]{.std .std-ref}](../boards/ststm32/malyanm200_f103cb.html#board-ststm32-malyanm200-f103cb){.reference .internal}   External   STM32F103CBT6   72MHz       120KB   20KB
:::

::: {#microduino .section}
### Microduino[](#microduino "Link to this heading"){.headerlink}

  Name                                                                                                                                                  Debug      MCU             Frequency   Flash      RAM
  ----------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ---------- ------
  [[Microduino Core STM32 to Flash]{.std .std-ref}](../boards/ststm32/microduino32_flash.html#board-ststm32-microduino32-flash){.reference .internal}   External   STM32F103CBT6   72MHz       105.47KB   20KB
:::

::: {#midatronics .section}
### Midatronics[](#midatronics "Link to this heading"){.headerlink}

  Name                                                                                                              Debug      MCU           Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------- ---------- ------------- ----------- ------- -------
  [[MKR Sharky]{.std .std-ref}](../boards/ststm32/mkr_sharky.html#board-ststm32-mkr-sharky){.reference .internal}   External   STM32WB55CG   64MHz       512KB   192KB
:::

::: {#multitech .section}
### MultiTech[](#multitech "Link to this heading"){.headerlink}

  Name                                                                                                                                     Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[MTS Dragonfly]{.std .std-ref}](../boards/ststm32/mts_dragonfly_f411re.html#board-ststm32-mts-dragonfly-f411re){.reference .internal}   External   STM32F411RET6   100MHz      512KB   128KB
  [[MultiTech mDot]{.std .std-ref}](../boards/ststm32/mts_mdot_f405rg.html#board-ststm32-mts-mdot-f405rg){.reference .internal}            External   STM32F411RET6   100MHz      512KB   128KB
  [[MultiTech mDot F411]{.std .std-ref}](../boards/ststm32/mts_mdot_f411re.html#board-ststm32-mts-mdot-f411re){.reference .internal}       External   STM32F411RET6   100MHz      512KB   128KB
  [[MultiTech xDot]{.std .std-ref}](../boards/ststm32/xdot_l151cc.html#board-ststm32-xdot-l151cc){.reference .internal}                    External   STM32L151CCU6   32MHz       256KB   32KB
:::

::: {#netduino .section}
### Netduino[](#netduino "Link to this heading"){.headerlink}

  Name                                                                                                             Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[N2+]{.std .std-ref}](../boards/ststm32/netduino2plus.html#board-ststm32-netduino2plus){.reference .internal}   External   STM32F405RGT6   168MHz      1MB     128KB
:::

::: {#olimex .section}
### Olimex[](#olimex "Link to this heading"){.headerlink}

  Name                                                                                                                                          Debug      MCU             Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[OLIMEXINO-STM32]{.std .std-ref}](../boards/ststm32/olimexino.html#board-ststm32-olimexino){.reference .internal}                            External   STM32F103RBT6   72MHz       128KB   20KB
  [[Olimex OLIMEXINO-STM32F3]{.std .std-ref}](../boards/ststm32/olimexino_stm32f3.html#board-ststm32-olimexino-stm32f3){.reference .internal}   External   STM32F303RCT6   72MHz       256KB   40KB
  [[Olimex STM32-H103]{.std .std-ref}](../boards/ststm32/olimex_f103.html#board-ststm32-olimex-f103){.reference .internal}                      External   STM32F103RBT6   72MHz       128KB   20KB
  [[Olimex STM32-P405]{.std .std-ref}](../boards/ststm32/olimex_p405.html#board-ststm32-olimex-p405){.reference .internal}                      External   STM32F405RGT6   168MHz      1MB     128KB
  [[STM32-E407]{.std .std-ref}](../boards/ststm32/olimex_e407.html#board-ststm32-olimex-e407){.reference .internal}                             External   STM32F407ZGT6   168MHz      1MB     128KB
  [[STM32-H407]{.std .std-ref}](../boards/ststm32/olimex_h407.html#board-ststm32-olimex-h407){.reference .internal}                             External   STM32F407ZGT6   168MHz      1MB     128KB
:::

::: {#pybstick .section}
### PYBStick[](#pybstick "Link to this heading"){.headerlink}

  Name                                                                                                                                Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[PYBSTICK26 Duino]{.std .std-ref}](../boards/ststm32/pybstick26_duino.html#board-ststm32-pybstick26-duino){.reference .internal}   External   STM32F072RB     48MHz       128KB   16KB
  [[PYBStick 26 Pro]{.std .std-ref}](../boards/ststm32/pybstick26_pro.html#board-ststm32-pybstick26-pro){.reference .internal}        External   STM32F412RE     100MHz      512KB   256KB
  [[PYBStick Lite 26]{.std .std-ref}](../boards/ststm32/pybstick26_lite.html#board-ststm32-pybstick26-lite){.reference .internal}     External   STM32F401CEU6   84MHz       512KB   96KB
  [[PYBStick Standard 26]{.std .std-ref}](../boards/ststm32/pybstick26_std.html#board-ststm32-pybstick26-std){.reference .internal}   External   STM32F411CEU6   100MHz      512KB   128KB
:::

::: {#piconomix .section}
### Piconomix[](#piconomix "Link to this heading"){.headerlink}

  Name                                                                                                                                   Debug      MCU           Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------- ---------- ------------- ----------- ------- ------
  [[Piconomix PX-HER0]{.std .std-ref}](../boards/ststm32/piconomix_px_her0.html#board-ststm32-piconomix-px-her0){.reference .internal}   External   STM32L072RB   32MHz       128KB   20KB
:::

::: {#prntrboard .section}
### PrntrBoard[](#prntrboard "Link to this heading"){.headerlink}

  Name                                                                                                             Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[PrntrBoard V2]{.std .std-ref}](../boards/ststm32/prntr_v2.html#board-ststm32-prntr-v2){.reference .internal}   External   STM32F407VET6   168MHz      512KB   128KB
:::

::: {#rak .section}
### RAK[](#rak "Link to this heading"){.headerlink}

  Name                                                                                                                                     Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[RAK811 LoRa Tracker]{.std .std-ref}](../boards/ststm32/rak811_tracker.html#board-ststm32-rak811-tracker){.reference .internal}         External   STM32L151RBT6   32MHz       128KB   16KB
  [[RAK811 LoRa Tracker]{.std .std-ref}](../boards/ststm32/rak811_tracker_32.html#board-ststm32-rak811-tracker-32){.reference .internal}   External   STM32L151RBT6   32MHz       128KB   32KB
:::

::: {#rumba .section}
### RUMBA[](#rumba "Link to this heading"){.headerlink}

  Name                                                                                                                                    Debug      MCU             Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[3D Printer control board]{.std .std-ref}](../boards/ststm32/rumba32_f446ve.html#board-ststm32-rumba32-f446ve){.reference .internal}   External   STM32F446RET6   180MHz      512KB   128KB
:::

::: {#rymcu .section}
### RYMCU[](#rymcu "Link to this heading"){.headerlink}

  Name                                                                                                                                                                      Debug      MCU             Frequency   Flash      RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ---------- -------
  [[RYMCU Nebula Pi F103VE (64k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/rymcu_nebulapi_f103ve.html#board-ststm32-rymcu-nebulapi-f103ve){.reference .internal}   External   STM32F103VET6   72MHz       512KB      64KB
  [[RYMCU STM32F407VE (192k RAM. 512k Flash)]{.std .std-ref}](../boards/ststm32/rymcu_f407ve.html#board-ststm32-rymcu-f407ve){.reference .internal}                         External   STM32F407VET6   168MHz      502.23KB   128KB
:::

::: {#remram .section}
### RemRam[](#remram "Link to this heading"){.headerlink}

  Name                                                                                                                       Debug      MCU             Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[3D printer controller]{.std .std-ref}](../boards/ststm32/remram_v1.html#board-ststm32-remram-v1){.reference .internal}   On-board   STM32F765VIT6   216MHz      2MB     512KB
:::

::: {#robotdyn .section}
### RobotDyn[](#robotdyn "Link to this heading"){.headerlink}

  Name                                                                                                                                                  Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[BlackPill F303CC]{.std .std-ref}](../boards/ststm32/robotdyn_blackpill_f303cc.html#board-ststm32-robotdyn-blackpill-f303cc){.reference .internal}   External   STM32F303CCT6   72MHz       256KB   40KB
:::

::: {#rushup .section}
### RushUp[](#rushup "Link to this heading"){.headerlink}

  Name                                                                                                                           Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------ ---------- --------------- ----------- ------- -------
  [[RushUp Cloud-JAM]{.std .std-ref}](../boards/ststm32/cloud_jam.html#board-ststm32-cloud-jam){.reference .internal}            On-board   STM32F401RET6   84MHz       512KB   96KB
  [[RushUp Cloud-JAM L4]{.std .std-ref}](../boards/ststm32/cloud_jam_l4.html#board-ststm32-cloud-jam-l4){.reference .internal}   On-board   STM32L476RGT6   80MHz       1MB     128KB
:::

::: {#st .section}
### ST[](#st "Link to this heading"){.headerlink}

  Name                                                                                                                                                                     Debug      MCU              Frequency   Flash    RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------- ---------------- ----------- -------- -------
  [[32F412GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f412zg.html#board-ststm32-disco-f412zg){.reference .internal}                                                On-board   STM32F412ZGT6    100MHz      1MB      256KB
  [[32F723EDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f723ie.html#board-ststm32-disco-f723ie){.reference .internal}                                                On-board   STM32F723IEK6    216MHz      512KB    192KB
  [[3DP001V1 Evaluation board for 3D printer]{.std .std-ref}](../boards/ststm32/st3dp001_eval.html#board-ststm32-st3dp001-eval){.reference .internal}                      On-board   STM32F401VET6    84MHz       512KB    96KB
  [[Black STM32F407VE]{.std .std-ref}](../boards/ststm32/black_f407ve.html#board-ststm32-black-f407ve){.reference .internal}                                               External   STM32F407VET6    168MHz      512KB    128KB
  [[Black STM32F407VG]{.std .std-ref}](../boards/ststm32/black_f407vg.html#board-ststm32-black-f407vg){.reference .internal}                                               External   STM32F407VGT6    168MHz      512KB    128KB
  [[Black STM32F407ZE]{.std .std-ref}](../boards/ststm32/black_f407ze.html#board-ststm32-black-f407ze){.reference .internal}                                               External   STM32F407ZET6    168MHz      512KB    128KB
  [[Black STM32F407ZG]{.std .std-ref}](../boards/ststm32/black_f407zg.html#board-ststm32-black-f407zg){.reference .internal}                                               External   STM32F407ZGT6    168MHz      1MB      128KB
  [[Blue STM32F407VE Mini]{.std .std-ref}](../boards/ststm32/blue_f407ve_mini.html#board-ststm32-blue-f407ve-mini){.reference .internal}                                   External   STM32F407VET6    168MHz      512KB    128KB
  [[Core board F401RCT6]{.std .std-ref}](../boards/ststm32/coreboard_f401rc.html#board-ststm32-coreboard-f401rc){.reference .internal}                                     External   STM32F401RCT6    84MHz       256KB    64KB
  [[Nucleo G070RB]{.std .std-ref}](../boards/ststm32/nucleo_g070rb.html#board-ststm32-nucleo-g070rb){.reference .internal}                                                 On-board   STM32G070RBT6    64MHz       128KB    36KB
  [[Nucleo G071RB]{.std .std-ref}](../boards/ststm32/nucleo_g071rb.html#board-ststm32-nucleo-g071rb){.reference .internal}                                                 On-board   STM32G071RBT6    64MHz       128KB    36KB
  [[Nucleo G431KB]{.std .std-ref}](../boards/ststm32/nucleo_g431kb.html#board-ststm32-nucleo-g431kb){.reference .internal}                                                 On-board   STM32G431KBT6    170MHz      128KB    32KB
  [[Nucleo G431RB]{.std .std-ref}](../boards/ststm32/nucleo_g431rb.html#board-ststm32-nucleo-g431rb){.reference .internal}                                                 On-board   STM32G431RBT6    170MHz      128KB    32KB
  [[Nucleo G474RE]{.std .std-ref}](../boards/ststm32/nucleo_g474re.html#board-ststm32-nucleo-g474re){.reference .internal}                                                 On-board   STM32G474RET6    170MHz      512KB    128KB
  [[P-Nucleo WB55RG]{.std .std-ref}](../boards/ststm32/nucleo_wb55rg_p.html#board-ststm32-nucleo-wb55rg-p){.reference .internal}                                           On-board   STM32WB55RG      64MHz       512KB    192KB
  [[RHF76 052]{.std .std-ref}](../boards/ststm32/rhf76_052.html#board-ststm32-rhf76-052){.reference .internal}                                                             External   STM32L051C8T6    32MHz       64KB     8KB
  [[ST 32F3348DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f334c8.html#board-ststm32-disco-f334c8){.reference .internal}                                             On-board   STM32F334C8T6    72MHz       64KB     12KB
  [[ST 32F401CDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f401vc.html#board-ststm32-disco-f401vc){.reference .internal}                                             On-board   STM32F401VCT6    84MHz       256KB    64KB
  [[ST 32F411EDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f411ve.html#board-ststm32-disco-f411ve){.reference .internal}                                             On-board   STM32F411VET6    100MHz      512KB    128KB
  [[ST 32F413HDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f413zh.html#board-ststm32-disco-f413zh){.reference .internal}                                             On-board   STM32F413ZHT6    100MHz      1.50MB   320KB
  [[ST 32F429IDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f429zi.html#board-ststm32-disco-f429zi){.reference .internal}                                             On-board   STM32F429ZIT6    180MHz      2MB      256KB
  [[ST 32F469IDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f469ni.html#board-ststm32-disco-f469ni){.reference .internal}                                             On-board   STM32F469NIH6    180MHz      2MB      384KB
  [[ST 32F746GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f746ng.html#board-ststm32-disco-f746ng){.reference .internal}                                             On-board   STM32F746NGH6    216MHz      1MB      320KB
  [[ST 32F769IDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f769ni.html#board-ststm32-disco-f769ni){.reference .internal}                                             On-board   STM32F769NIH6    216MHz      2MB      512KB
  [[ST 32L0538DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l053c8.html#board-ststm32-disco-l053c8){.reference .internal}                                             On-board   STM32L053C8T6    32MHz       64KB     8KB
  [[ST 32L100DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l100rc.html#board-ststm32-disco-l100rc){.reference .internal}                                              On-board   STM32L100RCT6    32MHz       256KB    16KB
  [[ST 32L476GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l476vg.html#board-ststm32-disco-l476vg){.reference .internal}                                             On-board   STM32L476VGT6    80MHz       1MB      128KB
  [[ST 32L496GDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l496ag.html#board-ststm32-disco-l496ag){.reference .internal}                                             On-board   STM32L496AGI6    80MHz       1MB      320KB
  [[ST B-G431B-ESC1 Discovery]{.std .std-ref}](../boards/ststm32/disco_b_g431b_esc1.html#board-ststm32-disco-b-g431b-esc1){.reference .internal}                           On-board   STM32G431CBU6    170MHz      128KB    32KB
  [[ST B-L475E-IOT01A Discovery kit]{.std .std-ref}](../boards/ststm32/disco_l475vg_iot01a.html#board-ststm32-disco-l475vg-iot01a){.reference .internal}                   On-board   STM32L475VGT6    80MHz       1MB      96KB
  [[ST B-U585I-IOT02A Discovery]{.std .std-ref}](../boards/ststm32/disco_b_u585i_iot02a.html#board-ststm32-disco-b-u585i-iot02a){.reference .internal}                     On-board   STM32U585AII6Q   160MHz      2MB      256KB
  [[ST DISCO-L072CZ-LRWAN1]{.std .std-ref}](../boards/ststm32/disco_l072cz_lrwan1.html#board-ststm32-disco-l072cz-lrwan1){.reference .internal}                            On-board   STM32L072CZ      32MHz       192KB    20KB
  [[ST Discovery F072RB]{.std .std-ref}](../boards/ststm32/disco_f072rb.html#board-ststm32-disco-f072rb){.reference .internal}                                             On-board   STM32F072RBT6    48MHz       128KB    16KB
  [[ST NUCLEO-G031K8]{.std .std-ref}](../boards/ststm32/nucleo_g031k8.html#board-ststm32-nucleo-g031k8){.reference .internal}                                              On-board   STM32G031K8      64MHz       64KB     8KB
  [[ST Nucleo F030R8]{.std .std-ref}](../boards/ststm32/nucleo_f030r8.html#board-ststm32-nucleo-f030r8){.reference .internal}                                              On-board   STM32F030R8T6    48MHz       64KB     8KB
  [[ST Nucleo F031K6]{.std .std-ref}](../boards/ststm32/nucleo_f031k6.html#board-ststm32-nucleo-f031k6){.reference .internal}                                              On-board   STM32F031K6T6    48MHz       32KB     4KB
  [[ST Nucleo F042K6]{.std .std-ref}](../boards/ststm32/nucleo_f042k6.html#board-ststm32-nucleo-f042k6){.reference .internal}                                              On-board   STM32F042K6T6    48MHz       32KB     6KB
  [[ST Nucleo F070RB]{.std .std-ref}](../boards/ststm32/nucleo_f070rb.html#board-ststm32-nucleo-f070rb){.reference .internal}                                              On-board   STM32F070RBT6    48MHz       128KB    16KB
  [[ST Nucleo F072RB]{.std .std-ref}](../boards/ststm32/nucleo_f072rb.html#board-ststm32-nucleo-f072rb){.reference .internal}                                              On-board   STM32F072RBT6    48MHz       128KB    16KB
  [[ST Nucleo F091RC]{.std .std-ref}](../boards/ststm32/nucleo_f091rc.html#board-ststm32-nucleo-f091rc){.reference .internal}                                              On-board   STM32F091RCT6    48MHz       256KB    32KB
  [[ST Nucleo F103RB]{.std .std-ref}](../boards/ststm32/nucleo_f103rb.html#board-ststm32-nucleo-f103rb){.reference .internal}                                              On-board   STM32F103RBT6    72MHz       128KB    20KB
  [[ST Nucleo F207ZG]{.std .std-ref}](../boards/ststm32/nucleo_f207zg.html#board-ststm32-nucleo-f207zg){.reference .internal}                                              On-board   STM32F207ZGT6    120MHz      1MB      128KB
  [[ST Nucleo F302R8]{.std .std-ref}](../boards/ststm32/nucleo_f302r8.html#board-ststm32-nucleo-f302r8){.reference .internal}                                              On-board   STM32F302R8T6    72MHz       64KB     16KB
  [[ST Nucleo F303K8]{.std .std-ref}](../boards/ststm32/nucleo_f303k8.html#board-ststm32-nucleo-f303k8){.reference .internal}                                              On-board   STM32F303K8T6    72MHz       64KB     12KB
  [[ST Nucleo F303RE]{.std .std-ref}](../boards/ststm32/nucleo_f303re.html#board-ststm32-nucleo-f303re){.reference .internal}                                              On-board   STM32F303RET6    72MHz       512KB    64KB
  [[ST Nucleo F303ZE]{.std .std-ref}](../boards/ststm32/nucleo_f303ze.html#board-ststm32-nucleo-f303ze){.reference .internal}                                              On-board   STM32F303ZET6    72MHz       512KB    64KB
  [[ST Nucleo F334R8]{.std .std-ref}](../boards/ststm32/nucleo_f334r8.html#board-ststm32-nucleo-f334r8){.reference .internal}                                              On-board   STM32F334R8T6    72MHz       64KB     16KB
  [[ST Nucleo F401RE]{.std .std-ref}](../boards/ststm32/nucleo_f401re.html#board-ststm32-nucleo-f401re){.reference .internal}                                              On-board   STM32F401RET6    84MHz       512KB    96KB
  [[ST Nucleo F410RB]{.std .std-ref}](../boards/ststm32/nucleo_f410rb.html#board-ststm32-nucleo-f410rb){.reference .internal}                                              On-board   STM32F410RBT6    100MHz      128KB    32KB
  [[ST Nucleo F411RE]{.std .std-ref}](../boards/ststm32/nucleo_f411re.html#board-ststm32-nucleo-f411re){.reference .internal}                                              On-board   STM32F411RET6    100MHz      512KB    128KB
  [[ST Nucleo F412ZG]{.std .std-ref}](../boards/ststm32/nucleo_f412zg.html#board-ststm32-nucleo-f412zg){.reference .internal}                                              On-board   STM32F412ZGT6    100MHz      1MB      256KB
  [[ST Nucleo F413ZH]{.std .std-ref}](../boards/ststm32/nucleo_f413zh.html#board-ststm32-nucleo-f413zh){.reference .internal}                                              On-board   STM32F413ZHT6    100MHz      1.50MB   320KB
  [[ST Nucleo F429ZI]{.std .std-ref}](../boards/ststm32/nucleo_f429zi.html#board-ststm32-nucleo-f429zi){.reference .internal}                                              On-board   STM32F429ZIT6    180MHz      2MB      192KB
  [[ST Nucleo F439ZI]{.std .std-ref}](../boards/ststm32/nucleo_f439zi.html#board-ststm32-nucleo-f439zi){.reference .internal}                                              On-board   STM32F439ZIT6    180MHz      2MB      192KB
  [[ST Nucleo F446RE]{.std .std-ref}](../boards/ststm32/nucleo_f446re.html#board-ststm32-nucleo-f446re){.reference .internal}                                              On-board   STM32F446RET6    180MHz      512KB    128KB
  [[ST Nucleo F446ZE]{.std .std-ref}](../boards/ststm32/nucleo_f446ze.html#board-ststm32-nucleo-f446ze){.reference .internal}                                              On-board   STM32F446ZET6    180MHz      512KB    128KB
  [[ST Nucleo F722ZE]{.std .std-ref}](../boards/ststm32/nucleo_f722ze.html#board-ststm32-nucleo-f722ze){.reference .internal}                                              On-board   STM32F722ZET6    216MHz      512KB    256KB
  [[ST Nucleo F746ZG]{.std .std-ref}](../boards/ststm32/nucleo_f746zg.html#board-ststm32-nucleo-f746zg){.reference .internal}                                              On-board   STM32F746ZGT6    216MHz      1MB      320KB
  [[ST Nucleo F756ZG]{.std .std-ref}](../boards/ststm32/nucleo_f756zg.html#board-ststm32-nucleo-f756zg){.reference .internal}                                              On-board   STM32F756ZG      216MHz      1MB      320KB
  [[ST Nucleo F767ZI]{.std .std-ref}](../boards/ststm32/nucleo_f767zi.html#board-ststm32-nucleo-f767zi){.reference .internal}                                              On-board   STM32F767ZIT6    216MHz      2MB      512KB
  [[ST Nucleo G0B1RE]{.std .std-ref}](../boards/ststm32/nucleo_g0b1re.html#board-ststm32-nucleo-g0b1re){.reference .internal}                                              On-board   STM32G0B1RET6    64MHz       512KB    144KB
  [[ST Nucleo H723ZG]{.std .std-ref}](../boards/ststm32/nucleo_h723zg.html#board-ststm32-nucleo-h723zg){.reference .internal}                                              On-board   STM32H723ZGT6    550MHz      1MB      320KB
  [[ST Nucleo H743ZI]{.std .std-ref}](../boards/ststm32/nucleo_h743zi.html#board-ststm32-nucleo-h743zi){.reference .internal}                                              On-board   STM32H743ZIT6    400MHz      2MB      512KB
  [[ST Nucleo H745ZI-Q]{.std .std-ref}](../boards/ststm32/nucleo_h745zi_q.html#board-ststm32-nucleo-h745zi-q){.reference .internal}                                        On-board   STM32H745ZIT6    480MHz      1MB      512KB
  [[ST Nucleo H753ZI]{.std .std-ref}](../boards/ststm32/nucleo_h753zi.html#board-ststm32-nucleo-h753zi){.reference .internal}                                              On-board   STM32H753ZIT6    400MHz      2MB      512KB
  [[ST Nucleo L010RB]{.std .std-ref}](../boards/ststm32/nucleo_l010rb.html#board-ststm32-nucleo-l010rb){.reference .internal}                                              On-board   STM32L010RBT6    32MHz       128KB    20KB
  [[ST Nucleo L011K4]{.std .std-ref}](../boards/ststm32/nucleo_l011k4.html#board-ststm32-nucleo-l011k4){.reference .internal}                                              On-board   STM32L011K4T6    32MHz       16KB     2KB
  [[ST Nucleo L031K6]{.std .std-ref}](../boards/ststm32/nucleo_l031k6.html#board-ststm32-nucleo-l031k6){.reference .internal}                                              On-board   STM32L031K6T6    32MHz       32KB     8KB
  [[ST Nucleo L053R8]{.std .std-ref}](../boards/ststm32/nucleo_l053r8.html#board-ststm32-nucleo-l053r8){.reference .internal}                                              On-board   STM32L053R8T6    32MHz       64KB     8KB
  [[ST Nucleo L073RZ]{.std .std-ref}](../boards/ststm32/nucleo_l073rz.html#board-ststm32-nucleo-l073rz){.reference .internal}                                              On-board   STM32L073RZ      32MHz       192KB    20KB
  [[ST Nucleo L152RE]{.std .std-ref}](../boards/ststm32/nucleo_l152re.html#board-ststm32-nucleo-l152re){.reference .internal}                                              On-board   STM32L152RET6    32MHz       512KB    80KB
  [[ST Nucleo L412KB]{.std .std-ref}](../boards/ststm32/nucleo_l412kb.html#board-ststm32-nucleo-l412kb){.reference .internal}                                              On-board   STM32L412KBU6    80MHz       128KB    40KB
  [[ST Nucleo L412RB-P]{.std .std-ref}](../boards/ststm32/nucleo_l412rb_p.html#board-ststm32-nucleo-l412rb-p){.reference .internal}                                        On-board   STM32L412RBT6P   80MHz       128KB    40KB
  [[ST Nucleo L432KC]{.std .std-ref}](../boards/ststm32/nucleo_l432kc.html#board-ststm32-nucleo-l432kc){.reference .internal}                                              On-board   STM32L432KCU6    80MHz       256KB    64KB
  [[ST Nucleo L433RC-P]{.std .std-ref}](../boards/ststm32/nucleo_l433rc_p.html#board-ststm32-nucleo-l433rc-p){.reference .internal}                                        On-board   STM32L433RC      80MHz       256KB    64KB
  [[ST Nucleo L452RE]{.std .std-ref}](../boards/ststm32/nucleo_l452re.html#board-ststm32-nucleo-l452re){.reference .internal}                                              On-board   STM32L452RET6    80MHz       512KB    160KB
  [[ST Nucleo L476RG]{.std .std-ref}](../boards/ststm32/nucleo_l476rg.html#board-ststm32-nucleo-l476rg){.reference .internal}                                              On-board   STM32L476RGT6    80MHz       1MB      96KB
  [[ST Nucleo L486RG]{.std .std-ref}](../boards/ststm32/nucleo_l486rg.html#board-ststm32-nucleo-l486rg){.reference .internal}                                              On-board   STM32L486RGT6    80MHz       1MB      128KB
  [[ST Nucleo L496ZG]{.std .std-ref}](../boards/ststm32/nucleo_l496zg.html#board-ststm32-nucleo-l496zg){.reference .internal}                                              On-board   STM32L496ZGT6    80MHz       1MB      320KB
  [[ST Nucleo L496ZG-P]{.std .std-ref}](../boards/ststm32/nucleo_l496zg_p.html#board-ststm32-nucleo-l496zg-p){.reference .internal}                                        On-board   STM32L496ZGT6P   80MHz       1MB      320KB
  [[ST Nucleo L4R5ZI]{.std .std-ref}](../boards/ststm32/nucleo_l4r5zi.html#board-ststm32-nucleo-l4r5zi){.reference .internal}                                              On-board   STM32L4R5ZIT6    120MHz      2MB      640KB
  [[ST Nucleo L552ZE-Q]{.std .std-ref}](../boards/ststm32/nucleo_l552ze_q.html#board-ststm32-nucleo-l552ze-q){.reference .internal}                                        On-board   STM32L552ZET6    80MHz       512KB    192KB
  [[ST Nucleo U575ZI-Q]{.std .std-ref}](../boards/ststm32/nucleo_u575zi_q.html#board-ststm32-nucleo-u575zi-q){.reference .internal}                                        On-board   STM32U575ZIT6Q   160MHz      2MB      256KB
  [[ST Nucleo WL55JC]{.std .std-ref}](../boards/ststm32/nucleo_wl55jc.html#board-ststm32-nucleo-wl55jc){.reference .internal}                                              On-board   STM32WL55JC      48MHz       256KB    64KB
  [[ST STM32F0308DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f030r8.html#board-ststm32-disco-f030r8){.reference .internal}                                          On-board   STM32F030R8T6    48MHz       64KB     8KB
  [[ST STM32F0DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f051r8.html#board-ststm32-disco-f051r8){.reference .internal}                                             On-board   STM32F051R8T6    48MHz       64KB     8KB
  [[ST STM32F3DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f303vc.html#board-ststm32-disco-f303vc){.reference .internal}                                             On-board   STM32F303VCT6    72MHz       256KB    40KB
  [[ST STM32F4DISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f407vg.html#board-ststm32-disco-f407vg){.reference .internal}                                             On-board   STM32F407VGT6    168MHz      1MB      128KB
  [[ST STM32G0316-DISCO]{.std .std-ref}](../boards/ststm32/disco_g031j6.html#board-ststm32-disco-g031j6){.reference .internal}                                             External   STM32G031J6      64MHz       32KB     8KB
  [[ST STM32G071B Discovery]{.std .std-ref}](../boards/ststm32/disco_g071rb.html#board-ststm32-disco-g071rb){.reference .internal}                                         On-board   STM32G071RBT6    64MHz       128KB    36KB
  [[ST STM32L073Z-EVAL]{.std .std-ref}](../boards/ststm32/eval_l073z.html#board-ststm32-eval-l073z){.reference .internal}                                                  On-board   STM32L073VZT6    32MHz       192KB    20KB
  [[ST STM32L4+ Discovery kit IoT node]{.std .std-ref}](../boards/ststm32/disco_l4s5i_iot01a.html#board-ststm32-disco-l4s5i-iot01a){.reference .internal}                  On-board   STM32L4S5VIT6    80MHz       2MB      640KB
  [[ST STM32LDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_l152rb.html#board-ststm32-disco-l152rb){.reference .internal}                                              On-board   STM32L152RBT6    32MHz       128KB    16KB
  [[ST STM32VLDISCOVERY]{.std .std-ref}](../boards/ststm32/disco_f100rb.html#board-ststm32-disco-f100rb){.reference .internal}                                             On-board   STM32F100RBT6    24MHz       128KB    8KB
  [[STEVAL-FCU001V1 Flight controller unit evaluation board]{.std .std-ref}](../boards/ststm32/steval_fcu001v1.html#board-ststm32-steval-fcu001v1){.reference .internal}   External   STM32F401CCU6    84MHz       256KB    64KB
  [[STM3210C-EVAL]{.std .std-ref}](../boards/ststm32/eval_f107vc.html#board-ststm32-eval-f107vc){.reference .internal}                                                     External   STM32F107VCT6    72MHz       256KB    64KB
  [[STM32373C-EVAL]{.std .std-ref}](../boards/ststm32/eval_f373vc.html#board-ststm32-eval-f373vc){.reference .internal}                                                    External   STM32F373VCT6    72MHz       256KB    32KB
  [[STM32F072-EVAL]{.std .std-ref}](../boards/ststm32/eval_f072vb.html#board-ststm32-eval-f072vb){.reference .internal}                                                    External   STM32F072VBT6    48MHz       128KB    16KB
  [[STM32F7508-DK]{.std .std-ref}](../boards/ststm32/disco_f750n8.html#board-ststm32-disco-f750n8){.reference .internal}                                                   On-board   STM32F750N8H6    216MHz      64KB     340KB
  [[STM32G431CB (32k RAM. 128k Flash)]{.std .std-ref}](../boards/ststm32/genericSTM32G431CB.html#board-ststm32-genericstm32g431cb){.reference .internal}                   External   STM32G431CBU6    170MHz      128KB    32KB
  [[STM32H735G-DK Discovery kit]{.std .std-ref}](../boards/ststm32/disco_h735ig.html#board-ststm32-disco-h735ig){.reference .internal}                                     On-board   STM32H735IGK6    550MHz      1MB      432KB
  [[STM32H747I-DISCO]{.std .std-ref}](../boards/ststm32/disco_h747xi.html#board-ststm32-disco-h747xi){.reference .internal}                                                On-board   STM32H747XIH6    400MHz      2MB      512KB
  [[SensorTile.box]{.std .std-ref}](../boards/ststm32/steval_mksboxv1.html#board-ststm32-steval-mksboxv1){.reference .internal}                                            External   STM32L4R9ZI      120MHz      2MB      640KB
:::

::: {#storm32 .section}
### STorM32[](#storm32 "Link to this heading"){.headerlink}

  Name                                                                                                                                    Debug      MCU             Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[STorM32 BGC v1.31 RC]{.std .std-ref}](../boards/ststm32/storm32_v1_31_rc.html#board-ststm32-storm32-v1-31-rc){.reference .internal}   External   STM32F103RCT6   72MHz       256KB   48KB
:::

::: {#seeedstudio .section}
### SeeedStudio[](#seeedstudio "Link to this heading"){.headerlink}

  Name                                                                                                                                               Debug      MCU             Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Seeed Arch Max]{.std .std-ref}](../boards/ststm32/seeedArchMax.html#board-ststm32-seeedarchmax){.reference .internal}                            On-board   STM32F407VET6   168MHz      512KB   192KB
  [[Seeed Wio 3G]{.std .std-ref}](../boards/ststm32/wio_3g.html#board-ststm32-wio-3g){.reference .internal}                                          On-board   STM32F439VI     180MHz      2MB     256KB
  [[SeeedStudio LoRa E5 Dev Board]{.std .std-ref}](../boards/ststm32/lora_e5_dev_board.html#board-ststm32-lora-e5-dev-board){.reference .internal}   External   STM32WLE5JC     48MHz       256KB   64KB
  [[SeeedStudio LoRa-E5 mini]{.std .std-ref}](../boards/ststm32/lora_e5_mini.html#board-ststm32-lora-e5-mini){.reference .internal}                  External   STM32WLE5JC     48MHz       256KB   64KB
:::

::: {#semtech .section}
### Semtech[](#semtech "Link to this heading"){.headerlink}

  Name                                                                                                              Debug      MCU           Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------- ---------- ------------- ----------- ------- ------
  [[NAMote72]{.std .std-ref}](../boards/ststm32/mote_l152rc.html#board-ststm32-mote-l152rc){.reference .internal}   External   STM32L152RC   32MHz       256KB   32KB
:::

::: {#sigma-ic .section}
### Sigma IC[](#sigma-ic "Link to this heading"){.headerlink}

  Name                                                                                                                       Debug      MCU             Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Sigma IC AGAFIA SG0]{.std .std-ref}](../boards/ststm32/agafia_sg0.html#board-ststm32-agafia-sg0){.reference .internal}   External   STM32G071RBT6   64MHz       128KB   36KB
:::

::: {#sparkfun .section}
### SparkFun[](#sparkfun "Link to this heading"){.headerlink}

  Name                                                                                                                                                       Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[SparkFun MicroMod STM32F405]{.std .std-ref}](../boards/ststm32/sparkfun_micromod_f405.html#board-ststm32-sparkfun-micromod-f405){.reference .internal}   External   STM32F405RGT6   168MHz      1MB     128KB
:::

::: {#taulabs .section}
### TauLabs[](#taulabs "Link to this heading"){.headerlink}

  Name                                                                                                                Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Sparky V1 F303]{.std .std-ref}](../boards/ststm32/sparky_v1.html#board-ststm32-sparky-v1){.reference .internal}   External   STM32F303CCT6   72MHz       256KB   40KB
:::

::: {#thunderpack .section}
### ThunderPack[](#thunderpack "Link to this heading"){.headerlink}

  Name                                                                                                                                   Debug      MCU             Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[ThunderPack v1.0]{.std .std-ref}](../boards/ststm32/thunder_pack.html#board-ststm32-thunder-pack){.reference .internal}              External   STM32L072KZ     32MHz       192KB   20KB
  [[ThunderPack v1.1+]{.std .std-ref}](../boards/ststm32/thunder_pack_f411.html#board-ststm32-thunder-pack-f411){.reference .internal}   External   STM32F411CEU6   100MHz      512KB   128KB
:::

::: {#tlera-corporation .section}
### Tlera Corporation[](#tlera-corporation "Link to this heading"){.headerlink}

  Name                                                                                                                                      Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Cicada-L082CZ]{.std .std-ref}](../boards/ststm32/cicada_l082cz.html#board-ststm32-cicada-l082cz){.reference .internal}                  External   STM32L082CZY6   32MHz       192KB   20KB
  [[Cricket-L082CZ]{.std .std-ref}](../boards/ststm32/cricket_l082cz.html#board-ststm32-cricket-l082cz){.reference .internal}               External   STM32L082CZY6   32MHz       192KB   20KB
  [[Gnat-L082CZ]{.std .std-ref}](../boards/ststm32/gnat_l082cz.html#board-ststm32-gnat-l082cz){.reference .internal}                        External   STM32L082CZY6   32MHz       192KB   20KB
  [[Grasshopper-L082CZ]{.std .std-ref}](../boards/ststm32/grasshopper_l082cz.html#board-ststm32-grasshopper-l082cz){.reference .internal}   External   STM32L082CZY6   32MHz       192KB   20KB
:::

::: {#vae .section}
### VAE[](#vae "Link to this heading"){.headerlink}

  Name                                                                                                       Debug      MCU             Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[VAkE v1.0]{.std .std-ref}](../boards/ststm32/vake_v1.html#board-ststm32-vake-v1){.reference .internal}   External   STM32F446RET6   180MHz      512KB   128KB
:::

::: {#vccgnd .section}
### VCCGND[](#vccgnd "Link to this heading"){.headerlink}

  Name                                                                                                                                        Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[VCCGND F103ZET6 Mini]{.std .std-ref}](../boards/ststm32/vccgnd_f103zet6.html#board-ststm32-vccgnd-f103zet6){.reference .internal}         External   STM32F103ZET6   72MHz       512KB   64KB
  [[VCCGND F407ZGT6 Mini]{.std .std-ref}](../boards/ststm32/vccgnd_f407zg_mini.html#board-ststm32-vccgnd-f407zg-mini){.reference .internal}   External   STM32F407ZGT6   168MHz      1MB     128KB
:::

::: {#waveshare .section}
### Waveshare[](#waveshare "Link to this heading"){.headerlink}

  Name                                                                                                                                      Debug      MCU             Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- ------
  [[Waveshare Open103Z]{.std .std-ref}](../boards/ststm32/waveshare_open103z.html#board-ststm32-waveshare-open103z){.reference .internal}   External   STM32F103ZET6   72MHz       512KB   64KB
:::

::: {#weact-studio .section}
### WeAct Studio[](#weact-studio "Link to this heading"){.headerlink}

  Name                                                                                                                                                         Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------- --------------- ----------- ------- -------
  [[WeAct Studio BlackPill V2.0 (STM32F401CC)]{.std .std-ref}](../boards/ststm32/blackpill_f401cc.html#board-ststm32-blackpill-f401cc){.reference .internal}   External   STM32F401CCU6   84MHz       256KB   64KB
  [[WeAct Studio BlackPill V2.0 (STM32F411CE)]{.std .std-ref}](../boards/ststm32/blackpill_f411ce.html#board-ststm32-blackpill-f411ce){.reference .internal}   External   STM32F411CEU6   100MHz      512KB   128KB
  [[WeAct Studio BlackPill V3.0 (STM32F401CE)]{.std .std-ref}](../boards/ststm32/blackpill_f401ce.html#board-ststm32-blackpill-f401ce){.reference .internal}   External   STM32F401CEU6   84MHz       512KB   96KB
  [[WeAct Studio MiniSTM32H743VITX]{.std .std-ref}](../boards/ststm32/weact_mini_h743vitx.html#board-ststm32-weact-mini-h743vitx){.reference .internal}        External   STM32H743VIT6   480MHz      2MB     512KB
  [[WeAct Studio MiniSTM32H750VBTX]{.std .std-ref}](../boards/ststm32/weact_mini_h750vbtx.html#board-ststm32-weact-mini-h750vbtx){.reference .internal}        External   STM32H750VBT6   480MHz      512KB   128KB
:::

::: {#rhomb-io .section}
### rhomb.io[](#rhomb-io "Link to this heading"){.headerlink}

  Name                                                                                                                           Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------ ---------- --------------- ----------- ------- -------
  [[L476DMW1K]{.std .std-ref}](../boards/ststm32/rhombio_l476dmw1k.html#board-ststm32-rhombio-l476dmw1k){.reference .internal}   On-board   STM32L476VGT6   80MHz       1MB     128KB
:::

::: {#sakura-io .section}
### sakura.io[](#sakura-io "Link to this heading"){.headerlink}

  Name                                                                                                                                        Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[sakura.io Evaluation Board]{.std .std-ref}](../boards/ststm32/sakuraio_evb_01.html#board-ststm32-sakuraio-evb-01){.reference .internal}   On-board   STM32F411RET6   100MHz      1MB     128KB
:::

::: {#u-blox .section}
### u-blox[](#u-blox "Link to this heading"){.headerlink}

  Name                                                                                                                                              Debug      MCU             Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------- ---------- --------------- ----------- ------- -------
  [[Mbed Connect Cloud]{.std .std-ref}](../boards/ststm32/mbed_connect_odin.html#board-ststm32-mbed-connect-odin){.reference .internal}             On-board   STM32F439ZIY6   168MHz      2MB     256KB
  [[u-blox C030-N211 IoT Starter Kit]{.std .std-ref}](../boards/ststm32/ublox_c030_n211.html#board-ststm32-ublox-c030-n211){.reference .internal}   External   STM32F437VG     180MHz      1MB     256KB
  [[u-blox C030-R410M IoT]{.std .std-ref}](../boards/ststm32/ublox_c030_r410m.html#board-ststm32-ublox-c030-r410m){.reference .internal}            On-board   STM32F437VG     180MHz      1MB     256KB
  [[u-blox C030-U201 IoT Starter Kit]{.std .std-ref}](../boards/ststm32/ublox_c030_u201.html#board-ststm32-ublox-c030-u201){.reference .internal}   External   STM32F437VG     180MHz      1MB     256KB
  [[u-blox EVK-ODIN-W2]{.std .std-ref}](../boards/ststm32/ublox_evk_odin_w2.html#board-ststm32-ublox-evk-odin-w2){.reference .internal}             External   STM32F439ZIY6   168MHz      2MB     256KB
  [[u-blox ODIN-W2]{.std .std-ref}](../boards/ststm32/mtb_ublox_odin_w2.html#board-ststm32-mtb-ublox-odin-w2){.reference .internal}                 On-board   STM32F439ZIY6   168MHz      2MB     256KB
:::
:::
:::
:::
:::

::: {.rst-footer-buttons role="navigation" aria-label="Footer"}
[[]{.fa .fa-arrow-circle-left aria-hidden="true"}
Previous](siliconlabsefm32.html "Silicon Labs EFM32"){.btn .btn-neutral
.float-left accesskey="p" rel="prev"} [Next []{.fa
.fa-arrow-circle-right aria-hidden="true"}](ststm8.html "ST STM8"){.btn
.btn-neutral .float-right accesskey="n" rel="next"}
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
:   [View](https://github.com/platformio/platformio-docs/blob/develop/platforms/ststm32.rst)
:   [Edit](https://github.com/platformio/platformio-docs/edit/develop/platforms/ststm32.rst)

```{=html}
<!-- -->
```

Search

:   ::: {role="search"}
    :::
:::
:::
