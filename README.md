# Linux ARM: development platform for [PlatformIO](https://platformio.org)

Linux ARM is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. This platform enables building native applications for ARM-based Linux systems (Raspberry Pi) using PlatformIO Core 6.0+.

**Key Features:**
- Cross-compilation support from Linux x86_64, macOS (Intel/ARM), and Windows
- Native compilation on ARM Linux systems
- Support for Raspberry Pi 1, 2, 3, and 4
- Optional WiringPi framework for GPIO access
- Bare-metal C/C++ application support

* [Home](https://registry.platformio.org/platforms/platformio/linux_arm) (home page in the PlatformIO Registry)
* [Documentation](https://docs.platformio.org/page/platforms/linux_arm.html) (advanced usage, packages, boards, frameworks, etc.)

# Cross-Compilation Setup

This platform supports cross-compilation from various host systems. The platform automatically detects your system and configures the appropriate toolchain.

## Linux (x86_64)

Install the ARM cross-compilation toolchain:

```bash
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf
```

## macOS (Intel or Apple Silicon)

Install using Homebrew:

```bash
brew install arm-linux-gnueabihf-binutils
```

Or download the ARM GNU Toolchain from the [ARM Developer website](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).

## Windows

Download and install the ARM GNU Toolchain from the [ARM Developer website](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads). Make sure the toolchain binaries are in your PATH.

## Native ARM Linux

When running PlatformIO directly on a Raspberry Pi or other ARM Linux system, the platform uses the system's native GCC compiler. No additional toolchain installation is required.

# Supported Boards

- `raspberrypi_1b` - Raspberry Pi 1 Model B
- `raspberrypi_2b` - Raspberry Pi 2 Model B
- `raspberrypi_3b` - Raspberry Pi 3 Model B
- `raspberrypi_4b` - Raspberry Pi 4 Model B (NEW)
- `raspberrypi_zero` - Raspberry Pi Zero

# Usage

1. [Install PlatformIO](https://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = linux_arm
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-linux_arm.git
board = ...
...
```

# Examples

## Bare-Metal Application (No Framework)

Create a simple C/C++ application without any framework:

```ini
[env:raspberrypi_4b]
platform = linux_arm
board = raspberrypi_4b
; No framework specified - bare-metal C application
```

See `examples/baremetal-hello/` for a complete example.

## WiringPi Framework

Use the WiringPi library for GPIO access:

```ini
[env:raspberrypi_3b]
platform = linux_arm
framework = wiringpi
board = raspberrypi_3b
```

**Note:** WiringPi framework currently requires building directly on a Raspberry Pi device (cross-compilation is not supported for WiringPi).

See `examples/wiringpi-blink/` and `examples/wiringpi-serial/` for complete examples.

# Building and Running

## Build a project

```bash
# From your project directory
pio run

# Build for specific environment
pio run -e raspberrypi_4b

# Clean build artifacts
pio run --target clean
```

## Run the compiled program

Transfer the compiled binary to your Raspberry Pi and run it:

```bash
# On your Raspberry Pi
.pio/build/raspberrypi_4b/program
```

# Configuration

Please navigate to [documentation](https://docs.platformio.org/page/platforms/linux_arm.html).
