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

"""Shared utilities for PlatformIO builder scripts."""

import shutil

from platform_constants import Architecture, ToolchainPrefix


def get_toolchain_prefix(arch):
    """Find an available toolchain prefix for the target architecture.

    Probes PATH for known toolchain prefixes, preferring the platform default
    but falling back to alternatives (e.g. ARM official SDK on a system that
    only has the apt-packaged toolchain, or vice versa).

    Args:
        arch: Target architecture (Architecture.AARCH64 or Architecture.ARMV7).

    Returns:
        str: The first toolchain prefix whose gcc is found in PATH,
             or the platform default if none found.
    """
    if arch == Architecture.AARCH64:
        candidates = [
            ToolchainPrefix.AARCH64,
            # Opposite vendor convention as fallback
            (
                "aarch64-linux-gnu-"
                if ToolchainPrefix.AARCH64.startswith("aarch64-none")
                else "aarch64-none-linux-gnu-"
            ),
        ]
    else:
        candidates = [
            ToolchainPrefix.ARMV7,
            (
                "arm-linux-gnueabihf-"
                if ToolchainPrefix.ARMV7.startswith("arm-none")
                else "arm-none-linux-gnueabihf-"
            ),
        ]

    for prefix in candidates:
        if shutil.which(prefix + "gcc"):
            return prefix

    return candidates[0]


def get_target_arch(env):
    """Detect target architecture from board config with user override.

    Reads build.arch from the board definition, then checks if the user
    explicitly set board_build.arch in platformio.ini (which takes precedence).

    Args:
        env: PlatformIO SCons environment object.

    Returns:
        str: Target architecture identifier (e.g., "armv7", "aarch64").
    """
    board = env.BoardConfig()
    target_arch = board.get("build.arch", "armv7")
    if env.GetProjectOption("board_build.arch", None):
        target_arch = env.GetProjectOption("board_build.arch")
    return target_arch
