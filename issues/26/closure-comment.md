## 🔄 Duplicate of #32 - Already Resolved

This issue is a **duplicate** of #32 which has been **resolved**.

### Summary

The toolchain error on Windows is **fixed**. Cross-compilation now works on Windows (and all platforms) using system-installed ARM toolchains.

### Solution

**For Windows users**:

1. **Download ARM GNU Toolchain**:
   - https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads
   - Choose "AArch32 GNU/Linux target (arm-linux-gnueabihf)"

2. **Install and add to PATH**

3. **Use this repository**:
```ini
[env:raspberrypi_zero_w]
platform = https://github.com/sfo2001/platform-linux_arm.git
board = raspberrypi_zero  ; or raspberrypi_zero2w
framework = lgpio  ; Recommended
```

4. **Build**:
```cmd
pio run
```

### WiringPi Note

WiringPi cross-compilation is blocked on all platforms (requires direct Pi hardware). Use lgpio or pigpio frameworks for cross-compilation, or build WiringPi projects on Raspberry Pi.

### Complete Details

**See issue #32** for full resolution:
- **Canonical issue**: #32 "[#2] The package 'toolchain-gccarmlinuxgnueabi' is not available"
- **Assessment**: [issues/32/assessment.md](../32/assessment.md)
- **Documentation**: [README.md#cross-compilation-setup](../README.md#cross-compilation-setup)

---

**Status**: 🔄 DUPLICATE of #32 (RESOLVED)
**Reference**: #32
