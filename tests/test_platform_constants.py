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

import platform_constants  # noqa: E402


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


class TestStaticConstants:
    """Test platform-critical constant values that must not drift."""

    def test_ssh_defaults_port(self):
        assert platform_constants.SSHDefaults.PORT == 22

    def test_ssh_defaults_user(self):
        assert platform_constants.SSHDefaults.USER == "pi"

    def test_exit_code_marker(self):
        assert platform_constants.TestConstants.EXIT_CODE_MARKER == "__EXIT_CODE__:"

    def test_debug_tools_default(self):
        assert platform_constants.DebugTools.DEFAULT == "gdbserver-ssh"

    def test_debug_tools_gdb_remote(self):
        assert platform_constants.DebugTools.GDB_REMOTE == "gdb-remote"

    def test_upload_protocol_all_contains_four(self):
        assert len(platform_constants.UploadProtocol.ALL) == 4
        assert "scp" in platform_constants.UploadProtocol.ALL
        assert "rsync" in platform_constants.UploadProtocol.ALL
        assert "ssh" in platform_constants.UploadProtocol.ALL
        assert "manual" in platform_constants.UploadProtocol.ALL

    def test_timeouts_are_positive_ints(self):
        for attr in ["UPLOAD", "UPLOAD_RUN", "TEST_UPLOAD", "TEST_EXECUTION", "CHMOD"]:
            value = getattr(platform_constants.Timeouts, attr)
            assert isinstance(value, int) and value > 0, f"Timeouts.{attr} = {value}"


class TestDevLoopConstants:
    """Test dev-loop constant values that agents parse — silent drift is a real risk."""

    def test_schema_version(self):
        assert platform_constants.DevLoopConstants.SCHEMA_VERSION == "1"

    def test_output_delimiter(self):
        assert platform_constants.DevLoopConstants.OUTPUT_DELIMITER == "--- DEV_LOOP_RESULT ---"

    def test_result_filename(self):
        assert platform_constants.DevLoopConstants.RESULT_FILENAME == "dev-loop-result.json"

    def test_max_output_bytes(self):
        assert platform_constants.DevLoopConstants.MAX_OUTPUT_BYTES == 64 * 1024

    def test_monitor_timeout(self):
        assert platform_constants.DevLoopConstants.MONITOR_TIMEOUT == 30
