#!/usr/bin/env python3
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

"""Unit tests for OS-conditional toolchain constants in platform_constants.py."""

import importlib
import os
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import platform_constants


class TestToolchainPrefixPosix:
    """Verify ToolchainPrefix values when simulating a non-Windows platform."""

    @pytest.fixture(autouse=True)
    def posix_constants(self):
        with patch.object(os, "name", "posix"):
            importlib.reload(platform_constants)
        yield
        importlib.reload(platform_constants)

    def test_aarch64_linux_prefix(self):
        assert platform_constants.ToolchainPrefix.AARCH64 == "aarch64-linux-gnu-"

    def test_armv7_linux_prefix(self):
        assert platform_constants.ToolchainPrefix.ARMV7 == "arm-linux-gnueabihf-"


class TestGDBExecutablePosix:
    """Verify GDBExecutable values when simulating a non-Windows platform."""

    @pytest.fixture(autouse=True)
    def posix_constants(self):
        with patch.object(os, "name", "posix"):
            importlib.reload(platform_constants)
        yield
        importlib.reload(platform_constants)

    def test_native_gdb(self):
        assert platform_constants.GDBExecutable.NATIVE == "gdb"

    def test_multiarch_gdb(self):
        assert platform_constants.GDBExecutable.MULTIARCH == "gdb-multiarch"

    def test_aarch64_gdb(self):
        assert platform_constants.GDBExecutable.AARCH64 == "aarch64-linux-gnu-gdb"

    def test_armv7_gdb(self):
        assert platform_constants.GDBExecutable.ARMV7 == "arm-linux-gnueabihf-gdb"


class TestToolchainPrefixWindows:
    """Verify ToolchainPrefix values when simulating Windows (os.name == 'nt')."""

    @pytest.fixture(autouse=True)
    def windows_constants(self):
        with patch.object(os, "name", "nt"):
            importlib.reload(platform_constants)
        yield
        importlib.reload(platform_constants)

    def test_aarch64_windows_prefix(self):
        assert platform_constants.ToolchainPrefix.AARCH64 == "aarch64-none-linux-gnu-"

    def test_armv7_windows_prefix(self):
        assert platform_constants.ToolchainPrefix.ARMV7 == "arm-none-linux-gnueabihf-"


class TestGDBExecutableWindows:
    """Verify GDBExecutable values when simulating Windows (os.name == 'nt')."""

    @pytest.fixture(autouse=True)
    def windows_constants(self):
        with patch.object(os, "name", "nt"):
            importlib.reload(platform_constants)
        yield
        importlib.reload(platform_constants)

    def test_aarch64_windows_gdb(self):
        assert platform_constants.GDBExecutable.AARCH64 == "aarch64-none-linux-gnu-gdb"

    def test_armv7_windows_gdb(self):
        assert platform_constants.GDBExecutable.ARMV7 == "arm-none-linux-gnueabihf-gdb"

    def test_native_gdb_unchanged(self):
        assert platform_constants.GDBExecutable.NATIVE == "gdb"

    def test_multiarch_gdb_unchanged(self):
        assert platform_constants.GDBExecutable.MULTIARCH == "gdb-multiarch"
