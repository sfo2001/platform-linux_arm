#!/usr/bin/env python3
"""
Unit tests for RemoteTestUploader in platform-test-uploader.py.

Tests cover __init__, parse_test_port, upload_test_binary, execute_test_binary, and run().
"""

import importlib.util
import os
import subprocess
import sys
from unittest.mock import MagicMock, Mock, call, patch

import pytest
from platformio import exception

from platform_constants import SSHDefaults

# Load module with hyphenated name
_uploader_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "platform_test_uploader.py",
)
_spec = importlib.util.spec_from_file_location("platform_test_uploader", _uploader_path)
_uploader_module = importlib.util.module_from_spec(_spec)
sys.modules["platform_test_uploader"] = _uploader_module
_spec.loader.exec_module(_uploader_module)

RemoteTestUploader = _uploader_module.RemoteTestUploader


def _make_env(**options):
    """Return a mock PlatformIO env where GetProjectOption returns kwargs values or None."""
    env = Mock()

    def get_option(key, default=None):
        return options.get(key, default)

    env.GetProjectOption = Mock(side_effect=get_option)
    return env


@pytest.fixture
def mock_config():
    cfg = Mock()
    cfg.get = Mock(side_effect=lambda key, default: default)
    return cfg


@pytest.fixture
def basic_env():
    return _make_env(test_port="pi@raspberrypi.local:/tmp/test_prog")


class TestRemoteTestUploaderInit:
    """Test __init__ sets up expected attributes."""

    @patch("platform_test_uploader.get_platform_config")
    def test_init_sets_default_attributes(
        self, mock_get_config, mock_config, basic_env
    ):
        mock_get_config.return_value = mock_config

        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        assert uploader.user is None
        assert uploader.host is None
        assert uploader.remote_path is None
        assert uploader.ssh_key is None
        assert uploader.ssh_port == SSHDefaults.PORT
        assert uploader._config is mock_config

    @patch("platform_test_uploader.get_platform_config")
    def test_init_calls_get_platform_config(
        self, mock_get_config, mock_config, basic_env
    ):
        mock_get_config.return_value = mock_config

        RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        mock_get_config.assert_called_once()


class TestParseTestPort:
    """Test parse_test_port populates connection components."""

    @patch("platform_test_uploader.get_platform_config")
    def test_full_format_parsed_correctly(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        env = _make_env(test_port="admin@myhost.local:/opt/testbin")

        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.parse_test_port()

        assert uploader.user == "admin"
        assert uploader.host == "myhost.local"
        assert uploader.remote_path == "/opt/testbin"

    @patch("platform_test_uploader.get_platform_config")
    def test_fallback_to_upload_port(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        env = _make_env(upload_port="pi@fallback.host:/tmp/prog")

        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.parse_test_port()

        assert uploader.host == "fallback.host"

    @patch("platform_test_uploader.get_platform_config")
    def test_missing_port_raises_exception(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        env = _make_env()  # no test_port or upload_port

        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)

        with pytest.raises(
            exception.PlatformioException,
            match="test_port or upload_port is not configured",
        ):
            uploader.parse_test_port()

    @patch("platform_test_uploader.get_platform_config")
    def test_custom_username_and_path_defaults(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        env = _make_env(
            test_port="myhost.example.com",
            test_username="customuser",
            test_path="/custom/path",
        )

        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.parse_test_port()

        assert uploader.user == "customuser"
        assert uploader.remote_path == "/custom/path"


class TestUploadTestBinary:
    """Test upload_test_binary delegates to subprocess correctly."""

    def _make_uploader(self, mock_config):
        with patch(
            "platform_test_uploader.get_platform_config", return_value=mock_config
        ):
            env = _make_env(test_port="pi@host:/tmp/prog")
            source_mock = Mock()
            source_mock.__str__ = lambda self: "/local/testbinary"
            uploader = RemoteTestUploader(target=Mock(), source=[source_mock], env=env)
        uploader.user = "pi"
        uploader.host = "host"
        uploader.remote_path = "/tmp/prog"
        uploader.ssh_port = SSHDefaults.PORT
        uploader.ssh_key = None
        return uploader

    @patch("platform_test_uploader.get_platform_config")
    def test_successful_upload_returns_zero(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        completed = Mock()
        completed.returncode = 0
        completed.stderr = ""

        with patch("subprocess.run", return_value=completed) as mock_run:
            result = uploader.upload_test_binary()

        assert result == 0
        assert len(mock_run.call_args_list) == 2  # scp upload + chmod
        first_cmd = mock_run.call_args_list[0][0][0]
        second_cmd = mock_run.call_args_list[1][0][0]
        assert any("scp" in str(a) for a in first_cmd)
        assert any("chmod" in str(a) for a in second_cmd)

    @patch("platform_test_uploader.get_platform_config")
    def test_upload_failure_raises_exception(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        failed = Mock()
        failed.returncode = 1
        failed.stderr = "Connection refused"

        with patch("subprocess.run", return_value=failed):
            with pytest.raises(
                exception.PlatformioException, match="Failed to upload test binary"
            ):
                uploader.upload_test_binary()

    @patch("platform_test_uploader.get_platform_config")
    def test_upload_timeout_raises_exception(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        with patch(
            "subprocess.run",
            side_effect=subprocess.TimeoutExpired(cmd="scp", timeout=120),
        ):
            with pytest.raises(exception.PlatformioException, match="timeout"):
                uploader.upload_test_binary()


class TestStrictHostCheck:
    """Test strict host check option flows through to SSH/SCP commands."""

    @patch("platform_test_uploader.get_platform_config")
    def test_ssh_command_includes_strict_checking_when_enabled(
        self, mock_get_config, mock_config
    ):
        mock_get_config.return_value = mock_config
        env = _make_env(
            test_port="pi@host:/tmp/prog",
            test_strict_host_check="yes",
        )
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.parse_test_port()

        cmd = uploader.build_ssh_command("ls")
        assert "StrictHostKeyChecking=no" not in cmd

    @patch("platform_test_uploader.get_platform_config")
    def test_ssh_command_disables_strict_checking_by_default(
        self, mock_get_config, mock_config
    ):
        mock_get_config.return_value = mock_config
        env = _make_env(test_port="pi@host:/tmp/prog")
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.parse_test_port()

        cmd = uploader.build_ssh_command("ls")
        assert "StrictHostKeyChecking=no" in cmd

    @patch("platform_test_uploader.get_platform_config")
    def test_scp_command_includes_strict_checking_when_enabled(
        self, mock_get_config, mock_config
    ):
        mock_get_config.return_value = mock_config
        env = _make_env(
            test_port="pi@host:/tmp/prog",
            test_strict_host_check="true",
        )
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.parse_test_port()

        cmd = uploader.build_scp_command("/local/bin", "/remote/bin")
        assert "StrictHostKeyChecking=no" not in cmd


class TestRunWorkflow:
    """Test the run() orchestration method."""

    @patch("platform_test_uploader.get_platform_config")
    def test_run_returns_exit_code_on_success(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        env = _make_env(test_port="pi@host:/tmp/prog")
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)

        uploader.parse_test_port = Mock()
        uploader.check_ssh_available = Mock()
        uploader.upload_test_binary = Mock(return_value=0)
        uploader.execute_test_binary = Mock(return_value=0)

        result = uploader.run()

        assert result == 0
        uploader.parse_test_port.assert_called_once()
        uploader.check_ssh_available.assert_called_once()
        uploader.upload_test_binary.assert_called_once()
        uploader.execute_test_binary.assert_called_once()

    @patch("platform_test_uploader.get_platform_config")
    def test_run_returns_nonzero_on_test_failure(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        env = _make_env(test_port="pi@host:/tmp/prog")
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)

        uploader.parse_test_port = Mock()
        uploader.check_ssh_available = Mock()
        uploader.upload_test_binary = Mock(return_value=0)
        uploader.execute_test_binary = Mock(return_value=1)

        result = uploader.run()

        assert result == 1

    @patch("platform_test_uploader.get_platform_config")
    def test_run_returns_one_on_exception(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        env = _make_env(test_port="pi@host:/tmp/prog")
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)

        uploader.parse_test_port = Mock(side_effect=Exception("connection failed"))

        result = uploader.run()

        assert result == 1


class TestCheckSSHAvailable:
    """Test check_ssh_available raises when tools are missing."""

    @patch("platform_test_uploader.get_platform_config")
    def test_raises_when_ssh_missing(self, mock_get_config, mock_config, basic_env):
        mock_get_config.return_value = mock_config
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        with patch("shutil.which", return_value=None):
            with pytest.raises(
                exception.PlatformioException, match="SSH is not installed"
            ):
                uploader.check_ssh_available()

    @patch("platform_test_uploader.get_platform_config")
    def test_raises_when_scp_missing(self, mock_get_config, mock_config, basic_env):
        mock_get_config.return_value = mock_config
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        def which_side_effect(cmd):
            return "/usr/bin/ssh" if cmd == "ssh" else None

        with patch("shutil.which", side_effect=which_side_effect):
            with pytest.raises(
                exception.PlatformioException, match="SCP is not installed"
            ):
                uploader.check_ssh_available()

    @patch("platform_test_uploader.get_platform_config")
    def test_passes_when_both_available(self, mock_get_config, mock_config, basic_env):
        mock_get_config.return_value = mock_config
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        with patch("shutil.which", return_value="/usr/bin/ssh"):
            uploader.check_ssh_available()  # must not raise


class TestExtractExitCode:
    """Test _extract_exit_code parses marker lines correctly."""

    def _make_uploader(self, mock_config):
        with patch(
            "platform_test_uploader.get_platform_config", return_value=mock_config
        ):
            env = _make_env(test_port="pi@host:/tmp/prog")
            uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        return uploader

    @patch("platform_test_uploader.get_platform_config")
    def test_valid_marker_returns_code(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)
        from platform_constants import TestConstants

        line = f"{TestConstants.EXIT_CODE_MARKER}42\n"
        assert uploader._extract_exit_code(line) == 42

    @patch("platform_test_uploader.get_platform_config")
    def test_malformed_marker_returns_zero(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)
        from platform_constants import TestConstants

        line = f"{TestConstants.EXIT_CODE_MARKER}not_a_number\n"
        assert uploader._extract_exit_code(line) == 0

    @patch("platform_test_uploader.get_platform_config")
    def test_empty_string_returns_zero(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)
        assert uploader._extract_exit_code("") == 0


class TestCollectTestOutput:
    """Test _collect_test_output timeout/drain and happy path."""

    def _make_uploader(self, mock_config):
        with patch(
            "platform_test_uploader.get_platform_config", return_value=mock_config
        ):
            env = _make_env(test_port="pi@host:/tmp/prog")
            uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.user = "pi"
        uploader.host = "host"
        uploader.remote_path = "/tmp/prog"
        uploader.ssh_port = SSHDefaults.PORT
        uploader.ssh_key = None
        return uploader

    @patch("platform_test_uploader.get_platform_config")
    def test_timeout_kills_process_and_raises(self, mock_get_config, mock_config):
        """TimeoutExpired path: process.kill() must be called and exception raised."""
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        mock_proc = Mock()
        mock_proc.communicate.side_effect = [
            subprocess.TimeoutExpired(cmd=["ssh"], timeout=10),
            ("", ""),  # drain after kill
        ]

        with pytest.raises(exception.PlatformioException, match="timeout"):
            uploader._collect_test_output(mock_proc, test_timeout=10)

        mock_proc.kill.assert_called_once()
        assert mock_proc.communicate.call_count == 2

    @patch("platform_test_uploader.get_platform_config")
    def test_returns_exit_code_from_marker(self, mock_get_config, mock_config):
        """Happy path: exit code is extracted from marker line."""
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)
        from platform_constants import TestConstants

        output = f"test output\n{TestConstants.EXIT_CODE_MARKER}7\n"
        mock_proc = Mock()
        mock_proc.communicate.return_value = (output, "")

        result = uploader._collect_test_output(mock_proc, test_timeout=30)
        assert result == 7


class TestExecuteTestBinary:
    """Test execute_test_binary delegates to Popen and streams output."""

    def _make_uploader(self, mock_config):
        with patch(
            "platform_test_uploader.get_platform_config", return_value=mock_config
        ):
            env = _make_env(test_port="pi@host:/tmp/prog")
            uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.user = "pi"
        uploader.host = "host"
        uploader.remote_path = "/tmp/prog"
        uploader.ssh_port = SSHDefaults.PORT
        uploader.ssh_key = None
        return uploader

    @patch("platform_test_uploader.get_platform_config")
    def test_execute_binary_returns_exit_code(self, mock_get_config, mock_config):
        """execute_test_binary calls Popen and returns exit code from _collect_test_output."""
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        mock_proc = Mock()
        with patch("subprocess.Popen", return_value=mock_proc) as mock_popen:
            with patch.object(uploader, "_collect_test_output", return_value=5):
                result = uploader.execute_test_binary()

        assert result == 5
        mock_popen.assert_called_once()
        # Verify stdout=PIPE was used
        call_kwargs = mock_popen.call_args[1]
        assert call_kwargs.get("stdout") == subprocess.PIPE


class TestBuildTestCommand:
    """Test _build_test_command constructs safe remote commands."""

    def _make_uploader(self, mock_config, remote_path="/tmp/prog"):
        with patch(
            "platform_test_uploader.get_platform_config", return_value=mock_config
        ):
            env = _make_env(test_port="pi@host:/tmp/prog")
            uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=env)
        uploader.remote_path = remote_path
        return uploader

    @patch("platform_test_uploader.get_platform_config")
    def test_command_includes_exit_code_marker(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        from platform_constants import TestConstants

        cmd = uploader._build_test_command()
        assert TestConstants.EXIT_CODE_MARKER in cmd
        assert cmd.endswith('$?"')

    @patch("platform_test_uploader.get_platform_config")
    def test_path_is_shell_quoted(self, mock_get_config, mock_config):
        """Paths with special characters are quoted to prevent injection."""
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config, remote_path="/tmp/my program")

        cmd = uploader._build_test_command()
        # shlex.quote wraps in single quotes
        assert "'/tmp/my program'" in cmd

    @patch("platform_test_uploader.get_platform_config")
    def test_path_with_shell_metacharacters_is_quoted(
        self, mock_get_config, mock_config
    ):
        """Shell metacharacters in paths are neutralized by quoting."""
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config, remote_path="/tmp/prog;rm -rf /")

        cmd = uploader._build_test_command()
        # The semicolon must be inside quotes, not interpreted as command separator
        assert "'/tmp/prog;rm -rf /'" in cmd

    @patch("platform_test_uploader.get_platform_config")
    def test_simple_path_format(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config, remote_path="/tmp/prog")

        cmd = uploader._build_test_command()
        assert cmd.startswith("/tmp/prog;")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
