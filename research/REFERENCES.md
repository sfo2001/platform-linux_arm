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
*(References to be added during Round 1)*

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
