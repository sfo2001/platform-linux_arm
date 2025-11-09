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

**Date**: 2025-11-09
**Status**: ✅ Complete
**Documents**: 02-priority-cross-compilation.md, 02-priority-frameworks.md, 02-priority-boards.md, 02-priority-ci-cd.md

#### Priority 1: Cross-Compilation Toolchains

**PlatformIO Core - get_systype()**:
- **Function**: https://github.com/platformio/platformio-core/blob/develop/platformio/util.py
- **Key Findings**: System type detection logic, possible return values (darwin_x86_64, linux_x86_64, windows_amd64, etc.)
- **Referenced In**: 02-priority-cross-compilation.md

**PlatformIO Package Issues**:
- **GitHub Issue #2**: https://github.com/platformio/platform-linux_arm/issues/2
  - Title: "The package 'toolchain-gccarmlinuxgnueabi' is not available"
  - Confirmed: Windows not supported
- **GitHub Issue #578**: https://github.com/platformio/platformio-core/issues/578
  - Title: Package not available for linux_x86_64
- **Package Registry**: https://registry.platformio.org/tools/platformio/toolchain-gccarmlinuxgnueabi
  - Only supports: macOS, Linux ARM (native)

**ARM GNU Toolchains**:
- **ARM Developer Downloads**: https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads
  - Official toolchain downloads for all platforms
- **Ubuntu ARM Cross-Compilation Guide**: https://jensd.be/1126/linux/cross-compiling-for-arm-or-aarch64-on-debian-or-ubuntu
  - gcc-arm-linux-gnueabihf and gcc-aarch64-linux-gnu installation
- **Homebrew arm-linux-gnueabihf-binutils**: https://formulae.brew.sh/formula/arm-linux-gnueabihf-binutils
  - macOS toolchain (binutils only, not full GCC)
- **messense/homebrew-macos-cross-toolchains**: https://github.com/messense/homebrew-macos-cross-toolchains
  - Community full ARM toolchains for macOS (Intel and Apple Silicon)

**ARM Architecture Documentation**:
- **ARM Toolchain Comparison (StackOverflow)**: https://stackoverflow.com/questions/73686292/which-version-of-arm-gnu-toolchain-should-i-use-to-run-on-rpi-4b
  - Explains arm-linux-gnueabihf (32-bit) vs aarch64-linux-gnu (64-bit)
- **Raspberry Pi Processors**: https://www.raspberrypi.com/documentation/computers/processors.html
  - BCM2711, BCM2712 specifications and capabilities
- **ARMv7 vs ARMv8 Discussion**: https://raspberrypi.stackexchange.com/questions/101215/
  - Why Pi 4 reports armv7l when running 32-bit OS on ARMv8 hardware

**Reference Platforms**:
- **platform-ststm32 builder/main.py**: https://github.com/platformio/platform-ststm32/blob/master/builder/main.py
  - Cross-compilation patterns for ARM embedded (arm-none-eabi prefix)

#### Priority 2: Framework Ecosystem (GPIO Libraries)

**lgpio (Modern GPIO Library)**:
- **Repository**: https://github.com/joan2937/lg
- **Documentation**: http://abyz.me.uk/lg/index.html
- **Key Findings**:
  - Modern successor to pigpio by same author (Joan)
  - Works on all Raspberry Pi models including Pi 5
  - Uses /dev/gpiochip kernel interface (not direct register access)
  - ~523k GPIO toggles/sec (slower than pigpio but Pi 5 compatible)
  - Unlicense (public domain)
- **Installation**: `sudo apt install liblgpio-dev liblgpio1`
- **Referenced In**: 02-priority-frameworks.md

**pigpio (High-Performance GPIO)**:
- **Repository**: https://github.com/joan2937/pigpio
- **Documentation**: http://abyz.me.uk/rpi/pigpio/
- **C API Reference**: https://abyz.me.uk/rpi/pigpio/cif.html
- **Examples**: https://abyz.me.uk/rpi/pigpio/examples.html
- **Key Findings**:
  - Very fast (~7.9M toggles/sec) via direct register access
  - Hardware-timed PWM, high-speed sampling (1M samples/sec)
  - NOT compatible with Raspberry Pi 5 (RP1 I/O controller incompatible)
  - Works on Pi 1-4, Zero, Zero 2 W
  - Requires root/sudo
  - Unlicense (public domain)
- **Installation**: `sudo apt install libpigpio-dev pigpio`
- **Compilation**: Link with `-lpigpio -lrt -lpthread`
- **Debian Package**: https://tracker.debian.org/pkg/pigpio
- **StackOverflow Compilation Guide**: https://stackoverflow.com/questions/69759904/
- **Future Status**: https://raspberrypi.stackexchange.com/questions/145553/future-of-pigpio-library-alive-or-dead
- **Referenced In**: 02-priority-frameworks.md

**WiringPi (GC2 Community Fork)**:
- **Repository**: https://github.com/WiringPi/WiringPi
- **Original**: http://wiringpi.com (deprecated 2019, defunct)
- **Key Findings**:
  - GC2 (Grazer Computer Club) took over maintenance in 2024
  - Supports Raspberry Pi 5 (except GCLK function)
  - Arduino-like API (pinMode, digitalWrite, etc.)
  - Very fast (~7.9M toggles/sec)
  - LGPL v3
- **Installation**: `sudo apt install wiringpi`
- **Referenced In**: 02-priority-frameworks.md, Round 1

**libgpiod (Kernel-Standard)**:
- **Repository**: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git
- **Debian Package**: https://packages.debian.org/unstable/libgpiod-dev
- **Ubuntu Package**: https://launchpad.net/ubuntu/+source/libgpiod
- **Key Findings**:
  - Official Linux kernel GPIO library
  - Platform-independent (works on any Linux GPIO system)
  - Raspberry Pi OS Bookworm has old v1.6 (poor docs, no examples)
  - v2.x is modern but not yet in Pi OS repos
  - LGPL v2.1+
- **Installation**: `sudo apt install libgpiod-dev gpiod`
- **Raspberry Pi Forum Discussion**: https://forums.raspberrypi.com/viewtopic.php?t=366693
- **Pi 5 Support**: https://raspberrypi.stackexchange.com/questions/145295/
- **Referenced In**: 02-priority-frameworks.md

**GPIO Library Comparisons**:
- **Performance Benchmarks (Xojo Forum)**: https://forum.xojo.com/t/libgpiod-vs-pigpiod-vs-wiringpi/59853
  - WiringPi: 7.9M toggles/sec
  - pigpio: 7.9M toggles/sec
  - lgpio: 523k toggles/sec
  - RPi.GPIO: 801k toggles/sec
- **Current Best Practices (2024)**: https://raspberrypi.stackexchange.com/questions/147465/current-proper-way-to-interface-gpio-from-c-code
- **Raspberry Pi GPIO White Paper**: https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices
  - Official Raspberry Pi Foundation guidance on GPIO libraries
- **Future of GPIO on Pi 5**: https://raspberrypi.stackexchange.com/questions/145013/future-of-gpio-access-on-pi5

**Framework Builder Reference**:
- **platform-espressif32 arduino.py**: https://github.com/platformio/platform-espressif32/blob/master/builder/frameworks/arduino.py
  - Reusable patterns for framework builder scripts

#### Priority 3: Modern Board Support (Hardware Specifications)

**Official Raspberry Pi Documentation**:
- **Raspberry Pi 4 Datasheet**: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf
  - BCM2711 specifications, GPIO, March 2024 release
- **Raspberry Pi 4 Specifications**: https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/
  - 1/2/4/8GB variants, Cortex-A72 @ 1.5GHz
- **Raspberry Pi 5 Specifications**: https://www.raspberrypi.com/products/raspberry-pi-5/specifications/
  - BCM2712 (Cortex-A76 @ 2.4GHz), 2/4/8/16GB variants, RP1 I/O controller
- **Raspberry Pi 400 Specifications**: https://www.raspberrypi.com/products/raspberry-pi-400/specifications/
  - BCM2711C0 @ 1.8GHz (higher than Pi 4), 4GB RAM, keyboard form factor
- **Compute Module 4 Product Brief**: https://datasheets.raspberrypi.com/cm4/cm4-product-brief.pdf
  - 1/2/4/8GB variants, 100-pin connectors, industrial specs
- **Raspberry Pi Zero 2 W Product Brief**: https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf
  - RP3A0 SiP (BCM2710A1), Cortex-A53 @ 1GHz, 512MB
- **Raspberry Pi Processors Documentation**: https://www.raspberrypi.com/documentation/computers/processors.html
  - Comprehensive BCM SoC technical details

**Technical Analyses**:
- **RP3A0 Teardown (Jeff Geerling)**: https://www.jeffgeerling.com/blog/2021/look-inside-raspberry-pi-zero-2-w-and-rp3a0-au
  - Internal analysis of Zero 2 W processor packaging
- **Pi 4 C0 Stepping (Jeff Geerling)**: https://www.jeffgeerling.com/blog/2021/raspberry-pi-4-model-bs-arriving-newer-c0-stepping
  - BCM2711C0 improvements, higher clock speed (1.8GHz)
- **Raspberry Pi 400 Announcement**: https://www.cnx-software.com/2020/11/02/raspberry-pi-400-keyboard-computer-features-1-8-ghz-bcm2711c0-processor/
  - C0 stepping, clock speed differences vs Pi 4
- **BCM2711 vs BCM2712**: https://www.cpu-monkey.com/en/cpu-raspberry_pi_4_b_broadcom_bcm2711
  - CPU benchmarks and specifications comparison

**Community Resources**:
- **Understanding CPU Architectures**: https://forums.raspberrypi.com/viewtopic.php?t=355555
  - ARMv7 vs ARMv8, 32-bit vs 64-bit OS
- **Raspberry Pi 5 Announcement**: https://dataconomy.com/2023/09/28/pi5-raspberry-pi-5-specs-bcm2712/
  - BCM2712 details, performance improvements over Pi 4
- **Compute Module 4 Specs**: https://magazine.raspberrypi.com/articles/raspberry-pi-compute-module-4-specs-benchmarks-testing
  - MagPi magazine analysis

#### Priority 4: CI/CD Infrastructure

**GitHub Actions & PlatformIO**:
- **platform-espressif32 examples.yml**: https://github.com/platformio/platform-espressif32/blob/master/.github/workflows/examples.yml
  - Complete workflow: 17 examples × 3 OS = 51 test combinations
  - Symlink installation pattern, fail-fast: false strategy
- **PlatformIO GitHub Actions Documentation**: https://docs.platformio.org/en/stable/integration/ci/github-actions.html
  - Official CI/CD integration guide
  - Matrix build examples
- **GitHub Actions Documentation**: https://docs.github.com/en/actions
  - Workflow syntax, matrix strategies, triggers
- **actions/checkout**: https://github.com/actions/checkout
  - Repository checkout action (v4)
- **actions/setup-python**: https://github.com/actions/setup-python
  - Python installation action (v5)

**ARM Cross-Compilation in CI**:
- **ARM Cross-Compiler Install Guide**: https://learn.arm.com/install-guides/gcc/cross/
  - Official ARM GNU Toolchain installation across platforms
- **Ubuntu ARM Cross-Compilation (Ask Ubuntu)**: https://askubuntu.com/questions/250696/how-to-cross-compile-for-arm
  - gcc-arm-linux-gnueabihf installation and usage
- **GitHub Actions ARM Example**: https://www.rohanjain.in/cargo-cross/
  - Cross-compilation patterns in CI (Rust example, but concepts apply)
- **messense/homebrew-macos-cross-toolchains**: https://github.com/messense/homebrew-macos-cross-toolchains
  - macOS ARM cross-compiler tap for CI

**Quality Tools**:
- **pre-commit Framework**: https://pre-commit.com/
  - Automated code quality hooks
- **black (Python Formatter)**: https://github.com/psf/black
  - Python code formatter for platform.py
- **flake8 (Python Linter)**: https://github.com/PyCQA/flake8
  - Python linter for code quality
- **softprops/action-gh-release**: https://github.com/softprops/action-gh-release
  - GitHub Release automation action

### Round 3: Implementation Roadmap
*(References to be added during Round 3)*

---

**Maintenance Notes**:
- Keep this document updated as new sources are discovered
- Include specific commit SHAs or permanent links (not branch names)
- Date all entries for temporal context
- Remove or mark obsolete references
