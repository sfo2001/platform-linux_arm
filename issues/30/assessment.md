# Issue #30 Assessment - NXP Pico i.MX7D Board Support

**Issue Number**: #30
**Title**: [#12] NXP Pico i.MX7D board support
**Assessment Date**: 2025-11-09
**Assessor**: Claude (AI Assistant)
**Status**: ⏳ PLANNED (Future Enhancement - Priority 6)

---

## Executive Summary

Issue #30 (originally issue #12 from platformio/platform-linux_arm) requests support for NXP Pico i.MX7D board, a development platform based on NXP's i.MX7 Dual ARM Cortex-A7 processor. This feature request is **not currently implemented** but is **planned for future development** as part of Priority 6: Non-Raspberry Pi ARM Boards.

**Quick Status**:
- **Original Problem**: No board definition for NXP Pico i.MX7D
- **Current Status**: ⏳ **PLANNED** (Priority 6, post-Phase 3)
- **Expected Timeline**: After Raspberry Pi modernization (3-5 days effort for non-Pi boards)
- **Recommendation**: KEEP OPEN - Valid enhancement, future roadmap item

---

## Issue Background

### Original Problem

**Reporter**: Community users (original upstream issue #12)
**Date Reported**: Prior to repository fork
**Environment**:
- Platform: linux_arm (requested addition)
- Board: NXP Pico i.MX7D (not available)
- Request type: Enhancement/feature request

**User Request**:
> "can you add NXP Pico i.MX7D board support"

**Impact**:
- Users with NXP Pico i.MX7D hardware cannot use this platform
- NXP i.MX7 used in industrial IoT, embedded Linux applications
- Different architecture from Raspberry Pi (NXP i.MX7 Dual vs Broadcom BCMxxxx)

---

## Root Cause Analysis

### Root Cause

**Primary Cause**: Platform modernization focused on Raspberry Pi ecosystem first (Phases 0-3) before expanding to other ARM Linux boards.

**Key Findings**:
1. NXP Pico i.MX7D is part of broader "Non-Raspberry Pi ARM Boards" category
2. Explicitly planned in roadmap: "Priority 6" (research/03-implementation-roadmap.md:1453-1457)
3. Estimated effort: 3-5 days for multiple non-Pi boards
4. Requires new board definition, similar toolchain (arm-linux-gnueabihf compatible)

---

## Current Status

### What's Available Now ❌

**NXP Pico i.MX7D Support**:
- ❌ No board definition
- ❌ No i.MX7 Dual SoC configuration
- ❌ Not listed in supported boards

**Platform Scope** (current):
- ✅ Raspberry Pi family (1, 2, 3, 4, 5, 400, CM4, Zero, Zero 2W)
- ❌ NXP boards: Not yet supported

### Future Implementation Plan

**Roadmap Location**: Priority 6 - Non-Raspberry Pi ARM Boards

**NXP Pico i.MX7D Specifications**:
- **Processor**: NXP i.MX7 Dual (dual Cortex-A7)
- **Clock Speed**: 1.2 GHz
- **RAM**: 512 MB to 1 GB (depending on variant)
- **Architecture**: ARMv7-A (32-bit)
- **Toolchain**: arm-linux-gnueabihf (same as Raspberry Pi) ✅

**Implementation Approach** (when scheduled):
1. Board definition: `boards/nxp_pico_imx7d.json`
2. Cross-compilation: Reuse existing arm-linux-gnueabihf toolchain
3. GPIO framework: libgpiod or NXP-specific libraries
4. Documentation and examples

---

## Recommendations

### For Users

**Current Workarounds**:
1. Wait for Priority 6 implementation (future)
2. Use native development on NXP hardware
3. Manual cross-compilation outside PlatformIO
4. **Contribute**: Implement board definition yourself (PRs welcome!)

### For Maintainers

**Immediate Actions**:
- ⏳ **KEEP OPEN** - Valid feature request, planned for Priority 6
- ⏳ Add label: "future-enhancement", "priority-6"

---

## Related Issues

**Related** (same Priority 6 category):
- #31 - BeagleBone Black support
- #29 - Orange Pi Zero support
- #25 - VIM boards support
- #24 - RK3568 board support

**All part of**: Priority 6 - Non-Raspberry Pi ARM Boards expansion

---

## References

**Research Documents**:
- [research/03-implementation-roadmap.md:1453-1457](../research/03-implementation-roadmap.md) - Priority 6 mention

**External References**:
- NXP Pico i.MX7D: https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/pico-pi-imx7d-development-board:PICO-PI-IMX7
- i.MX7 Dual Datasheet: https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-7-processors:IMX7-SERIES

---

## Closure Decision

**Recommendation**: ⏳ **KEEP OPEN** (Planned Future Enhancement)

**Rationale**: Valid feature request, explicitly planned for Priority 6 implementation.

**Status Comment**: See [status-comment.md](status-comment.md)

---

*Assessment Version: 1.0*
*Date: 2025-11-09*
*Status: PLANNED (Priority 6)*
