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

lgpio is a modern C library for Linux GPIO access, designed as a successor to
deprecated sysfs GPIO and the pigpio library. It uses the GPIO character device
(/dev/gpiochip*) introduced in Linux kernel 4.8.

lgpio works on ALL Raspberry Pi models (1-5) including Pi 5, which removed
support for older GPIO interfaces.

Supersedes pigpio (by same author Joan) - recommended for all new projects.

Installation for cross-compilation:
    Run: ./scripts/setup-lgpio-cross.sh

    This builds lgpio from source for ARM and installs to:
    $HOME/.local/arm-linux-gnueabihf/

For Raspberry Pi 1 (original models), set environment variable:
    export RPI_LGPIO_REVISION=800012

http://abyz.me.uk/lg/lgpio.html
"""

from SCons.Script import DefaultEnvironment
from os.path import isfile, join, expanduser
import sys

env = DefaultEnvironment()

# Detect lgpio installation paths
# Priority: 1) User local build, 2) System-wide build, 3) System package
home = expanduser("~")
lgpio_search_paths = [
    join(home, ".local", "arm-linux-gnueabihf"),  # User-built (recommended)
    "/usr/local/arm-linux-gnueabihf",             # System-wide build
    "/usr/arm-linux-gnueabihf",                   # Multiarch package location
    "/usr",                                        # Native package fallback
]

lgpio_include = None
lgpio_lib = None

for base_path in lgpio_search_paths:
    inc_path = join(base_path, "include")
    lib_path = join(base_path, "lib")

    if isfile(join(inc_path, "lgpio.h")) and \
       (isfile(join(lib_path, "liblgpio.so")) or isfile(join(lib_path, "liblgpio.so.1"))):
        lgpio_include = inc_path
        lgpio_lib = lib_path
        print("Found lgpio at: %s" % base_path)
        break

if not lgpio_include or not lgpio_lib:
    sys.stderr.write(
        "ERROR: lgpio library not found!\n"
        "\n"
        "Please build and install lgpio for cross-compilation:\n"
        "  1. Install ARM toolchain: sudo apt install gcc-arm-linux-gnueabihf\n"
        "  2. Run setup script: ./scripts/setup-lgpio-cross.sh\n"
        "\n"
        "Or install system package (requires multiarch setup):\n"
        "  sudo dpkg --add-architecture armhf\n"
        "  sudo apt install liblgpio-dev:armhf\n"
        "\n"
        "See docs/LGPIO_SETUP.md for details.\n"
    )
    env.Exit(1)

env.Replace(
    CPPFLAGS=[
        "-O2",
        "-Wall",
        "-Winline",
        "-pipe",
        "-fPIC"
    ]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"
    ],

    CPPPATH=[
        lgpio_include
    ],

    LIBPATH=[
        lgpio_lib
    ],

    LIBS=["lgpio"]
)
