# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a PlatformIO development platform for Linux ARM (including Raspberry Pi devices). It enables building native applications for ARM-based Linux systems using PlatformIO Core 6.0+. The platform supports cross-compilation from macOS and native compilation on ARM Linux systems.

## Build and Development Commands

### Building Projects
```bash
# Build a project (run from project directory, e.g., examples/wiringpi-blink/)
pio run

# Clean build artifacts
pio run --target clean

# Build with size calculation
pio run --target size
```

### Running Built Programs
```bash
# Run the compiled program (adjust board name as needed)
.pio/build/raspberrypi_2b/program
```

### Testing Platform Installation
```bash
# Install the platform from local repository
pio pkg install --global --platform file://.

# Or install from GitHub (development version)
pio pkg install --global --platform https://github.com/platformio/platform-linux_arm.git
```

## Architecture Overview

### Core Components

1. **platform.py**: Main platform class (`Linux_armPlatform`)
   - Extends `PlatformBase` from PlatformIO
   - Detects native ARM Linux environment (linux_arm/linux_aarch64)
   - Conditionally excludes cross-compilation toolchain when running natively
   - Enforces WiringPi framework restriction: must run directly on Raspberry Pi (no cross-compilation)

2. **platform.json**: Platform manifest
   - Defines platform metadata, version, dependencies
   - Declares supported frameworks (WiringPi)
   - Specifies required packages:
     - `toolchain-gccarmlinuxgnueabi`: Cross-compilation toolchain (optional on native ARM)
     - `framework-wiringpi`: WiringPi GPIO library (optional)

3. **builder/main.py**: SCons build script for Linux ARM targets
   - Configures GCC toolchain (native or cross-compilation)
   - On macOS x86_64: Uses `arm-linux-gnueabihf-` prefix for cross-compilation
   - On native ARM Linux: Uses system GCC without prefix
   - Defines build targets: program binary and size calculation

4. **builder/frameworks/wiringpi.py**: WiringPi framework integration
   - Configures compiler flags: `-O2 -Wall -Winline -pipe -fPIC`
   - Defines `_GNU_SOURCE` macro
   - Links pthread library
   - Builds WiringPi library from framework package

### Board Definitions

Located in `boards/` directory, each JSON file defines:
- MCU type (e.g., bcm2837 for RPi 3)
- CPU frequency
- Platform-specific defines (e.g., `-DRASPBERRYPI -DRASPBERRYPI3`)
- Memory specifications

Supported boards:
- `raspberrypi_1b.json`
- `raspberrypi_2b.json`
- `raspberrypi_3b.json`
- `raspberrypi_zero.json`

### Example Projects

Located in `examples/`, structured as standard PlatformIO projects:
- `platformio.ini`: Defines platform, framework, board
- `src/`: C source files
- `include/`, `lib/`, `test/`: Standard PlatformIO directories

## Key Implementation Details

### Cross-Compilation vs Native Build
The platform automatically detects the host system type:
- **macOS x86_64**: Enables cross-compilation with ARM toolchain prefix
- **ARM Linux (native)**: Removes toolchain package dependency, uses system GCC
- Detection logic in `platform.py:22-24` and `builder/main.py:39-42`

### WiringPi Framework Restriction
Cross-compilation for WiringPi is explicitly blocked in `platform.py:34-39`. Projects using WiringPi framework must run PlatformIO directly on a Raspberry Pi device.

### Build Output Location
Compiled binaries are placed in `.pio/build/<board_name>/program` (note: the example README incorrectly shows `.pio/raspberrypi_2b/program` - the correct path includes `build/`).

## Version Management

- Current version: 1.6.0 (defined in `platform.json:19`)
- Uses conventional commit messages (see git history)
- Git-flow workflow: `develop` branch for development, `release/*` branches for releases
- Versions should be bumped in `platform.json` before tagging releases
