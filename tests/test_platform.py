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

"""Unit tests for platform.py module."""

import importlib.util
import os
import platform as stdlib_platform  # Import stdlib platform first to avoid circular import
import sys
from unittest.mock import MagicMock, Mock, mock_open, patch

import pytest

# Add parent directory to path for imports (after stdlib platform is imported)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from platformio import exception

# Import platform.py module explicitly to avoid conflict with stdlib platform module
_platform_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "platform.py"
)
spec = importlib.util.spec_from_file_location("platform_module", _platform_path)
platform_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(platform_module)

# Make platform module available to patches
sys.modules["platform_module"] = platform_module


class TestLinuxArmPlatformInit:
    """Test cases for Linux_armPlatform initialization."""

    @patch("platform_module.Linux_armPlatform._show_welcome_if_needed")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_init_loads_config(
        self, mock_base_init, mock_get_config, mock_welcome, mock_platform_manifest
    ):
        """Test that initialization loads platform configuration."""
        from platform_module import Linux_armPlatform

        mock_config = Mock()
        mock_get_config.return_value = mock_config
        mock_base_init.return_value = None

        platform = Linux_armPlatform(mock_platform_manifest)

        mock_get_config.assert_called_once()
        assert platform._config == mock_config


class TestIsNative:
    """Test cases for _is_native static method."""

    @patch("platform_module.get_systype")
    def test_is_native_on_linux_arm(self, mock_get_systype):
        """Test _is_native returns True on linux_arm."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "linux_arm"
        assert Linux_armPlatform._is_native() is True

    @patch("platform_module.get_systype")
    def test_is_native_on_linux_aarch64(self, mock_get_systype):
        """Test _is_native returns True on linux_aarch64."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "linux_aarch64"
        assert Linux_armPlatform._is_native() is True

    @patch("platform_module.get_systype")
    def test_is_native_on_linux_x86_64(self, mock_get_systype):
        """Test _is_native returns False on linux_x86_64."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "linux_x86_64"
        assert Linux_armPlatform._is_native() is False

    @patch("platform_module.get_systype")
    def test_is_native_on_darwin_x86_64(self, mock_get_systype):
        """Test _is_native returns False on darwin_x86_64."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "darwin_x86_64"
        assert Linux_armPlatform._is_native() is False

    @patch("platform_module.get_systype")
    def test_is_native_on_windows(self, mock_get_systype):
        """Test _is_native returns False on Windows."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "windows_amd64"
        assert Linux_armPlatform._is_native() is False


class TestPackagesProperty:
    """Test cases for packages property (toolchain selection)."""

    @patch("platform_module.get_systype")
    @patch(
        "platform_module.PlatformBase.packages",
        new_callable=lambda: property(
            lambda self: {"toolchain-gccarmlinuxgnueabi": {}, "framework-wiringpi": {}}
        ),
    )
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_packages_excludes_toolchain_on_native_arm(
        self,
        mock_base_init,
        mock_get_config,
        mock_base_packages,
        mock_get_systype,
        mock_platform_manifest,
    ):
        """Test packages property excludes toolchain on native ARM."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "linux_arm"
        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)
        packages = platform.packages

        assert "toolchain-gccarmlinuxgnueabi" not in packages
        assert "framework-wiringpi" in packages

    @patch("platform_module.get_systype")
    @patch(
        "platform_module.PlatformBase.packages",
        new_callable=lambda: property(
            lambda self: {"toolchain-gccarmlinuxgnueabi": {}, "framework-wiringpi": {}}
        ),
    )
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_packages_keeps_toolchain_on_darwin_x86_64(
        self,
        mock_base_init,
        mock_get_config,
        mock_base_packages,
        mock_get_systype,
        mock_platform_manifest,
    ):
        """Test packages property keeps toolchain on macOS x86_64."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "darwin_x86_64"
        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)
        packages = platform.packages

        assert "toolchain-gccarmlinuxgnueabi" in packages
        assert "framework-wiringpi" in packages

    @patch("platform_module.get_systype")
    @patch(
        "platform_module.PlatformBase.packages",
        new_callable=lambda: property(
            lambda self: {"toolchain-gccarmlinuxgnueabi": {}, "framework-wiringpi": {}}
        ),
    )
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_packages_excludes_toolchain_on_linux_x86_64(
        self,
        mock_base_init,
        mock_get_config,
        mock_base_packages,
        mock_get_systype,
        mock_platform_manifest,
    ):
        """Test packages property excludes toolchain on Linux x86_64."""
        from platform_module import Linux_armPlatform

        mock_get_systype.return_value = "linux_x86_64"
        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)
        packages = platform.packages

        assert "toolchain-gccarmlinuxgnueabi" not in packages


class TestConfigureDefaultPackages:
    """Test cases for configure_default_packages method."""

    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.PlatformBase.configure_default_packages")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_configure_blocks_wiringpi_cross_compilation(
        self,
        mock_base_init,
        mock_get_config,
        mock_base_configure,
        mock_is_native,
        mock_platform_manifest,
    ):
        """Test that WiringPi cross-compilation is blocked."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = False  # Cross-compilation
        mock_base_configure.return_value = {}

        platform = Linux_armPlatform(mock_platform_manifest)

        variables = {"pioframework": ["wiringpi"]}
        targets = []

        with pytest.raises(
            exception.PlatformioException, match="does not support cross-compilation"
        ):
            platform.configure_default_packages(variables, targets)

    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.PlatformBase.configure_default_packages")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_configure_allows_wiringpi_on_native(
        self,
        mock_base_init,
        mock_get_config,
        mock_base_configure,
        mock_is_native,
        mock_platform_manifest,
    ):
        """Test that WiringPi is allowed on native ARM."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = True  # Native execution
        mock_base_configure.return_value = {}

        platform = Linux_armPlatform(mock_platform_manifest)

        variables = {"pioframework": ["wiringpi"]}
        targets = []

        # Should not raise exception
        result = platform.configure_default_packages(variables, targets)
        assert result == {}
        mock_base_configure.assert_called_once_with(variables, targets)

    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.PlatformBase.configure_default_packages")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_configure_allows_non_wiringpi_cross_compilation(
        self,
        mock_base_init,
        mock_get_config,
        mock_base_configure,
        mock_is_native,
        mock_platform_manifest,
    ):
        """Test that non-WiringPi frameworks work with cross-compilation."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = False  # Cross-compilation
        mock_base_configure.return_value = {}

        platform = Linux_armPlatform(mock_platform_manifest)

        variables = {"pioframework": ["lgpio"]}
        targets = []

        # Should not raise exception
        result = platform.configure_default_packages(variables, targets)
        assert result == {}


class TestGetUploadProtocol:
    """Test cases for _get_upload_protocol method."""

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_get_upload_protocol_valid_scp(
        self, mock_base_init, mock_get_config, mock_platform_manifest, mock_env
    ):
        """Test getting valid SCP upload protocol."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)
        mock_env.GetProjectOption = Mock(return_value="scp")

        protocol = platform._get_upload_protocol(mock_env)
        assert protocol == "scp"

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_get_upload_protocol_invalid(
        self, mock_base_init, mock_get_config, mock_platform_manifest, mock_env
    ):
        """Test that invalid upload protocol raises exception."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)
        mock_env.GetProjectOption = Mock(return_value="invalid_protocol")

        with pytest.raises(
            exception.PlatformioException, match="Unknown upload protocol"
        ):
            platform._get_upload_protocol(mock_env)


class TestCheckUploadTool:
    """Test cases for _check_upload_tool method."""

    @patch("shutil.which")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_check_upload_tool_available(
        self, mock_base_init, mock_get_config, mock_which, mock_platform_manifest
    ):
        """Test check passes when tool is available."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_which.return_value = "/usr/bin/scp"

        platform = Linux_armPlatform(mock_platform_manifest)

        # Should not raise exception
        platform._check_upload_tool("scp")
        mock_which.assert_called_once_with("scp")

    @patch("shutil.which")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_check_upload_tool_missing(
        self, mock_base_init, mock_get_config, mock_which, mock_platform_manifest
    ):
        """Test check raises exception when tool is missing."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_which.return_value = None

        platform = Linux_armPlatform(mock_platform_manifest)

        with pytest.raises(exception.PlatformioException, match="is not installed"):
            platform._check_upload_tool("rsync")


class TestParseUploadPort:
    """Test cases for _parse_upload_port method."""

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_parse_upload_port_full_format(
        self, mock_base_init, mock_get_config, mock_platform_manifest, mock_env
    ):
        """Test parsing full user@host:/path format."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)

        user, host, path = platform._parse_upload_port(
            "pi@raspberrypi:/tmp/prog", mock_env
        )

        assert user == "pi"
        assert host == "raspberrypi"
        assert path == "/tmp/prog"

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_parse_upload_port_none_raises_error(
        self, mock_base_init, mock_get_config, mock_platform_manifest, mock_env
    ):
        """Test that None upload_port raises exception."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)

        with pytest.raises(
            exception.PlatformioException, match="upload_port is not configured"
        ):
            platform._parse_upload_port(None, mock_env)

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_parse_upload_port_empty_raises_error(
        self, mock_base_init, mock_get_config, mock_platform_manifest, mock_env
    ):
        """Test that empty upload_port raises exception."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)

        with pytest.raises(
            exception.PlatformioException, match="upload_port is not configured"
        ):
            platform._parse_upload_port("", mock_env)


class TestDetermineGdbExecutable:
    """Test cases for _determine_gdb_executable method."""

    @patch("shutil.which")
    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_determine_gdb_native(
        self,
        mock_base_init,
        mock_get_config,
        mock_is_native,
        mock_which,
        mock_platform_manifest,
    ):
        """Test GDB executable determination on native ARM."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = True
        mock_which.return_value = "gdb"  # Mock shutil.which() to find gdb

        platform = Linux_armPlatform(mock_platform_manifest)

        gdb_path = platform._determine_gdb_executable("armv7")
        assert gdb_path == "gdb"

    @patch("shutil.which")
    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_determine_gdb_cross_aarch64(
        self,
        mock_base_init,
        mock_get_config,
        mock_is_native,
        mock_which,
        mock_platform_manifest,
    ):
        """Test GDB executable for cross-compilation to aarch64."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = False

        # Mock shutil.which() to simulate arch-specific GDB being available
        # Return None for gdb-multiarch, return the command for arch-specific GDB
        from platform_constants import GDBExecutable

        def which_side_effect(cmd):
            if cmd == GDBExecutable.AARCH64:
                return cmd
            return None

        mock_which.side_effect = which_side_effect

        platform = Linux_armPlatform(mock_platform_manifest)

        gdb_path = platform._determine_gdb_executable("aarch64")
        assert gdb_path == GDBExecutable.AARCH64

    @patch("shutil.which")
    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_determine_gdb_cross_armv7(
        self,
        mock_base_init,
        mock_get_config,
        mock_is_native,
        mock_which,
        mock_platform_manifest,
    ):
        """Test GDB executable for cross-compilation to armv7."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = False

        # Mock shutil.which() to simulate arch-specific GDB being available
        # Return None for gdb-multiarch, return the command for arch-specific GDB
        from platform_constants import GDBExecutable

        def which_side_effect(cmd):
            if cmd == GDBExecutable.ARMV7:
                return cmd
            return None

        mock_which.side_effect = which_side_effect

        platform = Linux_armPlatform(mock_platform_manifest)

        gdb_path = platform._determine_gdb_executable("armv7")
        assert gdb_path == GDBExecutable.ARMV7

    @patch("shutil.which")
    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_determine_gdb_prefers_multiarch(
        self,
        mock_base_init,
        mock_get_config,
        mock_is_native,
        mock_which,
        mock_platform_manifest,
    ):
        """Test GDB executable prefers gdb-multiarch when available."""
        from platform_module import Linux_armPlatform

        from platform_constants import GDBExecutable

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = False

        def which_side_effect(cmd):
            if cmd == GDBExecutable.MULTIARCH:
                return GDBExecutable.MULTIARCH
            return None

        mock_which.side_effect = which_side_effect

        platform = Linux_armPlatform(mock_platform_manifest)

        gdb_path = platform._determine_gdb_executable("armv7")
        assert gdb_path == GDBExecutable.MULTIARCH

    @patch("shutil.which")
    @patch("platform_module.Linux_armPlatform._is_native")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_determine_gdb_none_available_raises_error(
        self,
        mock_base_init,
        mock_get_config,
        mock_is_native,
        mock_which,
        mock_platform_manifest,
    ):
        """Test GDB raises PlatformioException when no GDB is found."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_is_native.return_value = False
        mock_which.return_value = None  # No GDB available anywhere

        platform = Linux_armPlatform(mock_platform_manifest)

        with pytest.raises(
            exception.PlatformioException, match="No suitable GDB found"
        ):
            platform._determine_gdb_executable("armv7")


class TestGetConfigDefault:
    """Test cases for _get_config_default method."""

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_get_config_default_from_config(
        self, mock_base_init, mock_get_config, mock_platform_manifest
    ):
        """Test getting config value from config file."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_config = Mock()
        mock_config.get = Mock(return_value=600)
        mock_get_config.return_value = mock_config

        platform = Linux_armPlatform(mock_platform_manifest)

        value = platform._get_config_default("upload_timeout", 300)
        assert value == 600
        mock_config.get.assert_called_once_with("upload_timeout", 300)

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_get_config_default_fallback(
        self, mock_base_init, mock_get_config, mock_platform_manifest
    ):
        """Test getting config value falls back to default."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_config = Mock()
        mock_config.get = Mock(return_value=300)  # Returns fallback
        mock_get_config.return_value = mock_config

        platform = Linux_armPlatform(mock_platform_manifest)

        value = platform._get_config_default("upload_timeout", 300)
        assert value == 300


class TestShowManualUploadInstructions:
    """Test cases for _show_manual_upload_instructions method."""

    @patch("builtins.print")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_show_manual_upload_instructions(
        self, mock_base_init, mock_get_config, mock_print, mock_platform_manifest
    ):
        """Test manual upload instructions display."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)

        source = ["/path/to/binary"]
        result = platform._show_manual_upload_instructions(source)

        assert result == 0
        # Verify some key output was printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        assert any("MANUAL UPLOAD" in str(call) for call in print_calls)
        assert any("/path/to/binary" in str(call) for call in print_calls)


class TestAddDebugToBoard:
    """Test cases for _add_debug_to_board method."""

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_add_debug_to_board(
        self, mock_base_init, mock_get_config, mock_platform_manifest, mock_board_config
    ):
        """Test adding debug configuration to board."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        platform = Linux_armPlatform(mock_platform_manifest)

        board = platform._add_debug_to_board(mock_board_config)

        assert "debug" in board.manifest
        assert "tools" in board.manifest["debug"]
        assert "gdbserver-ssh" in board.manifest["debug"]["tools"]
        assert "gdb-remote" in board.manifest["debug"]["tools"]
        assert "default" in board.manifest["debug"]
        assert board.manifest["debug"]["default"] == "gdbserver-ssh"


class TestOnUpload:
    """Test cases for on_upload protocol dispatch."""

    @patch("platform_module.Linux_armPlatform._show_manual_upload_instructions")
    @patch("platform_module.Linux_armPlatform._get_upload_protocol")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_on_upload_dispatches_manual_protocol(
        self,
        mock_base_init,
        mock_get_config,
        mock_get_protocol,
        mock_manual,
        mock_platform_manifest,
    ):
        """Test on_upload routes to manual instructions when protocol is manual."""
        from platform_module import Linux_armPlatform

        from platform_constants import UploadProtocol

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_get_protocol.return_value = UploadProtocol.MANUAL
        mock_manual.return_value = 0

        platform = Linux_armPlatform(mock_platform_manifest)
        result = platform.on_upload(target=Mock(), source=["/bin/app"], env=Mock())

        assert result == 0
        mock_manual.assert_called_once()

    @patch("platform_module.Linux_armPlatform._upload_scp")
    @patch("platform_module.Linux_armPlatform._get_upload_protocol")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_on_upload_dispatches_scp_protocol(
        self,
        mock_base_init,
        mock_get_config,
        mock_get_protocol,
        mock_scp,
        mock_platform_manifest,
    ):
        """Test on_upload routes to SCP handler when protocol is scp."""
        from platform_module import Linux_armPlatform

        from platform_constants import UploadProtocol

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_get_protocol.return_value = UploadProtocol.SCP
        mock_scp.return_value = 0

        platform = Linux_armPlatform(mock_platform_manifest)
        result = platform.on_upload(target=Mock(), source=["/bin/app"], env=Mock())

        assert result == 0
        mock_scp.assert_called_once()

    @patch("platform_module.Linux_armPlatform._upload_rsync")
    @patch("platform_module.Linux_armPlatform._get_upload_protocol")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_on_upload_dispatches_rsync_protocol(
        self,
        mock_base_init,
        mock_get_config,
        mock_get_protocol,
        mock_rsync,
        mock_platform_manifest,
    ):
        """Test on_upload routes to rsync handler when protocol is rsync."""
        from platform_module import Linux_armPlatform

        from platform_constants import UploadProtocol

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_get_protocol.return_value = UploadProtocol.RSYNC
        mock_rsync.return_value = 0

        platform = Linux_armPlatform(mock_platform_manifest)
        result = platform.on_upload(target=Mock(), source=["/bin/app"], env=Mock())

        assert result == 0
        mock_rsync.assert_called_once()

    @patch("platform_module.Linux_armPlatform._upload_ssh")
    @patch("platform_module.Linux_armPlatform._get_upload_protocol")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_on_upload_dispatches_ssh_protocol(
        self,
        mock_base_init,
        mock_get_config,
        mock_get_protocol,
        mock_ssh,
        mock_platform_manifest,
    ):
        """Test on_upload routes to SSH handler when protocol is ssh."""
        from platform_module import Linux_armPlatform

        from platform_constants import UploadProtocol

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_get_protocol.return_value = UploadProtocol.SSH
        mock_ssh.return_value = 0

        platform = Linux_armPlatform(mock_platform_manifest)
        result = platform.on_upload(target=Mock(), source=["/bin/app"], env=Mock())

        assert result == 0
        mock_ssh.assert_called_once()


class TestOnMonitor:
    """Test cases for on_monitor method."""

    @patch("builtins.print")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_on_monitor_skips_when_upload_run_after_enabled(
        self,
        mock_base_init,
        mock_get_config,
        mock_print,
        mock_platform_manifest,
    ):
        """Test on_monitor returns 0 without connecting when upload_run_after=True."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        env = Mock()
        env.GetProjectOption = Mock(
            side_effect=lambda key, default=None: (
                True if key == "upload_run_after" else default
            )
        )

        platform = Linux_armPlatform(mock_platform_manifest)
        result = platform.on_monitor(target=Mock(), source=Mock(), env=env)

        assert result == 0
        print_calls = [str(c) for c in mock_print.call_args_list]
        assert any("MONITOR SKIPPED" in c for c in print_calls)

    @patch("builtins.print")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_on_monitor_prints_config_message_when_no_port(
        self,
        mock_base_init,
        mock_get_config,
        mock_print,
        mock_platform_manifest,
    ):
        """Test on_monitor prints configuration hint when upload_port is not set."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        env = Mock()
        env.GetProjectOption = Mock(return_value=None)

        platform = Linux_armPlatform(mock_platform_manifest)
        result = platform.on_monitor(target=Mock(), source=Mock(), env=env)

        assert result == 0
        print_calls = [str(c) for c in mock_print.call_args_list]
        assert any("REMOTE MONITORING NOT CONFIGURED" in c for c in print_calls)

    @patch("platform_module.Linux_armPlatform._run_remote_command")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_on_monitor_calls_run_remote_command_when_port_set(
        self,
        mock_base_init,
        mock_get_config,
        mock_run_remote,
        mock_platform_manifest,
    ):
        """Test on_monitor delegates to _run_remote_command when upload_port is set."""
        from platform_module import Linux_armPlatform

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_run_remote.return_value = 0

        env = Mock()
        env.GetProjectOption = Mock(
            side_effect=lambda key, default=None: (
                "pi@host:/bin/app" if key == "upload_port" else default
            )
        )
        env.get = Mock(return_value=None)

        platform = Linux_armPlatform(mock_platform_manifest)
        result = platform.on_monitor(target=Mock(), source=[], env=env)

        assert result == 0
        mock_run_remote.assert_called_once()


class TestConfigureDebugSession:
    """Test cases for configure_debug_session method."""

    @patch("platform_module.Linux_armPlatform._configure_gdbserver_ssh")
    @patch("platform_module.Linux_armPlatform._parse_debug_connection_info")
    @patch("platform_module.Linux_armPlatform._determine_gdb_executable")
    @patch("platform_module.Linux_armPlatform.board_config")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_gdbserver_ssh_tool_calls_configure_gdbserver(
        self,
        mock_base_init,
        mock_get_config,
        mock_board_config,
        mock_determine_gdb,
        mock_parse_conn,
        mock_configure_gdbserver,
        mock_platform_manifest,
    ):
        """configure_debug_session routes to _configure_gdbserver_ssh for gdbserver-ssh."""
        from platform_module import Linux_armPlatform

        from platform_constants import DebugTools

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_board_config.return_value = Mock(**{"get.return_value": "armv7"})
        mock_determine_gdb.return_value = "gdb-multiarch"
        mock_parse_conn.return_value = ("pi", "host", "/tmp/app", "22", None)

        debug_config = Mock()
        debug_config.env_name = "env"
        debug_config.tool_name = DebugTools.GDBSERVER_SSH
        debug_config.env_options = {}
        debug_config.build_data = {}

        platform = Linux_armPlatform(mock_platform_manifest)
        platform.configure_debug_session(debug_config)

        mock_configure_gdbserver.assert_called_once()
        # strict_host_check should default to False
        call_args = mock_configure_gdbserver.call_args
        assert (
            call_args[0][-1] is False or call_args[1].get("strict_host_check") is False
        )

    @patch("platform_module.Linux_armPlatform._configure_gdbserver_ssh")
    @patch("platform_module.Linux_armPlatform._parse_debug_connection_info")
    @patch("platform_module.Linux_armPlatform._determine_gdb_executable")
    @patch("platform_module.Linux_armPlatform.board_config")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_gdbserver_ssh_passes_strict_host_check_when_enabled(
        self,
        mock_base_init,
        mock_get_config,
        mock_board_config,
        mock_determine_gdb,
        mock_parse_conn,
        mock_configure_gdbserver,
        mock_platform_manifest,
    ):
        """debug_strict_host_check=yes is forwarded to _configure_gdbserver_ssh."""
        from platform_module import Linux_armPlatform

        from platform_constants import DebugTools

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_board_config.return_value = Mock(**{"get.return_value": "armv7"})
        mock_determine_gdb.return_value = "gdb-multiarch"
        mock_parse_conn.return_value = ("pi", "host", "/tmp/app", "22", None)

        debug_config = Mock()
        debug_config.env_name = "env"
        debug_config.tool_name = DebugTools.GDBSERVER_SSH
        debug_config.env_options = {"debug_strict_host_check": "yes"}
        debug_config.build_data = {}

        platform = Linux_armPlatform(mock_platform_manifest)
        platform.configure_debug_session(debug_config)

        mock_configure_gdbserver.assert_called_once()
        call_args = mock_configure_gdbserver.call_args
        assert call_args[0][-1] is True

    @patch("platform_module.Linux_armPlatform._configure_gdb_remote")
    @patch("platform_module.Linux_armPlatform._parse_debug_connection_info")
    @patch("platform_module.Linux_armPlatform._determine_gdb_executable")
    @patch("platform_module.Linux_armPlatform.board_config")
    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_gdb_remote_tool_calls_configure_gdb_remote(
        self,
        mock_base_init,
        mock_get_config,
        mock_board_config,
        mock_determine_gdb,
        mock_parse_conn,
        mock_configure_gdb_remote,
        mock_platform_manifest,
    ):
        """configure_debug_session routes to _configure_gdb_remote for gdb-remote."""
        from platform_module import Linux_armPlatform

        from platform_constants import DebugTools

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()
        mock_board_config.return_value = Mock(**{"get.return_value": "armv7"})
        mock_determine_gdb.return_value = "gdb-multiarch"
        mock_parse_conn.return_value = ("pi", "host", "/tmp/app", "22", None)

        debug_config = Mock()
        debug_config.env_name = "env"
        debug_config.tool_name = DebugTools.GDB_REMOTE
        debug_config.env_options = {}
        debug_config.build_data = {}

        platform = Linux_armPlatform(mock_platform_manifest)
        platform.configure_debug_session(debug_config)

        mock_configure_gdb_remote.assert_called_once()


class TestBuildDebugInitCommands:
    """Test cases for _build_debug_init_commands method."""

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_gdbserver_ssh_commands_include_target_remote(
        self,
        mock_base_init,
        mock_get_config,
        mock_platform_manifest,
    ):
        """Test init commands for gdbserver-ssh include target extended-remote."""
        from platform_module import Linux_armPlatform

        from platform_constants import DebugTools

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        debug_config = Mock()
        debug_config.port = "| ssh pi@host gdbserver - /tmp/app"
        debug_config.env_options = {}
        debug_config.init_cmds = []

        platform = Linux_armPlatform(mock_platform_manifest)
        cmds = platform._build_debug_init_commands(
            DebugTools.GDBSERVER_SSH, debug_config, "/tmp/app"
        )

        assert any("target extended-remote" in cmd for cmd in cmds)
        assert any("/tmp/app" in cmd for cmd in cmds)

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_gdb_remote_commands_include_target_remote(
        self,
        mock_base_init,
        mock_get_config,
        mock_platform_manifest,
    ):
        """Test init commands for gdb-remote include target extended-remote."""
        from platform_module import Linux_armPlatform

        from platform_constants import DebugTools

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        debug_config = Mock()
        debug_config.port = ":3333"
        debug_config.env_options = {}
        debug_config.init_cmds = []

        platform = Linux_armPlatform(mock_platform_manifest)
        cmds = platform._build_debug_init_commands(
            DebugTools.GDB_REMOTE, debug_config, "/tmp/app"
        )

        assert any("target extended-remote" in cmd for cmd in cmds)

    @patch("platform_module.get_platform_config")
    @patch("platform_module.PlatformBase.__init__")
    def test_custom_init_cmds_are_appended(
        self,
        mock_base_init,
        mock_get_config,
        mock_platform_manifest,
    ):
        """Test custom debug_init_cmds from env_options are appended."""
        from platform_module import Linux_armPlatform

        from platform_constants import DebugTools

        mock_base_init.return_value = None
        mock_get_config.return_value = Mock()

        debug_config = Mock()
        debug_config.port = ":3333"
        debug_config.env_options = {"debug_init_cmds": ["monitor reset"]}
        debug_config.init_cmds = []

        platform = Linux_armPlatform(mock_platform_manifest)
        cmds = platform._build_debug_init_commands(
            DebugTools.GDB_REMOTE, debug_config, "/tmp/app"
        )

        assert "monitor reset" in cmds


class TestUploadScp:
    """Test cases for _upload_scp method."""

    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_successful_upload_returns_zero(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=0)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        result = platform._upload_scp(Mock(), [source_mock], env)
        assert result == 0
        mock_run.assert_called_once()

    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_failure_raises_exception(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=1)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        with pytest.raises(exception.PlatformioException, match="SCP upload failed"):
            platform._upload_scp(Mock(), [source_mock], env)

    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_timeout_raises_exception(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        import subprocess

        mock_run.side_effect = subprocess.TimeoutExpired(cmd="scp", timeout=120)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        with pytest.raises(exception.PlatformioException, match="timeout"):
            platform._upload_scp(Mock(), [source_mock], env)

    @patch("platform_module.Linux_armPlatform._run_remote_command")
    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_run_after_calls_run_remote_command(
        self,
        mock_print,
        mock_check_tool,
        mock_run,
        mock_run_remote,
        make_platform,
        make_env,
    ):
        mock_run.return_value = Mock(returncode=0)
        mock_run_remote.return_value = 0
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env(upload_run_after="yes")

        result = platform._upload_scp(Mock(), [source_mock], env)
        assert result == 0
        mock_run_remote.assert_called_once()

    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_run_after_false_skips_run_remote(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=0)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env(upload_run_after=False)

        with patch.object(platform, "_run_remote_command") as mock_remote:
            result = platform._upload_scp(Mock(), [source_mock], env)
            assert result == 0
            mock_remote.assert_not_called()


class TestUploadRsync:
    """Test cases for _upload_rsync method."""

    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_successful_upload_returns_zero(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=0)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        result = platform._upload_rsync(Mock(), [source_mock], env)
        assert result == 0
        mock_run.assert_called_once()

    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_failure_raises_exception(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=1)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        with pytest.raises(exception.PlatformioException, match="Rsync upload failed"):
            platform._upload_rsync(Mock(), [source_mock], env)

    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_timeout_raises_exception(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        import subprocess

        mock_run.side_effect = subprocess.TimeoutExpired(cmd="rsync", timeout=120)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        with pytest.raises(exception.PlatformioException, match="timeout"):
            platform._upload_rsync(Mock(), [source_mock], env)

    @patch("platform_module.Linux_armPlatform._run_remote_command")
    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_run_after_calls_run_remote_command(
        self,
        mock_print,
        mock_check_tool,
        mock_run,
        mock_run_remote,
        make_platform,
        make_env,
    ):
        mock_run.return_value = Mock(returncode=0)
        mock_run_remote.return_value = 0
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env(upload_run_after="yes")

        result = platform._upload_rsync(Mock(), [source_mock], env)
        assert result == 0
        mock_run_remote.assert_called_once()


class TestUploadSsh:
    """Test cases for _upload_ssh method."""

    @patch("builtins.open", mock_open(read_data=b"\x00\x01\x02"))
    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_successful_upload_returns_zero(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=0)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        result = platform._upload_ssh(Mock(), [source_mock], env)
        assert result == 0
        mock_run.assert_called_once()

    @patch("builtins.open", mock_open(read_data=b"\x00\x01\x02"))
    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_failure_raises_exception(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=1)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        with pytest.raises(exception.PlatformioException, match="SSH upload failed"):
            platform._upload_ssh(Mock(), [source_mock], env)

    @patch("builtins.open", mock_open(read_data=b"\x00\x01\x02"))
    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_timeout_raises_exception(
        self, mock_print, mock_check_tool, mock_run, make_platform, make_env
    ):
        import subprocess

        mock_run.side_effect = subprocess.TimeoutExpired(cmd="ssh", timeout=120)
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env()

        with pytest.raises(exception.PlatformioException, match="timeout"):
            platform._upload_ssh(Mock(), [source_mock], env)

    @patch("builtins.open", mock_open(read_data=b"\x00\x01\x02"))
    @patch("platform_module.Linux_armPlatform._run_remote_command")
    @patch("platform_module.subprocess.run")
    @patch("platform_module.Linux_armPlatform._check_upload_tool")
    @patch("builtins.print")
    def test_upload_run_after_calls_run_remote_command(
        self,
        mock_print,
        mock_check_tool,
        mock_run,
        mock_run_remote,
        make_platform,
        make_env,
    ):
        mock_run.return_value = Mock(returncode=0)
        mock_run_remote.return_value = 0
        platform = make_platform()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/binary"
        env = make_env(upload_run_after="yes")

        result = platform._upload_ssh(Mock(), [source_mock], env)
        assert result == 0
        mock_run_remote.assert_called_once()


class TestRunRemoteCommand:
    """Test cases for _run_remote_command method."""

    @patch("platform_module.subprocess.run")
    @patch("builtins.print")
    def test_successful_run_returns_zero(
        self, mock_print, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=0)
        platform = make_platform()
        env = make_env()

        result = platform._run_remote_command(
            "pi", "host", "22", None, "/home/pi/app", env
        )
        assert result == 0

    @patch("platform_module.subprocess.run")
    @patch("builtins.print")
    def test_nonzero_exit_code_returned(
        self, mock_print, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=42)
        platform = make_platform()
        env = make_env()

        result = platform._run_remote_command(
            "pi", "host", "22", None, "/home/pi/app", env
        )
        assert result == 42

    @patch("platform_module.subprocess.run")
    @patch("builtins.print")
    def test_timeout_raises_exception(
        self, mock_print, mock_run, make_platform, make_env
    ):
        import subprocess

        mock_run.side_effect = subprocess.TimeoutExpired(cmd="ssh", timeout=300)
        platform = make_platform()
        env = make_env()

        with pytest.raises(exception.PlatformioException, match="timeout"):
            platform._run_remote_command("pi", "host", "22", None, "/home/pi/app", env)

    @patch("platform_module.subprocess.run")
    @patch("builtins.print")
    def test_custom_run_command_used(
        self, mock_print, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=0)
        platform = make_platform()
        env = make_env(upload_run_command="sudo /opt/myapp --daemon")

        platform._run_remote_command("pi", "host", "22", None, "/home/pi/app", env)

        # The SSH command should contain the custom run command
        cmd_arg = mock_run.call_args[0][0]
        assert any("sudo /opt/myapp --daemon" in str(a) for a in cmd_arg)

    @patch("platform_module.subprocess.run")
    @patch("builtins.print")
    def test_directory_path_appends_program_name(
        self, mock_print, mock_run, make_platform, make_env
    ):
        mock_run.return_value = Mock(returncode=0)
        platform = make_platform()
        env = make_env()

        source_mock = Mock()
        source_mock.__str__ = lambda self: "/local/build/myapp"

        platform._run_remote_command(
            "pi", "host", "22", None, "/home/pi/bin/", env, source=[source_mock]
        )

        # Should construct /home/pi/bin/myapp (via posixpath.join)
        cmd_arg = mock_run.call_args[0][0]
        cmd_str = " ".join(str(a) for a in cmd_arg)
        assert "/home/pi/bin/myapp" in cmd_str


class TestParseDebugConnectionInfo:
    """Test _parse_debug_connection_info extracts connection details correctly."""

    def test_parses_full_upload_port(self, make_platform):
        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {
            "upload_port": "admin@myhost.local:/opt/myapp",
        }
        debug_config.build_data = {}

        user, host, prog_path, ssh_port, ssh_key = (
            platform._parse_debug_connection_info(debug_config)
        )

        assert user == "admin"
        assert host == "myhost.local"
        assert prog_path == "/opt/myapp"

    def test_defaults_when_minimal_config(self, make_platform):
        from platform_constants import SSHDefaults

        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {}
        debug_config.build_data = {}

        user, host, prog_path, ssh_port, ssh_key = (
            platform._parse_debug_connection_info(debug_config)
        )

        assert user == SSHDefaults.USER
        assert host is None
        assert ssh_port == SSHDefaults.PORT
        assert ssh_key is None

    def test_directory_path_appends_program_name(self, make_platform):
        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {
            "upload_port": "pi@host:/home/pi/bin/",
        }
        debug_config.build_data = {"prog_path": "/local/build/myapp"}

        user, host, prog_path, ssh_port, ssh_key = (
            platform._parse_debug_connection_info(debug_config)
        )

        assert prog_path == "/home/pi/bin/myapp"

    def test_custom_ssh_port_and_key(self, make_platform):
        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {
            "upload_port": "pi@host:/app",
            "debug_ssh_port": "2222",
            "debug_ssh_key": "/home/user/.ssh/custom_key",
        }
        debug_config.build_data = {}

        user, host, prog_path, ssh_port, ssh_key = (
            platform._parse_debug_connection_info(debug_config)
        )

        assert ssh_port == "2222"
        assert ssh_key == "/home/user/.ssh/custom_key"

    def test_upload_port_takes_precedence_over_debug_port(self, make_platform):
        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {
            "upload_port": "pi@upload-host:/app",
            "debug_port": "pi@debug-host:/debug-app",
        }
        debug_config.build_data = {}

        user, host, prog_path, ssh_port, ssh_key = (
            platform._parse_debug_connection_info(debug_config)
        )

        # upload_port is checked first in `or` chain, so it wins when both are set
        assert host == "upload-host"
        assert prog_path == "/app"


    def test_fallback_at_sign_parsing(self, make_platform):
        """Test fallback parsing when parse_upload_port raises ValueError."""
        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {
            "upload_port": "pi@somehost",
        }
        debug_config.build_data = {}

        with patch("ssh_utils.parse_upload_port", side_effect=ValueError("bad")):
            user, host, prog_path, ssh_port, ssh_key = (
                platform._parse_debug_connection_info(debug_config)
            )

        assert user == "pi"
        assert host == "somehost"

    def test_fallback_host_only_no_at(self, make_platform):
        """Test fallback parsing for host-only format without @ sign."""
        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {
            "upload_port": "myhost:3333",
        }
        debug_config.build_data = {}

        with patch("ssh_utils.parse_upload_port", side_effect=ValueError("bad")):
            user, host, prog_path, ssh_port, ssh_key = (
                platform._parse_debug_connection_info(debug_config)
            )

        assert host == "myhost"

    def test_debug_port_used_when_no_upload_port(self, make_platform):
        """Test debug_port is used when upload_port is not set."""
        platform = make_platform()

        debug_config = Mock()
        debug_config.env_options = {
            "debug_port": "pi@debug-host:/debug-app",
        }
        debug_config.build_data = {}

        user, host, prog_path, ssh_port, ssh_key = (
            platform._parse_debug_connection_info(debug_config)
        )

        assert host == "debug-host"
        assert prog_path == "/debug-app"


class TestShowWelcomeIfNeeded:
    """Test _show_welcome_if_needed first-run welcome message."""

    def _make_platform_raw(self, mock_platform_manifest):
        """Create platform WITHOUT patching _show_welcome_if_needed."""
        with patch("platform_module.PlatformBase.__init__", return_value=None), \
             patch("platform_module.get_platform_config", return_value=Mock()):
            from platform_module import Linux_armPlatform
            return Linux_armPlatform(mock_platform_manifest)

    @patch("builtins.print")
    @patch("os.path.exists", return_value=False)
    @patch("pathlib.Path.touch")
    def test_first_run_shows_message(
        self, mock_touch, mock_exists, mock_print, mock_platform_manifest
    ):
        platform = self._make_platform_raw(mock_platform_manifest)
        platform._show_welcome_if_needed()

        # Should have printed the welcome banner
        print_calls = [str(c) for c in mock_print.call_args_list]
        assert any("Welcome" in c for c in print_calls)
        assert mock_touch.called

    @patch("builtins.print")
    @patch("os.path.exists", return_value=True)
    def test_second_run_skips_message(
        self, mock_exists, mock_print, mock_platform_manifest
    ):
        platform = self._make_platform_raw(mock_platform_manifest)
        platform._show_welcome_if_needed()

        # Should NOT print anything when marker exists
        mock_print.assert_not_called()

    @patch("builtins.print")
    @patch("os.path.exists", return_value=False)
    @patch("pathlib.Path.touch", side_effect=OSError("permission denied"))
    def test_marker_write_failure_still_shows_message(
        self, mock_touch, mock_exists, mock_print, mock_platform_manifest
    ):
        platform = self._make_platform_raw(mock_platform_manifest)
        platform._show_welcome_if_needed()

        # Should still show message even if marker file can't be written
        print_calls = [str(c) for c in mock_print.call_args_list]
        assert any("Welcome" in c for c in print_calls)


class TestPosixPathUsage:
    """Verify remote paths always use forward slashes (posixpath, not os.path)."""

    def test_posixpath_join_produces_forward_slashes(self):
        import posixpath

        result = posixpath.join("/home/pi/", "program")
        assert "\\" not in result
        assert result == "/home/pi/program"

    def test_posixpath_join_without_trailing_slash(self):
        import posixpath

        result = posixpath.join("/home/pi", "program")
        assert result == "/home/pi/program"

    def test_posixpath_join_with_rstrip(self):
        """Mirrors usage in _parse_debug_connection_info: posixpath.join(path.rstrip('/'), name)."""
        import posixpath

        result = posixpath.join("/home/pi/".rstrip("/"), "program")
        assert result == "/home/pi/program"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
