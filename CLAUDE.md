# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a PlatformIO development platform for Linux ARM (including Raspberry Pi devices). It enables building native applications for ARM-based Linux systems using PlatformIO Core 6.0+. The platform supports cross-compilation from macOS and native compilation on ARM Linux systems.

**Current Status**: This is a forked repository (original last updated 2022) undergoing modernization to:
- Fix broken cross-compilation functionality
- Achieve compatibility with latest PlatformIO Core
- Match quality and feature completeness of reference platforms (platform-espressif32, platform-raspberrypi)

## Modernization Research Workflow

This repository includes a structured research and analysis workflow in the `research/` directory for planning and executing the modernization effort.

### Research Structure

The analysis follows an **iterative checkpoint approach** with manageable sessions:

1. **Round 1: Initial Assessment** (`research/01-ROUND-1-PROMPT.md`)
   - High-level comparison with reference platforms
   - Critical blocker identification
   - Priority area ranking for deep-dive
   - Estimated time: 2-3 hours

2. **Round 2: Priority Deep-Dive** (`research/02-ROUND-2-PROMPT.md`)
   - Detailed analysis of top 3-5 priority areas from Round 1
   - Technical solutions and code patterns
   - Effort estimates and dependencies
   - Customized based on Round 1 findings

3. **Round 3: Implementation Roadmap** (`research/03-ROUND-3-PROMPT.md`)
   - Synthesize findings into phased implementation plan
   - Prioritized task list with dependencies
   - Timeline and effort estimates
   - Quick-start action plan

### Key Files

- **`research/00-INDEX.md`**: Master progress tracker, links all rounds and deliverables
- **`research/REFERENCES.md`**: Centralized repository of all sources, links, and code references
- **`research/FINDINGS-TEMPLATE.md`**: Standard structure for analysis outputs
- **`research/ANALYSIS_PROMPT.md`**: Original comprehensive prompt (archived, use round-specific prompts instead)

### Usage

To conduct or continue research:
1. Review `research/00-INDEX.md` for current status
2. Execute the appropriate round prompt in a fresh Claude Code session
3. Update tracking files (`00-INDEX.md`, `REFERENCES.md`) after each round
4. Use findings to guide implementation work

### Benefits of This Approach
- Each round fits in single Claude session (avoids context overflow)
- Can pause/resume between checkpoints
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
