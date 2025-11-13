# Round 2: Priority Area Deep-Dive - Platform Linux ARM Modernization

**Status**: ✅ READY - Round 1 complete, priorities identified
**Prerequisites**: Read `01-initial-assessment.md` and `REFERENCES.md`
**Estimated Time**: 3-4 hours total (or split into two 2-hour sessions)

---

## Objective

Conduct **detailed technical analysis** of the top 4 priority areas identified in Round 1 to:
1. Extract concrete implementation patterns from reference platforms
2. Design specific technical solutions for each priority
3. Provide detailed effort estimates and implementation guidance
4. Identify dependencies and potential blockers

**Scope**: Deep technical analysis with code patterns and specific recommendations
**Approach**: Extract reusable patterns, propose concrete solutions, estimate effort
**Output**: Four separate analysis documents (one per priority area)

---

## Context from Round 1

**Top 4 Priorities** (in implementation order):

1. **Cross-Compilation Fixes** (S effort, High impact)
   - Current: Only macOS x86_64 supported
   - Target: Windows, Linux x86_64, macOS ARM support
   - Blocker severity: 🔴 Critical

2. **Framework Ecosystem Modernization** (M effort, High impact)
   - Current: WiringPi only (deprecated 2019)
   - Target: pigpio, lgpio, bare-metal options
   - Blocker severity: 🔴 Critical

3. **Modern Board Support** (S effort, Medium impact)
   - Current: RPi 3 and older (2016-)
   - Target: RPi 4, 5, 400, CM variants, Zero 2 W
   - Blocker severity: 🟡 High

4. **CI/CD Infrastructure** (S-M effort, High impact)
   - Current: Zero testing/automation
   - Target: GitHub Actions example testing
   - Blocker severity: 🔴 Critical
   - Dependency: Requires cross-compilation fixes first

---

## Priority 1: Cross-Compilation Fixes

### Objective
Enable cross-compilation from Windows, Linux x86_64, and macOS ARM hosts to ARM Linux targets.

### Research Questions

#### 1.1 Toolchain Identification (30-40 min)

**Research ARM cross-compilation toolchains for each host platform:**

1. **Linux x86_64 hosts:**
   - What are the standard ARM cross-toolchain packages?
   - Package names: `gcc-arm-linux-gnueabihf`, `gcc-aarch64-linux-gnu`?
   - Installation: `apt install` on Ubuntu/Debian, `yum/dnf` on RHEL/Fedora?
   - Which architectures: armv7 (32-bit), aarch64 (64-bit), or both?

2. **Windows hosts:**
   - ARM toolchain options: ARM GNU Toolchain direct download? MSYS2? WSL?
   - Package managers: Chocolatey? Scoop? Manual installation?
   - Executable naming: `arm-linux-gnueabihf-gcc.exe`?
   - PATH considerations?

3. **macOS ARM (Apple Silicon):**
   - Homebrew package: `brew install arm-linux-gnueabihf-binutils`?
   - Same toolchain as macOS x86_64 or different?
   - Rosetta 2 considerations?

4. **PlatformIO package options:**
   - Can PlatformIO provide cross-toolchain packages?
   - Check if `toolchain-gccarmlinuxgnueabi` works on all platforms?
   - Need platform-specific toolchain packages?

**Deliverable**: Table of toolchain packages per host OS

#### 1.2 Reference Platform Analysis (20-30 min)

**Analyze how other platforms handle multi-OS cross-compilation:**

1. **platform-ststm32** (STM32 platform, likely has cross-compile):
   - Fetch `builder/main.py` from https://github.com/platformio/platform-ststm32
   - How does it detect host OS and set toolchain prefix?
   - Multiple architecture support (Cortex-M0/M3/M4/M7)?

2. **platform-linux_i686** (similar to linux_arm):
   - Fetch `builder/main.py` from https://github.com/platformio/platform-linux_i686
   - How does it handle 32-bit cross-compilation?
   - Any Windows/macOS patterns?

3. **PlatformIO SCons API:**
   - How to get current host system type reliably?
   - `get_systype()` options: Full list of possible values?
   - Environment variables: `PLATFORM`, `OS`?

**Deliverable**: Code patterns for host OS detection and toolchain configuration

#### 1.3 Technical Design (20-30 min)

**Design the builder/main.py enhancement:**

1. **System type detection logic:**
   - List all `get_systype()` values to handle
   - Windows variants: `windows_x86`, `windows_amd64`?
   - Linux variants: `linux_i686`, `linux_x86_64`, `linux_armv7l`, `linux_aarch64`
   - macOS variants: `darwin_x86_64`, `darwin_arm64`

2. **Toolchain prefix mapping:**
   - For each host OS, what should `_BINPREFIX` be?
   - armv7 (32-bit ARM): `arm-linux-gnueabihf-`
   - aarch64 (64-bit ARM): `aarch64-linux-gnu-`
   - Native ARM: Empty prefix (use system GCC)

3. **Multi-architecture support:**
   - Should platform support both armv7 and aarch64 targets?
   - How to select toolchain based on board MCU type?
   - BCM2837 (RPi 3) = armv7, BCM2711 (RPi 4) = aarch64?

4. **Error handling:**
   - What if toolchain is not installed?
   - Helpful error messages with installation instructions?
   - Detect missing cross-compiler and guide user?

**Deliverable**: Pseudocode or actual Python code for enhanced builder/main.py

#### 1.4 Testing Strategy (15-20 min)

**Plan how to validate cross-compilation on all platforms:**

1. **Test matrix:**
   - Which OS × board combinations to test?
   - Minimum: Ubuntu x86_64 × RPi 3, Windows × RPi 3, macOS ARM × RPi 3?

2. **Validation approach:**
   - Build one of the examples (wiringpi-blink)?
   - Check binary exists and is ARM architecture (`file` command)?
   - Optionally: Deploy and run on actual hardware?

3. **CI/CD integration:**
   - Can GitHub Actions test this (Priority 4)?
   - Matrix strategy: `os: [ubuntu-latest, windows-latest, macos-latest]`?

**Deliverable**: Test plan for cross-compilation validation

### Deliverable Document

Create `02-priority-cross-compilation.md` with:

**Executive Summary**:
- Current state (macOS x86_64 only)
- Proposed solution (multi-OS support)
- Effort estimate (refined from Round 1's "S")
- Dependencies (toolchain packages)

**Toolchain Analysis**:
- Table: Host OS → Toolchain Package → Installation Method → Binary Prefix
- Example: `Linux x86_64 → gcc-arm-linux-gnueabihf → apt install → arm-linux-gnueabihf-`

**Code Patterns from Reference Platforms**:
- How ststm32/linux_i686 handle this
- Reusable detection logic

**Proposed Implementation**:
- Enhanced builder/main.py code (full implementation or pseudocode)
- System type detection logic
- Toolchain prefix mapping
- Error handling and user guidance

**Testing Plan**:
- Test matrix
- Validation steps
- CI/CD integration approach

**Effort Estimate**:
- Development time: X hours
- Testing time: Y hours
- Documentation time: Z hours
- Total: S/M/L (refined from Round 1)

**Dependencies and Risks**:
- Toolchain package availability
- PlatformIO package compatibility
- Windows-specific challenges (PATH, .exe handling)

---

## Priority 2: Framework Ecosystem Modernization

### Objective
Add modern GPIO frameworks (pigpio, lgpio) and bare-metal option to replace deprecated WiringPi.

### Research Questions

#### 2.1 GPIO Framework Survey (40-50 min)

**Research modern GPIO libraries for Raspberry Pi:**

1. **pigpio** (Joan's daemon-based library):
   - Website: https://abyz.me.uk/rpi/pigpio/
   - Current status: Maintained? Last release date?
   - Features: GPIO, PWM, servo, I2C, SPI, interrupts
   - API: C library, Python wrapper, socket interface
   - Packaging: How to get pigpio? System package (`apt install pigpio`)? Build from source?
   - Cross-compilation: Can pigpio be cross-compiled? Dependencies?
   - License: Compatible with PlatformIO usage?

2. **lgpio** (pigpio successor for kernel 5.11+):
   - Relation to pigpio: Transformation of pigpio codebase
   - Website/repo: Where to find lgpio source?
   - Raspberry Pi 5 support: Required for RPi 5 GPIO access?
   - API differences from pigpio: Breaking changes?
   - Packaging: Available as system package? PIO registry?

3. **gpiozero** (Raspberry Pi Foundation official beginner library):
   - Website: https://gpiozero.readthedocs.io/
   - Python-only or C API available?
   - Suitability for C/C++ projects: Not applicable?
   - Skip for PlatformIO platform (Python-focused)?

4. **RPi.GPIO** (most popular, but older):
   - Python-only library, skip for C/C++ platform

5. **libgpiod** (kernel-based, platform-independent):
   - Check sfo2001 analysis: https://github.com/sfo2001/esphome/blob/feature/linux-platform/docs/linux-platform/notes/wiringpi-analysis.md
   - Advantages: Works on any Linux system (not just RPi), modern kernel interface
   - Disadvantages: Limited interrupt support (mentioned in analysis)
   - Suitability for platform-linux_arm: Better than WiringPi for cross-platform?

**Deliverable**: Comparison table of GPIO libraries (features, maintenance, packaging, suitability)

#### 2.2 Framework Packaging Strategy (30-40 min)

**Determine how to package frameworks for PlatformIO:**

1. **PlatformIO Registry approach:**
   - Can we publish `framework-pigpio`, `framework-lgpio` to PlatformIO registry?
   - Registry submission process: https://docs.platformio.org/en/latest/registry/index.html
   - Package structure requirements?
   - Maintenance burden: Who will maintain packages?

2. **System dependency approach:**
   - Alternative: Document that users must `apt install pigpio` on target?
   - Builder script checks for system library: `pkg-config --exists pigpio`?
   - Pros: Less maintenance, users get latest versions
   - Cons: Cross-compilation complexity (need libs for ARM on x86_64 host)

3. **Hybrid approach:**
   - Provide pre-built PIO packages for convenience
   - Document system package alternative
   - Let users choose based on their workflow

4. **WiringPi community fork:**
   - Research GC2's WiringPi-NG: https://github.com/WiringPi/WiringPi
   - Status: Activity level, releases, issues?
   - Should we update framework-wiringpi to use community fork?
   - Or deprecate WiringPi entirely in favor of modern alternatives?

**Deliverable**: Recommended packaging strategy per framework

#### 2.3 Framework Builder Scripts (30-40 min)

**Design builder/frameworks/ scripts for each framework:**

1. **Bare-metal framework** (framework-less):
   - Create `builder/frameworks/baremetal.py` or just omit framework?
   - What does "no framework" mean: Just GCC + libc, no GPIO lib?
   - Compiler flags: Minimal set for generic ARM Linux apps
   - Use cases: Servers, data processing, non-GPIO utilities

2. **pigpio framework:**
   - Create `builder/frameworks/pigpio.py`
   - Based on wiringpi.py pattern
   - Include paths: Where is `pigpio.h`?
   - Libraries to link: `-lpigpio -lpthread -lrt`?
   - Build pigpio from source or use system library?

3. **lgpio framework:**
   - Create `builder/frameworks/lgpio.py`
   - Similar to pigpio pattern
   - Include paths and link flags
   - Conditional: Only for kernel 5.11+ (RPi 5)?

4. **Reference pattern analysis:**
   - Study platform-espressif32 `builder/frameworks/arduino.py` and `espidf.py`
   - How do they handle framework paths, libraries, build flags?
   - Extract reusable patterns

**Deliverable**: Pseudocode or actual Python for each framework builder script

#### 2.4 Example Projects (20-30 min)

**Plan example projects for each framework:**

1. **examples/pigpio-blink/**:
   - Port wiringpi-blink to pigpio API
   - Show basic GPIO setup and control

2. **examples/lgpio-blink/**:
   - Port to lgpio API (if different from pigpio)

3. **examples/baremetal-hello/**:
   - Simple C program: `printf("Hello from ARM Linux\n");`
   - No GPIO, just validates cross-compilation

4. **Migration guide:**
   - Document how to migrate from WiringPi to pigpio/lgpio
   - API mapping: `digitalWrite()` → `gpio_write()`
   - Pin numbering differences

**Deliverable**: Example project structure and code snippets

### Deliverable Document

Create `02-priority-frameworks.md` with:

**Executive Summary**:
- WiringPi deprecation context
- Proposed frameworks: pigpio, lgpio, bare-metal
- Recommended approach

**GPIO Framework Comparison**:
- Table: Framework × Features × Status × Packaging × Suitability
- Detailed analysis per framework

**Packaging Strategy**:
- Recommended approach (PIO registry vs system deps)
- Trade-offs and rationale

**Framework Builder Scripts**:
- Code patterns from reference platforms
- Proposed pigpio.py, lgpio.py, baremetal.py implementations
- Include paths, link flags, build configuration

**Example Projects**:
- Project structure per framework
- Code snippets (minimal blink example)
- Migration guide from WiringPi

**Effort Estimate**:
- Per framework: Development + packaging + testing + documentation
- Total: M effort (refined from Round 1)

**Dependencies and Risks**:
- Framework availability and licensing
- Cross-compilation challenges (ARM libraries on x86_64)
- Raspberry Pi 5 kernel requirements for lgpio

---

## Priority 3: Modern Board Support

### Objective
Add board definitions for Raspberry Pi 4, 5, 400, Compute Modules, and Zero 2 W.

### Research Questions

#### 3.1 Raspberry Pi Hardware Specifications (30-40 min)

**Research BCM SoC types and hardware specs for each board:**

1. **Raspberry Pi 4 Model B** (2019, most popular current board):
   - SoC: BCM2711 (Cortex-A72, quad-core, ARMv8-A 64-bit)
   - CPU frequency: 1.5 GHz (1500000000L)
   - RAM variants: 1GB, 2GB, 4GB, 8GB
   - Architecture: aarch64 (64-bit) or armv7l (32-bit OS option)
   - GPIO: 40-pin header, compatible with earlier models
   - Defines: `-DRASPBERRYPI -DRASPBERRYPI4`

2. **Raspberry Pi 5** (2023, latest flagship):
   - SoC: BCM2712 (Cortex-A76, quad-core, ARMv8.2-A 64-bit)
   - CPU frequency: 2.4 GHz (2400000000L)
   - RAM variants: 4GB, 8GB
   - Architecture: aarch64 only
   - GPIO: 40-pin header, RP1 I/O controller (new)
   - Kernel requirements: 6.1+ for GPIO (affects lgpio framework)
   - Defines: `-DRASPBERRYPI -DRASPBERRYPI5`

3. **Raspberry Pi 400** (2020, keyboard computer):
   - SoC: BCM2711 (same as RPi 4)
   - CPU frequency: 1.8 GHz (1800000000L) - slightly faster than RPi 4
   - RAM: 4GB only
   - GPIO: 40-pin header (same as RPi 4)
   - Defines: `-DRASPBERRYPI -DRASPBERRYPI400`

4. **Compute Module 4** (2020, industrial/embedded):
   - SoC: BCM2711 (same as RPi 4)
   - CPU frequency: 1.5 GHz
   - RAM variants: 1GB, 2GB, 4GB, 8GB
   - Storage: eMMC variants or Lite (no eMMC)
   - Form factor: SO-DIMM, no standard GPIO header (custom carrier boards)
   - Defines: `-DRASPBERRYPI -DRASPBERRYPI_CM4`

5. **Raspberry Pi Zero 2 W** (2021):
   - SoC: RP3A0 (BCM2837 quad-core variant, same as RPi 3)
   - CPU frequency: 1 GHz (1000000000L)
   - RAM: 512MB
   - Architecture: armv7l (32-bit), though capable of 64-bit
   - GPIO: 40-pin header (unpopulated)
   - Defines: `-DRASPBERRYPI -DRASPBERRYPI_ZERO2W`

**Sources:**
- Raspberry Pi official documentation: https://www.raspberrypi.com/documentation/computers/
- Raspberry Pi Wikipedia: Hardware specifications tables
- BCM SoC datasheets (if available)

**Deliverable**: Specifications table for each new board

#### 3.2 Board Definition Pattern Analysis (20-30 min)

**Analyze existing board definitions and create template:**

1. **Current boards pattern:**
   - Review `boards/raspberrypi_3b.json` structure
   - Required fields: `build`, `frameworks`, `name`, `upload`, `url`, `vendor`
   - Optional fields: `debug`, `upload.protocols`?

2. **platform-raspberrypi board examples:**
   - Fetch a few board JSON files from platform-raspberrypi
   - Compare structure and fields
   - Any additional fields used (debug config, upload methods)?

3. **Template creation:**
   - Create standard template for new RPi boards
   - Placeholders for: MCU, CPU freq, RAM, defines, name

**Deliverable**: Board definition template and field documentation

#### 3.3 Architecture Considerations (15-20 min)

**Determine 32-bit vs 64-bit support:**

1. **ARMv7 vs AArch64:**
   - RPi 4, 5: Support both 32-bit and 64-bit OS
   - Default: Raspberry Pi OS 64-bit recommended for RPi 4/5
   - Should boards support both architectures or pick one?

2. **Toolchain implications:**
   - armv7: `arm-linux-gnueabihf-gcc` (32-bit)
   - aarch64: `aarch64-linux-gnu-gcc` (64-bit)
   - Need both toolchains in platform.json?
   - Or board-specific toolchain selection?

3. **Framework compatibility:**
   - Do GPIO frameworks work on both architectures?
   - RPi 5: Requires 64-bit OS and kernel 6.1+ (lgpio)

**Deliverable**: Architecture strategy recommendation

#### 3.4 Non-Raspberry Pi Boards (Optional, 15-20 min)

**Research potential for other ARM Linux SBCs:**

1. **BeagleBone Black/Green:**
   - SoC: AM335x (Cortex-A8, ARMv7)
   - GPIO library: libgpiod, bone-gpio?
   - Worth adding? Demand level?

2. **ODROID-C2/C4/N2:**
   - SoCs: Amlogic S905/S905X/S922X (Cortex-A53/A73)
   - GPIO: WiringPi port, libgpiod
   - User base?

3. **Orange Pi, Rock Pi, Pine64:**
   - Various SoCs (Allwinner, Rockchip, etc.)
   - GPIO support varies
   - Complexity vs value?

**Decision**: Focus on Raspberry Pi for initial modernization, consider others later?

**Deliverable**: Assessment of non-RPi board support (defer or include?)

### Deliverable Document

Create `02-priority-boards.md` with:

**Executive Summary**:
- Current board coverage (RPi 1-3, Zero 1)
- Missing boards (RPi 4, 5, 400, CM4, Zero 2 W)
- Proposed additions

**Board Specifications**:
- Table: Board × SoC × CPU Freq × RAM × Architecture × GPIO
- Detailed specs per board

**Board Definition Template**:
- Standard JSON structure
- Field documentation
- Example: raspberrypi_4b.json (complete file)

**Architecture Strategy**:
- 32-bit vs 64-bit decision
- Toolchain implications
- Recommendation per board

**Implementation Plan**:
- Board creation order (priority: RPi 4 first)
- Testing approach
- Documentation updates

**Non-Raspberry Pi Boards**:
- Assessment of BeagleBone, ODROID, etc.
- Recommendation: Include now or defer?

**Effort Estimate**:
- Time per board (S effort)
- Total for all RPi boards
- Testing time

**Dependencies**:
- Framework compatibility (Priority 2)
- Cross-compilation working (Priority 1)

---

## Priority 4: CI/CD Infrastructure

### Objective
Establish GitHub Actions workflows for automated example testing across platforms.

### Research Questions

#### 4.1 GitHub Actions Best Practices (30-40 min)

**Study reference platform CI/CD implementations:**

1. **platform-espressif32 workflows:**
   - Fetch `.github/workflows/examples.yml`: https://github.com/platformio/platform-espressif32/blob/master/.github/workflows/examples.yml
   - Analyze structure:
     - Trigger conditions (push, pull_request, branches)
     - Matrix strategy (OS × examples)
     - PlatformIO installation method
     - Build commands
     - Artifact handling (if any)
   - Key patterns:
     - `fail-fast: false` (run all tests even if some fail)
     - `pio run -d ${{ matrix.example }}`
     - Install PIO Core from develop branch for latest features

2. **platform-raspberrypi workflows:**
   - Compare with espressif32 approach
   - Any differences in RP2040 testing?

3. **PlatformIO Core CI:**
   - Check https://github.com/platformio/platformio-core/.github/workflows/
   - How does PIO test itself?
   - Reusable patterns?

**Deliverable**: Best practices summary and reusable patterns

#### 4.2 Test Matrix Design (20-30 min)

**Design comprehensive test coverage:**

1. **Operating Systems:**
   - `ubuntu-latest` (Linux x86_64) - primary cross-compile platform
   - `windows-latest` (Windows) - cross-compile validation
   - `macos-latest` (macOS ARM) - Apple Silicon support
   - Skip `macos-13` (x86_64)? Already works per Round 1

2. **Examples to test:**
   - Current: `wiringpi-blink`, `wiringpi-serial`
   - Future: `pigpio-blink`, `lgpio-blink`, `baremetal-hello` (after Priority 2)
   - Start with existing 2 examples, expand as frameworks added

3. **Boards to target:**
   - Current: `raspberrypi_2b`, `raspberrypi_3b`
   - Future: `raspberrypi_4b`, `raspberrypi_5` (after Priority 3)
   - Matrix: OS × Example × Board, or just OS × Example (board auto-selected)?

4. **Matrix strategy:**
   - Total combinations: 3 OS × 2 examples = 6 builds (initial)
   - Expand to: 3 OS × 5 examples × 2 boards = 30 builds (future)
   - Acceptable CI time?

**Deliverable**: Test matrix definition

#### 4.3 Workflow Implementation (30-40 min)

**Design the GitHub Actions workflow file:**

1. **Workflow structure:**
   - Name: "Examples" or "Build Examples"?
   - Triggers: `on: [push, pull_request]`?
   - Branches: All branches or specific (main, develop)?

2. **Job steps:**
   - Checkout code: `actions/checkout@v4`
   - Set up Python: `actions/setup-python@v5` (PIO requires Python)
   - Install PlatformIO: `pip install platformio` or from develop?
   - Install cross-toolchain: OS-specific (apt/brew/choco)
   - Build example: `pio run -d examples/${{ matrix.example }}`
   - Validate binary: Check file exists, correct architecture?

3. **Cross-toolchain installation per OS:**
   - Ubuntu: `sudo apt-get update && sudo apt-get install -y gcc-arm-linux-gnueabihf`
   - macOS: `brew install arm-linux-gnueabihf-binutils` (if package exists)
   - Windows: Chocolatey? Or use MSYS2? Or rely on PIO package?

4. **Dependency on Priority 1:**
   - CI/CD cannot work until cross-compilation is fixed (builder/main.py)
   - Document this dependency
   - Recommend implementing Priority 1 first, then Priority 4

**Deliverable**: Complete workflow YAML file (draft)

#### 4.4 Additional Quality Gates (20-30 min)

**Design additional CI/CD enhancements:**

1. **Pre-commit hooks:**
   - Python linting: `flake8`, `black` for platform.py?
   - JSON validation: Validate board definitions?
   - Commit message format: Conventional commits check?

2. **Release automation:**
   - Automatic versioning: Bump version in platform.json?
   - Changelog generation: From commit messages?
   - GitHub Release creation: On version tags?

3. **Documentation checks:**
   - README sync: Ensure examples listed match examples/ directory?
   - Link validation: Check external URLs?

4. **Coverage reporting:**
   - Not applicable (no unit tests yet)?
   - Future: If Python unit tests added, run coverage?

**Deliverable**: Additional quality gate recommendations

#### 4.5 Documentation for Contributors (15-20 min)

**Plan testing documentation:**

1. **CONTRIBUTING.md:**
   - How to run tests locally before pushing
   - How to add new examples
   - CI/CD expectations (all examples must build)

2. **README updates:**
   - CI/CD badge: ![Build Status](...)
   - Testing status visibility

3. **Testing guide:**
   - How to test on local hardware (RPi)
   - How to validate cross-compilation worked
   - How to debug CI failures

**Deliverable**: Documentation outline

### Deliverable Document

Create `02-priority-ci-cd.md` with:

**Executive Summary**:
- Current state (no CI/CD)
- Proposed solution (GitHub Actions)
- Dependency on Priority 1 (cross-compilation)

**Reference Platform Analysis**:
- espressif32 workflow patterns
- Reusable CI/CD practices

**Test Matrix Design**:
- OS × Examples × Boards
- Initial matrix (6 builds) vs future matrix (30+ builds)

**Workflow Implementation**:
- Complete `.github/workflows/examples.yml` (draft)
- Cross-toolchain installation per OS
- Build validation steps

**Additional Quality Gates**:
- Pre-commit hooks
- Release automation
- Documentation checks

**Documentation Plan**:
- CONTRIBUTING.md outline
- Testing guide structure

**Effort Estimate**:
- Workflow creation: X hours
- Toolchain setup debugging: Y hours
- Documentation: Z hours
- Total: S-M effort (refined from Round 1)

**Dependencies**:
- **CRITICAL**: Requires Priority 1 (cross-compilation) complete first
- Optional: Priority 2 (more examples to test)
- Optional: Priority 3 (more boards to test)

**Implementation Order**:
1. Fix cross-compilation (Priority 1)
2. Create basic workflow (2 examples, 3 OS)
3. Expand as frameworks/boards added

---

## Research Methodology

### Tools and Approach

1. **Web Research:**
   - Use WebSearch and WebFetch to research toolchains, frameworks, hardware specs
   - Read official documentation (Raspberry Pi, PlatformIO, GPIO libraries)
   - Check GitHub repos for reference platforms and frameworks

2. **Code Analysis:**
   - Fetch specific files from reference platforms (platform.py, builder scripts, workflows)
   - Extract patterns and implementations
   - Compare with platform-linux_arm current state

3. **Local Inspection:**
   - Read existing platform-linux_arm files for context
   - Understand current patterns before proposing changes

4. **Synthesis:**
   - Combine research into concrete technical designs
   - Provide code examples, not just descriptions
   - Estimate effort based on complexity analysis

### Quality Checks

Before completing Round 2, verify each deliverable document has:
- ✅ Executive summary with clear recommendations
- ✅ Detailed technical analysis with references
- ✅ Code examples or pseudocode for implementation
- ✅ Refined effort estimates (S/M/L with justification)
- ✅ Dependencies and risks identified
- ✅ All sources added to REFERENCES.md
- ✅ Follows FINDINGS-TEMPLATE.md structure

---

## Output Checklist

When Round 2 is complete, you should have:

- [ ] `02-priority-cross-compilation.md` created
- [ ] `02-priority-frameworks.md` created
- [ ] `02-priority-boards.md` created
- [ ] `02-priority-ci-cd.md` created
- [ ] REFERENCES.md updated with all new sources
- [ ] 00-INDEX.md updated (Round 2 marked complete)
- [ ] Clear, actionable implementation guidance for each priority
- [ ] Ready to proceed to Round 3 (roadmap generation)

---

## Success Criteria

Round 2 is successful if:
- ✅ Each priority has detailed, implementable technical design
- ✅ Code patterns extracted from reference platforms
- ✅ Toolchains, packages, and dependencies identified
- ✅ Effort estimates refined with justification
- ✅ Dependencies and implementation order clear
- ✅ Can proceed directly to implementation or Round 3 roadmap

---

## Getting Started

To execute Round 2:

1. **Start fresh Claude Code session** in repository root
2. **Provide this entire prompt** (02-ROUND-2-PROMPT.md)
3. **Review context** from Round 1 (01-initial-assessment.md, REFERENCES.md)
4. **Execute research** for all 4 priorities
5. **Create deliverable documents** (one per priority)
6. **Update tracking** (REFERENCES.md, 00-INDEX.md)

**Estimated time**: 3-4 hours total
- Can be split into two 2-hour sessions if needed
- Natural breakpoint: After Priority 2, pause and resume for Priorities 3-4

**Next step after Round 2**: Proceed to Round 3 (Implementation Roadmap)
