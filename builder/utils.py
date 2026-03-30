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
