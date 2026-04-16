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

"""Unit tests for dev-loop feature (on_dev_loop, _run_dev_loop_monitor)."""

import datetime
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from unittest.mock import Mock, mock_open, patch

import pytest

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from platformio import exception  # noqa: E402

# Import platform.py module explicitly to avoid conflict with stdlib platform module
_platform_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "platform.py"
)
spec = importlib.util.spec_from_file_location("platform_module", _platform_path)
platform_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(platform_module)

sys.modules["platform_module"] = platform_module


@pytest.fixture
def mock_platform_manifest():
    """Create a mock platform manifest."""
    return "test_manifest"


@pytest.fixture
def make_platform(mock_platform_manifest):
    """Factory fixture that creates a Linux_armPlatform with mocks.

    Shadows conftest.make_platform to support per-test config_overrides via **kwargs.
    """

    def _make(**config_overrides):
        with patch("platform_module.PlatformBase.__init__", return_value=None), patch(
            "platform_module.get_platform_config", return_value=Mock()
        ), patch("platform_module.Linux_armPlatform._show_welcome_if_needed"):
            from platform_module import Linux_armPlatform

            platform = Linux_armPlatform(mock_platform_manifest)
            platform._config = config_overrides
            return platform

    return _make


def _make_env(options=None):
    """Create a mock env with GetProjectOption support."""
    defaults = {
        "upload_port": "pi@raspberrypi.local:/home/pi/app",
        "upload_protocol": "scp",
        "upload_ssh_port": 22,
        "upload_ssh_key": None,
        "upload_strict_host_check": False,
        "upload_run_command": None,
        "dev_loop_monitor_timeout": 30,
        "upload_run_after": False,
    }
    if options:
        defaults.update(options)

    env = Mock()
    env.GetProjectOption = Mock(side_effect=lambda key, default=None: defaults.get(key, default))
    env.subst = Mock(return_value=os.path.join(tempfile.gettempdir(), "build_dir"))
    env.get = Mock(return_value=None)
    return env


class TestOnDevLoopUploadRunAfter:
    """Test on_dev_loop behavior when upload_run_after=true."""

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_upload_run_after_true_prints_warning(
        self, mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test dev-loop prints warning when upload_run_after=true."""
        mock_upload.return_value = 0
        mock_monitor.return_value = ("output\n", 0, False)

        platform = make_platform()
        env = _make_env({"upload_run_after": True})
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        assert result == 0
        warning_found = any("upload_run_after" in str(call) for call in mock_print.call_args_list)
        assert warning_found, "Expected warning about upload_run_after double-execution"


class TestOnDevLoopSuccess:
    """Test on_dev_loop full success path."""

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_full_success_returns_zero(
        self, _mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test dev-loop returns 0 when all phases pass."""
        mock_upload.return_value = 0
        mock_monitor.return_value = ("Hello from ARM!\n", 0, False)

        platform = make_platform()
        env = _make_env()
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        assert result == 0
        mock_upload.assert_called_once()
        mock_monitor.assert_called_once()

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_json_output_contains_all_fields(
        self, mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test JSON output includes all required schema fields."""
        mock_upload.return_value = 0
        mock_monitor.return_value = ("test output\n", 0, False)

        platform = make_platform()
        env = _make_env()
        platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        # Find the JSON output in print calls
        json_str = None
        for call in mock_print.call_args_list:
            args = call[0]
            if args and isinstance(args[0], str) and '"schema_version"' in args[0]:
                json_str = args[0]
                break

        assert json_str is not None, "JSON output not found in print calls"
        result = json.loads(json_str)

        assert result["schema_version"] == "1"
        assert "timestamp_iso" in result
        assert "elapsed_seconds" in result
        assert result["phases"]["build"]["status"] == "pass"
        assert result["phases"]["upload"]["status"] == "pass"
        assert result["phases"]["upload"]["error"] is None
        assert result["phases"]["monitor"]["status"] == "pass"
        assert result["phases"]["monitor"]["exit_code"] == 0
        assert result["phases"]["monitor"]["timed_out"] is False
        assert result["phases"]["monitor"]["timeout_seconds"] == 30
        assert result["phases"]["monitor"]["output"] == "test output\n"
        assert result["overall_status"] == "pass"
        assert result["failure_phase"] is None


class TestOnDevLoopUploadFailure:
    """Test on_dev_loop when upload fails."""

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_upload_exception_returns_one(
        self, _mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test dev-loop returns 1 when upload raises PlatformioException."""
        mock_upload.side_effect = exception.PlatformioException("SSH connection failed")

        platform = make_platform()
        env = _make_env()
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        assert result == 1
        mock_monitor.assert_not_called()

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_upload_failure_json_has_failure_phase(
        self, mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test JSON output has failure_phase='upload' when upload fails."""
        mock_upload.side_effect = exception.PlatformioException("Connection refused")

        platform = make_platform()
        env = _make_env()
        platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        # Find JSON in print calls
        json_str = None
        for call in mock_print.call_args_list:
            args = call[0]
            if args and isinstance(args[0], str) and '"schema_version"' in args[0]:
                json_str = args[0]
                break

        assert json_str is not None
        result = json.loads(json_str)

        assert result["overall_status"] == "fail"
        assert result["failure_phase"] == "upload"
        assert result["phases"]["upload"]["status"] == "fail"
        assert "Connection refused" in result["phases"]["upload"]["error"]
        assert "monitor" not in result["phases"]

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_upload_nonzero_rc_returns_one(
        self, _mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test dev-loop returns 1 when upload returns non-zero exit code."""
        mock_upload.return_value = 1

        platform = make_platform()
        env = _make_env()
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        assert result == 1
        mock_monitor.assert_not_called()

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_upload_oserror_returns_one(
        self, _mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test dev-loop returns 1 when upload raises OSError."""
        mock_upload.side_effect = OSError("No such file or directory")

        platform = make_platform()
        env = _make_env()
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        assert result == 1
        mock_monitor.assert_not_called()

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_upload_timeout_expired_returns_one(
        self, _mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test dev-loop returns 1 when upload raises subprocess.TimeoutExpired."""
        mock_upload.side_effect = subprocess.TimeoutExpired(cmd="scp", timeout=60)

        platform = make_platform()
        env = _make_env()
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        assert result == 1
        mock_monitor.assert_not_called()


class TestOnDevLoopMonitorTimeout:
    """Test on_dev_loop when monitor times out."""

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_monitor_timeout_json_has_timed_out(
        self, mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test JSON has timed_out=true when monitor exceeds timeout."""
        mock_upload.return_value = 0
        mock_monitor.return_value = ("partial output\n", -1, True)

        platform = make_platform()
        env = _make_env()
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        # Timeout is not a failure — overall status is pass
        assert result == 0

        json_str = None
        for call in mock_print.call_args_list:
            args = call[0]
            if args and isinstance(args[0], str) and '"schema_version"' in args[0]:
                json_str = args[0]
                break

        parsed = json.loads(json_str)
        assert parsed["phases"]["monitor"]["timed_out"] is True
        assert parsed["phases"]["monitor"]["status"] == "timeout"
        assert parsed["overall_status"] == "pass"


class TestOnDevLoopMonitorNonZeroExit:
    """Test on_dev_loop when remote program returns non-zero exit code."""

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_monitor_nonzero_exit_returns_one(
        self, mock_print, mock_upload, mock_monitor, _mock_makedirs, make_platform
    ):
        """Test dev-loop returns 1 when remote program exits with non-zero code."""
        mock_upload.return_value = 0
        mock_monitor.return_value = ("error output\n", 1, False)

        platform = make_platform()
        env = _make_env()
        result = platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        assert result == 1

        json_str = None
        for call in mock_print.call_args_list:
            args = call[0]
            if args and isinstance(args[0], str) and '"schema_version"' in args[0]:
                json_str = args[0]
                break

        parsed = json.loads(json_str)
        assert parsed["phases"]["monitor"]["exit_code"] == 1
        assert parsed["phases"]["monitor"]["status"] == "fail"
        assert parsed["overall_status"] == "fail"
        assert parsed["failure_phase"] == "monitor"


class TestOnDevLoopMonitorTimeoutConfig:
    """Test on_dev_loop validation of dev_loop_monitor_timeout config value."""

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_zero_timeout_raises(
        self, _mock_print, mock_upload, _mock_monitor, _mock_makedirs, make_platform
    ):
        """Test on_dev_loop raises PlatformioException when timeout is 0."""
        mock_upload.return_value = 0

        platform = make_platform()
        env = _make_env({"dev_loop_monitor_timeout": 0})

        with pytest.raises(exception.PlatformioException, match="must be a positive integer"):
            platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_negative_timeout_raises(
        self, _mock_print, mock_upload, _mock_monitor, _mock_makedirs, make_platform
    ):
        """Test on_dev_loop raises PlatformioException when timeout is negative."""
        mock_upload.return_value = 0

        platform = make_platform()
        env = _make_env({"dev_loop_monitor_timeout": -1})

        with pytest.raises(exception.PlatformioException, match="must be a positive integer"):
            platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

    @patch("builtins.open", mock_open())
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_non_integer_timeout_raises(
        self, _mock_print, mock_upload, _mock_monitor, _mock_makedirs, make_platform
    ):
        """Test on_dev_loop raises PlatformioException when timeout is not an integer."""
        mock_upload.return_value = 0

        platform = make_platform()
        env = _make_env({"dev_loop_monitor_timeout": "abc"})

        with pytest.raises(exception.PlatformioException, match="must be an integer"):
            platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)


class TestRunDevLoopMonitor:
    """Test _run_dev_loop_monitor method."""

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_successful_execution(self, _mock_print, mock_popen, make_platform):
        """Test monitor captures output and returns exit code 0."""
        mock_process = Mock()
        mock_process.communicate.return_value = (b"Hello from ARM!\n", None)
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env()
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, exit_code, timed_out = platform._run_dev_loop_monitor(
            env, [source_path], timeout=30
        )

        assert output == "Hello from ARM!\n"
        assert exit_code == 0
        assert timed_out is False

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_timeout_kills_process(self, _mock_print, mock_popen, make_platform):
        """Test monitor kills process and sets timed_out on TimeoutExpired."""
        mock_process = Mock()
        mock_process.communicate.side_effect = [
            subprocess.TimeoutExpired(cmd="ssh", timeout=30),
            (b"partial\n", None),
        ]
        mock_process.returncode = None
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env()
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, exit_code, timed_out = platform._run_dev_loop_monitor(
            env, [source_path], timeout=30
        )

        assert timed_out is True
        assert exit_code == -1
        assert output == "partial\n"
        mock_process.kill.assert_called_once()

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_timeout_kills_process_inner_timeout(self, _mock_print, mock_popen, make_platform):
        """Test monitor handles case where post-kill communicate also times out."""
        mock_process = Mock()
        mock_process.communicate.side_effect = [
            subprocess.TimeoutExpired(cmd="ssh", timeout=30),
            subprocess.TimeoutExpired(cmd="ssh", timeout=10),
        ]
        mock_process.returncode = None
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env()
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, exit_code, timed_out = platform._run_dev_loop_monitor(
            env, [source_path], timeout=30
        )

        assert timed_out is True
        assert output == ""
        assert exit_code == -1
        mock_process.kill.assert_called_once()

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_output_sanitization(self, _mock_print, mock_popen, make_platform):
        """Test non-printable characters are stripped from output."""
        mock_process = Mock()
        # Include control characters that should be stripped
        mock_process.communicate.return_value = (
            b"clean\x00text\x01with\x02control\x07chars\n",
            None,
        )
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env()
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, _, _ = platform._run_dev_loop_monitor(env, [source_path], timeout=30)

        assert "\x00" not in output
        assert "\x01" not in output
        assert "\x07" not in output
        assert "cleantextwithcontrolchars\n" == output

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_output_truncation(self, _mock_print, mock_popen, make_platform):
        """Test output exceeding MAX_OUTPUT_BYTES is truncated."""
        from platform_constants import DevLoopConstants

        large_output = b"x" * (DevLoopConstants.MAX_OUTPUT_BYTES + 1000)
        mock_process = Mock()
        mock_process.communicate.return_value = (large_output, None)
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env()
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, _, _ = platform._run_dev_loop_monitor(env, [source_path], timeout=30)

        assert len(output) <= DevLoopConstants.MAX_OUTPUT_BYTES + len("\n[truncated]")
        assert output.endswith("\n[truncated]")

    def test_no_upload_port_raises(self, make_platform):
        """Test monitor raises PlatformioException when upload_port is not configured."""
        platform = make_platform()
        env = _make_env({"upload_port": None})

        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        with pytest.raises(exception.PlatformioException, match="upload_port"):
            platform._run_dev_loop_monitor(env, [source_path], timeout=30)

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_custom_run_command(self, _mock_print, mock_popen, make_platform):
        """Test upload_run_command is passed unquoted for remote execution."""
        mock_process = Mock()
        mock_process.communicate.return_value = (b"custom output\n", None)
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env({"upload_run_command": "/usr/local/bin/myapp --flag"})
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, exit_code, timed_out = platform._run_dev_loop_monitor(
            env, [source_path], timeout=30
        )

        assert exit_code == 0
        assert output == "custom output\n"
        mock_popen.assert_called_once()
        # Verify run command appears unquoted in SSH args (trusted user input)
        cmd = mock_popen.call_args[0][0]
        assert "/usr/local/bin/myapp --flag" in " ".join(cmd)

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_remote_path_with_trailing_slash(self, _mock_print, mock_popen, make_platform):
        """Test program name is appended when remote path ends with /."""
        mock_process = Mock()
        mock_process.communicate.return_value = (b"ok\n", None)
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env({"upload_port": "pi@host:/home/pi/apps/"})
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, exit_code, timed_out = platform._run_dev_loop_monitor(
            env, [source_path], timeout=30
        )

        assert exit_code == 0
        mock_popen.assert_called_once()
        # Verify program name was appended to remote path
        cmd = mock_popen.call_args[0][0]
        assert "/home/pi/apps/program" in " ".join(cmd)

    @patch("platform_module.subprocess.Popen")
    @patch("builtins.print")
    def test_remote_path_without_trailing_slash(self, _mock_print, mock_popen, make_platform):
        """Test remote path used directly when no trailing slash."""
        mock_process = Mock()
        mock_process.communicate.return_value = (b"ok\n", None)
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        platform = make_platform()
        env = _make_env({"upload_port": "pi@host:/home/pi/myapp"})
        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        output, exit_code, timed_out = platform._run_dev_loop_monitor(
            env, [source_path], timeout=30
        )

        assert exit_code == 0
        mock_popen.assert_called_once()
        # Verify remote path used as-is (no program name appended)
        cmd = mock_popen.call_args[0][0]
        assert "/home/pi/myapp" in " ".join(cmd)

    def test_ssh_config_error_returns_error(self, make_platform):
        """Test monitor returns error when SSHConnectionConfig raises ValueError."""
        platform = make_platform()
        env = _make_env({"upload_port": "pi@host:/path"})

        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        with patch(
            "ssh_utils.SSHConnectionConfig",
            side_effect=ValueError("Invalid SSH key path"),
        ):
            output, exit_code, timed_out = platform._run_dev_loop_monitor(
                env, [source_path], timeout=30
            )

        assert exit_code == 1
        assert "SSH config error" in output
        assert "Invalid SSH key path" in output

    def test_ssh_config_file_not_found_returns_error(self, make_platform):
        """Test monitor returns error when SSHConnectionConfig raises FileNotFoundError."""
        platform = make_platform()
        env = _make_env({"upload_port": "pi@host:/path"})

        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        with patch(
            "ssh_utils.SSHConnectionConfig",
            side_effect=FileNotFoundError("Key file not found"),
        ):
            output, exit_code, timed_out = platform._run_dev_loop_monitor(
                env, [source_path], timeout=30
            )

        assert exit_code == 1
        assert "SSH config error" in output


class TestIsoTimestamp:
    """Test _iso_timestamp static method."""

    def test_returns_valid_iso8601(self, make_platform):
        """Test _iso_timestamp returns a valid ISO 8601 string with timezone."""
        platform = make_platform()
        ts = platform._iso_timestamp()
        parsed = datetime.datetime.fromisoformat(ts)
        assert parsed.tzinfo is not None

    def test_returns_recent_timestamp(self, make_platform):
        """Test _iso_timestamp returns the current time."""
        platform = make_platform()
        fixed_now = datetime.datetime(2024, 1, 15, 12, 0, 0, tzinfo=datetime.timezone.utc)
        with patch("platform_module.datetime") as mock_dt:
            mock_dt.datetime.now.return_value = fixed_now
            mock_dt.timezone.utc = datetime.timezone.utc
            ts = platform._iso_timestamp()
        assert ts == fixed_now.astimezone().isoformat()


class TestEmitDevLoopResultFailure:
    """Test _emit_dev_loop_result error handling."""

    @patch("os.makedirs", side_effect=OSError("Permission denied"))
    @patch("builtins.print")
    def test_file_write_oserror_prints_warning(self, mock_print, mock_makedirs, make_platform):
        """Test _emit_dev_loop_result prints warning on OSError without raising."""
        platform = make_platform()
        env = _make_env()
        result = {"schema_version": "1", "overall_status": "pass"}

        # Should not raise
        platform._emit_dev_loop_result(result, env)

        # Verify warning was printed
        warning_found = False
        for call in mock_print.call_args_list:
            args = call[0]
            if args and isinstance(args[0], str) and "Warning:" in args[0]:
                warning_found = True
                break
        assert warning_found, "Expected warning message about file write failure"


class TestDevLoopHandlerFallback:
    """Test _dev_loop_handler fallback when platform lacks on_dev_loop.

    builder/main.py is a SCons script (uses DefaultEnvironment(), Import())
    and cannot be directly imported. We extract _dev_loop_handler via AST +
    compile so the test exercises the real function, not a reimplementation.
    """

    @staticmethod
    def _load_handler():
        """Extract _dev_loop_handler from builder/main.py source."""
        import ast

        builder_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "builder",
            "main.py",
        )
        with open(builder_path) as f:
            source = f.read()

        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "_dev_loop_handler":
                func_source = ast.get_source_segment(source, node)
                assert func_source is not None, (
                    "_dev_loop_handler source could not be extracted from builder/main.py. "
                    "The function may have been renamed or relocated."
                )
                code = compile(func_source, builder_path, "exec")
                namespace: dict = {}
                # Safe: source is version-controlled own-codebase, no user input
                exec(code, namespace)  # nosec B102
                return namespace["_dev_loop_handler"]
        raise RuntimeError("_dev_loop_handler not found in builder/main.py")

    @patch("builtins.print")
    def test_no_on_dev_loop_returns_one(self, mock_print):
        """Test handler returns 1 when platform has no on_dev_loop method."""
        handler = self._load_handler()

        mock_env = Mock()
        mock_platform = Mock(spec=[])  # Empty spec = no attributes
        mock_env.PioPlatform.return_value = mock_platform

        result = handler(Mock(), [Mock()], mock_env)
        assert result == 1

    @patch("builtins.print")
    def test_has_on_dev_loop_dispatches_and_returns_value(self, mock_print):
        """Test handler dispatches to on_dev_loop and returns its return value."""
        handler = self._load_handler()

        mock_env = Mock()
        mock_platform = Mock()  # Has on_dev_loop by default (Mock has all attrs)
        mock_platform.on_dev_loop.return_value = 42
        mock_env.PioPlatform.return_value = mock_platform

        target = Mock()
        source = [Mock()]
        result = handler(target, source, mock_env)

        mock_platform.on_dev_loop.assert_called_once_with(target, source, mock_env)
        assert result == 42


class TestDevLoopResultFile:
    """Test result file writing."""

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("platform_module.Linux_armPlatform._run_dev_loop_monitor")
    @patch("platform_module.Linux_armPlatform.on_upload")
    @patch("builtins.print")
    def test_result_file_written(
        self,
        mock_print,
        mock_upload,
        mock_monitor,
        mock_makedirs,
        mock_file,
        make_platform,
    ):
        """Test result JSON is written to BUILD_DIR/dev-loop-result.json."""
        mock_upload.return_value = 0
        mock_monitor.return_value = ("output\n", 0, False)

        platform = make_platform()
        env = _make_env()
        platform.on_dev_loop(target=Mock(), source=[Mock()], env=env)

        build_dir = os.path.join(tempfile.gettempdir(), "build_dir")
        mock_makedirs.assert_called_once_with(build_dir, exist_ok=True)
        from platform_constants import DevLoopConstants

        mock_file.assert_called_with(
            os.path.join(build_dir, DevLoopConstants.RESULT_FILENAME), "w", encoding="utf-8"
        )


class TestBuildSshExecuteCmd:
    """Test _build_ssh_execute_cmd static method directly."""

    def _make_config(self):
        config = Mock()
        config.host = "raspberrypi.local"
        config.user = "pi"
        config.port = 22
        config.key_file = None
        config.strict_host_check = False
        return config

    @patch("ssh_utils.SSHCommandBuilder")
    def test_trailing_slash_appends_program_name(self, mock_builder_cls):
        """Test program name is appended to remote path when it ends with /."""
        from platform_module import Linux_armPlatform

        mock_builder = Mock()
        mock_builder.build_ssh_command.return_value = [
            "ssh",
            "pi@host",
            "/home/pi/apps/program",
        ]
        mock_builder_cls.return_value = mock_builder

        config = self._make_config()
        env = Mock()
        env.GetProjectOption.return_value = None

        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        cmd, display_path = Linux_armPlatform._build_ssh_execute_cmd(
            config, env, "/home/pi/apps/", [source_path]
        )

        call_args = mock_builder.build_ssh_command.call_args[0][0]
        assert "program" in call_args
        assert display_path == "/home/pi/apps/program"

    @patch("ssh_utils.SSHCommandBuilder")
    def test_no_trailing_slash_uses_path_directly(self, mock_builder_cls):
        """Test remote path is used as-is when it does not end with /."""
        from platform_module import Linux_armPlatform

        mock_builder = Mock()
        mock_builder.build_ssh_command.return_value = [
            "ssh",
            "pi@host",
            "/home/pi/myapp",
        ]
        mock_builder_cls.return_value = mock_builder

        config = self._make_config()
        env = Mock()
        env.GetProjectOption.return_value = None

        source_path = os.path.join(tempfile.gettempdir(), "build", "program")
        cmd, display_path = Linux_armPlatform._build_ssh_execute_cmd(
            config, env, "/home/pi/myapp", [source_path]
        )

        call_args = mock_builder.build_ssh_command.call_args[0][0]
        assert "myapp" in call_args
        assert display_path == "/home/pi/myapp"

    @patch("ssh_utils.SSHCommandBuilder")
    def test_custom_run_command_passed_unquoted(self, mock_builder_cls):
        """Test upload_run_command is passed through without shell-quoting."""
        from platform_module import Linux_armPlatform

        mock_builder = Mock()
        mock_builder.build_ssh_command.return_value = [
            "ssh",
            "pi@host",
            "/usr/bin/myapp --flag",
        ]
        mock_builder_cls.return_value = mock_builder

        config = self._make_config()
        env = Mock()
        env.GetProjectOption.return_value = "/usr/bin/myapp --flag"

        cmd, display_path = Linux_armPlatform._build_ssh_execute_cmd(config, env, "/home/pi/", None)

        call_args = mock_builder.build_ssh_command.call_args[0][0]
        assert call_args == "/usr/bin/myapp --flag"
        assert display_path == "/usr/bin/myapp --flag"


class TestScrubErrorMessage:
    """Test _scrub_error_message static method directly."""

    def test_redacts_unix_absolute_path(self):
        """Test Unix absolute paths are redacted."""
        from platform_module import Linux_armPlatform

        result = Linux_armPlatform._scrub_error_message(
            "Permission denied (publickey): /home/user/.ssh/id_rsa"
        )
        assert "/home/user/.ssh/id_rsa" not in result
        assert "[redacted]" in result

    def test_redacts_user_at_host(self):
        """Test user@host patterns are redacted."""
        from platform_module import Linux_armPlatform

        result = Linux_armPlatform._scrub_error_message(
            "Connection refused by pi@raspberrypi.local"
        )
        assert "pi@raspberrypi.local" not in result
        assert "[redacted]" in result

    def test_redacts_windows_path(self):
        """Test Windows-style absolute paths are redacted."""
        from platform_module import Linux_armPlatform

        result = Linux_armPlatform._scrub_error_message(
            r"Key not found: C:\Users\testuser\.ssh\id_rsa"
        )
        assert r"C:\Users\testuser\.ssh\id_rsa" not in result
        assert "[redacted]" in result

    def test_preserves_plain_error_text(self):
        """Test messages without paths or hostnames are unchanged."""
        from platform_module import Linux_armPlatform

        msg = "Connection refused"
        result = Linux_armPlatform._scrub_error_message(msg)
        assert result == msg

    def test_redacts_multiple_paths(self):
        """Test multiple paths in a single message are all redacted."""
        from platform_module import Linux_armPlatform

        result = Linux_armPlatform._scrub_error_message(
            "Could not read /etc/ssh/sshd_config or /root/.ssh/authorized_keys"
        )
        assert "/etc/ssh/sshd_config" not in result
        assert "/root/.ssh/authorized_keys" not in result

    def test_redacts_relative_ssh_path(self):
        """Test relative paths containing .ssh are redacted."""
        from platform_module import Linux_armPlatform

        result = Linux_armPlatform._scrub_error_message("Could not open key file: keys/deploy_key")
        assert "keys/deploy_key" not in result
        assert "[redacted]" in result

    def test_redacts_unc_path(self):
        """Test Windows UNC paths are redacted."""
        from platform_module import Linux_armPlatform

        result = Linux_armPlatform._scrub_error_message(
            r"Key not found at \\server\share\keys\id_rsa"
        )
        assert r"\\server\share\keys\id_rsa" not in result
        assert "[redacted]" in result
