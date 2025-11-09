# Round 2 - Priority 3: Modern Board Support

**Date**: 2025-11-09
**Round**: 2
**Status**: Complete
**Related Documents**: [01-initial-assessment.md](01-initial-assessment.md), [REFERENCES.md](REFERENCES.md)

---

## Executive Summary

**Current State**: Platform supports only 4 Raspberry Pi boards from 2016 and earlier (RPi 1, 2, 3, Zero 1). Missing all modern boards released 2019-2024.

**Root Cause**:
- No board definition updates since platform creation (pre-2022)
- No process for adding new boards as hardware releases
- Focus on legacy Raspberry Pi models only

**Proposed Solution**:
1. **Add Raspberry Pi 4 Model B** - Most popular current board (2019, BCM2711)
2. **Add Raspberry Pi 5** - Latest flagship (2023, BCM2712)
3. **Add Raspberry Pi 400** - Keyboard computer (2020, BCM2711 @ 1.8GHz)
4. **Add Compute Module 4** - Industrial/embedded (2020, BCM2711)
5. **Add Raspberry Pi Zero 2 W** - Compact quad-core (2021, RP3A0/BCM2710A1)
6. **(Future)** Consider non-Raspberry Pi ARM Linux boards (BeagleBone, ODROID, etc.)

**Critical Findings**:
- **Board definitions are simple** - mostly copy-paste from existing templates
- **Pi 4 and 5 support both 32-bit and 64-bit** architectures (OS-dependent)
- **BCM2711** (Pi 4/400/CM4) uses ARMv8-A (64-bit capable, 1.5-1.8GHz)
- **BCM2712** (Pi 5) uses ARMv8.2-A Cortex-A76 (64-bit only, 2.4GHz)
- **RP3A0** (Zero 2 W) uses BCM2710A1/Cortex-A53 (64-bit capable, 1GHz)
- All new boards use **standard 40-pin GPIO** header (backward compatible)

**Recommended Actions**:
1. **Immediate**: Add Raspberry Pi 4 Model B (30 min, highest user demand)
2. **High Priority**: Add Raspberry Pi 5 (30 min, latest hardware + requires lgpio framework)
3. **Medium Priority**: Add Raspberry Pi 400, CM4, Zero 2 W (30 min each)
4. **Documentation**: Update board selection guide with architecture notes (1 hour)
5. **Testing**: Validate board definitions with examples (1-2 hours)

---

## Detailed Findings

### Current Board Coverage

**Existing Boards** (in `boards/` directory):

| Board | SoC | CPU | Frequency | Release Year | Status |
|-------|-----|-----|-----------|--------------|--------|
| raspberrypi_1b | BCM2835 | ARM1176JZF-S | 700MHz | 2012 | ✅ Defined |
| raspberrypi_2b | BCM2836 | Cortex-A7 (quad) | 900MHz | 2015 | ✅ Defined |
| raspberrypi_3b | BCM2837 | Cortex-A53 (quad) | 1.2GHz | 2016 | ✅ Defined |
| raspberrypi_zero | BCM2835 | ARM1176JZF-S | 1GHz | 2015 | ✅ Defined |

**Missing Modern Boards**:

| Board | SoC | CPU | Frequency | Release Year | Priority |
|-------|-----|-----|-----------|--------------|----------|
| **Raspberry Pi 4 Model B** | BCM2711 | Cortex-A72 (quad) | 1.5GHz | 2019 | 🔴 Critical (most popular) |
| **Raspberry Pi 5** | BCM2712 | Cortex-A76 (quad) | 2.4GHz | 2023 | 🔴 Critical (latest) |
| Raspberry Pi 400 | BCM2711 | Cortex-A72 (quad) | 1.8GHz | 2020 | 🟡 High (keyboard PC) |
| Compute Module 4 | BCM2711 | Cortex-A72 (quad) | 1.5GHz | 2020 | 🟡 Medium (industrial) |
| Raspberry Pi Zero 2 W | RP3A0 (BCM2710A1) | Cortex-A53 (quad) | 1GHz | 2021 | 🟡 Medium (compact) |
| Raspberry Pi 3B+ | BCM2837B0 | Cortex-A53 (quad) | 1.4GHz | 2018 | 🟢 Low (similar to 3B) |
| Raspberry Pi 3A+ | BCM2837B0 | Cortex-A53 (quad) | 1.4GHz | 2018 | 🟢 Low (niche) |

---

## Hardware Specifications

### Raspberry Pi 4 Model B

**SoC**: Broadcom BCM2711
**CPU**: Quad-core Cortex-A72 (ARM v8) 64-bit @ 1.5GHz (C0 stepping: 1.8GHz)
**Architecture**: ARMv8-A (64-bit capable, can run 32-bit or 64-bit OS)
**RAM Variants**: 1GB, 2GB, 4GB, 8GB LPDDR4 SDRAM
**GPIO**: 40-pin header (backward compatible with all previous models)
**Release**: June 2019
**Availability**: Guaranteed until January 2031

**Key Features**:
- Dual 4K HDMI output
- USB 3.0 ports
- Gigabit Ethernet (full throughput, not USB-limited)
- PCIe lane (used for USB controller)

**PlatformIO Configuration**:
```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI4",
    "f_cpu": "1500000000L",  // 1.5 GHz (C0 stepping runs at 1.8GHz)
    "mcu": "bcm2711"
  },
  "frameworks": ["wiringpi", "lgpio", "pigpio"],
  "name": "Raspberry Pi 4 Model B",
  "upload": {
    "maximum_ram_size": 8589934592,  // 8GB (max variant)
    "maximum_size": 8589934592
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-4-model-b/",
  "vendor": "Raspberry Pi"
}
```

**References**:
- Official Datasheet: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf
- Specifications: https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/

---

### Raspberry Pi 5

**SoC**: Broadcom BCM2712
**CPU**: Quad-core Cortex-A76 (ARM v8.2-A) 64-bit @ 2.4GHz
**Architecture**: ARMv8.2-A (64-bit, three generations beyond Cortex-A72)
**RAM Variants**: 2GB, 4GB, 8GB, 16GB LPDDR4X SDRAM
**GPIO**: 40-pin header (via RP1 I/O controller)
**Release**: October 2023
**Manufacturing**: 16nm process (vs 28nm for BCM2711)

**Key Features**:
- **RP1 I/O Controller** (custom Raspberry Pi design)
- 2-3x faster than Pi 4
- Dual 4K60 display support (VideoCore VII GPU)
- PCIe 2.0 x1 interface (16 Gb/s) for NVMe SSD
- USB 3.0 (5 Gbps) and USB 2.0 ports

**Important**: Requires **lgpio framework** (pigpio incompatible due to RP1 controller)

**PlatformIO Configuration**:
```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI5",
    "f_cpu": "2400000000L",  // 2.4 GHz
    "mcu": "bcm2712"
  },
  "frameworks": ["lgpio"],  // NOTE: pigpio NOT compatible, WiringPi limited (GCLK missing)
  "name": "Raspberry Pi 5",
  "upload": {
    "maximum_ram_size": 17179869184,  // 16GB (max variant)
    "maximum_size": 17179869184
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-5/",
  "vendor": "Raspberry Pi"
}
```

**References**:
- Official Documentation: https://www.raspberrypi.com/documentation/computers/processors.html#bcm2712
- Specifications: https://www.raspberrypi.com/products/raspberry-pi-5/specifications/

---

### Raspberry Pi 400

**SoC**: Broadcom BCM2711C0 (C0 stepping)
**CPU**: Quad-core Cortex-A72 (ARM v8) 64-bit @ **1.8GHz** (faster than Pi 4)
**Architecture**: ARMv8-A (same as Pi 4)
**RAM**: 4GB LPDDR4 SDRAM (only one variant)
**GPIO**: Horizontal 40-pin header on back of keyboard
**Form Factor**: Keyboard computer (compact desktop PC)
**Release**: November 2020

**Key Features**:
- Built into keyboard housing (improved cooling → higher clock)
- Same BCM2711 as Pi 4, but C0 stepping at 1.8GHz (vs 1.5GHz)
- GPIO header accessible (but horizontal orientation)
- **No CSI (camera) or DSI (display) connectors** (vs Pi 4 has both)

**PlatformIO Configuration**:
```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI400",
    "f_cpu": "1800000000L",  // 1.8 GHz (higher than Pi 4)
    "mcu": "bcm2711"
  },
  "frameworks": ["wiringpi", "lgpio", "pigpio"],
  "name": "Raspberry Pi 400",
  "upload": {
    "maximum_ram_size": 4294967296,  // 4GB (only variant)
    "maximum_size": 4294967296
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-400/",
  "vendor": "Raspberry Pi"
}
```

**References**:
- Specifications: https://www.raspberrypi.com/products/raspberry-pi-400/specifications/
- Announcement: https://www.cnx-software.com/2020/11/02/raspberry-pi-400-keyboard-computer-features-1-8-ghz-bcm2711c0-processor/

---

### Compute Module 4

**SoC**: Broadcom BCM2711
**CPU**: Quad-core Cortex-A72 (ARM v8) 64-bit @ 1.5GHz
**Architecture**: ARMv8-A (same as Pi 4)
**RAM Variants**: 1GB, 2GB, 4GB, 8GB LPDDR4 SDRAM
**Storage**: 8GB, 16GB, 32GB eMMC (or "Lite" with no eMMC)
**Form Factor**: 55mm × 40mm module with dual 100-pin connectors
**GPIO**: 28 GPIO signals via connectors (no standard header)
**Release**: October 2020

**Key Features**:
- **Industrial/embedded use case** (requires custom carrier board)
- Wireless variants (WiFi + Bluetooth) available
- PCIe Gen 2 x1 interface exposed
- **No standard 40-pin GPIO header** (GPIO via 100-pin connectors)
- Gigabit Ethernet, USB 2.0

**PlatformIO Configuration**:
```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI_CM4",
    "f_cpu": "1500000000L",  // 1.5 GHz
    "mcu": "bcm2711"
  },
  "frameworks": ["wiringpi", "lgpio", "pigpio"],
  "name": "Raspberry Pi Compute Module 4",
  "upload": {
    "maximum_ram_size": 8589934592,  // 8GB (max variant)
    "maximum_size": 8589934592
  },
  "url": "https://www.raspberrypi.com/products/compute-module-4/",
  "vendor": "Raspberry Pi"
}
```

**References**:
- Product Brief: https://datasheets.raspberrypi.com/cm4/cm4-product-brief.pdf
- Specifications: https://www.raspberrypi.com/products/compute-module-4/specifications/

---

### Raspberry Pi Zero 2 W

**SoC**: RP3A0 system-in-package (SiP) containing BCM2710A1 die
**CPU**: Quad-core Cortex-A53 (ARM v8) 64-bit @ 1GHz (same family as Pi 3)
**Architecture**: ARMv8-A (64-bit capable)
**RAM**: 512MB LPDDR2 SDRAM
**GPIO**: 40-pin header (unpopulated footprint)
**Form Factor**: Same as original Pi Zero (65mm × 30mm)
**Wireless**: 2.4GHz WiFi, Bluetooth 4.2 (built-in)
**Release**: October 2021

**Key Features**:
- **5x faster multi-threaded** performance vs original Zero
- Same compact form factor as Zero 1
- CSI-2 camera connector
- Mini HDMI, micro USB OTG
- **40-pin GPIO header footprint** (header not soldered by default)

**Note**: CPU is **BCM2710A1** (variant of BCM2837 used in Pi 3), packaged as **RP3A0**

**PlatformIO Configuration**:
```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI_ZERO2W",
    "f_cpu": "1000000000L",  // 1 GHz
    "mcu": "bcm2710"  // RP3A0 contains BCM2710A1 die
  },
  "frameworks": ["wiringpi", "lgpio", "pigpio"],
  "name": "Raspberry Pi Zero 2 W",
  "upload": {
    "maximum_ram_size": 536870912,  // 512MB
    "maximum_size": 536870912
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/",
  "vendor": "Raspberry Pi"
}
```

**References**:
- Product Brief: https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf
- Specifications: https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/specifications/
- RP3A0 Analysis: https://www.jeffgeerling.com/blog/2021/look-inside-raspberry-pi-zero-2-w-and-rp3a0-au

---

## Architecture Strategy

### 32-bit vs 64-bit ARM

**Key Decision**: Should boards support **ARMv7 (32-bit)** or **AArch64 (64-bit)** or both?

#### Hardware Capabilities

| Board | SoC | Architecture | 32-bit OS? | 64-bit OS? | Default OS (2024) |
|-------|-----|--------------|-----------|-----------|-------------------|
| RPi 4 | BCM2711 | ARMv8-A (64-bit capable) | ✅ Yes | ✅ Yes | 64-bit recommended |
| RPi 5 | BCM2712 | ARMv8.2-A (64-bit) | ✅ Yes (compat) | ✅ Yes | 64-bit only (practical) |
| RPi 400 | BCM2711 | ARMv8-A (64-bit capable) | ✅ Yes | ✅ Yes | 64-bit recommended |
| CM4 | BCM2711 | ARMv8-A (64-bit capable) | ✅ Yes | ✅ Yes | Varies by carrier |
| Zero 2 W | BCM2710A1 | ARMv8-A (64-bit capable) | ✅ Yes | ✅ Yes | 32-bit common |

**ARMv8-A processors** (Cortex-A53, A72, A76) support **both** 32-bit and 64-bit operation:
- **AArch64 mode**: Native 64-bit execution
- **AArch32 mode**: ARMv7 compatibility (32-bit)

**OS determines mode**: Raspberry Pi OS offers both 32-bit and 64-bit images.

---

#### Recommended Approach: Default to 32-bit (ARMv7) with Notes

**Rationale**:
1. **Backward compatibility**: Works with both 32-bit and 64-bit OS
2. **Ecosystem consistency**: Existing platform uses ARMv7 toolchain (`arm-linux-gnueabihf-`)
3. **Simplicity**: Single toolchain for all boards
4. **Common deployment**: Many users still run 32-bit Raspberry Pi OS

**Board Definitions**: Use 32-bit defaults (`arm-linux-gnueabihf-` toolchain)

**Documentation**: Explain how to build for 64-bit if needed:

```markdown
### Building for 64-bit ARM (AArch64)

Raspberry Pi 4, 5, 400, CM4, and Zero 2 W support 64-bit operation when running 64-bit OS.

To cross-compile for 64-bit ARM:

1. Install aarch64 toolchain:
   \`\`\`bash
   sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
   \`\`\`

2. Override toolchain in platformio.ini:
   \`\`\`ini
   [env:raspberrypi_5_64bit]
   platform = linux_arm
   board = raspberrypi_5
   framework = lgpio
   build_flags =
       -DTOOLCHAIN_PREFIX=aarch64-linux-gnu-
   \`\`\`

3. Or modify builder/main.py to detect 64-bit boards (see Priority 1 document)
```

**Future Enhancement**: Implement dual-architecture support (from Priority 1, Implementation Option 2)

---

## Board Definition Template

### Standard Structure

Based on existing `raspberrypi_3b.json` pattern:

```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -D<BOARD_SPECIFIC_FLAG>",
    "f_cpu": "<FREQUENCY_IN_HZ>L",
    "mcu": "<BCM_SOC_TYPE>"
  },
  "frameworks": ["<framework1>", "<framework2>", ...],
  "name": "<Human-Readable Board Name>",
  "upload": {
    "maximum_ram_size": <RAM_SIZE_BYTES>,
    "maximum_size": <STORAGE_SIZE_BYTES>
  },
  "url": "<OFFICIAL_PRODUCT_URL>",
  "vendor": "Raspberry Pi"
}
```

### Field Documentation

| Field | Description | Example | Notes |
|-------|-------------|---------|-------|
| `build.extra_flags` | Preprocessor defines | `"-DRASPBERRYPI -DRASPBERRYPI4"` | Always include `-DRASPBERRYPI`, add board-specific define |
| `build.f_cpu` | CPU frequency in Hz | `"1500000000L"` (1.5 GHz) | Must end with `L` (long integer) |
| `build.mcu` | SoC/MCU identifier | `"bcm2711"` | Lowercase, used for architecture detection |
| `frameworks` | Supported frameworks | `["wiringpi", "lgpio", "pigpio"]` | Array of framework names |
| `name` | Display name | `"Raspberry Pi 4 Model B"` | User-facing name |
| `upload.maximum_ram_size` | RAM size in bytes | `8589934592` (8GB) | Use max variant if multiple RAM options |
| `upload.maximum_size` | Storage size in bytes | Same as RAM for Linux | Arbitrary for native Linux (no flash limit) |
| `url` | Official product page | `"https://www.raspberrypi.com/..."` | Link to specs/documentation |
| `vendor` | Manufacturer | `"Raspberry Pi"` | Consistent across all RPi boards |

**Note**: `upload.maximum_size` and `upload.maximum_ram_size` are nominal for Linux ARM (no firmware upload). Values match RAM for consistency.

---

## Board Definition Files

### boards/raspberrypi_4b.json

```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI4",
    "f_cpu": "1500000000L",
    "mcu": "bcm2711"
  },
  "frameworks": [
    "wiringpi",
    "lgpio",
    "pigpio"
  ],
  "name": "Raspberry Pi 4 Model B",
  "upload": {
    "maximum_ram_size": 8589934592,
    "maximum_size": 8589934592
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-4-model-b/",
  "vendor": "Raspberry Pi"
}
```

---

### boards/raspberrypi_5.json

```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI5",
    "f_cpu": "2400000000L",
    "mcu": "bcm2712"
  },
  "frameworks": [
    "lgpio"
  ],
  "name": "Raspberry Pi 5",
  "upload": {
    "maximum_ram_size": 17179869184,
    "maximum_size": 17179869184
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-5/",
  "vendor": "Raspberry Pi"
}
```

**Note**: Only `lgpio` framework listed (pigpio incompatible, WiringPi GCLK function missing)

---

### boards/raspberrypi_400.json

```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI400",
    "f_cpu": "1800000000L",
    "mcu": "bcm2711"
  },
  "frameworks": [
    "wiringpi",
    "lgpio",
    "pigpio"
  ],
  "name": "Raspberry Pi 400",
  "upload": {
    "maximum_ram_size": 4294967296,
    "maximum_size": 4294967296
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-400/",
  "vendor": "Raspberry Pi"
}
```

---

### boards/raspberrypi_cm4.json

```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI_CM4",
    "f_cpu": "1500000000L",
    "mcu": "bcm2711"
  },
  "frameworks": [
    "wiringpi",
    "lgpio",
    "pigpio"
  ],
  "name": "Raspberry Pi Compute Module 4",
  "upload": {
    "maximum_ram_size": 8589934592,
    "maximum_size": 8589934592
  },
  "url": "https://www.raspberrypi.com/products/compute-module-4/",
  "vendor": "Raspberry Pi"
}
```

---

### boards/raspberrypi_zero2w.json

```json
{
  "build": {
    "extra_flags": "-DRASPBERRYPI -DRASPBERRYPI_ZERO2W",
    "f_cpu": "1000000000L",
    "mcu": "bcm2710"
  },
  "frameworks": [
    "wiringpi",
    "lgpio",
    "pigpio"
  ],
  "name": "Raspberry Pi Zero 2 W",
  "upload": {
    "maximum_ram_size": 536870912,
    "maximum_size": 536870912
  },
  "url": "https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/",
  "vendor": "Raspberry Pi"
}
```

---

## Non-Raspberry Pi ARM Linux Boards

### Assessment: Defer to Phase 2

**Question**: Should platform-linux_arm support other ARM Linux SBCs (BeagleBone, ODROID, Orange Pi, etc.)?

**Rationale for Deferral**:
1. **Focus on Raspberry Pi first** - Complete modernization of RPi support before expanding
2. **Different GPIO ecosystems** - Each board family has unique GPIO libraries
3. **Limited demand validation** - Unclear if PlatformIO users need non-RPi ARM Linux
4. **Testing complexity** - Requires acquiring multiple hardware platforms

**Future Candidates**:

| Board Family | SoC Family | GPIO Libraries | Market Share | Recommendation |
|--------------|-----------|----------------|--------------|----------------|
| **BeagleBone Black/Green** | TI AM335x (Cortex-A8) | libgpiod, bone-gpio | Medium | ✅ Consider Phase 2 |
| **ODROID-C4/N2+** | Amlogic S905X3/S922X (Cortex-A55/A73) | WiringPi port, libgpiod | Low-Medium | ⚠️ Evaluate demand |
| **Orange Pi** | Allwinner H6/H616 | WiringPi port, wiringOP | Low | ⬜ Low priority |
| **Rock Pi 4** | Rockchip RK3399 (Cortex-A72/A53) | mraa, libgpiod | Low | ⬜ Low priority |
| **Pine64** | Allwinner A64 (Cortex-A53) | WiringPi port | Low | ⬜ Low priority |

**Recommendation**:
- **Immediate**: Focus on Raspberry Pi 4, 5, 400, CM4, Zero 2 W
- **Phase 2** (if demand exists): Add BeagleBone Black/Green (well-established, different from RPi)
- **Phase 3+**: Evaluate others based on user requests

**Note**: libgpiod framework (Priority 2) enables platform-independent GPIO, making non-RPi boards easier to support in future.

---

## Implementation Plan

### Phase 1: Critical Boards (Highest Impact)

**Priority Order**:
1. **Raspberry Pi 4 Model B** (30 min)
   - Most popular current board
   - Copy raspberrypi_3b.json → raspberrypi_4b.json
   - Update MCU to bcm2711, CPU to 1.5GHz, RAM to 8GB
   - Add frameworks: wiringpi, lgpio, pigpio

2. **Raspberry Pi 5** (30 min)
   - Latest flagship
   - Copy raspberrypi_4b.json → raspberrypi_5.json
   - Update MCU to bcm2712, CPU to 2.4GHz, RAM to 16GB
   - **Framework**: lgpio only (pigpio incompatible)

**Total Phase 1**: 1 hour (unblocks 90%+ of modern Pi users)

---

### Phase 2: Additional Modern Boards

3. **Raspberry Pi 400** (30 min)
   - Similar to Pi 4, higher clock (1.8GHz)

4. **Compute Module 4** (30 min)
   - Industrial/embedded variant of Pi 4

5. **Raspberry Pi Zero 2 W** (30 min)
   - Compact quad-core variant

**Total Phase 2**: 1.5 hours

---

### Phase 3: Documentation and Testing

6. **Board Selection Guide** (1 hour)
   - Document which board to choose
   - Architecture notes (32-bit vs 64-bit)
   - Framework compatibility matrix

7. **Testing** (1-2 hours)
   - Build examples for each board
   - Validate on hardware (if available)
   - Cross-compilation testing

8. **README Updates** (30 min)
   - List all supported boards
   - Link to board specifications

**Total Phase 3**: 2.5-3.5 hours

---

**Total Effort**: 5-6 hours (all phases)

---

## Testing Strategy

### Build Validation

**For each new board definition**:

1. **Syntax Check**:
   ```bash
   python3 -m json.tool boards/raspberrypi_5.json
   # Should output valid JSON or error
   ```

2. **Board Recognition**:
   ```bash
   pio boards linux_arm raspberrypi_5
   # Should display board details
   ```

3. **Example Build** (native or cross-compile):
   ```bash
   cd examples/lgpio-blink
   pio run -e raspberrypi_5
   # Should compile successfully
   ```

4. **Binary Architecture Validation**:
   ```bash
   file .pio/build/raspberrypi_5/program
   # Should show: ELF 32-bit ARM or ELF 64-bit ARM
   ```

---

### Hardware Testing (If Available)

**Deploy and run on actual hardware**:

```bash
# Copy binary to Raspberry Pi
scp .pio/build/raspberrypi_5/program pi@raspberrypi.local:/tmp/

# SSH and execute
ssh pi@raspberrypi.local
cd /tmp
chmod +x program
sudo ./program  # GPIO requires root

# Expected: Program runs successfully
```

**Validate**:
- Program executes without errors
- GPIO operations work (if using GPIO frameworks)
- No architecture mismatches

---

### Test Matrix

| Board | Build Test | Cross-Compile | Native Build | Hardware Test | Status |
|-------|-----------|---------------|--------------|---------------|--------|
| raspberrypi_4b | ✅ Required | ✅ Linux x86_64 | ⚠️ Optional (if Pi 4 available) | ⚠️ If available | Pending |
| raspberrypi_5 | ✅ Required | ✅ Linux x86_64 | ⚠️ Optional (if Pi 5 available) | ⚠️ If available | Pending |
| raspberrypi_400 | ✅ Required | ✅ Linux x86_64 | ⬜ Skip (keyboard form factor) | ⬜ Skip | Pending |
| raspberrypi_cm4 | ✅ Required | ✅ Linux x86_64 | ⬜ Skip (requires carrier) | ⬜ Skip | Pending |
| raspberrypi_zero2w | ✅ Required | ✅ Linux x86_64 | ⚠️ Optional (if Zero 2W available) | ⚠️ If available | Pending |

**Minimum Viable Testing**: Build test + cross-compile test for all boards

---

## Documentation Requirements

### 1. Board Selection Guide (README.md)

```markdown
## Supported Boards

### Raspberry Pi 4 Series
- **Raspberry Pi 4 Model B** - Quad-core Cortex-A72 @ 1.5GHz, 1/2/4/8GB RAM
- **Raspberry Pi 400** - Keyboard computer, Cortex-A72 @ 1.8GHz, 4GB RAM
- **Compute Module 4** - Industrial module, Cortex-A72 @ 1.5GHz, 1/2/4/8GB RAM

### Raspberry Pi 5
- **Raspberry Pi 5** - Quad-core Cortex-A76 @ 2.4GHz, 2/4/8/16GB RAM
  - **Note**: Requires `lgpio` framework (pigpio not compatible)

### Raspberry Pi 3 Series
- **Raspberry Pi 3 Model B** - Quad-core Cortex-A53 @ 1.2GHz, 1GB RAM

### Raspberry Pi 2
- **Raspberry Pi 2 Model B** - Quad-core Cortex-A7 @ 900MHz, 1GB RAM

### Raspberry Pi 1
- **Raspberry Pi 1 Model B** - ARM1176JZF-S @ 700MHz, 512MB RAM

### Raspberry Pi Zero
- **Raspberry Pi Zero** - ARM1176JZF-S @ 1GHz, 512MB RAM
- **Raspberry Pi Zero 2 W** - Quad-core Cortex-A53 @ 1GHz, 512MB RAM, WiFi/Bluetooth

### Architecture Notes

- **Pi 4, 5, 400, CM4, Zero 2 W**: Support both 32-bit and 64-bit OS
  - Default: 32-bit builds (armhf) for compatibility
  - For 64-bit (aarch64): See "Building for 64-bit ARM" section
- **Pi 1-3, Zero**: 32-bit only

### Framework Compatibility

| Board | WiringPi | lgpio | pigpio | Bare-Metal |
|-------|----------|-------|--------|------------|
| Pi 5 | ⚠️ Limited (GCLK missing) | ✅ | ❌ | ✅ |
| Pi 4, 400, CM4 | ✅ | ✅ | ✅ | ✅ |
| Pi 3, 2, 1, Zero, Zero 2W | ✅ | ✅ | ✅ | ✅ |

**Recommendation**: Use **lgpio** for all new projects (works on all boards including Pi 5)
```

---

### 2. platformio.ini Examples

**Example 1: Raspberry Pi 5 with lgpio**:
```ini
[env:blink_pi5]
platform = linux_arm
board = raspberrypi_5
framework = lgpio
```

**Example 2: Raspberry Pi 4 with pigpio**:
```ini
[env:sensor_pi4]
platform = linux_arm
board = raspberrypi_4b
framework = pigpio
```

**Example 3: Compute Module 4 bare-metal**:
```ini
[env:server_cm4]
platform = linux_arm
board = raspberrypi_cm4
; No framework - bare-metal build
```

---

## Effort Estimates

| Task | Effort (Hours) | Justification |
|------|---------------|---------------|
| **Board Definitions** | | |
| Create raspberrypi_4b.json | 0.5 | Copy template, update specs |
| Create raspberrypi_5.json | 0.5 | Copy template, update specs, note lgpio requirement |
| Create raspberrypi_400.json | 0.5 | Similar to Pi 4, higher clock |
| Create raspberrypi_cm4.json | 0.5 | Similar to Pi 4 |
| Create raspberrypi_zero2w.json | 0.5 | Copy Zero, update specs |
| **Subtotal** | **2.5** | Straightforward copy-paste |
| | | |
| **Documentation** | | |
| Board selection guide | 1 | Feature matrix, recommendations |
| Architecture notes (32/64-bit) | 0.5 | Explain ARMv7 vs AArch64 |
| Framework compatibility matrix | 0.5 | Which frameworks work on which boards |
| README updates | 0.5 | List new boards, links |
| **Subtotal** | **2.5** | Critical for usability |
| | | |
| **Testing** | | |
| JSON syntax validation (5 boards) | 0.5 | Automated check |
| Build test (5 boards) | 1 | `pio run` for each |
| Cross-compile validation | 1 | Test on Linux x86_64 |
| Hardware testing (if available) | 1 | Deploy to Pi 4/5, run |
| **Subtotal** | **3.5** | Ensure quality |
| | | |
| **Integration** | | |
| Update CI/CD (Priority 4) | 0.5 | Add new boards to test matrix |
| **Subtotal** | **0.5** | Depends on Priority 4 |

**Total Effort**: **9 hours** (complete implementation + docs + testing)

**Recommended Phased Approach**:

**Phase 1 (Quick Win - 2 hours)**:
- Add Pi 4 and Pi 5 board definitions (1 hour)
- Basic README update (30 min)
- Build testing (30 min)
- **Impact**: Unblocks modern Pi users immediately

**Phase 2 (Full Coverage - 4 hours)**:
- Add Pi 400, CM4, Zero 2W (1.5 hours)
- Complete documentation (2 hours)
- Hardware testing (30 min)
- **Impact**: Complete modern board coverage

**Phase 3 (Quality - 3 hours)**:
- Comprehensive testing (2 hours)
- CI/CD integration (30 min)
- Examples for new boards (30 min)
- **Impact**: Professional quality assurance

---

## Dependencies and Risks

### Dependencies

**Requires**:
- ⬜ None - board definitions are standalone

**Enabled by**:
- ✅ **Priority 2: Framework Ecosystem** - lgpio framework enables Pi 5 support
- ✅ **Priority 1: Cross-Compilation** - Enables testing board definitions from dev machines

**Enables**:
- ✅ **Priority 4: CI/CD** - More boards to test in automation
- ✅ **User adoption** - Modern hardware support attracts users

---

### Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Incorrect board specs | Low | Medium | Cross-reference official datasheets, test on hardware |
| Framework incompatibility (Pi 5 + pigpio) | Medium | Low | Document clearly, builder script check (Priority 2) |
| 32-bit vs 64-bit confusion | High | Low | Clear documentation, examples for both |
| Missing boards users want | Medium | Low | Community can submit PRs for additional boards |
| Non-RPi boards requested | Low | Low | Defer to Phase 2, evaluate demand |

---

### Known Limitations

**After implementation, these will remain**:

1. **No 64-bit optimized builds by default**:
   - Board definitions default to 32-bit (armhf)
   - **Rationale**: Backward compatibility, single toolchain simplicity
   - **Mitigation**: Document 64-bit build process (see Architecture Strategy)

2. **Pi 5 lgpio requirement**:
   - Cannot use pigpio on Pi 5 (hardware incompatible)
   - **Rationale**: Hardware limitation (RP1 I/O controller change)
   - **Mitigation**: Builder script check (Priority 2), documentation

3. **No Compute Module-specific features**:
   - CM4 board definition doesn't expose PCIe, custom GPIO layout
   - **Rationale**: Requires carrier-board-specific configuration
   - **Mitigation**: Users can customize via platformio.ini build_flags

4. **No non-Raspberry Pi boards**:
   - Focus on Raspberry Pi only initially
   - **Rationale**: Different GPIO ecosystems, limited demand validation
   - **Mitigation**: Add in Phase 2 if users request

---

## References & Sources

**All detailed references are in [REFERENCES.md](REFERENCES.md)**

**Key sources used in this analysis**:

### Raspberry Pi Official Documentation
1. **Raspberry Pi 4 Datasheet**: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf
   - BCM2711 specifications, GPIO, release March 2024
2. **Raspberry Pi 4 Specifications**: https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/
   - Official product page, RAM variants
3. **Raspberry Pi 5 Specifications**: https://www.raspberrypi.com/products/raspberry-pi-5/specifications/
   - BCM2712, Cortex-A76, RP1 I/O controller
4. **Raspberry Pi Processors Documentation**: https://www.raspberrypi.com/documentation/computers/processors.html
   - BCM2711, BCM2712, RP3A0 technical details
5. **Raspberry Pi 400 Specifications**: https://www.raspberrypi.com/products/raspberry-pi-400/specifications/
   - BCM2711C0 @ 1.8GHz, keyboard form factor
6. **Compute Module 4 Product Brief**: https://datasheets.raspberrypi.com/cm4/cm4-product-brief.pdf
   - Industrial specs, 100-pin connectors
7. **Raspberry Pi Zero 2 W Product Brief**: https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf
   - RP3A0 SiP, BCM2710A1 die

### Technical Analyses
8. **RP3A0 Teardown (Jeff Geerling)**: https://www.jeffgeerling.com/blog/2021/look-inside-raspberry-pi-zero-2-w-and-rp3a0-au
   - Internal analysis of Zero 2 W processor
9. **Raspberry Pi 4 C0 Stepping (Jeff Geerling)**: https://www.jeffgeerling.com/blog/2021/raspberry-pi-4-model-bs-arriving-newer-c0-stepping
   - BCM2711C0 improvements, higher clock
10. **BCM2711/BCM2712 Comparison**: https://www.cpu-monkey.com/en/cpu-raspberry_pi_4_b_broadcom_bcm2711
    - CPU benchmarks, specifications

### Community Resources
11. **Raspberry Pi Forums - Processor Discussion**: https://forums.raspberrypi.com/viewtopic.php?t=355555
    - Understanding CPU architectures, ARMv7 vs ARMv8
12. **Raspberry Pi 5 Announcement**: https://dataconomy.com/2023/09/28/pi5-raspberry-pi-5-specs-bcm2712/
    - BCM2712 details, performance improvements

### Local Files
13. **platform-linux_arm/boards/raspberrypi_3b.json**: Lines 1-17 (local)
    - Current board definition template

---

**Document Status**:
- ✅ Research complete
- ✅ Hardware specifications documented (5 new boards)
- ✅ Board definition files designed (complete JSON)
- ✅ Architecture strategy defined (32-bit vs 64-bit)
- ✅ Testing strategy provided
- ✅ Documentation requirements specified
- ⬜ References added to REFERENCES.md (next step)
- ⬜ Implementation pending
