# libgpiod Setup and Usage Guide

## Overview

**libgpiod** is the official userspace library for the Linux kernel GPIO subsystem. It provides a standardized C API for GPIO control across all Linux-based single-board computers (SBCs).

### Why libgpiod?

- ✅ **Official Linux Standard**: Maintained by Linux kernel developers
- ✅ **Universal SBC Support**: Works on Raspberry Pi, Orange Pi, Rock Pi, Odroid, NanoPi, etc.
- ✅ **Kernel-Enforced Exclusivity**: Only one process can claim a GPIO line at a time
- ✅ **Future-Proof**: Uses kernel character device interface (`/dev/gpiochip*`)
- ✅ **Clean Resource Management**: Kernel automatically cleans up on process exit
- ✅ **Portable**: Same API across different ARM SBCs and architectures

### When to Use libgpiod

**Choose libgpiod when:**
- Building system services or daemons
- Targeting multiple SBC platforms (not just Raspberry Pi)
- Need guaranteed GPIO exclusivity
- Want the most portable solution
- Building production deployments

**Consider alternatives when:**
- Need I2C/SPI/PWM in the same library → Use `lgpio` (Raspberry Pi only)
- Need hardware-timed PWM on Pi 1-4 → Use `pigpio` (legacy, no Pi 5)
- Rapid prototyping on Raspberry Pi → Use `lgpio` for convenience

## Architecture Overview

### Character Device Interface

libgpiod uses the Linux GPIO character device interface:

```
/dev/gpiochip0  → Main GPIO controller (BCM2835/BCM2711/RP1 on Raspberry Pi)
/dev/gpiochip1  → Additional GPIO controllers (if present)
```

### Key Concepts

1. **GPIO Chips**: Hardware GPIO controllers (e.g., `/dev/gpiochip0`)
2. **GPIO Lines**: Individual GPIO pins (numbered by kernel, not always same as physical pin)
3. **Line Requests**: Must request (claim) lines before use
4. **Exclusivity**: Only one consumer can request a line at a time
5. **Resource Cleanup**: Lines are automatically released when process exits

### Threading Model

- **Basic GPIO operations**: Direct `ioctl()` syscalls, no background threads
- **Event monitoring**: Application must implement polling loop for interrupts
- **No daemon**: Unlike `pigpiod`, no persistent background service required

## Installation

### Recommended: Build from Source (Automated Script)

**⚠️ Ubuntu 24.04 (Noble) Multiarch Issue**: Ubuntu 24.04 no longer provides ARM packages on the main security repositories for cross-architecture installation (multiarch). This causes 404 errors when trying to install `libgpiod-dev:armhf` or `libgpiod-dev:arm64`. The build-from-source approach is now the recommended method for all Ubuntu versions.

The easiest way to set up libgpiod for cross-compilation is using the provided setup script:

```bash
# Install build dependencies
sudo apt-get install -y \
  autoconf autoconf-archive automake libtool pkg-config \
  gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf \
  gcc-aarch64-linux-gnu g++-aarch64-linux-gnu

# Build and install for 32-bit ARM (armhf)
./scripts/setup-libgpiod-cross.sh

# Build and install for 64-bit ARM (aarch64)
CROSS_PREFIX=aarch64-linux-gnu- \
INSTALL_DIR=$HOME/.local/aarch64-linux-gnu \
./scripts/setup-libgpiod-cross.sh
```

The script will:
- Clone libgpiod from the official kernel.org repository
- Check out the latest stable version (v2.x)
- Cross-compile using autotools
- Install headers, libraries, and tools to `~/.local/arm-linux-gnueabihf/` or `~/.local/aarch64-linux-gnu/`

### Option 1: System Package (Multiarch) - Deprecated

**⚠️ Warning**: This method fails on Ubuntu 24.04 (Noble) due to missing ARM packages on security repositories. Use the build-from-source approach instead.

<details>
<summary>Click to expand legacy multiarch instructions (Ubuntu 22.04 and earlier only)</summary>

#### 32-bit ARM (armhf)

```bash
# Enable armhf architecture
sudo dpkg --add-architecture armhf
sudo apt update

# Install libgpiod for armhf
sudo apt install libgpiod-dev:armhf libgpiod2:armhf

# Install cross-compilation toolchain
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf
```

#### 64-bit ARM (arm64)

```bash
# Enable arm64 architecture
sudo dpkg --add-architecture arm64
sudo apt update

# Install libgpiod for arm64
sudo apt install libgpiod-dev:arm64 libgpiod2:arm64

# Install cross-compilation toolchain
sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
```

</details>

### Option 2: Manual Build from Source

For more control or custom install location:

```bash
# Clone libgpiod repository
git clone https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git
cd libgpiod

# Check out stable version (optional)
git checkout v2.1  # Or latest stable tag

# Install build dependencies
sudo apt install autoconf autoconf-archive automake libtool pkg-config

# For 32-bit ARM (armhf)
./autogen.sh --enable-tools=yes --enable-bindings-cxx \
  --prefix=$HOME/.local/arm-linux-gnueabihf \
  --host=arm-linux-gnueabihf \
  CC=arm-linux-gnueabihf-gcc \
  CXX=arm-linux-gnueabihf-g++

# For 64-bit ARM (arm64)
./autogen.sh --enable-tools=yes --enable-bindings-cxx \
  --prefix=$HOME/.local/aarch64-linux-gnu \
  --host=aarch64-linux-gnu \
  CC=aarch64-linux-gnu-gcc \
  CXX=aarch64-linux-gnu-g++

# Build and install
make -j$(nproc)
make install
```

### Option 3: Native Installation (On Raspberry Pi)

If building directly on a Raspberry Pi:

```bash
sudo apt update
sudo apt install libgpiod-dev gpiod
```

The `gpiod` package provides command-line tools like `gpiodetect`, `gpioinfo`, `gpioset`, `gpioget`.

## GPIO State Persistence

### Important Caveat

⚠️ **By default, GPIO lines may revert to their default state when your program exits.**

This is a key difference from libraries like `lgpio`, `pigpio`, and `WiringPi`, which typically maintain GPIO state after program exit.

### Raspberry Pi: Enable Persistent State

On Raspberry Pi, enable the `strict_gpiod` device tree parameter:

#### For Raspberry Pi OS (Bookworm and later)

Edit `/boot/firmware/config.txt`:

```bash
sudo nano /boot/firmware/config.txt
```

Add this line:

```
dtparam=strict_gpiod
```

#### For Older Raspberry Pi OS (Bullseye and earlier)

Edit `/boot/config.txt`:

```bash
sudo nano /boot/config.txt
```

Add this line:

```
dtparam=strict_gpiod
```

#### Apply Changes

```bash
sudo reboot
```

### What Does `strict_gpiod` Do?

- **Without `strict_gpiod`**: GPIO lines revert to default state (usually input) when process exits
- **With `strict_gpiod`**: GPIO lines maintain their state (output high/low) after process exits

### Other SBCs

Check your SBC's documentation for equivalent device tree parameters or kernel options.

## API Versions

libgpiod has two major API versions with different design philosophies.

### Version 1.x (Legacy API)

**Characteristics:**
- Simpler, function-based API
- Widely deployed (Debian Bullseye, Ubuntu 20.04)
- Less flexible but easier to learn
- Many online examples use this API

**Example:**

```c
#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    struct gpiod_chip *chip;
    struct gpiod_line *line;

    // Open GPIO chip
    chip = gpiod_chip_open_by_name("gpiochip0");
    if (!chip) {
        perror("gpiod_chip_open_by_name");
        return 1;
    }

    // Get GPIO line 23
    line = gpiod_chip_get_line(chip, 23);
    if (!line) {
        perror("gpiod_chip_get_line");
        gpiod_chip_close(chip);
        return 1;
    }

    // Request line as output
    if (gpiod_line_request_output(line, "example", 0) < 0) {
        perror("gpiod_line_request_output");
        gpiod_chip_close(chip);
        return 1;
    }

    // Blink LED
    for (int i = 0; i < 10; i++) {
        gpiod_line_set_value(line, 1);
        sleep(1);
        gpiod_line_set_value(line, 0);
        sleep(1);
    }

    // Cleanup (automatic on exit, but explicit is better)
    gpiod_line_release(line);
    gpiod_chip_close(chip);

    return 0;
}
```

### Version 2.x (Modern API)

**Characteristics:**
- More flexible, object-oriented design
- Better support for bulk operations
- More configuration options
- Recommended for new projects
- Available in Debian Bookworm, Ubuntu 22.04+

**Example:**

```c
#include <gpiod.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    struct gpiod_chip *chip;
    struct gpiod_request_config *req_cfg;
    struct gpiod_line_config *line_cfg;
    struct gpiod_line_request *request;
    unsigned int offsets[1] = {23};

    // Open GPIO chip
    chip = gpiod_chip_open("/dev/gpiochip0");
    if (!chip) {
        perror("gpiod_chip_open");
        return 1;
    }

    // Create request configuration
    req_cfg = gpiod_request_config_new();
    gpiod_request_config_set_consumer(req_cfg, "example");

    // Create line configuration
    line_cfg = gpiod_line_config_new();
    gpiod_line_config_set_direction_default(line_cfg, GPIOD_LINE_DIRECTION_OUTPUT);
    gpiod_line_config_set_output_value_default(line_cfg, 0);

    // Request lines
    request = gpiod_chip_request_lines(chip, req_cfg, line_cfg);
    if (!request) {
        perror("gpiod_chip_request_lines");
        gpiod_line_config_free(line_cfg);
        gpiod_request_config_free(req_cfg);
        gpiod_chip_close(chip);
        return 1;
    }

    // Blink LED
    for (int i = 0; i < 10; i++) {
        gpiod_line_request_set_value(request, 23, 1);
        sleep(1);
        gpiod_line_request_set_value(request, 23, 0);
        sleep(1);
    }

    // Cleanup
    gpiod_line_request_release(request);
    gpiod_line_config_free(line_cfg);
    gpiod_request_config_free(req_cfg);
    gpiod_chip_close(chip);

    return 0;
}
```

### API Version Detection

The PlatformIO framework automatically detects which API version is installed and defines:

- `LIBGPIOD_V1` for version 1.x
- `LIBGPIOD_V2` for version 2.x

You can use conditional compilation:

```c
#include <gpiod.h>

#ifdef LIBGPIOD_V2
    // Use v2 API
    struct gpiod_chip *chip = gpiod_chip_open("/dev/gpiochip0");
#else
    // Use v1 API
    struct gpiod_chip *chip = gpiod_chip_open_by_name("gpiochip0");
#endif
```

## GPIO Pin Numbering

### Raspberry Pi

libgpiod uses **kernel GPIO numbering**, which corresponds to **BCM GPIO numbers** on Raspberry Pi:

| Physical Pin | BCM GPIO | libgpiod Line |
|--------------|----------|---------------|
| 11           | GPIO17   | 17            |
| 13           | GPIO27   | 27            |
| 15           | GPIO22   | 22            |
| 16           | GPIO23   | 23            |
| 18           | GPIO24   | 24            |

**Note**: This is the same numbering as BCM mode in WiringPi and RPi.GPIO.

### Finding GPIO Numbers

Use the `gpioinfo` command-line tool:

```bash
gpioinfo

# Output:
# gpiochip0 - 54 lines:
#   line   0:      "ID_SDA"       unused   input  active-high
#   line   1:      "ID_SCL"       unused   input  active-high
#   line  17:     "GPIO17"       unused   input  active-high
#   ...
```

### Other SBCs

GPIO numbering varies by SBC. Always use `gpioinfo` to identify the correct line numbers for your board.

## Common Operations

### Input with Pull-up/Pull-down

```c
// v1.x API
gpiod_line_request_input_flags(line, "example",
    GPIOD_LINE_REQUEST_FLAG_BIAS_PULL_UP);

int value = gpiod_line_get_value(line);

// v2.x API
gpiod_line_config_set_direction_default(line_cfg, GPIOD_LINE_DIRECTION_INPUT);
gpiod_line_config_set_bias_default(line_cfg, GPIOD_LINE_BIAS_PULL_UP);

int value = gpiod_line_request_get_value(request, line_offset);
```

### Edge Detection (Interrupts)

```c
// v1.x API
gpiod_line_request_rising_edge_events(line, "example");

struct gpiod_line_event event;
struct timespec timeout = {1, 0};  // 1 second

int ret = gpiod_line_event_wait(line, &timeout);
if (ret > 0) {
    gpiod_line_event_read(line, &event);
    printf("Event detected!\n");
}

// v2.x API
gpiod_line_config_set_edge_detection_default(line_cfg, GPIOD_LINE_EDGE_RISING);

struct gpiod_edge_event_buffer *buffer = gpiod_edge_event_buffer_new(1);
struct timespec timeout = {1, 0};

int ret = gpiod_line_request_wait_edge_events(request, &timeout);
if (ret > 0) {
    gpiod_line_request_read_edge_events(request, buffer, 1);
    printf("Event detected!\n");
}
```

## Comparison with Other Libraries

### libgpiod vs lgpio

| Feature | libgpiod | lgpio |
|---------|----------|-------|
| **Target** | Universal Linux | Raspberry Pi focused |
| **Standards** | Official kernel API | Third-party library |
| **Threading** | Direct ioctl calls | May spawn threads for callbacks |
| **Exclusivity** | ✅ Kernel-enforced | ❌ Not guaranteed |
| **Multi-protocol** | ❌ GPIO only | ✅ GPIO+I2C+SPI+PWM+UART |
| **State Persistence** | ⚠️ Requires dtparam | ✅ Maintains state |
| **SBC Support** | ✅ Any with chardev | ⚠️ Primarily RPi |

**Recommendation**:
- Use **libgpiod** for portability, daemons, and multi-SBC support
- Use **lgpio** for Raspberry Pi projects needing multi-protocol convenience

### libgpiod vs pigpio

| Feature | libgpiod | pigpio |
|---------|----------|--------|
| **Pi 5 Support** | ✅ Yes | ❌ No |
| **Architecture** | Kernel chardev | Direct register access |
| **Future-proof** | ✅ Yes | ❌ Legacy |
| **Daemon** | ❌ Not required | ⚠️ Required (pigpiod) |
| **Timing** | ⚠️ Standard | ✅ Microsecond (DMA) |
| **PWM** | ❌ None | ✅ Hardware PWM |

**Recommendation**: Use **libgpiod** unless you need pigpio's unique DMA-timed PWM on Pi 1-4.

### libgpiod vs WiringPi

| Feature | libgpiod | WiringPi |
|---------|----------|----------|
| **Maintenance** | ✅ Active | ⚠️ Deprecated |
| **Pi 5 Support** | ✅ Yes | ⚠️ Partial (GC2 fork) |
| **Cross-compilation** | ✅ Yes | ❌ No |
| **Pin Numbering** | BCM | WiringPi/BCM/Physical |
| **API Style** | Modern C | Arduino-like |

**Recommendation**: Migrate from WiringPi to **libgpiod** for maintained, portable code.

## CI/CD Integration

The platform's CI workflow automatically builds libgpiod from source for both ARM architectures. This ensures consistent, reliable builds across all Ubuntu versions without dependency on external package repositories.

### Workflow Steps

1. Install autotools and cross-compilers
2. Run `setup-libgpiod-cross.sh` for armhf (32-bit)
3. Run `setup-libgpiod-cross.sh` for aarch64 (64-bit)
4. Build examples with PlatformIO

This approach:
- ✅ Works on Ubuntu 22.04, 24.04, and future versions
- ✅ Uses official kernel.org source code
- ✅ No external package repository dependencies
- ✅ Consistent with lgpio build pattern
- ✅ Provides latest stable libgpiod version (v2.x)

## Troubleshooting

### Error: Ubuntu 24.04 multiarch 404 errors

**Symptom**:
```
E: Failed to fetch https://security.ubuntu.com/ubuntu/dists/noble/main/binary-armhf/Packages  404  Not Found
```

**Cause**: Ubuntu 24.04 (Noble) no longer provides ARM packages on the main security repositories for cross-architecture installation.

**Solution**: Use the build-from-source approach instead of multiarch:
```bash
# Install build dependencies
sudo apt-get install -y \
  autoconf autoconf-archive automake libtool pkg-config \
  gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf

# Build and install
./scripts/setup-libgpiod-cross.sh
```

### Error: "Permission denied" when opening `/dev/gpiochip0`

Add your user to the `gpio` group:

```bash
sudo usermod -a -G gpio $USER
```

Log out and log back in for group changes to take effect.

### Error: "Device or resource busy"

Another process has already requested that GPIO line. libgpiod enforces exclusivity.

**Check what's using the GPIO:**

```bash
gpioinfo | grep -A 1 "line  23"
```

Output will show if the line is in use:

```
line  23:     "GPIO23"  "some-app"  output  active-high [used]
```

### GPIO Line Numbers Don't Match Physical Pins

Use `gpioinfo` to find the correct mapping for your board. Don't assume BCM numbering on non-Raspberry Pi SBCs.

### State Doesn't Persist After Program Exits

Enable `dtparam=strict_gpiod` in `/boot/config.txt` (Raspberry Pi). See "GPIO State Persistence" section above.

### Cross-compilation Fails to Find libgpiod

Ensure you've installed the correct architecture:

```bash
# Check installed packages
dpkg -l | grep libgpiod

# Should see both:
# libgpiod-dev:armhf
# libgpiod2:armhf
```

If missing, install multiarch packages as described in "Installation" section.

## Command-Line Tools

libgpiod includes useful command-line utilities (part of the `gpiod` package):

### gpiodetect

List all GPIO chips:

```bash
gpiodetect

# Output:
# gpiochip0 [pinctrl-bcm2711] (58 lines)
```

### gpioinfo

Show detailed information about all GPIO lines:

```bash
gpioinfo

# Or for specific chip:
gpioinfo gpiochip0
```

### gpioget

Read GPIO input:

```bash
gpioget gpiochip0 23

# Output: 0 or 1
```

### gpioset

Set GPIO output:

```bash
# Set GPIO 23 high
gpioset gpiochip0 23=1

# Set GPIO 23 low
gpioset gpiochip0 23=0

# Hold the line (doesn't exit, maintains state)
gpioset --mode=wait gpiochip0 23=1
```

### gpiomon

Monitor GPIO for events:

```bash
# Monitor GPIO 23 for rising edges
gpiomon --rising-edge gpiochip0 23

# Monitor for both edges
gpiomon --edges=both gpiochip0 23
```

## References

### Official Documentation

- **libgpiod Documentation**: https://libgpiod.readthedocs.io/
- **libgpiod Git Repository**: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
- **Linux GPIO Documentation**: https://www.kernel.org/doc/html/latest/driver-api/gpio/

### Raspberry Pi Resources

- **Raspberry Pi GPIO White Paper**: https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/
- **Raspberry Pi Forums**: https://forums.raspberrypi.com/

### Tutorials

- **Migrating from sysfs to libgpiod**: https://www.embeddedpi.com/documentation/gpio-interfaces/libgpiod-guide
- **libgpiod on Libre Computer Boards**: https://hub.libre.computer/t/how-to-use-libgpiod-on-libre-computer-boards/73

## Next Steps

1. Install libgpiod for your target architecture (see "Installation" section)
2. Enable GPIO state persistence with `dtparam=strict_gpiod` (Raspberry Pi)
3. Try the example projects:
   - `examples/libgpiod-blink/` - Basic LED blink (v1 API)
   - `examples/libgpiod-blink-v2/` - LED blink (v2 API)
   - `examples/libgpiod-button/` - Button input with interrupts
4. Build and deploy to your target device

Happy GPIO coding! 🎉
