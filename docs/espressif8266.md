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
        -   [Espressif 8266](#){.current .reference .internal}
            -   [Configuration](#configuration){.reference .internal}
            -   [Examples](#examples){.reference .internal}
            -   [Stable and upstream
                versions](#stable-and-upstream-versions){.reference
                .internal}
            -   [Packages](#packages){.reference .internal}
            -   [Frameworks](#frameworks){.reference .internal}
            -   [Boards](#boards){.reference .internal}
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
-   Espressif 8266
-   [Edit on
    GitHub](https://github.com/platformio/platformio-docs/blob/develop/platforms/espressif8266.rst){.fa
    .fa-github}

------------------------------------------------------------------------
:::

::: {.document role="main" itemscope="itemscope" itemtype="http://schema.org/Article"}
::: {itemprop="articleBody"}
::: {#espressif-8266 .section}
[]{#platform-espressif8266}

# Espressif 8266[](#espressif-8266 "Link to this heading"){.headerlink}

Registry[:]{.colon}

:   [https://registry.platformio.org/platforms/platformio/espressif8266](https://registry.platformio.org/platforms/platformio/espressif8266){.reference
    .external}

Configuration[:]{.colon}

:   [[platform]{.std
    .std-ref}](../projectconf/sections/env/options/platform/platform.html#projectconf-env-platform){.reference
    .internal} = [`platformio/espressif8266`{.docutils .literal
    .notranslate}]{.pre}

ESP8266 is a cost-effective and highly integrated Wi-Fi MCU with
built-in TCP/IP networking software for IoT applications. ESP8266
integrates an enhanced version of Tensilica's L106 Diamond series 32-bit
processor and on-chip SRAM.

For more detailed information please visit [vendor
site](https://espressif.com/?utm_source=platformio.org&utm_medium=docs){.reference
.external}.

Contents

-   [Configuration](#configuration){#id5 .reference .internal}

-   [Examples](#examples){#id6 .reference .internal}

-   [Stable and upstream versions](#stable-and-upstream-versions){#id7
    .reference .internal}

-   [Packages](#packages){#id8 .reference .internal}

-   [Frameworks](#frameworks){#id9 .reference .internal}

-   [Boards](#boards){#id10 .reference .internal}

::: {#configuration .section}
## [Configuration](#id5){.toc-backref role="doc-backlink"}[](#configuration "Link to this heading"){.headerlink}

-   [CPU Frequency](#cpu-frequency){#id11 .reference .internal}

-   [FLASH Frequency](#flash-frequency){#id12 .reference .internal}

-   [FLASH Mode](#flash-mode){#id13 .reference .internal}

-   [Reset Method](#reset-method){#id14 .reference .internal}

-   [Flash Size](#flash-size){#id15 .reference .internal}

-   [Upload Speed](#upload-speed){#id16 .reference .internal}

-   [lwIP Variant](#lwip-variant){#id17 .reference .internal}

-   [SDK Version](#sdk-version){#id18 .reference .internal}

-   [SSL Support](#ssl-support){#id19 .reference .internal}

-   [Serial Debug](#serial-debug){#id20 .reference .internal}

-   [Debug Level](#debug-level){#id21 .reference .internal}

-   [VTables](#vtables){#id22 .reference .internal}

-   [MMU - Adjusting ICACHE to IRAM
    ratio](#mmu-adjusting-icache-to-iram-ratio){#id23 .reference
    .internal}

-   [Exceptions](#exceptions){#id24 .reference .internal}

-   [Using Filesystem](#using-filesystem){#id25 .reference .internal}

    -   [Selecting appropriate
        Filesystem](#selecting-appropriate-filesystem){#id26 .reference
        .internal}

    -   [Uploading files to
        Filesystem](#uploading-files-to-filesystem){#id27 .reference
        .internal}

    -   [Overriding Filesystem image
        name](#overriding-filesystem-image-name){#id28 .reference
        .internal}

-   [Over-the-Air (OTA) update](#over-the-air-ota-update){#id29
    .reference .internal}

    -   [Authentication and upload
        options](#authentication-and-upload-options){#id30 .reference
        .internal}

-   [Using Arduino Framework with Staging
    version](#using-arduino-framework-with-staging-version){#id31
    .reference .internal}

::: {#cpu-frequency .section}
### [CPU Frequency](#id11){.toc-backref role="doc-backlink"}[](#cpu-frequency "Link to this heading"){.headerlink}

See [[board_build.f_cpu]{.std
.std-ref}](../projectconf/sections/env/options/platform/board_build.f_cpu.html#projectconf-board-build-f-cpu){.reference
.internal} option from [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ; set frequency to 160MHz
    board_build.f_cpu = 160000000L
:::
:::
:::

::: {#flash-frequency .section}
### [FLASH Frequency](#id12){.toc-backref role="doc-backlink"}[](#flash-frequency "Link to this heading"){.headerlink}

Please use [`board_build.f_flash`{.docutils .literal
.notranslate}]{.pre} option from [["platformio.ini" (Project
Configuration File)]{.std
.std-ref}](../projectconf/index.html#projectconf){.reference .internal}
to change a value. Possible values:

-   [`20000000L`{.docutils .literal .notranslate}]{.pre}

-   [`26000000L`{.docutils .literal .notranslate}]{.pre}

-   [`40000000L`{.docutils .literal .notranslate}]{.pre} (default)

-   [`80000000L`{.docutils .literal .notranslate}]{.pre}

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ; set frequency to 80MHz
    board_build.f_flash = 80000000L
:::
:::
:::

::: {#flash-mode .section}
### [FLASH Mode](#id13){.toc-backref role="doc-backlink"}[](#flash-mode "Link to this heading"){.headerlink}

Flash chip interface mode. This parameter is stored in the binary image
header, along with the flash size and flash frequency. The ROM
bootloader in the ESP chip uses the value of these parameters in order
to know how to talk to the flash chip.

Please use [`board_build.flash_mode`{.docutils .literal
.notranslate}]{.pre} option from [["platformio.ini" (Project
Configuration File)]{.std
.std-ref}](../projectconf/index.html#projectconf){.reference .internal}
to change a value. Possible values:

-   [`qio`{.docutils .literal .notranslate}]{.pre}

-   [`qout`{.docutils .literal .notranslate}]{.pre}

-   [`dio`{.docutils .literal .notranslate}]{.pre}

-   [`dout`{.docutils .literal .notranslate}]{.pre}

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    board_build.flash_mode = qio
:::
:::
:::

::: {#reset-method .section}
### [Reset Method](#id14){.toc-backref role="doc-backlink"}[](#reset-method "Link to this heading"){.headerlink}

You can set custom reset method using [[upload_resetmethod]{.std
.std-ref}](../projectconf/sections/env/options/upload/upload_resetmethod.html#projectconf-upload-resetmethod){.reference
.internal} option from [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}.

The [possible
values](https://github.com/igrr/esptool-ck#supported-boards){.reference
.external} are:

-   [`ck`{.docutils .literal .notranslate}]{.pre} - RTS controls RESET
    or CH_PD, DTR controls GPIO0

-   [`wifio`{.docutils .literal .notranslate}]{.pre} - TXD controls
    GPIO0 via PNP transistor and DTR controls RESET via a capacitor

-   [`nodemcu`{.docutils .literal .notranslate}]{.pre} - GPIO0 and RESET
    controlled using two NPN transistors as in NodeMCU devkit.

See [default reset methods per
board](https://github.com/platformio/platform-espressif8266/search?p=1&q=resetmethod){.reference
.external}.

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    upload_resetmethod = ck
:::
:::
:::

::: {#flash-size .section}
[]{#platform-espressif-customflash}

### [Flash Size](#id15){.toc-backref role="doc-backlink"}[](#flash-size "Link to this heading"){.headerlink}

::: {.admonition .warning}
Warning

Please make sure to read [ESP8266 Flash
layout](https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#flash-layout){.reference
.external} information first.
:::

Available LD-scripts:
[https://github.com/esp8266/Arduino/tree/master/tools/sdk/ld](https://github.com/esp8266/Arduino/tree/master/tools/sdk/ld){.reference
.external}

Please open [`eagle.flash.***.ld`{.docutils .literal
.notranslate}]{.pre} file to check how flash is split.

To override default LD script please use [[board_build.ldscript]{.std
.std-ref}](../projectconf/sections/env/options/platform/board_build.ldscript.html#projectconf-board-build-ldscript){.reference
.internal} option from [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}.

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    board_build.ldscript = eagle.flash.4m.ld
:::
:::
:::

::: {#upload-speed .section}
### [Upload Speed](#id16){.toc-backref role="doc-backlink"}[](#upload-speed "Link to this heading"){.headerlink}

You can set custom upload speed using [[upload_speed]{.std
.std-ref}](../projectconf/sections/env/options/upload/upload_speed.html#projectconf-upload-speed){.reference
.internal} option from [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    upload_speed = 9600
:::
:::
:::

::: {#lwip-variant .section}
### [lwIP Variant](#id17){.toc-backref role="doc-backlink"}[](#lwip-variant "Link to this heading"){.headerlink}

Available variants (macros):

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_LWIP2_LOW_MEMORY`{.docutils
    .literal .notranslate}]{.pre} v2 Lower Memory **(default)**

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH`{.docutils
    .literal .notranslate}]{.pre} v2 Higher Bandwidth

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_LWIP2_LOW_MEMORY_LOW_FLASH`{.docutils
    .literal .notranslate}]{.pre} v2 Lower Memory (no features)

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_LWIP2_HIGHER_BANDWIDTH_LOW_FLASH`{.docutils
    .literal .notranslate}]{.pre} v2 Higher Bandwidth (no features)

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_LWIP2_IPV6_LOW_MEMORY`{.docutils
    .literal .notranslate}]{.pre} v2 IPv6 Lower Memory

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_LWIP2_IPV6_HIGHER_BANDWIDTH`{.docutils
    .literal .notranslate}]{.pre} v2 IPv6 Higher Bandwidth

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_LWIP_HIGHER_BANDWIDTH`{.docutils
    .literal .notranslate}]{.pre} v1.4 Higher Bandwidth

You can change lwIP Variant by passing a custom macro using project
[[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal}.

For example, to switch to lwIP v1.4

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ...
    build_flags = -D PIO_FRAMEWORK_ARDUINO_LWIP_HIGHER_BANDWIDTH
:::
:::
:::

::: {#sdk-version .section}
### [SDK Version](#id18){.toc-backref role="doc-backlink"}[](#sdk-version "Link to this heading"){.headerlink}

Available versions (macros):

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK305`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK-3.0.5 (available since
    [Arduino core for ESP8266
    3.1.0](https://github.com/esp8266/Arduino/releases/tag/3.1.0){.reference
    .external})

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK3`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK-pre-3.0 as of Jun 26, 2018
    (removed in Arduino core for ESP8266 3.1.0)

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK221`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK v2.2.1 (legacy) as of Jun 8,
    2018

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_190313`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK v2.2.x branch as of Mar 13,
    2019

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_190703`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK v2.2.x branch as of Jul 03,
    2019 **(default)**

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_191024`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK v2.2.x branch as of Oct 24,
    2019

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_191105`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK v2.2.x branch as of to Nov
    05, 2019

-   [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x_191122`{.docutils
    .literal .notranslate}]{.pre} NonOS SDK v2.2.x branch as of to Nov
    22, 2019

You can change SDK version by passing a custom macro using project
[[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal}.

For example, to switch to SDK-pre-3.0:

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ...
    build_flags = -D PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK3
:::
:::
:::

::: {#ssl-support .section}
### [SSL Support](#id19){.toc-backref role="doc-backlink"}[](#ssl-support "Link to this heading"){.headerlink}

By default, all SSL ciphers (most compatible) are supported.

You can control SSL support passing a custom macro using project
[[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal}.

For example, use basic SSL ciphers (lower ROM use):

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ...
    build_flags = -D BEARSSL_SSL_BASIC
:::
:::
:::

::: {#serial-debug .section}
[]{#platform-espressif8266-serial-debug}

### [Serial Debug](#id20){.toc-backref role="doc-backlink"}[](#serial-debug "Link to this heading"){.headerlink}

Please use the next [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} to enable Serial debug:

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ...
    build_flags = -DDEBUG_ESP_PORT=Serial

    ; or for Serial1
    build_flags = -DDEBUG_ESP_PORT=Serial1
:::
:::
:::

::: {#debug-level .section}
### [Debug Level](#id21){.toc-backref role="doc-backlink"}[](#debug-level "Link to this heading"){.headerlink}

Please use one of the next [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} to change debug level. A [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} option could be used only the one time per build environment.
If you need to specify more flags, please separate them with a new line
or space.

Also, please note that you will need to extend [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} with [[Serial Debug]{.std
.std-ref}](#platform-espressif8266-serial-debug){.reference .internal}
macro. For example, [`build_flags`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`-DDEBUG_ESP_PORT=Serial`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`-DDEBUG_ESP_SSL`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`...`{.docutils
.literal .notranslate}]{.pre}.

Actual information is available in [Arduino for ESP8266 Board
Manifest](https://github.com/esp8266/Arduino/blob/master/boards.txt#L286){.reference
.external}. Please scroll to [`generic.menu.lvl`{.docutils .literal
.notranslate}]{.pre} section.

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    platform = ...
    board = ...
    framework = arduino

    ;;;;; Possible options ;;;;;;

    ; SSL
    build_flags = -DDEBUG_ESP_SSL

    ; TLS_MEM
    build_flags = -DDEBUG_ESP_TLS_MEM

    ; HTTP_CLIENT
    build_flags = -DDEBUG_ESP_HTTP_CLIENT

    ; HTTP_SERVER
    build_flags = -DDEBUG_ESP_HTTP_SERVER

    ; SSL+TLS_MEM
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM

    ; SSL+HTTP_CLIENT
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_HTTP_CLIENT

    ; SSL+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_HTTP_SERVER

    ; TLS_MEM+HTTP_CLIENT
    build_flags =
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT

    ; TLS_MEM+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_SERVER

    ; HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; SSL+TLS_MEM+HTTP_CLIENT
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT

    ; SSL+TLS_MEM+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_SERVER

    ; SSL+HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; TLS_MEM+HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; SSL+TLS_MEM+HTTP_CLIENT+HTTP_SERVER
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER

    ; CORE
    build_flags = -DDEBUG_ESP_CORE

    ; WIFI
    build_flags = -DDEBUG_ESP_WIFI

    ; HTTP_UPDATE
    build_flags = -DDEBUG_ESP_HTTP_UPDATE

    ; UPDATER
    build_flags = -DDEBUG_ESP_UPDATER

    ; OTA
    build_flags = -DDEBUG_ESP_OTA

    ; OOM
    build_flags =
      -DDEBUG_ESP_OOM
      -include "umm_malloc/umm_malloc_cfg.h"

    ; CORE+WIFI+HTTP_UPDATE+UPDATER+OTA+OOM
    build_flags =
      -DDEBUG_ESP_CORE
      -DDEBUG_ESP_WIFI
      -DDEBUG_ESP_HTTP_UPDATE
      -DDEBUG_ESP_UPDATER
      -DDEBUG_ESP_OTA
      -DDEBUG_ESP_OOM -include "umm_malloc/umm_malloc_cfg.h"

    ; SSL+TLS_MEM+HTTP_CLIENT+HTTP_SERVER+CORE+WIFI+HTTP_UPDATE+UPDATER+OTA+OOM
    build_flags =
      -DDEBUG_ESP_SSL
      -DDEBUG_ESP_TLS_MEM
      -DDEBUG_ESP_HTTP_CLIENT
      -DDEBUG_ESP_HTTP_SERVER
      -DDEBUG_ESP_CORE
      -DDEBUG_ESP_WIFI
      -DDEBUG_ESP_HTTP_UPDATE
      -DDEBUG_ESP_UPDATER
      -DDEBUG_ESP_OTA
      -DDEBUG_ESP_OOM -include "umm_malloc/umm_malloc_cfg.h"

    ; NoAssert-NDEBUG
    build_flags = -DNDEBUG
:::
:::
:::

::: {#vtables .section}
### [VTables](#id22){.toc-backref role="doc-backlink"}[](#vtables "Link to this heading"){.headerlink}

Please use one of the next [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal}:

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ...

    ; Flash (default)
    build_flags = -DVTABLES_IN_FLASH

    ; Heap
    build_flags = -DVTABLES_IN_DRAM

    ; IRAM
    build_flags = -DVTABLES_IN_IRAM
:::
:::
:::

::: {#mmu-adjusting-icache-to-iram-ratio .section}
### [MMU - Adjusting ICACHE to IRAM ratio](#id23){.toc-backref role="doc-backlink"}[](#mmu-adjusting-icache-to-iram-ratio "Link to this heading"){.headerlink}

By default the balanced ratio (32KB cache + 32KB IRAM) configuration is
used. Alternative configurations can be enabled using the
[[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal} option in [["platformio.ini" (Project Configuration
File)]{.std .std-ref}](../projectconf/index.html#projectconf){.reference
.internal}:

  Name                                                                                                    Description
  ------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------
  [`PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM48`{.docutils .literal .notranslate}]{.pre}                     16KB cache + 48KB IRAM (IRAM)
  [`PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM48_SECHEAP_SHARED`{.docutils .literal .notranslate}]{.pre}      16KB cache + 48KB IRAM and 2nd Heap (shared)
  [`PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM32_SECHEAP_NOTSHARED`{.docutils .literal .notranslate}]{.pre}   16KB cache + 32KB IRAM + 16KB 2nd Heap (not shared)
  [`PIO_FRAMEWORK_ARDUINO_MMU_EXTERNAL_128K`{.docutils .literal .notranslate}]{.pre}                      128K External 23LC1024
  [`PIO_FRAMEWORK_ARDUINO_MMU_EXTERNAL_1024K`{.docutils .literal .notranslate}]{.pre}                     1M External 64 MBit PSRAM
  [`PIO_FRAMEWORK_ARDUINO_MMU_CUSTOM`{.docutils .literal .notranslate}]{.pre}                             Disables default configuration and expects user-specified flags

  : [MMU Configuration
  Options]{.caption-text}[](#id4 "Link to this table"){.headerlink}

Examples:

::: {.highlight-ini .notranslate}
::: highlight
    [env:espduino]
    platform = espressif8266
    framework = arduino
    board = espduino
    build_flags =
        -D PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM48

    [env:espino]
    platform = espressif8266
    framework = arduino
    board = espino
    build_flags =
        -D PIO_FRAMEWORK_ARDUINO_MMU_CACHE16_IRAM32_SECHEAP_NOTSHARED

    [env:d1_mini]
    platform = espressif8266
    framework = arduino
    board = d1_mini
    build_flags =
        -D PIO_FRAMEWORK_ARDUINO_MMU_CUSTOM
        -D MMU_IRAM_SIZE=0xC000
        -D MMU_ICACHE_SIZE=0x4000
        -D MMU_IRAM_HEAP
:::
:::

More detailed information on this matter can be found in the [official
documentation](https://arduino-esp8266.readthedocs.io/en/latest/mmu.html){.reference
.external}.
:::

::: {#exceptions .section}
### [Exceptions](#id24){.toc-backref role="doc-backlink"}[](#exceptions "Link to this heading"){.headerlink}

Exceptions are disabled by default. To enable exceptions, use the
[`PIO_FRAMEWORK_ARDUINO_ENABLE_EXCEPTIONS`{.docutils .literal
.notranslate}]{.pre} macro in [[build_flags]{.std
.std-ref}](../projectconf/sections/env/options/build/build_flags.html#projectconf-build-flags){.reference
.internal}. That macro will add the [`-fexceptions`{.docutils .literal
.notranslate}]{.pre} flag and will link the final firmware against the
[`stdc++-exc`{.docutils .literal .notranslate}]{.pre} library with
enabled exceptions. For example:

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    ...

    ; Enable exceptions
    build_flags = -D PIO_FRAMEWORK_ARDUINO_ENABLE_EXCEPTIONS
:::
:::
:::

::: {#using-filesystem .section}
[]{#platform-espressif-uploadfs}

### [Using Filesystem](#id25){.toc-backref role="doc-backlink"}[](#using-filesystem "Link to this heading"){.headerlink}

::: {#selecting-appropriate-filesystem .section}
#### [Selecting appropriate Filesystem](#id26){.toc-backref role="doc-backlink"}[](#selecting-appropriate-filesystem "Link to this heading"){.headerlink}

There are two file systems for utilizing the on-board flash on the
ESP8266: [`SPIFFS`{.docutils .literal .notranslate}]{.pre} and
[`LittleFS`{.docutils .literal .notranslate}]{.pre}. They provide a
compatible API but have incompatible on-flash implementations, so it is
important to choose one or the other per project as attempting to mount
a SPIFFS volume under LittleFS may result in a format operation and
definitely will not preserve any files, and vice-versa.

::: {.admonition .warning}
Warning

SPIFFS is currently deprecated and may be removed in future releases of
the core. Please consider moving your code to LittleFS.
:::

The [`SPIFFS`{.docutils .literal .notranslate}]{.pre} file system is
used by default in order to keep legacy project compatible. To choose
[`LittleFS`{.docutils .literal .notranslate}]{.pre} as the file system,
it should be explicitly specified using
[`board_build.filesystem`{.docutils .literal .notranslate}]{.pre} option
in [["platformio.ini" (Project Configuration File)]{.std
.std-ref}](../projectconf/index.html#projectconf){.reference .internal},
for example:

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    platform = espressif8266
    framework = arduino
    board = ...
    board_build.filesystem = littlefs
:::
:::

More information about pros and cons of each file system can be found in
[the official
documentation](https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#filesystem){.reference
.external}.
:::

::: {#uploading-files-to-filesystem .section}
#### [Uploading files to Filesystem](#id27){.toc-backref role="doc-backlink"}[](#uploading-files-to-filesystem "Link to this heading"){.headerlink}

::: {.admonition .warning}
Warning

Please make sure to read [ESP8266 Flash
layout](https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html#flash-layout){.reference
.external} information first.
:::

1.  Create a new project using [[PlatformIO IDE]{.std
    .std-ref}](../integration/ide/pioide.html#pioide){.reference
    .internal} or initialize project using [[PlatformIO Core (CLI)]{.std
    .std-ref}](../core/index.html#piocore){.reference .internal} and
    [[pio project init]{.std
    .std-ref}](../core/userguide/project/cmd_init.html#cmd-project-init){.reference
    .internal} (if you have not initialized it yet)

2.  Create the [`data`{.docutils .literal .notranslate}]{.pre} folder
    (it should be on the same level as the [`src`{.docutils .literal
    .notranslate}]{.pre} folder) and put files there. Also, you can
    specify your own location for [[data_dir]{.std
    .std-ref}](../projectconf/sections/platformio/options/directory/data_dir.html#projectconf-pio-data-dir){.reference
    .internal}

3.  Run the "Upload File System image" task in [[PlatformIO IDE]{.std
    .std-ref}](../integration/ide/pioide.html#pioide){.reference
    .internal} or use [[PlatformIO Core (CLI)]{.std
    .std-ref}](../core/index.html#piocore){.reference .internal} and the
    [[`pio`{.xref .std .std-option .docutils .literal
    .notranslate}]{.pre}` `{.xref .std .std-option .docutils .literal
    .notranslate}[`run`{.xref .std .std-option .docutils .literal
    .notranslate}]{.pre}` `{.xref .std .std-option .docutils .literal
    .notranslate}[`--target`{.xref .std .std-option .docutils .literal
    .notranslate}]{.pre}](../core/userguide/cmd_run.html#cmdoption-pio-run-t){.reference
    .internal} command with the [`uploadfs`{.docutils .literal
    .notranslate}]{.pre} target.

To upload file system image using OTA update please specify
[`upload_port`{.docutils .literal .notranslate}]{.pre} /
[`--upload-port`{.docutils .literal .notranslate}]{.pre} as IP address
or mDNS host name (ending with the [`*.local`{.docutils .literal
.notranslate}]{.pre}). For the details please follow to [[Over-the-Air
(OTA) update]{.std .std-ref}](#platform-espressif-ota){.reference
.internal}.

By default, will be used default LD Script for the board where is
specified file system offsets (start, end, page, block). You can
override it using [[Flash Size]{.std
.std-ref}](#platform-espressif-customflash){.reference .internal}.

Active discussion is located in [issue
#382](https://github.com/platformio/platformio-core/issues/382){.reference
.external}.
:::

::: {#overriding-filesystem-image-name .section}
#### [Overriding Filesystem image name](#id28){.toc-backref role="doc-backlink"}[](#overriding-filesystem-image-name "Link to this heading"){.headerlink}

By default, the image file name is set according to the used file
system: [`spiffs.bin`{.docutils .literal .notranslate}]{.pre} or
[`littlefs.bin`{.docutils .literal .notranslate}]{.pre}. You can change
the file name using [a PRE extra
script](https://docs.platformio.org/en/latest/projectconf/advanced_scripting.html#before-pre-and-after-post-actions){.reference
.external}, for example:

::: {.highlight-ini .notranslate}
::: highlight
    [env:d1]
    platform = espressif8266
    framework = arduino
    board = d1
    board_build.filesystem = littlefs
    extra_scripts =
        pre:extra_script.py
:::
:::

Where a special variable [`ESP8266_FS_IMAGE_NAME`{.docutils .literal
.notranslate}]{.pre} can be overridden:

::: {.highlight-python .notranslate}
::: highlight
    Import("env")
    env.Replace(ESP8266_FS_IMAGE_NAME="custom_image_name")
:::
:::
:::
:::

::: {#over-the-air-ota-update .section}
[]{#platform-espressif-ota}

### [Over-the-Air (OTA) update](#id29){.toc-backref role="doc-backlink"}[](#over-the-air-ota-update "Link to this heading"){.headerlink}

::: {.admonition .warning}
Warning

Please make sure to read the theory behind the OTA updates in the [What
is OTA? How to use
it?](https://arduino-esp8266.readthedocs.io/en/latest/ota_updates/readme.html){.reference
.external} article first.
:::

1.  Create a new project using [[PlatformIO Home]{.std
    .std-ref}](../home/index.html#piohome){.reference .internal} or
    initialize a project via [[PlatformIO Core (CLI)]{.std
    .std-ref}](../core/index.html#piocore){.reference .internal} and
    [[pio project init]{.std
    .std-ref}](../core/userguide/project/cmd_init.html#cmd-project-init){.reference
    .internal} (if you have not initialized it yet)

2.  Copy the
    [basicOTA](https://github.com/esp8266/Arduino/blob/master/libraries/ArduinoOTA/examples/BasicOTA/BasicOTA.ino){.reference
    .external} example to [[src_dir]{.std
    .std-ref}](../projectconf/sections/platformio/options/directory/src_dir.html#projectconf-pio-src-dir){.reference
    .internal} and configure your WiFi credentials (SSID and password).

3.  Compile the project to ensure there are no syntax errors in the
    code.

To upload the binary you can either specify the upload address directly
in the CLI command using the [[`pio`{.xref .std .std-option .docutils
.literal .notranslate}]{.pre}` `{.xref .std .std-option .docutils
.literal .notranslate}[`run`{.xref .std .std-option .docutils .literal
.notranslate}]{.pre}` `{.xref .std .std-option .docutils .literal
.notranslate}[`--upload-port`{.xref .std .std-option .docutils .literal
.notranslate}]{.pre}](../core/userguide/cmd_run.html#cmdoption-pio-run-upload-port){.reference
.internal} option:

::: {.highlight-bash .notranslate}
::: highlight
    pio run --target upload --upload-port IP_ADDRESS_HERE or mDNS_NAME.local
:::
:::

For example:

::: {.highlight-none .notranslate}
::: highlight
    pio run -t upload --upload-port 192.168.0.255
    pio run -t upload --upload-port myesp8266.local
:::
:::

Or use the [`upload_port`{.docutils .literal .notranslate}]{.pre} option
in [["platformio.ini" (Project Configuration File)]{.std
.std-ref}](../projectconf/index.html#projectconf){.reference .internal}.
Please note that you also need to set [[upload_protocol]{.std
.std-ref}](../projectconf/sections/env/options/upload/upload_protocol.html#projectconf-upload-protocol){.reference
.internal} to [`espota`{.docutils .literal .notranslate}]{.pre}:

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    upload_protocol = espota
    upload_port = IP_ADDRESS_HERE or mDNS_NAME.local
:::
:::

For example:

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    platform = espressif8266
    board = nodemcuv2
    framework = arduino
    upload_protocol = espota
    upload_port = 192.168.0.255
:::
:::

::: {#authentication-and-upload-options .section}
#### [Authentication and upload options](#id30){.toc-backref role="doc-backlink"}[](#authentication-and-upload-options "Link to this heading"){.headerlink}

You can pass additional options/flags to OTA uploader using
[`upload_flags`{.docutils .literal .notranslate}]{.pre} option in
[["platformio.ini" (Project Configuration File)]{.std
.std-ref}](../projectconf/index.html#projectconf){.reference .internal}

::: {.highlight-ini .notranslate}
::: highlight
    [env:myenv]
    upload_protocol = espota
    ; each flag in a new line
    upload_flags =
      --port=8266
:::
:::

Available flags

-   [`--port=ESP_PORT`{.docutils .literal .notranslate}]{.pre} ESP8266
    OTA Port. Default 8266

-   [`--auth=AUTH`{.docutils .literal .notranslate}]{.pre} Set
    authentication password

-   [`--spiffs`{.docutils .literal .notranslate}]{.pre} Use this option
    to transmit a SPIFFS image and do not flash the module

For the full list with available options please run

::: {.highlight-bash .notranslate}
::: highlight
    ~/.platformio/packages/framework-arduinoespressif8266/tools/espota.py --help

    Usage: espota.py [options]

    Transmit image over the air to the esp8266 module with OTA support.

    Options:
      -h, --help            show this help message and exit

      Destination:
        -i ESP_IP, --ip=ESP_IP
                            ESP8266 IP Address.
        -I HOST_IP, --host_ip=HOST_IP
                            Host IP Address.
        -p ESP_PORT, --port=ESP_PORT
                            ESP8266 ota Port. Default 8266
        -P HOST_PORT, --host_port=HOST_PORT
                            Host server ota Port. Default random 10000-60000

      Authentication:
        -a AUTH, --auth=AUTH
                            Set authentication password.

      Image:
        -f FILE, --file=FILE
                            Image file.
        -s, --spiffs        Use this option to transmit a SPIFFS image and do not
                            flash the module.

      Output:
        -d, --debug         Show debug output. And override loglevel with debug.
        -r, --progress      Show progress output. Does not work for ArduinoIDE
:::
:::
:::
:::

::: {#using-arduino-framework-with-staging-version .section}
### [Using Arduino Framework with Staging version](#id31){.toc-backref role="doc-backlink"}[](#using-arduino-framework-with-staging-version "Link to this heading"){.headerlink}

PlatformIO will install the latest Arduino Core for ESP8266 from
[https://github.com/esp8266/Arduino](https://github.com/esp8266/Arduino){.reference
.external}. The [Git](https://git-scm.com){.reference .external} should
be installed in a system. To update Arduino Core to the latest revision,
please open [[PlatformIO IDE]{.std
.std-ref}](../integration/ide/pioide.html#pioide){.reference .internal}
and navigate to [`PlatformIO`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`Home`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`>`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`Platforms`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`>`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`Updates`{.docutils .literal .notranslate}]{.pre}.

1.  Please install [[PlatformIO IDE]{.std
    .std-ref}](../integration/ide/pioide.html#pioide){.reference
    .internal}

2.  Initialize a new project, open [["platformio.ini" (Project
    Configuration File)]{.std
    .std-ref}](../projectconf/index.html#projectconf){.reference
    .internal} and specify the link to the framework repository in
    [[platform_packages]{.std
    .std-ref}](../projectconf/sections/env/options/platform/platform_packages.html#projectconf-env-platform-packages){.reference
    .internal} section. For example,

    ::: {.highlight-ini .notranslate}
    ::: highlight
        [env:nodemcuv2]
        platform = espressif8266
        board = nodemcuv2
        framework = arduino
        platform_packages =
            platformio/framework-arduinoespressif8266 @ https://github.com/esp8266/Arduino.git
    :::
    :::

3.  Try to build the project

4.  If you see build errors, then try to build this project using the
    same [`stage`{.docutils .literal .notranslate}]{.pre} with Arduino
    IDE

5.  If it works with Arduino IDE but doesn't work with PlatformIO, then
    please [file a new
    issue](https://github.com/platformio/platform-espressif8266/issuess){.reference
    .external} with attached information:

    -   test project/files

    -   detailed log of build process from Arduino IDE (please copy it
        from console to
        [https://hastebin.com](https://hastebin.com){.reference
        .external})

    -   detailed log of build process from PlatformIO Build System
        (please copy it from console to
        [https://hastebin.com](https://hastebin.com){.reference
        .external})
:::
:::

::: {#examples .section}
## [Examples](#id6){.toc-backref role="doc-backlink"}[](#examples "Link to this heading"){.headerlink}

Examples are listed from [Espressif 8266 development platform
repository](https://github.com/platformio/platform-espressif8266/tree/master/examples?utm_source=platformio.org&utm_medium=docs){.reference
.external}:

-   [arduino-webserver](https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-webserver?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-asyncudp](https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-asyncudp?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-blink](https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [esp8266-rtos-sdk-blink](https://github.com/platformio/platform-espressif8266/tree/master/examples/esp8266-rtos-sdk-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [esp8266-nonos-sdk-blink](https://github.com/platformio/platform-espressif8266/tree/master/examples/esp8266-nonos-sdk-blink?utm_source=platformio.org&utm_medium=docs){.reference
    .external}

-   [arduino-wifiscan](https://github.com/platformio/platform-espressif8266/tree/master/examples/arduino-wifiscan?utm_source=platformio.org&utm_medium=docs){.reference
    .external}
:::

::: {#stable-and-upstream-versions .section}
## [Stable and upstream versions](#id7){.toc-backref role="doc-backlink"}[](#stable-and-upstream-versions "Link to this heading"){.headerlink}

You can switch between [stable
releases](https://github.com/platformio/platform-espressif8266/releases){.reference
.external} of Espressif 8266 development platform and the latest
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
    platform = espressif8266
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = espressif8266@x.y.z
    board = ...
:::
:::
:::

::: {#upstream .section}
### Upstream[](#upstream "Link to this heading"){.headerlink}

::: {.highlight-ini .notranslate}
::: highlight
    [env:upstream_develop]
    platform = https://github.com/platformio/platform-espressif8266.git
    board = ...
:::
:::
:::
:::

::: {#packages .section}
## [Packages](#id8){.toc-backref role="doc-backlink"}[](#packages "Link to this heading"){.headerlink}

  Name                                                                                                                                      Description
  ----------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  [framework-arduinoespressif8266](https://registry.platformio.org/tools/platformio/framework-arduinoespressif8266){.reference .external}   Arduino Wiring-based Framework for Espressif ESP8266 microcontrollers
  [framework-esp8266-nonos-sdk](https://registry.platformio.org/tools/platformio/framework-esp8266-nonos-sdk){.reference .external}         Espressif ESP8266 Non-OS SDK
  [framework-esp8266-rtos-sdk](https://registry.platformio.org/tools/platformio/framework-esp8266-rtos-sdk){.reference .external}           Espressif ESP8266 SDK based on FreeRTOS
  [tool-esptool](https://registry.platformio.org/tools/platformio/tool-esptool){.reference .external}                                       Espressif ESP8266 build/flash helper tool
  [tool-esptoolpy](https://registry.platformio.org/tools/platformio/tool-esptoolpy){.reference .external}                                   A Python-based, open-source, platform-independent utility to communicate with the ROM bootloader in Espressif chips
  [tool-mklittlefs](https://registry.platformio.org/tools/platformio/tool-mklittlefs){.reference .external}                                 Utility for creating littlefs images for upload on the ESP8266
  [tool-mkspiffs](https://registry.platformio.org/tools/platformio/tool-mkspiffs){.reference .external}                                     Tool to build and unpack SPIFFS images
  [toolchain-xtensa](https://registry.platformio.org/tools/platformio/toolchain-xtensa){.reference .external}                               GCC Toolchain for Xtensa processor

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
## [Frameworks](#id9){.toc-backref role="doc-backlink"}[](#frameworks "Link to this heading"){.headerlink}

  Name                                                                                                                            Description
  ------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[Arduino]{.std .std-ref}](../frameworks/arduino.html#framework-arduino){.reference .internal}                                  Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences.
  [[ESP8266 Non-OS SDK]{.std .std-ref}](../frameworks/esp8266-nonos-sdk.html#framework-esp8266-nonos-sdk){.reference .internal}   Espressif ESP8266 Non-OS SDK
  [[ESP8266 RTOS SDK]{.std .std-ref}](../frameworks/esp8266-rtos-sdk.html#framework-esp8266-rtos-sdk){.reference .internal}       Espressif ESP8266 SDK based on FreeRTOS
:::

::: {#boards .section}
## [Boards](#id10){.toc-backref role="doc-backlink"}[](#boards "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

-   You can list pre-configured boards by [[pio boards]{.std
    .std-ref}](../core/userguide/cmd_boards.html#cmd-boards){.reference
    .internal} command

-   For more detailed [`board`{.docutils .literal .notranslate}]{.pre}
    information please scroll the tables below by horizontally.
:::

::: {#d-systems .section}
### 4D Systems[](#d-systems "Link to this heading"){.headerlink}

  Name                                                                                                                                   Debug   MCU       Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[4D Systems gen4 IoD Range]{.std .std-ref}](../boards/espressif8266/gen4iod.html#board-espressif8266-gen4iod){.reference .internal}   No      ESP8266   80MHz       512KB   80KB
:::

::: {#adafruit .section}
### Adafruit[](#adafruit "Link to this heading"){.headerlink}

  Name                                                                                                                               Debug   MCU       Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[Adafruit HUZZAH ESP8266]{.std .std-ref}](../boards/espressif8266/huzzah.html#board-espressif8266-huzzah){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#amperka .section}
### Amperka[](#amperka "Link to this heading"){.headerlink}

  Name                                                                                                                       Debug   MCU       Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[WiFi Slot]{.std .std-ref}](../boards/espressif8266/wifi_slot.html#board-espressif8266-wifi-slot){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#digistump .section}
### DigiStump[](#digistump "Link to this heading"){.headerlink}

  Name                                                                                                               Debug   MCU       Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------ ------- --------- ----------- ------- ------
  [[DigiStump Oak]{.std .std-ref}](../boards/espressif8266/oak.html#board-espressif8266-oak){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#doit .section}
### Doit[](#doit "Link to this heading"){.headerlink}

  Name                                                                                                                                         Debug   MCU       Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[ESP-Mx DevKit (ESP8285)]{.std .std-ref}](../boards/espressif8266/espmxdevkit.html#board-espressif8266-espmxdevkit){.reference .internal}   No      ESP8266   80MHz       1MB     80KB
  [[ESPDuino (ESP-13 Module)]{.std .std-ref}](../boards/espressif8266/espduino.html#board-espressif8266-espduino){.reference .internal}        No      ESP8266   80MHz       4MB     80KB
:::

::: {#dycodex .section}
### DycodeX[](#dycodex "Link to this heading"){.headerlink}

  Name                                                                                                                         Debug   MCU       Frequency   Flash   RAM
  ---------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[ESPectro Core]{.std .std-ref}](../boards/espressif8266/espectro.html#board-espressif8266-espectro){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#espert .section}
### ESPert[](#espert "Link to this heading"){.headerlink}

  Name                                                                                                                                             Debug   MCU       Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------ ------- --------- ----------- ------- ------
  [[ESPresso Lite 1.0]{.std .std-ref}](../boards/espressif8266/espresso_lite_v1.html#board-espressif8266-espresso-lite-v1){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
  [[ESPresso Lite 2.0]{.std .std-ref}](../boards/espressif8266/espresso_lite_v2.html#board-espressif8266-espresso-lite-v2){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#espino .section}
### ESPino[](#espino "Link to this heading"){.headerlink}

  Name                                                                                                              Debug   MCU       Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[ESPino]{.std .std-ref}](../boards/espressif8266/espino.html#board-espressif8266-espino){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#espressif .section}
### Espressif[](#espressif "Link to this heading"){.headerlink}

  Name                                                                                                                                               Debug   MCU       Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[Espressif ESP-WROOM-02]{.std .std-ref}](../boards/espressif8266/esp_wroom_02.html#board-espressif8266-esp-wroom-02){.reference .internal}        No      ESP8266   80MHz       2MB     80KB
  [[Espressif ESP8266 ESP-12E]{.std .std-ref}](../boards/espressif8266/esp12e.html#board-espressif8266-esp12e){.reference .internal}                 No      ESP8266   80MHz       4MB     80KB
  [[Espressif Generic ESP8266 ESP-01 1M]{.std .std-ref}](../boards/espressif8266/esp01_1m.html#board-espressif8266-esp01-1m){.reference .internal}   No      ESP8266   80MHz       1MB     80KB
  [[Espressif Generic ESP8266 ESP-01 512k]{.std .std-ref}](../boards/espressif8266/esp01.html#board-espressif8266-esp01){.reference .internal}       No      ESP8266   80MHz       512KB   80KB
  [[Espressif Generic ESP8266 ESP-07 1MB]{.std .std-ref}](../boards/espressif8266/esp07.html#board-espressif8266-esp07){.reference .internal}        No      ESP8266   80MHz       1MB     80KB
  [[Espressif Generic ESP8266 ESP-07S]{.std .std-ref}](../boards/espressif8266/esp07s.html#board-espressif8266-esp07s){.reference .internal}         No      ESP8266   80MHz       4MB     80KB
  [[Generic ESP8285 Module]{.std .std-ref}](../boards/espressif8266/esp8285.html#board-espressif8266-esp8285){.reference .internal}                  No      ESP8266   80MHz       1MB     80KB
  [[Phoenix 1.0]{.std .std-ref}](../boards/espressif8266/phoenix_v1.html#board-espressif8266-phoenix-v1){.reference .internal}                       No      ESP8266   80MHz       4MB     80KB
  [[Phoenix 2.0]{.std .std-ref}](../boards/espressif8266/phoenix_v2.html#board-espressif8266-phoenix-v2){.reference .internal}                       No      ESP8266   80MHz       4MB     80KB
  [[WifInfo]{.std .std-ref}](../boards/espressif8266/wifinfo.html#board-espressif8266-wifinfo){.reference .internal}                                 No      ESP8266   80MHz       1MB     80KB
:::

::: {#heltec .section}
### Heltec[](#heltec "Link to this heading"){.headerlink}

  Name                                                                                                                                               Debug   MCU       Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[Heltec Wifi kit 8]{.std .std-ref}](../boards/espressif8266/heltec_wifi_kit_8.html#board-espressif8266-heltec-wifi-kit-8){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#itead .section}
### ITEAD[](#itead "Link to this heading"){.headerlink}

  Name                                                                                                                                Debug   MCU       Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[Sonoff Basic]{.std .std-ref}](../boards/espressif8266/sonoff_basic.html#board-espressif8266-sonoff-basic){.reference .internal}   No      ESP8266   80MHz       1MB     80KB
  [[Sonoff S20]{.std .std-ref}](../boards/espressif8266/sonoff_s20.html#board-espressif8266-sonoff-s20){.reference .internal}         No      ESP8266   80MHz       1MB     80KB
  [[Sonoff SV]{.std .std-ref}](../boards/espressif8266/sonoff_sv.html#board-espressif8266-sonoff-sv){.reference .internal}            No      ESP8266   80MHz       1MB     80KB
  [[Sonoff TH]{.std .std-ref}](../boards/espressif8266/sonoff_th.html#board-espressif8266-sonoff-th){.reference .internal}            No      ESP8266   80MHz       1MB     80KB
:::

::: {#invent-one .section}
### Invent One[](#invent-one "Link to this heading"){.headerlink}

  Name                                                                                                                        Debug   MCU       Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[Invent One]{.std .std-ref}](../boards/espressif8266/inventone.html#board-espressif8266-inventone){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#lifely-cc .section}
### Lifely.cc[](#lifely-cc "Link to this heading"){.headerlink}

  Name                                                                                                                                              Debug   MCU       Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[Lifely Agrumino Lemon v4]{.std .std-ref}](../boards/espressif8266/agruminolemon.html#board-espressif8266-agruminolemon){.reference .internal}   No      ESP8266   80MHz       2MB     80KB
:::

::: {#nodemcu .section}
### NodeMCU[](#nodemcu "Link to this heading"){.headerlink}

  Name                                                                                                                                          Debug   MCU       Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[NodeMCU 0.9 (ESP-12 Module)]{.std .std-ref}](../boards/espressif8266/nodemcu.html#board-espressif8266-nodemcu){.reference .internal}        No      ESP8266   80MHz       4MB     80KB
  [[NodeMCU 1.0 (ESP-12E Module)]{.std .std-ref}](../boards/espressif8266/nodemcuv2.html#board-espressif8266-nodemcuv2){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#olimex .section}
### Olimex[](#olimex "Link to this heading"){.headerlink}

  Name                                                                                                                                       Debug   MCU       Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------ ------- --------- ----------- ------- ------
  [[Olimex MOD-WIFI-ESP8266(-DEV)]{.std .std-ref}](../boards/espressif8266/modwifi.html#board-espressif8266-modwifi){.reference .internal}   No      ESP8266   80MHz       2MB     80KB
:::

::: {#schirmilabs .section}
### Schirmilabs[](#schirmilabs "Link to this heading"){.headerlink}

  Name                                                                                                                                       Debug   MCU       Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------ ------- --------- ----------- ------- ------
  [[Schirmilabs Eduino WiFi]{.std .std-ref}](../boards/espressif8266/eduinowifi.html#board-espressif8266-eduinowifi){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#seeedstudio .section}
### SeeedStudio[](#seeedstudio "Link to this heading"){.headerlink}

  Name                                                                                                                    Debug   MCU       Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[Wio Link]{.std .std-ref}](../boards/espressif8266/wio_link.html#board-espressif8266-wio-link){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
  [[Wio Node]{.std .std-ref}](../boards/espressif8266/wio_node.html#board-espressif8266-wio-node){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#sparkfun .section}
### SparkFun[](#sparkfun "Link to this heading"){.headerlink}

  Name                                                                                                                                          Debug   MCU       Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[SparkFun Blynk Board]{.std .std-ref}](../boards/espressif8266/sparkfunBlynk.html#board-espressif8266-sparkfunblynk){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
  [[SparkFun ESP8266 Thing]{.std .std-ref}](../boards/espressif8266/thing.html#board-espressif8266-thing){.reference .internal}                 No      ESP8266   80MHz       512KB   80KB
  [[SparkFun ESP8266 Thing Dev]{.std .std-ref}](../boards/espressif8266/thingdev.html#board-espressif8266-thingdev){.reference .internal}       No      ESP8266   80MHz       512KB   80KB
:::

::: {#sweetpea .section}
### SweetPea[](#sweetpea "Link to this heading"){.headerlink}

  Name                                                                                                                        Debug   MCU       Frequency   Flash   RAM
  --------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[SweetPea ESP-210]{.std .std-ref}](../boards/espressif8266/esp210.html#board-espressif8266-esp210){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#thaieasyelec .section}
### ThaiEasyElec[](#thaieasyelec "Link to this heading"){.headerlink}

  Name                                                                                                                                 Debug   MCU       Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------ ------- --------- ----------- ------- ------
  [[ThaiEasyElec ESPino]{.std .std-ref}](../boards/espressif8266/espinotee.html#board-espressif8266-espinotee){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#wemos .section}
### WEMOS[](#wemos "Link to this heading"){.headerlink}

  Name                                                                                                                                      Debug   MCU       Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[WEMOS D1 R1]{.std .std-ref}](../boards/espressif8266/d1.html#board-espressif8266-d1){.reference .internal}                              No      ESP8266   80MHz       4MB     80KB
  [[WeMos D1 R2 and mini]{.std .std-ref}](../boards/espressif8266/d1_mini.html#board-espressif8266-d1-mini){.reference .internal}           No      ESP8266   80MHz       4MB     80KB
  [[WeMos D1 mini Lite]{.std .std-ref}](../boards/espressif8266/d1_mini_lite.html#board-espressif8266-d1-mini-lite){.reference .internal}   No      ESP8266   80MHz       1MB     80KB
  [[WeMos D1 mini Pro]{.std .std-ref}](../boards/espressif8266/d1_mini_pro.html#board-espressif8266-d1-mini-pro){.reference .internal}      No      ESP8266   80MHz       16MB    80KB
:::

::: {#id3 .section}
### WeMos[](#id3 "Link to this heading"){.headerlink}

  Name                                                                                                                                       Debug   MCU       Frequency   Flash   RAM
  ------------------------------------------------------------------------------------------------------------------------------------------ ------- --------- ----------- ------- ------
  [[WeMos D1 ESP-WROOM-02]{.std .std-ref}](../boards/espressif8266/d1_wroom_02.html#board-espressif8266-d1-wroom-02){.reference .internal}   No      ESP8266   80MHz       2MB     80KB
:::

::: {#wifiduino .section}
### WifiDuino[](#wifiduino "Link to this heading"){.headerlink}

  Name                                                                                                                       Debug   MCU       Frequency   Flash   RAM
  -------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[WiFiduino]{.std .std-ref}](../boards/espressif8266/wifiduino.html#board-espressif8266-wifiduino){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::

::: {#xinabox .section}
### XinaBox[](#xinabox "Link to this heading"){.headerlink}

  Name                                                                                                                                Debug   MCU       Frequency   Flash   RAM
  ----------------------------------------------------------------------------------------------------------------------------------- ------- --------- ----------- ------- ------
  [[XinaBox CW01]{.std .std-ref}](../boards/espressif8266/xinabox_cw01.html#board-espressif8266-xinabox-cw01){.reference .internal}   No      ESP8266   80MHz       4MB     80KB
:::
:::
:::
:::
:::

::: {.rst-footer-buttons role="navigation" aria-label="Footer"}
[[]{.fa .fa-arrow-circle-left aria-hidden="true"}
Previous](espressif32.html "Espressif 32"){.btn .btn-neutral .float-left
accesskey="p" rel="prev"} [Next []{.fa .fa-arrow-circle-right
aria-hidden="true"}](freescalekinetis.html "Freescale Kinetis"){.btn
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
:   [View](https://github.com/platformio/platformio-docs/blob/develop/platforms/espressif8266.rst)
:   [Edit](https://github.com/platformio/platformio-docs/edit/develop/platforms/espressif8266.rst)

```{=html}
<!-- -->
```

Search

:   ::: {role="search"}
    :::
:::
:::
