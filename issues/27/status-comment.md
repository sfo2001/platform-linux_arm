## ℹ️ Requesting More Information - Likely Stale Issue

This issue reports an AssertionError from **old platform version (v1.5.1)** and may no longer be reproducible.

### Issue Background

**Original Error**:
```python
File "piosize.py", line 56, in _get_symbol_locations
assert len(addrs) == len(locations) / AssertionError
```

**Reported Environment**:
- Platform: linux_arm v1.5.1 (old, pre-modernization)
- Board: Raspberry Pi 2B
- Build Mode: Debug

### Current Status

**Cannot reproduce** with modern platform:
- ✅ Current platform: v1.6.0+ (modernized)
- ✅ PlatformIO Core: 6.x (updated)
- ✅ Cross-compilation reworked (Phase 0)
- ✅ System toolchains (not old PlatformIO packages)
- ✅ CI/CD passing (no AssertionError reported)

### Request for Information

**Can you still reproduce this issue?**

If yes, please provide:
1. **PlatformIO Core version**: `pio --version`
2. **Platform configuration**:
```ini
platform = https://github.com/sfo2001/platform-linux_arm.git
; or upstream?
```
3. **Full build log** (with `--verbose` flag)
4. **platformio.ini** contents
5. **Toolchain details**: System toolchain or PlatformIO package?

### Likely Resolution

**Try updating to current platform**:
```ini
[env:raspberrypi_2b]
platform = https://github.com/sfo2001/platform-linux_arm.git
board = raspberrypi_2b
framework = lgpio
```

**Update PlatformIO Core**:
```bash
pio upgrade
pio pkg update
```

**Install system toolchain** (follow [README.md](../README.md#cross-compilation-setup))

### Next Steps

**If no response within 30 days**: Close as stale (old version, cannot reproduce)

**If reproducible with modern setup**: Investigate further (may be PlatformIO Core bug)

---

**Status**: ℹ️ NEEDS_INFO
**Labels**: needs-info, bug?, stale?
**Waiting**: User confirmation with modern platform
