# Archive Directory

This directory contains internal project artifacts that are not intended for end users but are valuable for project history and transparency.

## Contents

### ~~`research/`~~ → **Moved to GitHub Wiki**
**Modernization research and planning artifacts**

All research documentation has been published to the **GitHub Wiki**:
- **Wiki URL**: https://github.com/sfo2001/platform-linux_arm/wiki

**Wiki Pages**:
- Modernization Overview (master progress tracker)
- Implementation Status (current state)
- Round 1: Initial Assessment
- Round 2: Boards, CI/CD, Cross-compilation, Frameworks analyses
- Round 3: Implementation Roadmap
- Fork Analysis Summary
- References (centralized sources)
- Python Codebase Analysis (security audit)

**Value**: Documents the thought process and decision-making behind platform modernization. Now publicly discoverable via wiki.

---

### `references/`
**Reference documentation from other PlatformIO platforms**

Contains documentation snapshots from reference PlatformIO platforms used during research:

- `espressif8266.md/html` - Espressif8266 platform documentation
- `ststm32.md/html` - STM32 platform documentation
- `raspberrypi.md/html` - Raspberry Pi RP2040 platform documentation
- `creating_platform.md/html` - PlatformIO platform creation guide

**Value**: Research materials showing best practices and structure from established platforms. Helped inform the modernization effort.

**Recommended Action**: Can be deleted after modernization is complete, or kept for historical reference. Original sources are available at docs.platformio.org.

---

### Root Files

- `DOCUMENTATION_PLAN.md` - Internal planning document for documentation reorganization
- `HARDWARE_TESTING.md` - Internal testing methodology and hardware validation notes

---

## Why This Directory Exists

During the transition from "modernized fork with comprehensive internal docs" to "clean PlatformIO-standard platform," we needed to:

1. **Preserve valuable research** - ✅ Published to GitHub Wiki (https://github.com/sfo2001/platform-linux_arm/wiki)
2. **Match PlatformIO standards** - ✅ Reference platforms don't have research directories
3. **Maintain transparency** - ✅ All research publicly accessible via wiki

This `.archive/` directory contains historical reference materials and documentation snapshots.

---

## For Official PlatformIO Submission

If submitting this platform to the official PlatformIO registry:

- ✅ **Research moved to wiki** - Published at https://github.com/sfo2001/platform-linux_arm/wiki
- ✅ **Clean repository structure** - Matches reference platform standards
- **Remaining**: Reference documentation (can be deleted or kept for historical purposes)

The research artifacts provide transparency and decision documentation, now properly organized via the GitHub Wiki.

---

**Created**: 2025-11-13
**Last Updated**: 2025-11-14
**Research Wiki**: https://github.com/sfo2001/platform-linux_arm/wiki
