#!/usr/bin/env python3
"""
Unit tests for platform configuration file support.

Tests the PlatformConfig class and configuration file loading functionality.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

import platform_config as _pc_module
from platform_config import PlatformConfig, parse_bool_option


class TestPlatformConfig:
    """Test cases for PlatformConfig class."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        """Set up test fixtures."""
        self.temp_dir = str(tmp_path)
        # Reset the module-level singleton so tests don't share state
        _pc_module._global_config_instance = None
        yield
        _pc_module._global_config_instance = None

    def test_empty_config(self):
        """Test with no configuration files."""
        config = PlatformConfig(project_dir=self.temp_dir)

        # Should return default values when no config exists
        assert config.get("upload_timeout", 300) == 300
        assert config.get("upload_user", "pi") == "pi"
        assert len(config.get_loaded_files()) == 0

    def test_project_config_loading(self):
        """Test loading project-local configuration."""
        # Create project-local config
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text(
            """[defaults]
upload_timeout = 600
upload_user = admin
upload_ssh_port = 2222
"""
        )

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should load values from project config
        assert config.get("upload_timeout", 300) == 600
        assert config.get("upload_user", "pi") == "admin"
        assert config.get("upload_ssh_port", "22") == "2222"
        assert len(config.get_loaded_files()) == 1

    def test_type_conversion_int(self):
        """Test integer type conversion."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text(
            """[defaults]
upload_timeout = 600
test_timeout = 1200
"""
        )

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should convert to int when default is int
        timeout = config.get("upload_timeout", 300)
        assert isinstance(timeout, int)
        assert timeout == 600

    def test_type_conversion_bool(self):
        """Test boolean type conversion."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text(
            """[defaults]
upload_run_after = true
debug_enabled = false
test_flag = yes
"""
        )

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should convert to bool when default is bool
        assert config.get("upload_run_after", False) is True
        assert config.get("debug_enabled", True) is False
        assert config.get("test_flag", False) is True

    def test_type_conversion_string(self):
        """Test string type preservation."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text(
            """[defaults]
upload_user = testuser
upload_path = /opt/myapp
"""
        )

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should preserve as string when default is string
        user = config.get("upload_user", "pi")
        assert isinstance(user, str)
        assert user == "testuser"

    def test_invalid_config_file(self):
        """Test handling of invalid config file."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        # A key=value line without a section header reliably triggers
        # configparser.MissingSectionHeaderError on all Python versions
        assert config_path.parent.exists(), "temp dir should exist before writing"
        config_path.write_text("key = value_without_section\n")

        # Should not raise exception, just ignore invalid file
        config = PlatformConfig(project_dir=self.temp_dir)
        assert config.get("upload_timeout", 300) == 300

    def test_get_all(self):
        """Test get_all method."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text(
            """[defaults]
upload_timeout = 600
upload_user = admin
"""
        )

        config = PlatformConfig(project_dir=self.temp_dir)
        all_config = config.get_all()

        assert len(all_config) == 2
        assert "upload_timeout" in all_config
        assert "upload_user" in all_config

    def test_missing_defaults_section(self):
        """Test config file without [defaults] section."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text(
            """[other_section]
upload_timeout = 600
"""
        )

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should not load values from other sections
        assert config.get("upload_timeout", 300) == 300
        assert len(config.get_loaded_files()) == 0

    def test_multiple_config_values(self):
        """Test loading multiple configuration values."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text(
            """[defaults]
upload_timeout = 600
upload_user = admin
upload_ssh_port = 2222
test_timeout = 1200
test_username = testuser
"""
        )

        config = PlatformConfig(project_dir=self.temp_dir)

        assert config.get("upload_timeout", 300) == 600
        assert config.get("upload_user", "pi") == "admin"
        assert config.get("upload_ssh_port", "22") == "2222"
        assert config.get("test_timeout", 600) == 1200
        assert config.get("test_username", "pi") == "testuser"


class TestConfigIntegration:
    """Integration tests for configuration system."""

    def test_backward_compatibility(self, tmp_path):
        """Test that missing config files don't break anything."""
        config = PlatformConfig(project_dir=str(tmp_path))

        # Should work fine with defaults
        assert config.get("upload_timeout", 300) == 300
        assert config.get("upload_user", "pi") == "pi"
        assert len(config.get_loaded_files()) == 0

    def test_config_file_example(self):
        """Test that the example config file is valid."""
        example_path = Path(__file__).parent.parent / ".platform-linux_arm.ini.example"

        if not example_path.exists():
            pytest.skip(f"Example config file not found: {example_path}")

        # Should be readable and parseable (even though we won't load it as config)
        content = example_path.read_text()
        assert "[defaults]" in content
        assert "upload_timeout" in content
        assert "upload_user" in content


class TestPlatformConfigEnvVar:
    """Test environment variable interaction for PlatformConfig."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        """Set up test fixtures."""
        self.temp_dir = str(tmp_path)
        _pc_module._global_config_instance = None
        yield
        _pc_module._global_config_instance = None
        _env_key = "PLATFORMIO_CORE_DIR"
        if _env_key in os.environ:
            del os.environ[_env_key]

    def test_global_config_path_respects_env_var(self):
        """PLATFORMIO_CORE_DIR controls the global config path."""
        os.environ["PLATFORMIO_CORE_DIR"] = self.temp_dir
        config = PlatformConfig(project_dir=self.temp_dir)
        global_path = config._get_global_config_path()
        assert str(global_path.parent) == self.temp_dir

    def test_project_config_overrides_global_config(self, tmp_path):
        """Project-local config takes priority over global config for the same key."""
        # Global config: upload_timeout = 100
        global_dir = tmp_path / "global"
        global_dir.mkdir()
        global_config = global_dir / ".platform-linux_arm.ini"
        global_config.write_text("[defaults]\nupload_timeout = 100\n")

        # Project config: upload_timeout = 999
        project_config = Path(self.temp_dir) / ".platform-linux_arm.ini"
        project_config.write_text("[defaults]\nupload_timeout = 999\n")

        os.environ["PLATFORMIO_CORE_DIR"] = str(global_dir)
        config = PlatformConfig(project_dir=self.temp_dir)

        # Project-local value must win (int conversion because default is int)
        assert config.get("upload_timeout", 300) == 999


class TestSingletonIsolation:
    """Verify that get_platform_config() singleton resets correctly between tests."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up test fixtures."""
        _pc_module._global_config_instance = None
        yield
        _pc_module._global_config_instance = None

    def test_singleton_returns_same_instance(self):
        """get_platform_config() returns the same object on repeated calls."""
        from platform_config import get_platform_config

        first = get_platform_config()
        second = get_platform_config()
        assert first is second

    def test_singleton_resets_between_tests(self):
        """setUp resets the singleton so each test starts with a fresh instance."""
        assert _pc_module._global_config_instance is None


class TestParseBoolOption:
    """Test the parse_bool_option standalone function."""

    @pytest.mark.parametrize(
        "value",
        ["true", "True", "TRUE", "yes", "Yes", "1", "on", "ON"],
    )
    def test_truthy_values(self, value):
        assert parse_bool_option(value) is True

    @pytest.mark.parametrize(
        "value",
        ["false", "False", "no", "0", "off", "", "random"],
    )
    def test_falsy_values(self, value):
        assert parse_bool_option(value) is False

    def test_python_bool_true(self):
        assert parse_bool_option(True) is True

    def test_python_bool_false(self):
        assert parse_bool_option(False) is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
