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
arduino-bridge.

arduino-bridge is a C++ MsgPack-RPC client framework for the Arduino Uno Q.
It enables Linux C++ code running on the QRB2210 (AArch64, Debian) to call
user-defined methods registered by MCU firmware on the STM32U585 via the
arduino-router Unix socket at /var/run/arduino-router.sock.

The bridge has no predefined GPIO method names. MCU firmware registers arbitrary
methods via Bridge.provide("name", cb). Linux C++ calls them via
Bridge.call("name", params) over the arduino-router Unix socket. See
docs/boards/arduino_uno_q.md for the standard GPIO RPC contract.

Runtime dependency:
    arduino-router daemon (pre-installed on stock Arduino Uno Q Debian image)
    Install: sudo apt install ./arduino-router_0.8.0-1_arm64.deb
    Verify:  systemctl status arduino-router

Cross-compilation setup (required):
    sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu cmake
    CROSS_PREFIX=aarch64-linux-gnu- ./scripts/setup-mraa-cross.sh

    This installs MRAA and msgpack headers to:
    $HOME/.local/aarch64-linux-gnu/

https://github.com/eclipse/mraa
https://github.com/arduino/arduino-router
"""

import os
import shutil
import subprocess
import sys
from os.path import expanduser, isfile, join

from SCons.Script import COMMAND_LINE_TARGETS, DefaultEnvironment
from utils import get_target_arch, get_toolchain_prefix

from platform_constants import Architecture

env = DefaultEnvironment()


def _find_mraa(home):
    """Find MRAA include and lib paths for AArch64.

    Returns (include_path, lib_path) or (None, None) if not found.
    """
    search_paths = [
        join(home, ".local", "aarch64-linux-gnu"),
        "/usr/local/aarch64-linux-gnu",
        "/usr/aarch64-linux-gnu",
        "/usr/local",
        "/usr",
    ]
    for base_path in search_paths:
        inc_path = join(base_path, "include")
        lib_path = join(base_path, "lib")
        lib_path_multiarch = join(base_path, "lib", "aarch64-linux-gnu")
        if isfile(join(inc_path, "mraa", "mraa.hpp")) or isfile(join(inc_path, "mraa.hpp")):
            for lp in [lib_path_multiarch, lib_path]:
                if isfile(join(lp, "libmraa.so")) or isfile(join(lp, "libmraa.so.2")):
                    return inc_path, lp
    return None, None


def _find_msgpack(home):
    """Find msgpack-cxx include path.

    Returns include path string or None if not found.
    """
    search_paths = [
        join(home, ".local", "aarch64-linux-gnu", "include"),
        "/opt/homebrew/include",  # macOS Apple Silicon (Homebrew)
        "/usr/local/include",  # macOS Intel (Homebrew) / Linux
        "/usr/include",
    ]
    for p in search_paths:
        if isfile(join(p, "msgpack.hpp")):
            return p
    return None


# --------------------------------------------------------------------------
# setup-mraa custom target
#
# Registered BEFORE any env.Exit() calls so it is always available, even
# when MRAA is not yet installed. Developers can run:
#
#   pio run --target setup-mraa
#
# from any arduino-bridge example directory to cross-compile and install
# MRAA without manually invoking scripts/setup-mraa-cross.sh.
# --------------------------------------------------------------------------


def _mraa_setup_action(target, source, env):
    """Cross-compile and install MRAA for AArch64 via setup-mraa-cross.sh.

    Returns non-zero to signal failure to SCons — do NOT call env.Exit() here.
    SCons action functions communicate failure via return code, not env.Exit().
    """
    if sys.platform == "win32":
        sys.stderr.write(
            "ERROR: setup-mraa is not supported on Windows.\n"
            "Use WSL2 (Ubuntu) to cross-compile MRAA for AArch64.\n"
        )
        return 1

    if not shutil.which("cmake"):
        sys.stderr.write(
            "ERROR: cmake not found. Install it first:\n"
            "  Linux:  sudo apt install cmake\n"
            "  macOS:  brew install cmake\n"
        )
        return 1

    prefix = get_toolchain_prefix(Architecture.AARCH64)
    install_dir = join(expanduser("~"), ".local", "aarch64-linux-gnu")
    platform_dir = env.PioPlatform().get_dir()
    script = join(platform_dir, "scripts", "setup-mraa-cross.sh")

    print("\nSetting up MRAA for AArch64 cross-compilation...")
    print(f"  CROSS_PREFIX: {prefix}")
    print(f"  INSTALL_DIR:  {install_dir}")
    print(f"  Script:       {script}")
    print()

    # Pass only required variables — do not forward CI secrets or tokens.
    _passthrough = ("PATH", "HOME", "TMPDIR", "TEMP", "LANG", "LC_ALL")
    env_vars = {k: os.environ[k] for k in _passthrough if k in os.environ}
    env_vars["CROSS_PREFIX"] = prefix
    env_vars["INSTALL_DIR"] = install_dir

    try:
        result = subprocess.run(["bash", script], env=env_vars, cwd=platform_dir, timeout=600)
    except subprocess.TimeoutExpired:
        sys.stderr.write(
            "\nMRAA setup timed out after 10 minutes.\n"
            "Check your network connection and cmake installation, then retry.\n"
        )
        return 1

    if result.returncode == 0:
        print("\nMRAA setup complete. You can now build arduino-bridge projects.")
    else:
        sys.stderr.write(
            f"\nMRAA setup failed (exit code {result.returncode}).\n"
            "Check the output above for details.\n"
        )
    return result.returncode


env.AddCustomTarget(
    "setup-mraa",
    None,
    [_mraa_setup_action],
    title="Setup MRAA",
    description="Cross-compile and install MRAA for AArch64 (arduino-bridge framework)",
)

# When setup-mraa is the only requested target, skip framework configuration —
# MRAA may not be installed yet, so the checks below would fail. Exact-match
# is intentional: mixing setup-mraa with build targets (e.g. "setup-mraa upload")
# is not a supported workflow and should fall through to the normal MRAA check.
_SETUP_ONLY = list(COMMAND_LINE_TARGETS) == ["setup-mraa"]

# Arduino Uno Q is AArch64-only. The arduino-bridge framework is not supported
# on 32-bit ARM targets.
target_arch = get_target_arch(env)
if not _SETUP_ONLY and target_arch != "aarch64":
    sys.stderr.write(
        "ERROR: arduino-bridge framework is only supported on AArch64 targets.\n"
        "The Arduino Uno Q uses a Qualcomm QRB2210 (AArch64). "
        "Set board_build.arch = aarch64 in platformio.ini.\n"
    )
    env.Exit(1)

if not _SETUP_ONLY:
    home = expanduser("~")

    mraa_include, mraa_lib = _find_mraa(home)

    if not mraa_include or not mraa_lib:
        sys.stderr.write(
            "ERROR: MRAA library not found for AArch64!\n"
            "\n"
            "The arduino-bridge framework requires MRAA cross-compiled for AArch64.\n"
            "\n"
            "Quick fix — run the setup target from your project directory:\n"
            "  pio run --target setup-mraa\n"
            "\n"
            "Or manually:\n"
            "  sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu cmake\n"
            "  CROSS_PREFIX=aarch64-linux-gnu- ./scripts/setup-mraa-cross.sh\n"
            "\n"
            "  (macOS) brew tap messense/macos-cross-toolchains\n"
            "  (macOS) brew install aarch64-unknown-linux-gnu cmake\n"
            "  (macOS) CROSS_PREFIX=aarch64-unknown-linux-gnu- "
            "INSTALL_DIR=$HOME/.local/aarch64-linux-gnu ./scripts/setup-mraa-cross.sh\n"
            "\n"
            "See docs/boards/arduino_uno_q.md for complete instructions.\n"
        )
        env.Exit(1)

    # Find msgpack-cxx headers (header-only, installed via libmsgpack-cxx-dev)
    # Required for ArduinoBridgeImpl.cpp serialization
    msgpack_include = _find_msgpack(home)

    if not msgpack_include:
        sys.stderr.write(
            "ERROR: msgpack-cxx headers not found!\n"
            "\n"
            "Install with:\n"
            "  sudo apt install libmsgpack-cxx-dev  (Ubuntu/Debian)\n"
            "  brew install msgpack-cxx           (macOS)\n"
            "\n"
        )
        env.Exit(1)

    framework_dir = join(env.PioPlatform().get_dir(), "framework-arduino-bridge")

    env.Replace(CPPFLAGS=["-O2", "-Wall", "-std=c++17", "-pipe", "-fPIC"])

    # Suppress Boost dependency in msgpack-cxx headers (set by arduino_bridge.py via CPPDEFINES).
    # Listed here so the file compiles correctly in IDEs without the PlatformIO env.
    env.Append(CPPDEFINES=["MSGPACK_NO_BOOST"])

    env.Append(
        CPPPATH=[mraa_include, msgpack_include, framework_dir],
        LIBPATH=[mraa_lib],
        LIBS=["mraa"],
    )

    # Build the ArduinoBridge C++ MsgPack-RPC client library
    env.BuildSources(join("$BUILD_DIR", "FrameworkArduinoBridge"), framework_dir)
