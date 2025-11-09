# Round 2 - Priority 2: Framework Ecosystem Modernization

**Date**: 2025-11-09
**Round**: 2
**Status**: Complete
**Related Documents**: [01-initial-assessment.md](01-initial-assessment.md), [REFERENCES.md](REFERENCES.md)

---

## Executive Summary

**Current State**: Platform supports only WiringPi framework, which was officially deprecated in 2019. While a community fork (GC2) maintains WiringPi with Raspberry Pi 5 support, relying on a single deprecated framework severely limits platform utility.

**Root Cause**:
- No framework diversification since platform creation
- No modern GPIO alternatives (pigpio, lgpio, libgpiod)
- No bare-metal option for non-GPIO applications

**Proposed Solution**:
1. **Add lgpio framework** - Modern, Pi 5-compatible, maintained by pigpio author
2. **Add pigpio framework** - Feature-rich, Pi 4 and earlier, widely used
3. **Add bare-metal option** - Framework-less builds for generic Linux apps
4. **Keep WiringPi** - Update to GC2 fork for legacy support
5. **Add libgpiod option** - Platform-independent, kernel-based (advanced users)

**Critical Findings**:
- **lgpio** is the **recommended modern choice** - works on all Pi models including Pi 5, maintained by Joan (pigpio author)
- **pigpio** is widely deployed but **doesn't work on Pi 5** due to hardware changes
- **WiringPi GC2 fork** (2024+) adds Pi 5 support, reviving the deprecated library
- **libgpiod** is kernel-standard but has poor documentation (v1.6) and v2 not yet in Pi OS
- All frameworks can use **system packages** (apt install) - no PlatformIO packaging required initially

**Recommended Actions**:
1. **Immediate**: Add bare-metal/framework-less option (1-2 hours, unblocks non-GPIO use cases)
2. **High Priority**: Add lgpio framework with builder script (3-4 hours, modern Pi 5 support)
3. **High Priority**: Add pigpio framework for Pi 4 and earlier (2-3 hours, battle-tested library)
4. **Medium Priority**: Update WiringPi to GC2 fork (1-2 hours, adds Pi 5 support)
5. **Documentation**: Create framework selection guide and migration examples (2-3 hours)

---

## Detailed Findings

### Current State: WiringPi Framework

**builder/frameworks/wiringpi.py** (current implementation):
```python
env.Replace(
    CPPFLAGS=["-O2", "-Wformat=2", "-Wall", "-Winline", "-pipe", "-fPIC"],
    LIBS=["pthread"]
)

env.Append(
    CPPDEFINES=["_GNU_SOURCE"],
    CPPPATH=[
        join(env.PioPlatform().get_package_dir("framework-wiringpi"), "wiringPi")
    ]
)

libs = []
libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkWiringPi"),
    join(env.PioPlatform().get_package_dir("framework-wiringpi"), "wiringPi")
))

env.Append(LIBS=libs)
```

**Pattern Analysis**:
- Sets compiler flags: `-O2`, `-Wall`, `-fPIC`
- Defines `_GNU_SOURCE` macro
- Links pthread library
- Adds framework include path from PIO package
- Builds framework library from package directory
- Simple, functional, ~67 lines total

**Limitations**:
- ❌ Cross-compilation blocked (platform.py:34-39)
- ❌ Uses deprecated original WiringPi (2019), not GC2 fork (2024+)
- ⚠️ PIO package `framework-wiringpi` version ~1.242.0 outdated
- ✅ Works on Pi 1-4 for native builds

---

## GPIO Framework Comparison

### Framework Feature Matrix

| Framework | Maintainer | Status (2024) | Pi 5 Support | Cross-Compile | Features | Performance | License |
|-----------|-----------|---------------|--------------|---------------|----------|-------------|---------|
| **lgpio** | Joan (pigpio author) | ✅ Active | ✅ Yes | ✅ Yes | GPIO, PWM, I2C, SPI, serial, callbacks, notifications | Fast (~523k toggles/sec) | Unlicense (Public Domain) |
| **pigpio** | Joan | ⚠️ Maintained | ❌ No (hardware incompatible) | ✅ Yes | GPIO, PWM (hardware-timed), I2C, SPI, serial, callbacks, waves, high-speed sampling | Very Fast (~7.9M toggles/sec) | Unlicense (Public Domain) |
| **WiringPi (original)** | Gordon Henderson | ❌ Deprecated (2019) | ❌ No | ❌ Blocked in PIO | GPIO, PWM, I2C, SPI, serial, Arduino-like API | Fastest (~7.9M toggles/sec) | LGPL v3 |
| **WiringPi (GC2)** | GC2 (community) | ✅ Active (2024+) | ✅ Yes (GCLK missing) | ❌ Blocked in PIO | Same as original + Pi 5 | Fast | LGPL v3 |
| **libgpiod** | Linux kernel | ✅ Active | ✅ Yes | ✅ Yes | GPIO (lines, events, chips), platform-independent | Unknown | LGPL v2.1+ |

**Legend**:
- ✅ Fully supported
- ⚠️ Partial support or limitations
- ❌ Not supported

---

### Framework Detailed Analysis

#### 1. lgpio - Recommended Modern Choice

**Website**: http://abyz.me.uk/lg/index.html
**Repository**: https://github.com/joan2937/lg
**Author**: Joan (same author as pigpio)
**Status**: ✅ **Actively maintained** (2024)

**Description**: lgpio is Joan's modern successor to pigpio, using `/dev/gpiochip` kernel interface instead of direct register access. Works on all Raspberry Pi models including Pi 5.

**Key Features**:
- GPIO read/write (single and groups)
- Software-timed PWM and wave generation
- Real-time callbacks on GPIO level changes
- Pipe-based notifications for GPIO state changes
- I2C, SPI, serial communication wrappers
- Network daemon interface (similar to pigpiod)

**Advantages**:
- ✅ **Pi 5 compatible** (uses kernel interface, not direct registers)
- ✅ Works on **all Pi models** (Pi 1-5, Zero, CM)
- ✅ **Actively maintained** by original pigpio author
- ✅ **Cross-compilation friendly** (no hardware dependencies)
- ✅ Clean, modern API (learned from pigpio experience)
- ✅ **Permissive license** (Unlicense - public domain)

**Disadvantages**:
- ⚠️ Slower than pigpio (~523k vs 7.9M toggles/sec) due to kernel interface
- ⚠️ Less mature ecosystem than pigpio (newer library)
- ⚠️ Fewer tutorials and examples available

**Installation**:
```bash
# Raspberry Pi OS (Debian/Ubuntu)
sudo apt install liblgpio-dev liblgpio1

# From source
wget https://github.com/joan2937/lg/archive/master.zip
unzip master.zip
cd lg-master
make
sudo make install
```

**C API Example (Basic GPIO)**:
```c
#include <stdio.h>
#include <lgpio.h>

int main() {
    int h = lgGpiochipOpen(0);  // Open GPIO chip 0
    if (h < 0) return 1;

    int gpio = 23;
    lgGpioClaimOutput(h, 0, gpio, 0);  // Set GPIO23 as output

    lgGpioWrite(h, gpio, 1);  // Write HIGH
    lgGpioWrite(h, gpio, 0);  // Write LOW

    lgGpiochipClose(h);
    return 0;
}
```

**Compile Flags**:
```bash
gcc -o program program.c -llgpio
```

**Link Libraries**: `-llgpio`

**Recommendation**: ⭐ **Primary framework choice** for new projects and Pi 5 compatibility.

---

#### 2. pigpio - Battle-Tested Legacy

**Website**: http://abyz.me.uk/rpi/pigpio/
**Repository**: https://github.com/joan2937/pigpio
**Author**: Joan
**Status**: ⚠️ **Maintained but Pi 5 incompatible**

**Description**: pigpio is Joan's original high-performance GPIO library using direct hardware register access. Widely deployed, feature-rich, but incompatible with Pi 5 due to hardware changes (new RP1 I/O controller).

**Key Features**:
- **Hardware-timed PWM** on all GPIO (DMA-based, very precise)
- High-speed GPIO sampling (up to 1 million samples/sec)
- Wave generation for complex PWM patterns
- GPIO callbacks, alerts, notifications
- I2C, SPI, serial communication
- Network daemon (pigpiod) for remote GPIO control

**Advantages**:
- ✅ **Very fast** (~7.9M GPIO toggles/sec - direct register access)
- ✅ **Hardware-timed PWM** (unique feature, microsecond precision)
- ✅ **Mature ecosystem** - extensive documentation, tutorials, examples
- ✅ **Widely deployed** in production systems
- ✅ **Cross-compilation friendly**

**Disadvantages**:
- ❌ **Pi 5 incompatible** (hardware register access no longer works)
- ⚠️ **Pi-specific** (Broadcom SoC only, won't work on other ARM Linux boards)
- ⚠️ Requires running as **root/sudo** for GPIO access

**Installation**:
```bash
# Raspberry Pi OS
sudo apt install pigpio libpigpio-dev

# From source
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```

**C API Example (Basic GPIO)**:
```c
#include <stdio.h>
#include <pigpio.h>

int main() {
    if (gpioInitialise() < 0) return 1;  // Initialize library

    int gpio = 23;
    gpioSetMode(gpio, PI_OUTPUT);  // Set GPIO23 as output

    gpioWrite(gpio, 1);  // Write HIGH
    gpioWrite(gpio, 0);  // Write LOW

    gpioTerminate();
    return 0;
}
```

**Compile Flags**:
```bash
gcc -Wall -pthread -o program program.c -lpigpio -lrt
```

**Link Libraries**: `-lpigpio -lrt -lpthread`

**Recommendation**: ✅ **Excellent choice for Pi 1-4**, avoid for Pi 5.

---

#### 3. WiringPi GC2 Fork - Revived Legacy

**Website**: http://wiringpi.com (original, defunct)
**Repository**: https://github.com/WiringPi/WiringPi (GC2 fork)
**Maintainer**: GC2 (Grazer Computer Club)
**Status**: ✅ **Actively maintained since 2024**

**Description**: Community fork of Gordon Henderson's original WiringPi (deprecated 2019). GC2 has taken over maintenance, adding Pi 5 support and new OS compatibility.

**Key Features**:
- **Arduino-like API** (pinMode, digitalWrite, digitalRead, analogWrite)
- GPIO, PWM, I2C, SPI, serial
- Pin numbering schemes (WiringPi, BCM, physical)
- Familiar to Arduino developers

**Advantages**:
- ✅ **Pi 5 support** (GC2 fork adds compatibility, except GCLK function)
- ✅ **Arduino-like API** (easy migration for Arduino users)
- ✅ **Fast** (~7.9M toggles/sec - direct register access)
- ✅ **Community maintained** (GC2 organization, not individual)

**Disadvantages**:
- ❌ **Cross-compilation blocked in PlatformIO** (platform.py:34-39)
- ⚠️ **Legacy codebase** (technical debt from 2012-2019 development)
- ⚠️ **Pi-specific** (Broadcom SoC only)
- ⚠️ Platform's `framework-wiringpi` package outdated (uses original, not GC2)

**Installation**:
```bash
# GC2 fork (recommended)
sudo apt install wiringpi

# Or from source
git clone https://github.com/WiringPi/WiringPi.git
cd WiringPi
./build
```

**C API Example (Basic GPIO)**:
```c
#include <wiringPi.h>

int main() {
    wiringPiSetup();  // Initialize using WiringPi pin numbering

    int pin = 2;  // WiringPi pin 2 (BCM GPIO 27)
    pinMode(pin, OUTPUT);

    digitalWrite(pin, HIGH);
    digitalWrite(pin, LOW);

    return 0;
}
```

**Compile Flags**:
```bash
gcc -o program program.c -lwiringPi -lpthread
```

**Link Libraries**: `-lwiringPi -lpthread`

**Recommendation**: ✅ **Good for legacy projects**, but lgpio preferred for new work.

---

#### 4. libgpiod - Kernel-Standard (Advanced)

**Website**: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git
**Repository**: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git
**Maintainer**: Linux kernel community (Bartosz Golaszewski)
**Status**: ✅ **Active** (kernel-standard library)

**Description**: Official Linux kernel GPIO library using character device interface (`/dev/gpiochipN`). Platform-independent, works on any Linux system with GPIO.

**Key Features**:
- GPIO line management (request, release, get/set values)
- Event monitoring (rising/falling edge detection)
- Platform-independent (works on any ARM Linux board, not just Pi)
- Standard kernel interface (`/dev/gpiochip`)

**Advantages**:
- ✅ **Platform-independent** (works on BeagleBone, ODROID, Orange Pi, etc.)
- ✅ **Kernel-standard** (official Linux GPIO interface)
- ✅ **Pi 5 compatible** (uses character device, not registers)
- ✅ **Cross-compilation friendly**

**Disadvantages**:
- ❌ **Poor documentation** for v1.6 (Raspberry Pi OS Bookworm version)
- ❌ **No examples** for v1.6 (v2 has examples but not yet in Pi OS)
- ⚠️ **v2 not packaged** for Raspberry Pi OS yet (users must build from source)
- ⚠️ **Different API** between v1.6 and v2.x (migration barrier)
- ⚠️ **Less feature-rich** than pigpio/lgpio (basic GPIO only)

**Installation**:
```bash
# Raspberry Pi OS (v1.6.3 - old version)
sudo apt install libgpiod-dev gpiod

# v2.x requires building from source (not yet in Pi OS repos)
```

**C API Example (v1.6 - Bookworm)**:
```c
#include <gpiod.h>

int main() {
    struct gpiod_chip *chip = gpiod_chip_open_by_name("gpiochip0");
    struct gpiod_line *line = gpiod_chip_get_line(chip, 23);

    gpiod_line_request_output(line, "example", 0);

    gpiod_line_set_value(line, 1);  // Write HIGH
    gpiod_line_set_value(line, 0);  // Write LOW

    gpiod_line_release(line);
    gpiod_chip_close(chip);
    return 0;
}
```

**Compile Flags**:
```bash
gcc -o program program.c -lgpiod
```

**Link Libraries**: `-lgpiod`

**Recommendation**: ⚠️ **Advanced users only** - wait for v2 in Pi OS or use lgpio instead.

---

### Framework Selection Guide

#### Use lgpio if:
- ✅ You need **Pi 5 support**
- ✅ You want a **modern, maintained** library
- ✅ You're starting a **new project**
- ✅ You need **cross-compilation**
- ✅ You value **clean API** and **future-proofing**

#### Use pigpio if:
- ✅ You need **hardware-timed PWM** (unique feature)
- ✅ You're targeting **Pi 4 or earlier**
- ✅ You need **high-speed GPIO** (sampling, fast toggles)
- ✅ You have **existing pigpio code** to migrate
- ⚠️ Pi 5 is **not** in your deployment plan

#### Use WiringPi (GC2) if:
- ✅ You have **legacy WiringPi code**
- ✅ You prefer **Arduino-like API** (digitalWrite, etc.)
- ✅ You're **not cross-compiling** (native Pi build only)
- ⚠️ Accept **technical debt** of legacy codebase

#### Use libgpiod if:
- ✅ You need **platform-independence** (non-Pi ARM boards)
- ✅ You're comfortable with **sparse documentation**
- ✅ You're building **professional/enterprise** systems
- ⚠️ Wait for **v2 in Pi OS** or build from source

#### Use bare-metal (no framework) if:
- ✅ You're building **non-GPIO applications** (servers, utilities, data processing)
- ✅ You don't need GPIO access
- ✅ You want **minimal dependencies**

---

## Framework Packaging Strategy

### Recommended Approach: System Dependencies

**Rationale**: All GPIO frameworks are available via `apt install` on Raspberry Pi OS. Creating PlatformIO packages is unnecessary overhead and duplicates system package management.

**Advantages**:
- ✅ Users get **latest versions** from OS repos
- ✅ **Zero maintenance burden** for PlatformIO platform
- ✅ Leverages existing **Debian/Ubuntu packaging** infrastructure
- ✅ Works for both **native and cross-compilation** (install libs on host)

**Disadvantages**:
- ⚠️ Users must **manually install** frameworks
- ⚠️ No automatic dependency resolution (must document)
- ⚠️ Cross-compilation requires **ARM libraries on x86_64 host**

### Implementation Strategy

**Phase 1**: Document system dependencies (immediate)
```markdown
## Framework Installation

### lgpio
sudo apt install liblgpio-dev liblgpio1

### pigpio
sudo apt install libpigpio-dev pigpio

### WiringPi (GC2 fork)
sudo apt install wiringpi

### libgpiod
sudo apt install libgpiod-dev gpiod
```

**Phase 2**: Enhance builder scripts to check for libraries (optional)
```python
# In builder/frameworks/lgpio.py
import os

# Check if library exists
if not os.path.exists("/usr/lib/arm-linux-gnueabihf/liblgpio.so"):
    print("WARNING: lgpio not found. Install with: sudo apt install liblgpio-dev")
```

**Phase 3**: Create PlatformIO packages (future, if demand exists)
- Package pre-built libraries for cross-compilation
- Submit to PlatformIO registry
- Requires ongoing maintenance for new releases

**Recommended**: **Phase 1 only** - document system dependencies, avoid packaging complexity.

---

### Cross-Compilation Considerations

**Challenge**: Cross-compiling requires ARM libraries on x86_64 host.

**Solution 1**: Install ARM cross-libraries (Debian/Ubuntu)
```bash
# For armhf (32-bit ARM)
sudo dpkg --add-architecture armhf
sudo apt update
sudo apt install liblgpio-dev:armhf libpigpio-dev:armhf

# For arm64 (64-bit ARM)
sudo dpkg --add-architecture arm64
sudo apt install liblgpio-dev:arm64
```

**Solution 2**: Build frameworks from source with cross-compiler
```bash
# Build lgpio for ARM on x86_64 host
git clone https://github.com/joan2937/lg.git
cd lg
make CC=arm-linux-gnueabihf-gcc
# Copy libraries to project or system path
```

**Solution 3**: Use sysroot approach (advanced)
```bash
# Extract RPi OS filesystem as sysroot
# Point cross-compiler to sysroot for libraries
export PKG_CONFIG_PATH=/path/to/sysroot/usr/lib/arm-linux-gnueabihf/pkgconfig
arm-linux-gnueabihf-gcc --sysroot=/path/to/sysroot ...
```

**Recommendation for PlatformIO platform**:
- **Document Solution 1** (simplest for Debian/Ubuntu users)
- **Provide Solution 2 script** for other platforms
- **Defer Solution 3** (too complex for initial implementation)

---

## Framework Builder Scripts

### Pattern: Based on wiringpi.py

All framework builders follow similar structure:
1. Set compiler flags
2. Define macros
3. Link required libraries
4. Add include paths
5. Optionally build framework library

---

### Bare-Metal (Framework-Less) Builder

**File**: `builder/frameworks/baremetal.py`

```python
# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Bare-Metal (Framework-Less)

Build native Linux ARM applications without GPIO framework dependencies.
Use this for servers, utilities, data processing, or any non-GPIO applications.
"""

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

# Minimal compiler flags for generic Linux applications
env.Replace(
    CPPFLAGS=[
        "-O2",           # Optimize for speed
        "-Wall",         # Enable warnings
        "-Wextra",       # Extra warnings
        "-pipe"          # Use pipes instead of temp files
    ]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE",   # Enable GNU extensions
        "_POSIX_C_SOURCE=200809L"  # Enable POSIX.1-2008 features
    ],

    LIBS=[
        "pthread",       # POSIX threads (commonly needed)
        "rt",            # Real-time extensions (timers, etc.)
        "m"              # Math library
    ]
)

# No framework library to build - just standard libraries
```

**Usage** (in platformio.ini):
```ini
[env:myapp]
platform = linux_arm
board = raspberrypi_4b
; No framework specified = bare-metal build
```

**Effort**: 30 min (create file, test)

---

### lgpio Framework Builder

**File**: `builder/frameworks/lgpio.py`

```python
# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
lgpio

lgpio is a modern C library for Linux GPIO access using the /dev/gpiochip
kernel interface. Works on all Raspberry Pi models including Pi 5.
Successor to pigpio by the same author (Joan).

http://abyz.me.uk/lg/index.html
https://github.com/joan2937/lg

Installation:
    sudo apt install liblgpio-dev liblgpio1

Cross-compilation (Debian/Ubuntu):
    sudo dpkg --add-architecture armhf
    sudo apt update
    sudo apt install liblgpio-dev:armhf
"""

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

env.Replace(
    CPPFLAGS=[
        "-O2",           # Optimize for speed
        "-Wall",         # Enable warnings
        "-Wextra",       # Extra warnings
        "-pipe",         # Use pipes
        "-fPIC"          # Position-independent code
    ]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"    # Enable GNU extensions
    ],

    LIBS=[
        "lgpio",         # lgpio library (GPIO, PWM, I2C, SPI, callbacks)
        "pthread"        # POSIX threads (lgpio uses threads internally)
    ]
)

# lgpio headers are in system include path (/usr/include)
# No additional CPPPATH needed if installed via apt

# No framework library to build - lgpio is a system library
```

**platformio.json update**:
```json
{
  "frameworks": {
    "lgpio": {
      "script": "builder/frameworks/lgpio.py",
      "description": "lgpio is a modern C library for Linux GPIO access using /dev/gpiochip. Works on all Raspberry Pi models including Pi 5.",
      "url": "http://abyz.me.uk/lg/",
      "title": "lgpio"
    }
  }
}
```

**Usage** (in platformio.ini):
```ini
[env:blink_lgpio]
platform = linux_arm
board = raspberrypi_5
framework = lgpio
```

**Effort**: 1 hour (create file, test on Pi 5, documentation)

---

### pigpio Framework Builder

**File**: `builder/frameworks/pigpio.py`

```python
# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
pigpio

pigpio is a high-performance C library for Raspberry Pi GPIO access.
Features hardware-timed PWM and high-speed GPIO sampling.
DOES NOT work on Raspberry Pi 5 (hardware incompatible).

http://abyz.me.uk/rpi/pigpio/
https://github.com/joan2937/pigpio

Installation:
    sudo apt install libpigpio-dev pigpio

Cross-compilation (Debian/Ubuntu):
    sudo dpkg --add-architecture armhf
    sudo apt update
    sudo apt install libpigpio-dev:armhf

WARNING: Not compatible with Raspberry Pi 5. Use lgpio for Pi 5.
"""

from SCons.Script import DefaultEnvironment
from platformio import exception

env = DefaultEnvironment()
board = env.BoardConfig()

# Check if target board is Raspberry Pi 5
mcu = board.get("build.mcu", "").lower()
if mcu == "bcm2712":
    raise exception.PlatformioException(
        "pigpio is not compatible with Raspberry Pi 5 (BCM2712). "
        "Use the 'lgpio' framework instead for Pi 5 GPIO access."
    )

env.Replace(
    CPPFLAGS=[
        "-O2",           # Optimize for speed
        "-Wall",         # Enable warnings
        "-Wextra",       # Extra warnings
        "-pthread",      # Enable POSIX threads
        "-pipe",         # Use pipes
        "-fPIC"          # Position-independent code
    ]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"    # Enable GNU extensions
    ],

    LIBS=[
        "pigpio",        # pigpio library (GPIO, PWM, I2C, SPI, waves)
        "rt",            # Real-time extensions (required by pigpio)
        "pthread"        # POSIX threads (required by pigpio)
    ]
)

# pigpio headers are in system include path (/usr/include)
# No additional CPPPATH needed if installed via apt

# No framework library to build - pigpio is a system library
```

**platformio.json update**:
```json
{
  "frameworks": {
    "pigpio": {
      "script": "builder/frameworks/pigpio.py",
      "description": "pigpio is a high-performance C library for Raspberry Pi GPIO (Pi 1-4 only, NOT Pi 5). Features hardware-timed PWM and high-speed sampling.",
      "url": "http://abyz.me.uk/rpi/pigpio/",
      "title": "pigpio"
    }
  }
}
```

**Usage** (in platformio.ini):
```ini
[env:blink_pigpio]
platform = linux_arm
board = raspberrypi_4b  ; NOT raspberrypi_5
framework = pigpio
```

**Effort**: 1-2 hours (create file, add Pi 5 check, test, documentation)

---

### libgpiod Framework Builder (Optional)

**File**: `builder/frameworks/libgpiod.py`

```python
"""
libgpiod

libgpiod is the Linux kernel's standard C library for GPIO access via
character device interface (/dev/gpiochipN). Platform-independent.

WARNING: Raspberry Pi OS Bookworm includes old libgpiod v1.6 with poor
documentation. Version 2.x is recommended but requires building from source.

https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git

Installation:
    sudo apt install libgpiod-dev gpiod
"""

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

env.Replace(
    CPPFLAGS=[
        "-O2",
        "-Wall",
        "-Wextra",
        "-pipe",
        "-fPIC"
    ]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"
    ],

    LIBS=[
        "gpiod"          # libgpiod library
    ]
)
```

**Recommendation**: **Defer implementation** - wait for libgpiod v2 in Pi OS repos, or advise users to use lgpio instead.

**Effort (if implemented)**: 30 min

---

## Example Projects

### Bare-Metal Example

**File**: `examples/baremetal-hello/src/main.c`

```c
/*
 * Bare-metal example: Hello World without GPIO framework
 *
 * Demonstrates framework-less builds for generic Linux ARM applications
 * (servers, utilities, data processing, etc.)
 */

#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Hello from ARM Linux!\n");
    printf("Platform: Linux ARM (bare-metal, no GPIO framework)\n");

    // Example: Simple loop
    for (int i = 0; i < 10; i++) {
        printf("Count: %d\n", i);
        sleep(1);
    }

    return 0;
}
```

**File**: `examples/baremetal-hello/platformio.ini`

```ini
[env:raspberrypi_4b]
platform = linux_arm
board = raspberrypi_4b
; No framework specified = bare-metal
```

**Effort**: 30 min

---

### lgpio Blink Example

**File**: `examples/lgpio-blink/src/main.c`

```c
/*
 * lgpio blink example
 *
 * Blinks GPIO 23 (physical pin 16) using lgpio library.
 * Works on all Raspberry Pi models including Pi 5.
 */

#include <stdio.h>
#include <unistd.h>
#include <lgpio.h>

#define GPIO_PIN 23

int main() {
    int h;  // GPIO chip handle
    int gpio = GPIO_PIN;

    printf("lgpio blink example\n");

    // Open GPIO chip 0
    h = lgGpiochipOpen(0);
    if (h < 0) {
        fprintf(stderr, "Failed to open GPIO chip: %d\n", h);
        return 1;
    }

    // Claim GPIO as output
    if (lgGpioClaimOutput(h, 0, gpio, 0) < 0) {
        fprintf(stderr, "Failed to claim GPIO %d\n", gpio);
        lgGpiochipClose(h);
        return 1;
    }

    printf("Blinking GPIO %d (press Ctrl+C to stop)\n", gpio);

    // Blink loop
    while (1) {
        lgGpioWrite(h, gpio, 1);  // HIGH
        printf("LED ON\n");
        sleep(1);

        lgGpioWrite(h, gpio, 0);  // LOW
        printf("LED OFF\n");
        sleep(1);
    }

    // Cleanup (unreachable in this example)
    lgGpiochipClose(h);
    return 0;
}
```

**File**: `examples/lgpio-blink/platformio.ini`

```ini
[env:raspberrypi_5]
platform = linux_arm
board = raspberrypi_5
framework = lgpio
```

**Installation instructions** (in README):
```markdown
## Prerequisites

Install lgpio library on your Raspberry Pi:
\`\`\`bash
sudo apt install liblgpio-dev liblgpio1
\`\`\`

For cross-compilation on Debian/Ubuntu x86_64:
\`\`\`bash
sudo dpkg --add-architecture armhf
sudo apt update
sudo apt install liblgpio-dev:armhf
\`\`\`

## Build and Run

\`\`\`bash
pio run
scp .pio/build/raspberrypi_5/program pi@raspberrypi.local:/tmp/
ssh pi@raspberrypi.local
cd /tmp
chmod +x program
sudo ./program
\`\`\`
```

**Effort**: 1 hour

---

### pigpio Blink Example

**File**: `examples/pigpio-blink/src/main.c`

```c
/*
 * pigpio blink example
 *
 * Blinks GPIO 23 using pigpio library (hardware-timed PWM capable).
 * Works on Raspberry Pi 1-4, Zero. DOES NOT work on Pi 5.
 */

#include <stdio.h>
#include <unistd.h>
#include <pigpio.h>

#define GPIO_PIN 23

int main() {
    int gpio = GPIO_PIN;

    printf("pigpio blink example\n");

    // Initialize pigpio
    if (gpioInitialise() < 0) {
        fprintf(stderr, "Failed to initialize pigpio\n");
        fprintf(stderr, "Note: pigpio requires root/sudo and is not compatible with Pi 5\n");
        return 1;
    }

    // Set GPIO as output
    gpioSetMode(gpio, PI_OUTPUT);

    printf("Blinking GPIO %d (press Ctrl+C to stop)\n", gpio);

    // Blink loop
    while (1) {
        gpioWrite(gpio, 1);  // HIGH
        printf("LED ON\n");
        sleep(1);

        gpioWrite(gpio, 0);  // LOW
        printf("LED OFF\n");
        sleep(1);
    }

    // Cleanup (unreachable)
    gpioTerminate();
    return 0;
}
```

**File**: `examples/pigpio-blink/platformio.ini`

```ini
[env:raspberrypi_4b]
platform = linux_arm
board = raspberrypi_4b  ; Use Pi 1-4, NOT Pi 5
framework = pigpio
```

**Effort**: 30 min (very similar to lgpio)

---

## Migration Guide

### WiringPi → lgpio Migration

**Pin Numbering Differences**:
- **WiringPi**: Custom pin numbering (WiringPi pin 2 = BCM GPIO 27)
- **lgpio**: BCM GPIO numbering only (GPIO 23 = physical pin 16)

**API Mapping**:

| WiringPi | lgpio | Notes |
|----------|-------|-------|
| `wiringPiSetup()` | `lgGpiochipOpen(0)` | Returns chip handle |
| `pinMode(pin, OUTPUT)` | `lgGpioClaimOutput(h, 0, gpio, 0)` | |
| `pinMode(pin, INPUT)` | `lgGpioClaimInput(h, 0, gpio)` | |
| `digitalWrite(pin, HIGH)` | `lgGpioWrite(h, gpio, 1)` | |
| `digitalWrite(pin, LOW)` | `lgGpioWrite(h, gpio, 0)` | |
| `digitalRead(pin)` | `lgGpioRead(h, gpio)` | Returns 0/1 |
| `delay(ms)` | `usleep(ms * 1000)` or `sleep(s)` | Not in lgpio |
| *(cleanup implicit)* | `lgGpiochipClose(h)` | Required |

**Example Migration**:

**Before (WiringPi)**:
```c
#include <wiringPi.h>

wiringPiSetup();
pinMode(2, OUTPUT);  // WiringPi pin 2
digitalWrite(2, HIGH);
delay(1000);
digitalWrite(2, LOW);
```

**After (lgpio)**:
```c
#include <lgpio.h>
#include <unistd.h>

int h = lgGpiochipOpen(0);
int gpio = 27;  // BCM GPIO 27 (was WiringPi pin 2)
lgGpioClaimOutput(h, 0, gpio, 0);
lgGpioWrite(h, gpio, 1);
usleep(1000000);  // 1 second in microseconds
lgGpioWrite(h, gpio, 0);
lgGpiochipClose(h);
```

---

### WiringPi → pigpio Migration

**API Mapping**:

| WiringPi | pigpio | Notes |
|----------|--------|-------|
| `wiringPiSetup()` | `gpioInitialise()` | Returns status code |
| `pinMode(pin, OUTPUT)` | `gpioSetMode(gpio, PI_OUTPUT)` | BCM numbering |
| `pinMode(pin, INPUT)` | `gpioSetMode(gpio, PI_INPUT)` | |
| `digitalWrite(pin, HIGH)` | `gpioWrite(gpio, 1)` | |
| `digitalWrite(pin, LOW)` | `gpioWrite(gpio, 0)` | |
| `digitalRead(pin)` | `gpioRead(gpio)` | |
| `delay(ms)` | `gpioDelay(us)` | Microseconds, or use sleep() |
| *(cleanup implicit)* | `gpioTerminate()` | Required |

**Example Migration**:

**Before (WiringPi)**:
```c
#include <wiringPi.h>

wiringPiSetupGpio();  // BCM numbering
pinMode(23, OUTPUT);
digitalWrite(23, HIGH);
```

**After (pigpio)**:
```c
#include <pigpio.h>

gpioInitialise();
gpioSetMode(23, PI_OUTPUT);
gpioWrite(23, 1);
gpioTerminate();
```

---

## Effort Estimates

| Task | Effort (Hours) | Justification |
|------|---------------|---------------|
| **Bare-Metal Framework** | | |
| Create builder/frameworks/baremetal.py | 0.5 | Minimal file, no library build |
| Create example project | 0.5 | Simple hello-world |
| Test and document | 0.5 | Build test, README |
| **Subtotal** | **1.5** | Quick win |
| | | |
| **lgpio Framework** | | |
| Create builder/frameworks/lgpio.py | 1 | Builder script, error handling |
| Update platform.json | 0.5 | Add framework definition |
| Create lgpio-blink example | 1 | Example code, platformio.ini |
| Test on Pi 5 (native + cross) | 1 | Hardware testing, validation |
| Documentation (install, API) | 1 | README, migration guide |
| **Subtotal** | **4.5** | High value |
| | | |
| **pigpio Framework** | | |
| Create builder/frameworks/pigpio.py | 1 | Builder script, Pi 5 check |
| Update platform.json | 0.5 | Add framework definition |
| Create pigpio-blink example | 0.5 | Similar to lgpio |
| Test on Pi 4 (native + cross) | 1 | Hardware testing |
| Documentation | 1 | README, Pi 5 warning |
| **Subtotal** | **4** | Medium value |
| | | |
| **Update WiringPi to GC2 Fork** | | |
| Research GC2 package version | 0.5 | Check if GC2 in apt repos |
| Update framework-wiringpi package or docs | 1 | Depends on packaging approach |
| Test on Pi 5 | 0.5 | Validate GCLK limitation |
| Update documentation | 0.5 | Note GC2 fork, Pi 5 support |
| **Subtotal** | **2.5** | Low priority |
| | | |
| **libgpiod Framework (Optional)** | | |
| Create builder/frameworks/libgpiod.py | 0.5 | Simple builder |
| Documentation (v1.6 vs v2 warning) | 0.5 | API differences |
| **Subtotal** | **1** | Defer to Phase 2 |
| | | |
| **Cross-Compilation Documentation** | | |
| Multi-arch apt setup guide | 1 | Debian/Ubuntu instructions |
| Build-from-source scripts | 1.5 | lgpio, pigpio build scripts |
| Troubleshooting section | 0.5 | Common errors |
| **Subtotal** | **3** | Critical for usability |
| | | |
| **Framework Selection Guide** | | |
| Comparison matrix | 0.5 | Table of features |
| Decision tree / recommendations | 0.5 | When to use each |
| Migration examples | 1 | WiringPi → lgpio/pigpio |
| **Subtotal** | **2** | Helps users choose |
| | | |
| **Testing and Integration** | | |
| Test all frameworks (native) | 2 | Pi 4 and Pi 5 |
| Test cross-compilation (x86_64) | 2 | Linux, macOS, Windows |
| CI/CD integration | 1 | Add frameworks to test matrix |
| **Subtotal** | **5** | Quality assurance |

**Total Effort**: **23.5 hours** (all frameworks + docs + testing)

**Recommended Phased Approach**:

**Phase 1 (Quick Win - 6 hours)**:
- Bare-metal framework (1.5 hours)
- lgpio framework (4.5 hours)
- **Impact**: Pi 5 support + non-GPIO use cases

**Phase 2 (Full Modernization - 10 hours)**:
- pigpio framework (4 hours)
- Cross-compilation docs (3 hours)
- Framework selection guide (2 hours)
- Testing (1 hour)
- **Impact**: Complete framework ecosystem

**Phase 3 (Polish - 7.5 hours)**:
- Update WiringPi to GC2 (2.5 hours)
- libgpiod framework (1 hour)
- Additional testing (2 hours)
- CI/CD integration (2 hours)
- **Impact**: Legacy support + platform-independence

---

## Dependencies and Risks

### Dependencies

**Requires**:
- ⬜ None - frameworks use system libraries

**Enables**:
- ✅ **Priority 3: Modern Board Support** - Pi 5 board definitions now useful (lgpio support)
- ✅ **Priority 4: CI/CD** - Can test multiple frameworks in CI pipeline
- ⬜ **Priority 1: Cross-Compilation** - Independent, but cross-compile enables framework testing

**Blocks**:
- ⬜ None

---

### Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Users don't install system packages | High | High | Clear error messages, installation guide in README, builder script checks |
| Cross-compilation missing ARM libs | Medium | High | Document multi-arch apt setup, provide build-from-source scripts |
| Framework version incompatibility | Low | Medium | Document tested versions, pin versions in docs |
| pigpio used on Pi 5 (unsupported) | Medium | Medium | Add Pi 5 detection in builder script, raise clear error |
| libgpiod v1.6 poor docs confuse users | Medium | Low | Defer libgpiod or document v2 source build |
| WiringPi cross-compile still blocked | High | Low | Keep existing restriction (platform.py:34-39), document native-only |

---

### Known Limitations

**After implementation, these will remain**:

1. **WiringPi cross-compilation blocked** (platform.py:34-39):
   - Historical limitation from original platform
   - Could be removed now (WiringPi is just another library)
   - **Recommendation**: Remove block in future update, allow cross-compile

2. **System package dependency**:
   - Users must install frameworks via `apt install`
   - No automatic installation
   - **Rationale**: Avoid PlatformIO packaging complexity, leverage Debian repos

3. **pigpio Pi 5 incompatibility**:
   - Hardware limitation, cannot be fixed
   - **Mitigation**: Builder script raises clear error for Pi 5 boards

4. **libgpiod v2 not in Pi OS**:
   - Must build from source for v2 features
   - **Mitigation**: Wait for Raspberry Pi OS to package v2, or document build process

---

## References & Sources

**All detailed references are in [REFERENCES.md](REFERENCES.md)**

**Key sources used in this analysis**:

### GPIO Libraries
1. **lgpio GitHub**: https://github.com/joan2937/lg
   - Modern GPIO library by pigpio author, Pi 5 compatible
2. **lgpio Documentation**: http://abyz.me.uk/lg/index.html
   - API reference, features, installation
3. **pigpio GitHub**: https://github.com/joan2937/pigpio
   - High-performance GPIO library, Pi 1-4 only
4. **pigpio Documentation**: http://abyz.me.uk/rpi/pigpio/
   - C API reference, examples, compilation instructions
5. **WiringPi GC2 Fork**: https://github.com/WiringPi/WiringPi
   - Community-maintained WiringPi with Pi 5 support
6. **libgpiod Kernel Git**: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git
   - Official kernel GPIO library

### Comparisons and Guides
7. **GPIO Library Comparison (Xojo Forum)**: https://forum.xojo.com/t/libgpiod-vs-pigpiod-vs-wiringpi/59853
   - Performance benchmarks, feature comparison
8. **Current Proper GPIO Access (StackExchange)**: https://raspberrypi.stackexchange.com/questions/147465/
   - 2024 recommendations for GPIO libraries
9. **Raspberry Pi GPIO White Paper**: https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices
   - Official Raspberry Pi Foundation guidance

### Installation and Compilation
10. **pigpio Debian Package**: https://tracker.debian.org/pkg/pigpio
    - Package versions, dependencies
11. **libgpiod Debian Package**: https://packages.debian.org/unstable/libgpiod-dev
    - Package versions, installation
12. **pigpio Compilation Guide (StackOverflow)**: https://stackoverflow.com/questions/69759904/
    - CMake setup, linking flags

### Technical Analysis
13. **WiringPi vs libgpiod Analysis (sfo2001)**: https://github.com/sfo2001/esphome/blob/feature/linux-platform/docs/linux-platform/notes/wiringpi-analysis.md
    - In-depth technical comparison (from Round 1)

### Local Files
14. **platform-linux_arm/builder/frameworks/wiringpi.py**: Lines 1-67 (local)
    - Current framework builder pattern
15. **platform-linux_arm/platform.py**: Lines 34-39 (local)
    - WiringPi cross-compile block

---

**Document Status**:
- ✅ Research complete
- ✅ Findings documented
- ✅ Framework comparison matrix created
- ✅ Builder scripts designed (3 frameworks + bare-metal)
- ✅ Example projects outlined
- ✅ Migration guide provided
- ⬜ References added to REFERENCES.md (next step)
- ⬜ Implementation pending
