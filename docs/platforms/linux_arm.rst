.. _platform_linux_arm:

Linux ARM
=========

Registry:
    `https://registry.platformio.org/platforms/platformio/linux_arm <https://registry.platformio.org/platforms/platformio/linux_arm>`__

Configuration:
    :ref:`projectconf_env_platform` = ``platformio/linux_arm``

Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. This platform enables building native applications for ARM-based Linux systems (Raspberry Pi) using PlatformIO Core 6.0+.

**Key Features:**

* Cross-compilation support from Linux x86_64, macOS (Intel/ARM), and Windows
* Native compilation on ARM Linux systems
* Support for Raspberry Pi 1-5, Pi 400, Compute Module 4, and Zero/Zero 2W
* Modern GPIO frameworks: lgpio (Pi 5 compatible) and pigpio
* Legacy WiringPi framework for compatibility
* Bare-metal C/C++ application support

For more detailed information please visit `vendor site <https://www.raspberrypi.org?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1

Examples
--------

Examples are listed from `Linux ARM development platform repository <https://github.com/platformio/platform-linux_arm/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `baremetal-hello <https://github.com/platformio/platform-linux_arm/tree/master/examples/baremetal-hello?utm_source=platformio.org&utm_medium=docs>`_ - Simple bare-metal C application
* `lgpio-blink <https://github.com/platformio/platform-linux_arm/tree/master/examples/lgpio-blink?utm_source=platformio.org&utm_medium=docs>`_ - LED blink using lgpio framework
* `pigpio-blink <https://github.com/platformio/platform-linux_arm/tree/master/examples/pigpio-blink?utm_source=platformio.org&utm_medium=docs>`_ - LED blink using pigpio framework
* `wiringpi-blink <https://github.com/platformio/platform-linux_arm/tree/master/examples/wiringpi-blink?utm_source=platformio.org&utm_medium=docs>`_ - LED blink using WiringPi framework
* `wiringpi-serial <https://github.com/platformio/platform-linux_arm/tree/master/examples/wiringpi-serial?utm_source=platformio.org&utm_medium=docs>`_ - Serial communication using WiringPi

Configuration
-------------

Native vs Cross-Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform automatically detects your host system type and configures the appropriate toolchain:

**Native ARM Linux (Raspberry Pi):**

When running PlatformIO directly on a Raspberry Pi or other ARM Linux system, the platform uses the system's native GCC compiler. No additional toolchain installation is required.

.. code-block:: ini

    [env:raspberrypi_5]
    platform = linux_arm
    board = raspberrypi_5
    framework = lgpio

**Cross-Compilation (Linux x86_64):**

Install the ARM cross-compilation toolchain:

.. code-block:: bash

    sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf

**Cross-Compilation (macOS):**

Install using Homebrew:

.. code-block:: bash

    brew install arm-linux-gnueabihf-binutils

Or download the ARM GNU Toolchain from the `ARM Developer website <https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads>`_.

**Cross-Compilation (Windows):**

Download and install the ARM GNU Toolchain from the `ARM Developer website <https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads>`_. Make sure the toolchain binaries are in your PATH.

Architecture Support (32-bit vs 64-bit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This platform supports both 32-bit ARM (ARMv7) and 64-bit ARM (AArch64/ARMv8) architectures.

**Default: 32-bit ARM (ARMv7)**

By default, all boards use 32-bit cross-compilation for maximum compatibility. This works with both 32-bit and 64-bit Raspberry Pi OS installations.

Toolchain requirements:

.. code-block:: bash

    # Linux
    sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf

    # macOS
    brew tap messense/macos-cross-toolchains
    brew install arm-unknown-linux-gnueabihf

**Optional: 64-bit ARM (AArch64)**

For Raspberry Pi 4, Pi 5, Pi 400, and CM4 running a 64-bit OS, you can build 64-bit binaries by setting ``board_build.arch = aarch64`` in your ``platformio.ini``:

.. code-block:: ini

    [env:raspberrypi_5_64bit]
    platform = linux_arm
    board = raspberrypi_5
    framework = lgpio
    board_build.arch = aarch64

Toolchain requirements:

.. code-block:: bash

    # Linux
    sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu

    # macOS
    brew tap messense/macos-cross-toolchains
    brew install aarch64-unknown-linux-gnu

.. note::
    64-bit builds require a 64-bit Raspberry Pi OS installation on the target device. For cross-compilation setup with lgpio framework, you'll also need the 64-bit library:

    .. code-block:: bash

        # For cross-compilation with lgpio on 64-bit targets
        sudo dpkg --add-architecture arm64
        sudo apt install liblgpio-dev:arm64

Framework Selection
~~~~~~~~~~~~~~~~~~~

See the :ref:`Frameworks <linux_arm_frameworks>` section below for detailed comparison and selection guidance.

Quick recommendations:

* **New projects:** Use ``lgpio`` framework
* **Raspberry Pi 5:** Use ``lgpio`` (only compatible framework)
* **Advanced timing/PWM (Pi 1-4):** Use ``pigpio``
* **Legacy projects:** Use ``wiringpi`` (not recommended for new projects)
* **Bare-metal:** Omit framework specification

Stable and upstream versions
-----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-linux_arm/releases>`__ of Linux ARM development platform and the latest upstream version using :ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = linux_arm
    board = ...

    ; Specific version
    [env:custom_stable]
    platform = linux_arm@x.y.z
    board = ...

Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-linux_arm.git
    board = ...

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `toolchain-gccarmlinuxgnueabi <https://registry.platformio.org/tools/platformio/toolchain-gccarmlinuxgnueabi>`__
      - GNU toolchain for ARM Linux (cross-compilation)

.. note::
    This package is optional when running natively on ARM Linux systems. The platform automatically uses the system's native GCC compiler when detected.

.. _linux_arm_frameworks:

Frameworks
----------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - :ref:`framework_lgpio`
      - lgpio is a modern C library for Linux GPIO access, supporting all Raspberry Pi models including Pi 5 with the RP1 I/O controller

    * - :ref:`framework_pigpio`
      - pigpio is a feature-rich C library for Raspberry Pi GPIO control with microsecond timing, PWM, and servo support (Pi 1-4, not Pi 5 compatible)

    * - :ref:`framework_wiringpi`
      - WiringPi is a GPIO access library written in C for the BCM2835+ used in the Raspberry Pi. Now maintained by GC2 (Grazer Computer Club) with Raspberry Pi 5 support (GCLK function not supported on Pi 5)

Framework Comparison
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1

    * - Feature
      - lgpio
      - pigpio
      - WiringPi
      - Bare-metal
    * - **Pi 5 Support**
      - ✅ Yes
      - ❌ No
      - ⚠️ Limited (no GCLK)
      - ✅ Yes
    * - **Pi 1-4 Support**
      - ✅ Yes
      - ✅ Yes
      - ✅ Yes
      - ✅ Yes
    * - **Cross-compilation**
      - ✅ Yes
      - ✅ Yes
      - ❌ No
      - ✅ Yes
    * - **GPIO Control**
      - ✅ Full
      - ✅ Full
      - ✅ Full
      - ⚠️ Manual
    * - **PWM**
      - ✅ Basic
      - ✅ Advanced
      - ✅ Basic
      - ⚠️ Manual
    * - **I2C/SPI/Serial**
      - ✅ Yes
      - ✅ Yes
      - ✅ Yes
      - ⚠️ Manual
    * - **Precise Timing**
      - ⚠️ Standard
      - ✅ Microsecond
      - ⚠️ Standard
      - ⚠️ Standard
    * - **Maintenance Status**
      - ✅ Active
      - ✅ Active
      - ⚠️ Maintenance Mode
      - N/A

**Recommendations:**

* **For new projects:** Use **lgpio** - modern, actively maintained, works on all Raspberry Pi models including Pi 5
* **For Raspberry Pi 5:** Use **lgpio** only - the only framework fully compatible with Pi 5's RP1 I/O controller
* **For precise timing and advanced PWM (Pi 1-4):** Use **pigpio** for microsecond timing accuracy, complex PWM patterns, and servo control
* **For legacy compatibility (Pi 1-4):** Use **WiringPi** only if maintaining existing projects (cross-compilation not supported)
* **For maximum portability:** Use **bare-metal** - direct system calls work on all boards

System Dependencies
~~~~~~~~~~~~~~~~~~~

Each framework requires system libraries on the target Raspberry Pi:

**lgpio:**

.. code-block:: bash

    sudo apt update
    sudo apt install liblgpio-dev liblgpio1

**pigpio:**

.. code-block:: bash

    sudo apt update
    sudo apt install libpigpio-dev pigpio

**WiringPi:**

.. code-block:: bash

    sudo apt install wiringpi

Or build from source:

.. code-block:: bash

    git clone https://github.com/WiringPi/WiringPi.git
    cd WiringPi
    ./build debian
    sudo apt install ./wiringpi-*.deb

Boards
------

.. note::
    * You can list pre-configured boards by :ref:`cmd_boards` command
    * For more detailed ``board`` information please scroll the tables below by horizontally.

Raspberry Pi
~~~~~~~~~~~~

.. list-table::
    :header-rows:  1

    * - Name
      - MCU
      - Frequency
      - RAM
      - Frameworks
    * - :ref:`board_linux_arm_raspberrypi_1b`
      - BCM2835
      - 700MHz
      - 512MB
      - lgpio, pigpio, wiringpi
    * - :ref:`board_linux_arm_raspberrypi_2b`
      - BCM2836
      - 900MHz
      - 1GB
      - lgpio, pigpio, wiringpi
    * - :ref:`board_linux_arm_raspberrypi_3b`
      - BCM2837
      - 1200MHz
      - 1GB
      - lgpio, pigpio, wiringpi
    * - :ref:`board_linux_arm_raspberrypi_4b`
      - BCM2711
      - 1500MHz
      - 1-8GB
      - lgpio, pigpio, wiringpi
    * - :ref:`board_linux_arm_raspberrypi_400`
      - BCM2711
      - 1800MHz
      - 4GB
      - lgpio, pigpio, wiringpi
    * - :ref:`board_linux_arm_raspberrypi_5`
      - BCM2712
      - 2400MHz
      - 4-16GB
      - lgpio, wiringpi (limited)
    * - :ref:`board_linux_arm_raspberrypi_cm4`
      - BCM2711
      - 1500MHz
      - 1-8GB
      - lgpio, pigpio, wiringpi
    * - :ref:`board_linux_arm_raspberrypi_zero`
      - BCM2835
      - 1000MHz
      - 512MB
      - lgpio, pigpio, wiringpi
    * - :ref:`board_linux_arm_raspberrypi_zero2w`
      - BCM2837
      - 1000MHz
      - 512MB
      - lgpio, pigpio, wiringpi

.. note::
    * **Raspberry Pi 5:** pigpio is NOT compatible. WiringPi has limited support (GCLK function not available). Use lgpio for full Pi 5 compatibility.
    * **64-bit support:** Pi 3B, 4B, 400, 5, CM4, and Zero 2W support both 32-bit (ARMv7) and 64-bit (AArch64) builds.
    * **Architecture:** Set ``board_build.arch = aarch64`` in platformio.ini for 64-bit builds. Default is 32-bit (armv7).
