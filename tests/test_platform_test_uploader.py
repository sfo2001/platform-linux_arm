#!/usr/bin/env python3
"""
Unit tests for RemoteTestUploader in platform-test-uploader.py.

Tests cover __init__, parse_test_port, upload_test_binary, execute_test_binary, and run().
"""

import importlib.util
import os
import sys
import subprocess
from unittest.mock import MagicMock, Mock, patch, call
import pytest

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
    def test_init_sets_default_attributes(self, mock_get_config, mock_config, basic_env):
        mock_get_config.return_value = mock_config

        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        assert uploader.user is None
        assert uploader.host is None
        assert uploader.remote_path is None
        assert uploader.ssh_key is None
        assert uploader._config is mock_config

    @patch("platform_test_uploader.get_platform_config")
    def test_init_calls_get_platform_config(self, mock_get_config, mock_config, basic_env):
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

        with pytest.raises(Exception, match="test_port or upload_port is not configured"):
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
        with patch("platform_test_uploader.get_platform_config", return_value=mock_config):
            env = _make_env(test_port="pi@host:/tmp/prog")
            source_mock = Mock()
            source_mock.__str__ = lambda self: "/local/testbinary"
            uploader = RemoteTestUploader(
                target=Mock(), source=[source_mock], env=env
            )
        uploader.user = "pi"
        uploader.host = "host"
        uploader.remote_path = "/tmp/prog"
        uploader.ssh_port = 22
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
        assert mock_run.call_count == 2  # scp upload + chmod

    @patch("platform_test_uploader.get_platform_config")
    def test_upload_failure_raises_exception(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        failed = Mock()
        failed.returncode = 1
        failed.stderr = "Connection refused"

        with patch("subprocess.run", return_value=failed):
            with pytest.raises(Exception, match="Failed to upload test binary"):
                uploader.upload_test_binary()

    @patch("platform_test_uploader.get_platform_config")
    def test_upload_timeout_raises_exception(self, mock_get_config, mock_config):
        mock_get_config.return_value = mock_config
        uploader = self._make_uploader(mock_config)

        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="scp", timeout=120)):
            with pytest.raises(Exception, match="timeout"):
                uploader.upload_test_binary()


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
            with pytest.raises(Exception, match="SSH is not installed"):
                uploader.check_ssh_available()

    @patch("platform_test_uploader.get_platform_config")
    def test_raises_when_scp_missing(self, mock_get_config, mock_config, basic_env):
        mock_get_config.return_value = mock_config
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        def which_side_effect(cmd):
            return "/usr/bin/ssh" if cmd == "ssh" else None

        with patch("shutil.which", side_effect=which_side_effect):
            with pytest.raises(Exception, match="SCP is not installed"):
                uploader.check_ssh_available()

    @patch("platform_test_uploader.get_platform_config")
    def test_passes_when_both_available(self, mock_get_config, mock_config, basic_env):
        mock_get_config.return_value = mock_config
        uploader = RemoteTestUploader(target=Mock(), source=[Mock()], env=basic_env)

        with patch("shutil.which", return_value="/usr/bin/ssh"):
            uploader.check_ssh_available()  # must not raise


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
