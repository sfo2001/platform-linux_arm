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

"""Unit tests for builder/frameworks/arduino_bridge.py — path-search helpers."""

import importlib.util
import os
import types
from unittest.mock import patch

import pytest

# Import only the helper functions — avoids executing SCons DefaultEnvironment()
# by patching the SCons import before loading the module.
_FRAMEWORK_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "builder",
    "frameworks",
    "arduino_bridge.py",
)


def _load_helpers():
    """Load _find_mraa and _find_msgpack without triggering SCons execution."""

    class _FakeEnv:
        def Exit(self, code):
            raise SystemExit(code)

    scons_stub = types.ModuleType("SCons")
    scons_script_stub = types.ModuleType("SCons.Script")
    scons_script_stub.DefaultEnvironment = _FakeEnv
    scons_stub.Script = scons_script_stub

    utils_stub = types.ModuleType("utils")
    utils_stub.get_target_arch = lambda env: "aarch64"

    with patch.dict(
        "sys.modules",
        {
            "SCons": scons_stub,
            "SCons.Script": scons_script_stub,
            "utils": utils_stub,
        },
    ):
        spec = importlib.util.spec_from_file_location("arduino_bridge", _FRAMEWORK_PATH)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except SystemExit:
            pass  # env.Exit(1) expected when MRAA/msgpack not found in test env
        if not hasattr(mod, "_find_mraa") or not hasattr(mod, "_find_msgpack"):
            raise ImportError(
                "Module loaded but _find_mraa/_find_msgpack not defined. "
                "The module may have exited before defining helpers."
            )
        return mod


def _load_module_with_arch(arch):
    """Reload the module with a specific target architecture, capturing SystemExit."""

    class _FakeEnv:
        def Exit(self, code):
            raise SystemExit(code)

    scons_stub = types.ModuleType("SCons")
    scons_script_stub = types.ModuleType("SCons.Script")
    scons_script_stub.DefaultEnvironment = _FakeEnv
    scons_stub.Script = scons_script_stub

    utils_stub = types.ModuleType("utils")
    utils_stub.get_target_arch = lambda env: arch

    with patch.dict(
        "sys.modules",
        {
            "SCons": scons_stub,
            "SCons.Script": scons_script_stub,
            "utils": utils_stub,
        },
    ):
        spec = importlib.util.spec_from_file_location(
            "arduino_bridge_arch_test", _FRAMEWORK_PATH
        )
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            return mod, None
        except SystemExit as e:
            return None, e


@pytest.fixture(scope="module")
def bridge_helpers():
    """Load the arduino_bridge module and expose _find_mraa and _find_msgpack.

    Returns a 3-tuple (mod, _find_mraa, _find_msgpack) so that callers which
    need to patch attributes on the module object (e.g. ``patch.object(mod,
    "isfile", ...)``) can do so without a separate module-level reference.

    Using a fixture ensures that a load failure surfaces as a test error
    rather than a collection-time crash that masks all test results.
    """
    mod = _load_helpers()
    return mod, mod._find_mraa, mod._find_msgpack


class TestFindMraa:
    """Test _find_mraa path discovery."""

    def test_finds_mraa_at_user_local_path(self, bridge_helpers, tmp_path):
        """Finds MRAA installed to ~/.local/aarch64-linux-gnu by setup-mraa-cross.sh."""
        _, find_mraa, _ = bridge_helpers
        base = tmp_path / ".local" / "aarch64-linux-gnu"
        (base / "include" / "mraa").mkdir(parents=True)
        (base / "include" / "mraa" / "mraa.hpp").write_text("")
        (base / "lib").mkdir(parents=True)
        (base / "lib" / "libmraa.so").write_text("")

        inc, lib = find_mraa(str(tmp_path))

        assert inc == str(base / "include")
        assert lib == str(base / "lib")

    def test_prefers_multiarch_lib_path(self, bridge_helpers, tmp_path):
        """Prefers lib/aarch64-linux-gnu over lib/ when both exist."""
        _, find_mraa, _ = bridge_helpers
        base = tmp_path / ".local" / "aarch64-linux-gnu"
        (base / "include" / "mraa").mkdir(parents=True)
        (base / "include" / "mraa" / "mraa.hpp").write_text("")
        (base / "lib").mkdir(parents=True)
        (base / "lib" / "libmraa.so").write_text("")
        (base / "lib" / "aarch64-linux-gnu").mkdir(parents=True)
        (base / "lib" / "aarch64-linux-gnu" / "libmraa.so").write_text("")

        inc, lib = find_mraa(str(tmp_path))

        assert lib == str(base / "lib" / "aarch64-linux-gnu")

    def test_accepts_mraa_hpp_at_include_root(self, bridge_helpers, tmp_path):
        """Accepts mraa.hpp directly under include/ (not in include/mraa/)."""
        _, find_mraa, _ = bridge_helpers
        base = tmp_path / ".local" / "aarch64-linux-gnu"
        (base / "include").mkdir(parents=True)
        (base / "include" / "mraa.hpp").write_text("")
        (base / "lib").mkdir(parents=True)
        (base / "lib" / "libmraa.so.2").write_text("")

        inc, lib = find_mraa(str(tmp_path))

        assert inc == str(base / "include")
        assert lib == str(base / "lib")

    def test_returns_none_when_not_found(self, bridge_helpers, tmp_path):
        """Returns (None, None) when MRAA is not present in any search path."""
        _, find_mraa, _ = bridge_helpers
        inc, lib = find_mraa(str(tmp_path))
        assert inc is None
        assert lib is None

    def test_returns_none_when_header_found_but_lib_missing(
        self, bridge_helpers, tmp_path
    ):
        """Returns (None, None) when header exists but no libmraa.so[.2] found."""
        _, find_mraa, _ = bridge_helpers
        base = tmp_path / ".local" / "aarch64-linux-gnu"
        (base / "include" / "mraa").mkdir(parents=True)
        (base / "include" / "mraa" / "mraa.hpp").write_text("")
        # No lib directory created

        inc, lib = find_mraa(str(tmp_path))
        assert inc is None
        assert lib is None


class TestFindMsgpack:
    """Test _find_msgpack path discovery."""

    def test_finds_msgpack_at_user_local(self, bridge_helpers, tmp_path):
        """Finds msgpack.hpp in ~/.local/aarch64-linux-gnu/include."""
        _, _, find_msgpack = bridge_helpers
        inc_dir = tmp_path / ".local" / "aarch64-linux-gnu" / "include"
        inc_dir.mkdir(parents=True)
        (inc_dir / "msgpack.hpp").write_text("")

        result = find_msgpack(str(tmp_path))

        assert result == str(inc_dir)

    def test_finds_msgpack_at_usr_include(self, bridge_helpers, tmp_path):
        """Finds msgpack.hpp at /usr/include — explicit False-by-default mock."""
        mod, _, find_msgpack = bridge_helpers
        found = {os.path.join("/usr/include", "msgpack.hpp")}
        with patch.object(mod, "isfile", side_effect=lambda p: p in found):
            result = find_msgpack("/nonexistent-home")
        assert result == "/usr/include"

    def test_finds_msgpack_homebrew_apple_silicon(self, bridge_helpers, tmp_path):
        """Finds msgpack.hpp at /opt/homebrew/include (macOS Apple Silicon)."""
        mod, _, find_msgpack = bridge_helpers
        found = {os.path.join("/opt/homebrew/include", "msgpack.hpp")}
        with patch.object(mod, "isfile", side_effect=lambda p: p in found):
            result = find_msgpack("/nonexistent-home")
        assert result == "/opt/homebrew/include"

    def test_returns_none_when_not_found(self, bridge_helpers, tmp_path):
        """Returns None when msgpack.hpp is not present in any search path."""
        mod, _, find_msgpack = bridge_helpers
        with patch.object(mod, "isfile", return_value=False):
            result = find_msgpack(str(tmp_path))
        assert result is None


class TestModuleGuards:
    """Test module-level guards in arduino_bridge.py."""

    def test_arch_guard_exits_for_non_aarch64(self, capsys):
        """Module-level arch guard exits with code 1 for armv7 targets."""
        _, exc = _load_module_with_arch("armv7")
        assert exc is not None, "Expected SystemExit for non-aarch64 target"
        assert exc.code == 1
        captured = capsys.readouterr()
        assert "aarch64" in captured.err.lower()

    def test_arch_guard_exits_for_x86(self, capsys):
        """Module-level arch guard exits with code 1 for x86_64 targets."""
        _, exc = _load_module_with_arch("x86_64")
        assert exc is not None, "Expected SystemExit for x86_64 target"
        assert exc.code == 1
        captured = capsys.readouterr()
        assert "aarch64" in captured.err.lower()

    def test_mraa_not_found_exits(self, capsys):
        """Module-level MRAA guard exits with code 1 when MRAA not found.

        Patches os.path.isfile to return False so the test is deterministic
        regardless of whether MRAA is installed on the host machine.
        """
        with patch("os.path.isfile", return_value=False):
            _, exc = _load_module_with_arch("aarch64")
        assert exc is not None, "Expected SystemExit when MRAA not found"
        assert exc.code == 1
        captured = capsys.readouterr()
        assert "mraa" in captured.err.lower()
