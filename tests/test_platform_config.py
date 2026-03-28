#!/usr/bin/env python3
"""
Unit tests for platform configuration file support.

Tests the PlatformConfig class and configuration file loading functionality.
"""

import os
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import platform_config as _pc_module
from platform_config import PlatformConfig


class TestPlatformConfig(unittest.TestCase):
    """Test cases for PlatformConfig class."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(lambda: self._cleanup_temp_dir())
        # Reset the module-level singleton so tests don't share state
        _pc_module._global_config_instance = None

    def tearDown(self):
        """Reset singleton after each test."""
        _pc_module._global_config_instance = None

    def _cleanup_temp_dir(self):
        """Clean up temporary directory."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_empty_config(self):
        """Test with no configuration files."""
        config = PlatformConfig(project_dir=self.temp_dir)

        # Should return default values when no config exists
        self.assertEqual(config.get('upload_timeout', 300), 300)
        self.assertEqual(config.get('upload_user', 'pi'), 'pi')
        self.assertEqual(len(config.get_loaded_files()), 0)

    def test_project_config_loading(self):
        """Test loading project-local configuration."""
        # Create project-local config
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[defaults]
upload_timeout = 600
upload_user = admin
upload_ssh_port = 2222
""")

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should load values from project config
        self.assertEqual(config.get('upload_timeout', 300), 600)
        self.assertEqual(config.get('upload_user', 'pi'), 'admin')
        self.assertEqual(config.get('upload_ssh_port', '22'), '2222')
        self.assertEqual(len(config.get_loaded_files()), 1)

    def test_type_conversion_int(self):
        """Test integer type conversion."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[defaults]
upload_timeout = 600
test_timeout = 1200
""")

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should convert to int when default is int
        timeout = config.get('upload_timeout', 300)
        self.assertIsInstance(timeout, int)
        self.assertEqual(timeout, 600)

    def test_type_conversion_bool(self):
        """Test boolean type conversion."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[defaults]
upload_run_after = true
debug_enabled = false
test_flag = yes
""")

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should convert to bool when default is bool
        self.assertEqual(config.get('upload_run_after', False), True)
        self.assertEqual(config.get('debug_enabled', True), False)
        self.assertEqual(config.get('test_flag', False), True)

    def test_type_conversion_string(self):
        """Test string type preservation."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[defaults]
upload_user = testuser
upload_path = /opt/myapp
""")

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should preserve as string when default is string
        user = config.get('upload_user', 'pi')
        self.assertIsInstance(user, str)
        self.assertEqual(user, 'testuser')

    def test_invalid_config_file(self):
        """Test handling of invalid config file."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        # A key=value line without a section header reliably triggers
        # configparser.MissingSectionHeaderError on all Python versions
        self.assertTrue(config_path.parent.exists(), "temp dir should exist before writing")
        config_path.write_text("key = value_without_section\n")

        # Should not raise exception, just ignore invalid file
        config = PlatformConfig(project_dir=self.temp_dir)
        self.assertEqual(config.get('upload_timeout', 300), 300)

    def test_has_key(self):
        """Test has_key method."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[defaults]
upload_timeout = 600
""")

        config = PlatformConfig(project_dir=self.temp_dir)

        self.assertTrue(config.has_key('upload_timeout'))
        self.assertFalse(config.has_key('nonexistent_key'))

    def test_get_all(self):
        """Test get_all method."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[defaults]
upload_timeout = 600
upload_user = admin
""")

        config = PlatformConfig(project_dir=self.temp_dir)
        all_config = config.get_all()

        self.assertEqual(len(all_config), 2)
        self.assertIn('upload_timeout', all_config)
        self.assertIn('upload_user', all_config)

    def test_missing_defaults_section(self):
        """Test config file without [defaults] section."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[other_section]
upload_timeout = 600
""")

        config = PlatformConfig(project_dir=self.temp_dir)

        # Should not load values from other sections
        self.assertEqual(config.get('upload_timeout', 300), 300)
        self.assertEqual(len(config.get_loaded_files()), 0)

    def test_multiple_config_values(self):
        """Test loading multiple configuration values."""
        config_path = Path(self.temp_dir) / ".platform-linux_arm.ini"
        config_path.write_text("""[defaults]
upload_timeout = 600
upload_user = admin
upload_ssh_port = 2222
test_timeout = 1200
test_username = testuser
""")

        config = PlatformConfig(project_dir=self.temp_dir)

        self.assertEqual(config.get('upload_timeout', 300), 600)
        self.assertEqual(config.get('upload_user', 'pi'), 'admin')
        self.assertEqual(config.get('upload_ssh_port', '22'), '2222')
        self.assertEqual(config.get('test_timeout', 600), 1200)
        self.assertEqual(config.get('test_username', 'pi'), 'testuser')


class TestConfigIntegration(unittest.TestCase):
    """Integration tests for configuration system."""

    def test_backward_compatibility(self):
        """Test that missing config files don't break anything."""
        # Create a temporary directory with no config files
        with tempfile.TemporaryDirectory() as temp_dir:
            config = PlatformConfig(project_dir=temp_dir)

            # Should work fine with defaults
            self.assertEqual(config.get('upload_timeout', 300), 300)
            self.assertEqual(config.get('upload_user', 'pi'), 'pi')
            self.assertEqual(len(config.get_loaded_files()), 0)

    def test_config_file_example(self):
        """Test that the example config file is valid."""
        example_path = Path(__file__).parent.parent / ".platform-linux_arm.ini.example"

        # Example file should exist
        self.assertTrue(example_path.exists(),
            f"Example config file not found: {example_path}")

        # Should be readable and parseable (even though we won't load it as config)
        content = example_path.read_text()
        self.assertIn('[defaults]', content)
        self.assertIn('upload_timeout', content)
        self.assertIn('upload_user', content)


class TestPlatformConfigEnvVar(unittest.TestCase):
    """Test environment variable interaction for PlatformConfig."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(self._cleanup)
        _pc_module._global_config_instance = None

    def tearDown(self):
        _pc_module._global_config_instance = None

    def _cleanup(self):
        import shutil
        _env_key = 'PLATFORMIO_CORE_DIR'
        if _env_key in os.environ:
            del os.environ[_env_key]
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_global_config_path_respects_env_var(self):
        """PLATFORMIO_CORE_DIR controls the global config path."""
        os.environ['PLATFORMIO_CORE_DIR'] = self.temp_dir
        config = PlatformConfig(project_dir=self.temp_dir)
        global_path = config._get_global_config_path()
        self.assertEqual(str(global_path.parent), self.temp_dir)

    def test_project_config_overrides_global_config(self):
        """Project-local config takes priority over global config for the same key."""
        # Global config: upload_timeout = 100
        global_dir = tempfile.mkdtemp()
        self.addCleanup(lambda: __import__('shutil').rmtree(global_dir, ignore_errors=True))
        global_config = Path(global_dir) / ".platform-linux_arm.ini"
        global_config.write_text("[defaults]\nupload_timeout = 100\n")

        # Project config: upload_timeout = 999
        project_config = Path(self.temp_dir) / ".platform-linux_arm.ini"
        project_config.write_text("[defaults]\nupload_timeout = 999\n")

        os.environ['PLATFORMIO_CORE_DIR'] = global_dir
        config = PlatformConfig(project_dir=self.temp_dir)

        # Project-local value must win (int conversion because default is int)
        self.assertEqual(config.get('upload_timeout', 300), 999)


class TestSingletonIsolation(unittest.TestCase):
    """Verify that get_platform_config() singleton resets correctly between tests."""

    def setUp(self):
        _pc_module._global_config_instance = None

    def tearDown(self):
        _pc_module._global_config_instance = None

    def test_singleton_returns_same_instance(self):
        """get_platform_config() returns the same object on repeated calls."""
        from platform_config import get_platform_config
        first = get_platform_config()
        second = get_platform_config()
        self.assertIs(first, second)

    def test_singleton_resets_between_tests(self):
        """setUp resets the singleton so each test starts with a fresh instance."""
        self.assertIsNone(_pc_module._global_config_instance)


if __name__ == '__main__':
    unittest.main()
