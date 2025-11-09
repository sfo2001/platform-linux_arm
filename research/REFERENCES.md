# Research References

This document tracks all external references, repositories, documentation, and code locations referenced during the analysis. Use this to revisit sources for deep-dives without bloating the main analysis documents.

## Primary Repositories

### Current Platform
- **platform-linux_arm** (this repository)
  - GitHub: https://github.com/platformio/platform-linux_arm
  - Last official update: 2022
  - Status: Forked for modernization

### Reference Platforms (Best Practices)

- **platform-espressif32**
  - GitHub: https://github.com/platformio/platform-espressif32
  - Status: Actively maintained, feature-complete
  - Key strengths: Multiple framework support, comprehensive CI/CD, excellent documentation

- **platform-raspberrypi**
  - GitHub: https://github.com/platformio/platform-raspberrypi
  - Status: Actively maintained
  - Key strengths: RP2040 + ARM Linux support, modern board definitions
  - Note: Covers both RP2040 microcontrollers and Raspberry Pi SBCs

### PlatformIO Core
- **platformio-core**
  - GitHub: https://github.com/platformio/platformio-core
  - Documentation: https://docs.platformio.org/
  - Latest Release: *(to be filled during research)*
  - API Docs: https://docs.platformio.org/en/latest/scripting/index.html

## Documentation

### PlatformIO
- Platform Creation Guide: https://docs.platformio.org/en/latest/platforms/creating_platform.html
- Platform JSON Schema: https://docs.platformio.org/en/latest/manifests/platform-json.html
- Board JSON Schema: https://docs.platformio.org/en/latest/manifests/board-json.html
- Build Scripts: https://docs.platformio.org/en/latest/scripting/index.html
- SCons Integration: https://docs.platformio.org/en/latest/integration/scons.html

### Toolchains
- ARM GNU Toolchain: https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain
- GCC ARM Linux GNUEABI: *(links to be added)*
- AArch64 toolchains: *(links to be added)*

### Frameworks
- WiringPi: http://wiringpi.com *(Note: Check if deprecated)*
- libgpiod: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git
- pigpio: https://abyz.me.uk/rpi/pigpio/

## Code References

### platform-espressif32 Key Files
*(To be filled during Round 1 & 2 analysis)*

**Platform Structure**:
- `platform.json`: [link to specific commit/line]
- `platform.py`: [link to specific commit/line]
- `builder/main.py`: [link to specific commit/line]

**Framework Integration Examples**:
- Arduino framework: [link]
- ESP-IDF framework: [link]

**CI/CD**:
- GitHub Actions workflows: [link]
- Test infrastructure: [link]

### platform-raspberrypi Key Files
*(To be filled during Round 1 & 2 analysis)*

**Platform Structure**:
- `platform.json`: [link to specific commit/line]
- `platform.py`: [link to specific commit/line]
- Cross-compilation logic: [link]

**Board Definitions**:
- Raspberry Pi board examples: [link]
- RP2040 board examples: [link]

### platform-linux_arm Current State
*(Local files - reference for comparison)*

**Core Files**:
- `platform.json`: [Current issues to note]
- `platform.py`: [Known limitations]
- `builder/main.py`: [Cross-compilation problems]
- `builder/frameworks/wiringpi.py`: [Framework restrictions]

## Issues & Discussions

### Reported Issues
*(To be filled during research)*
- Issue #xxx: Cross-compilation broken since PlatformIO 6.0
- Issue #xxx: WiringPi deprecated/unmaintained
- *(Add relevant GitHub issues)*

### Community Discussions
*(To be filled during research)*
- Forum posts about linux_arm platform
- Stack Overflow questions
- Reddit discussions

## Research Notes Template

When adding new references during analysis rounds, use this format:

```markdown
### [Category] - [Source Name]
- **URL**: [direct link]
- **Relevance**: [why this is important]
- **Key Findings**: [1-2 sentence summary]
- **Referenced In**: [which round/document uses this]
- **Code Location**: [specific file:line if applicable]
- **Last Checked**: [date]
```

## Round-Specific References

### Round 1: Initial Assessment

**Date**: 2025-11-09
**Status**: ✅ Complete

#### Platform Repositories Analyzed

**platform-espressif32**:
- **Repository**: https://github.com/platformio/platform-espressif32
- **platform.json**: https://raw.githubusercontent.com/platformio/platform-espressif32/master/platform.json
- **platform.py**: https://raw.githubusercontent.com/platformio/platform-espressif32/master/platform.py
- **CI Workflow**: https://github.com/platformio/platform-espressif32/tree/master/.github/workflows
- **examples.yml**: https://raw.githubusercontent.com/platformio/platform-espressif32/master/.github/workflows/examples.yml
- **Latest Release**: v6.12.0 (July 31, 2025)
- **Key Findings**:
  - 1.1k stars, 760 forks, 94 contributors, 84 releases
  - 21 packages (7 toolchains, 2 frameworks, 9 tools, 3 debuggers)
  - 2 frameworks (Arduino, ESP-IDF)
  - ~380 lines in platform.py with advanced dynamic configuration
  - CI/CD: 17 examples × 3 OS = 51 test combinations
- **Referenced In**: Round 1 Initial Assessment, Reference Platform Comparison

**platform-raspberrypi**:
- **Repository**: https://github.com/platformio/platform-raspberrypi
- **platform.json**: https://raw.githubusercontent.com/platformio/platform-raspberrypi/master/platform.json
- **platform.py**: https://raw.githubusercontent.com/platformio/platform-raspberrypi/master/platform.py
- **Latest Release**: v1.18.0 (October 23, 2025)
- **Key Findings**:
  - 83 stars, 127 forks, 4 contributors
  - Focus: RP2040 microcontroller (not Linux ARM SBCs)
  - 4 packages (toolchain, framework, uploaders, debug tools)
  - 1 framework (Arduino with mbed)
  - ~95 lines in platform.py with moderate sophistication
  - GitHub Actions CI/CD for example testing
- **Referenced In**: Round 1 Initial Assessment, Reference Platform Comparison

**platform-linux_i686**:
- **Repository**: https://github.com/platformio/platform-linux_i686
- **platform.py**: https://raw.githubusercontent.com/platformio/platform-linux_i686/develop/platform.py
- **Key Findings**:
  - Similar pattern to linux_arm: removes 32-bit toolchain on native 32-bit Linux
  - Conditional package filtering in `packages` property
  - Defensive programming (checks package existence before deletion)
- **Referenced In**: Round 1 Initial Assessment, Platform Class Analysis

#### PlatformIO Core Research

**PlatformIO Core Releases**:
- **Repository**: https://github.com/platformio/platformio-core
- **Latest Release**: v6.1.18 (March 11, 2025)
- **Release Page**: https://github.com/platformio/platformio-core/releases
- **Key Findings**:
  - PIO Core 6.0+ is fully backward compatible with 5.0 projects
  - No breaking changes in 6.x series (6.0 → 6.1.18)
  - Unified package management (no more global packages)
  - Cross-platform virtual symlinks
- **Last Checked**: 2025-11-09

**PlatformIO Documentation** (attempted access, returned 403):
- Platform Creation Guide: https://docs.platformio.org/en/latest/platforms/creating_platform.html
- Platform JSON Schema: https://docs.platformio.org/en/latest/manifests/platform-json.html
- Migration Guide 5.x → 6.0: https://docs.platformio.org/en/latest/core/migration.html
- Build Scripts API: https://docs.platformio.org/en/latest/scripting/index.html

**PlatformIO Core Source Code**:
- **public.py**: https://github.com/platformio/platformio-core/blob/develop/platformio/public.py
  - Exports PlatformBase from platformio.platform.base
  - Public API for platform developers

#### WiringPi and GPIO Alternatives

**WiringPi Status**:
- **Original WiringPi**: http://wiringpi.com (defunct, deprecated August 2019)
- **Relevance**: Single framework supported by platform-linux_arm
- **Deprecation**: Gordon Henderson discontinued project in 2019
- **Community Fork**: GC2 took over maintenance in 2024, supporting new OS and hardware
- **Key Findings**:
  - Official WiringPi is deprecated and unmaintained
  - Community fork exists but not official/guaranteed long-term
  - Modern alternatives recommended for new projects
- **Last Checked**: 2025-11-09

**Modern GPIO Alternatives**:
1. **pigpio**:
   - Website: https://abyz.me.uk/rpi/pigpio/
   - Status: Actively maintained, powerful daemon-based approach
   - Use case: Advanced GPIO with precise timing

2. **lgpio** (libgpiod successor):
   - Transformation from pigpio codebase
   - Works with Raspberry Pi 5
   - Modern kernel-based GPIO access

3. **gpiozero**:
   - Official Raspberry Pi Foundation recommendation for beginners
   - Simple wrapper library
   - Well-documented

4. **RPi.GPIO**:
   - Most popular, first GPIO library
   - Extensive examples available
   - May not support latest hardware

**Community Discussion Sources**:
- Raspberry Pi Forums: WiringPi replacement discussions
- Stack Exchange: GPIO library comparisons
- GitHub: WiringPi alternatives and forks

**Detailed Technical Analysis (sfo2001)**:
- **WiringPi vs libgpiod Analysis**: https://github.com/sfo2001/esphome/blob/feature/linux-platform/docs/linux-platform/notes/wiringpi-analysis.md
- **Relevance**: In-depth comparison of WiringPi V3 vs libgpiod for Linux platform GPIO support
- **Key Conclusions**:
  - Recommends against WiringPi adoption due to Raspberry Pi-only support and architectural conflicts
  - Strongly favors enhanced libgpiod implementation using native Linux kernel interfaces
  - Identifies GPIO interrupt support as primary missing feature (not in current libgpiod wrapper)
  - Proposes using chardev, i2c-dev, spidev kernel APIs for platform independence
- **Main Differences**:
  - WiringPi: RPi-only, full interrupt/PWM support, additional dependency
  - libgpiod: Any Linux system, modern kernel APIs, minimal dependencies
- **Implementation Approach**: Three-phase enhancement (1) Add libgpiod interrupt support, (2) Optional PWM, (3) Documentation/testing
- **Referenced In**: Round 1 Initial Assessment - Framework alternatives research
- **Priority Relevance**: Critical for Round 2 Priority #2 (Framework Ecosystem Modernization)
- **Last Checked**: 2025-11-09

#### Local Repository Analysis

**platform-linux_arm** (this repository):
- **platform.json**: Lines 1-42
  - Version: 1.6.0
  - Declares PIO Core ^6 compatibility
  - 1 framework (WiringPi), 2 packages

- **platform.py**: Lines 1-41
  - ~40 lines total
  - Imports from platformio.public (modern style)
  - _is_native() method: Detects linux_arm/linux_aarch64
  - packages property: Removes toolchain on native ARM
  - configure_default_packages(): Blocks WiringPi cross-compilation

- **builder/main.py**: Lines 1-63
  - Simple SCons build script
  - Lines 39-42: macOS x86_64 cross-compilation only
  - No Windows, Linux x86_64, macOS ARM support

- **builder/frameworks/wiringpi.py**: Lines 1-67
  - WiringPi framework integration
  - Compiler flags, pthread linking
  - Builds WiringPi library from package

- **boards/**: 4 board definitions
  - raspberrypi_1b.json, raspberrypi_2b.json, raspberrypi_3b.json, raspberrypi_zero.json
  - Missing: RPi 4, 5, 400, CM variants, Zero 2 W

- **examples/**: 2 example projects
  - wiringpi-blink, wiringpi-serial
  - No automated testing

**Git History Analysis**:
- **Commit 87daebb** (May 27, 2022): "Add compatibility with PIO Core 6.0"
  - Changed platform.json: ^5 → ^6
  - Updated imports: platformio.managers.platform → platformio.public
  - Modernized super() call
  - Author: Ivan Kravets (PlatformIO maintainer)
- **Commit a5f75bd** (recent): "refined research approach"
- **Commit dfa0489** (recent): "Added CLAUDE.md and analysis prompt"

### Round 2: Priority Deep-Dive
*(References to be added during Round 2)*

### Round 3: Implementation Roadmap
*(References to be added during Round 3)*

---

**Maintenance Notes**:
- Keep this document updated as new sources are discovered
- Include specific commit SHAs or permanent links (not branch names)
- Date all entries for temporal context
- Remove or mark obsolete references
