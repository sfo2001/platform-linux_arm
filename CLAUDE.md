# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a PlatformIO development platform for Linux ARM (including Raspberry Pi devices). It enables building native applications for ARM-based Linux systems using PlatformIO Core 6.0+. The platform supports cross-compilation from macOS and native compilation on ARM Linux systems.

**Current Status**: This is a forked repository (original last updated 2022) undergoing modernization to:
- Fix broken cross-compilation functionality
- Achieve compatibility with latest PlatformIO Core
- Match quality and feature completeness of reference platforms (platform-espressif32, platform-raspberrypi)

## Modernization Research Workflow

This repository underwent a structured research and analysis workflow to guide the modernization effort.

**Research Documentation**: The complete research artifacts are available on the **GitHub Wiki**:
- **Wiki**: https://github.com/sfo2001/platform-linux_arm/wiki

### Research Structure

The analysis followed an **iterative checkpoint approach** with manageable sessions:

1. **Round 1: Initial Assessment**
   - High-level comparison with reference platforms
   - Critical blocker identification
   - Priority area ranking for deep-dive
   - Wiki: [[Round 1 Initial Assessment]](https://github.com/sfo2001/platform-linux_arm/wiki/Round-1-Initial-Assessment)

2. **Round 2: Priority Deep-Dive** (multiple focused analyses)
   - Detailed analysis of top priority areas from Round 1
   - Technical solutions and code patterns
   - Effort estimates and dependencies
   - Wiki: [[Round 2 Analyses]](https://github.com/sfo2001/platform-linux_arm/wiki)

3. **Round 3: Implementation Roadmap**
   - Synthesized findings into phased implementation plan
   - Prioritized task list with dependencies
   - Timeline and effort estimates
   - Wiki: [[Round 3 Implementation Roadmap]](https://github.com/sfo2001/platform-linux_arm/wiki/Round-3-Implementation-Roadmap)

### Key Research Pages

- **[Modernization Overview](https://github.com/sfo2001/platform-linux_arm/wiki/Modernization-Overview)**: Master progress tracker
- **[References](https://github.com/sfo2001/platform-linux_arm/wiki/References)**: Centralized repository of sources and links
- **[Implementation Status](https://github.com/sfo2001/platform-linux_arm/wiki/Implementation-Status)**: Current modernization status
- **[Python Codebase Analysis](https://github.com/sfo2001/platform-linux_arm/wiki/Python-Codebase-Analysis)**: Security and quality audit

### Benefits of This Approach
- Each round fit in single Claude session (avoided context overflow)
- Pause/resume capability between checkpoints
- High-level patterns with references (detailed sources available for deep-dive)
- Pivot based on discoveries
- Clear decision trail and rationale

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
pio pkg install --global --platform https://github.com/sfo2001/platform-linux_arm.git
```

## Remote Development Workflows

The platform supports comprehensive remote development workflows for Raspberry Pi and ARM SBC targets:

### Remote Deployment
```bash
# Upload and run program on remote target (e.g., Raspberry Pi)
pio run --target upload

# Example platformio.ini configuration
# [env:raspberrypi_4b]
# upload_protocol = scp
# upload_port = pi@raspberrypi.local:/home/pi/program
# upload_run_after = true
```

See `docs/UPLOAD.md` and `examples/remote-deployment/` for complete documentation.

### Remote Testing
```bash
# Run tests on remote hardware via SSH
pio test

# Example platformio.ini configuration
# [env:raspberrypi_4b]
# test_transport = ssh
# test_port = pi@raspberrypi.local:/tmp/test_program
```

Cross-compiled test binaries are automatically deployed and executed on target hardware with real-time output streaming. See `docs/REMOTE_TESTING.md` and `examples/remote-testing/` for complete documentation.

### Remote Debugging
```bash
# Launch GDB debugging session over SSH
pio debug

# Example platformio.ini configuration
# [env:raspberrypi_4b]
# debug_tool = gdbserver-ssh
# debug_port = pi@raspberrypi.local
```

Supports IDE-integrated debugging (VS Code) with breakpoints, variable inspection, and stepping. See `docs/DEBUGGING.md` and `examples/remote-debugging/` for complete documentation.

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
- Raspberry Pi: `raspberrypi_1b.json`, `raspberrypi_2b.json`, `raspberrypi_3b.json`, `raspberrypi_4b.json`, `raspberrypi_5.json`, `raspberrypi_400.json`, `raspberrypi_cm4.json`, `raspberrypi_zero.json`, `raspberrypi_zero2w.json`
- Orange Pi: `orangepi_zero.json` (Allwinner H2+/H3)

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

- Development version: 1.7.0 (unreleased, defined in `platform.json:19`)
- Last released version: 1.6.0 (2025-11-09)
- Uses conventional commit messages (see git history)
- Git-flow workflow: `develop` branch for development, `release/*` branches for releases
- Versions should be bumped in `platform.json` before tagging releases
