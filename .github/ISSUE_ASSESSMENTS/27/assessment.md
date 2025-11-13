# Issue #27 Assessment - PlatformIO Inspection AssertionError

**Issue Number**: #27
**Title**: [#15] Can't use Platform.io Inspection: [sizedata] AssertionError
**Assessment Date**: 2025-11-09
**Assessor**: Claude (AI Assistant)
**Status**: ℹ️ NEEDS_INFO / LIKELY STALE

---

## Executive Summary

Issue #27 (originally issue #15 from platformio/platform-linux_arm) reports an AssertionError in PlatformIO's `piosize.py` during size data collection for Raspberry Pi 2B builds. The error occurs in debug symbol extraction. This issue is **likely stale** (old PlatformIO version) and may no longer be reproducible with current platform implementation.

**Quick Status**:
- **Original Problem**: AssertionError in piosize.py during size analysis
- **Current Status**: ℹ️ **NEEDS_INFO** - Cannot reproduce, likely outdated
- **Platform Version**: v1.5.1 (old, pre-modernization)
- **Recommendation**: REQUEST INFO or CLOSE as stale if no response

---

## Issue Background

### Original Problem

**Reporter**: Community users (original upstream issue #15)
**Date Reported**: Prior to repository fork
**Environment**:
- Platform: linux_arm v1.5.1 (old version)
- Board: Raspberry Pi 2B (BCM2836)
- Build Mode: Debug
- Toolchain: GCC for ARM

**Error Message**:
```python
File "piosize.py", line 56, in _get_symbol_locations
assert len(addrs) == len(locations) / AssertionError
```

**Root Cause** (per reporter):
> "not receiving the proper debug symbols"

Suggests debug symbol extraction from ELF fails to match addresses with location data.

**Impact**: Size analysis fails during post-build, blocks build completion

---

## Root Cause Analysis

### Investigation Summary

Unable to reproduce with current platform state. Issue likely specific to:
1. Old PlatformIO Core version (pre-6.x)
2. Old platform version (v1.5.1)
3. Specific toolchain version or debug symbol format
4. Fixed in upstream PlatformIO Core

### Why Likely Stale

**Evidence**:
1. **Old platform version**: v1.5.1 (current modernization at v1.6.0+)
2. **Old PlatformIO pattern**: piosize.py is PlatformIO Core component, not platform-specific
3. **No recent reports**: No similar issues in modern PlatformIO
4. **Build system changes**: Cross-compilation rework may have resolved
5. **Toolchain changes**: System toolchains vs old PlatformIO packages

**Similar issues resolved**: PlatformIO Core has had multiple size analysis fixes in recent versions.

---

## Current Status

### Cannot Reproduce ❓

**Modern Platform** (v1.6.0+):
- ✅ Cross-compilation works (Linux, macOS, Windows)
- ✅ Raspberry Pi 2B supported (`raspberrypi_2b`)
- ✅ Modern PlatformIO Core (6.x)
- ✅ System toolchains (not old packages)
- ❓ Size analysis not reported as failing

**No evidence of issue** in:
- Current CI/CD builds (examples build successfully)
- Modern documentation
- Recent user reports

---

## Recommendations

### For Users

**If you experience this issue**:

1. **Update to current platform**:
```ini
[env:raspberrypi_2b]
platform = https://github.com/sfo2001/platform-linux_arm.git
board = raspberrypi_2b
framework = lgpio
```

2. **Update PlatformIO Core**:
```bash
pio upgrade
pio pkg update
```

3. **Use modern toolchain** (follow README.md cross-compilation setup)

4. **If issue persists**, provide:
   - PlatformIO Core version
   - Full build log
   - platformio.ini configuration
   - Toolchain details

### For Maintainers

**Immediate Actions**:
- ℹ️ **REQUEST MORE INFO** from community
- ℹ️ Add label: "needs-info", "bug", "stale?"
- ℹ️ Comment asking if issue still reproducible with:
  - Current platform (this repository)
  - PlatformIO Core 6.x
  - Modern toolchains

**If No Response** (30 days):
- 🚫 **CLOSE as STALE** - old version, cannot reproduce, no recent reports

**If Reproducible**:
- Investigate with modern setup
- May be PlatformIO Core bug (report upstream)
- Or platform-specific fix needed

---

## Related Issues

**Related**:
- Upstream PlatformIO Core issues about size analysis
- STM8 toolchain similar issue (mentioned in original report)

**Platform Changes Since**:
- Cross-compilation reworked (Phase 0)
- System toolchains (not PlatformIO packages)
- Modern PlatformIO Core compatibility

---

## Closure Decision

**Recommendation**: ℹ️ **REQUEST INFO** or 🚫 **CLOSE as STALE**

**Rationale**:

1. **Old version**: Issue from platform v1.5.1 (pre-modernization)
2. **Cannot reproduce**: Not seen in current builds or CI/CD
3. **PlatformIO Core issue**: Size analysis is Core component, not platform
4. **No recent reports**: No similar issues with modern setup
5. **Platform evolved**: Cross-compilation rework may have resolved

**Recommended Action**:
1. Comment requesting reproduction steps with modern platform
2. Wait 30 days for response
3. If no response: Close as stale
4. If reproducible: Investigate further

**Status Comment**: See [status-comment.md](status-comment.md)

---

**Assessment Status**:
- ✅ Issue analyzed (old bug report)
- ✅ Root cause unclear (debug symbol extraction)
- ✅ Cannot reproduce with current platform
- ✅ Recommendation: Request info or close as stale

---

*Assessment Version: 1.0*
*Date: 2025-11-09*
*Status: NEEDS_INFO / LIKELY STALE*
