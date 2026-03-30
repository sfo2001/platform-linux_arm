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

"""Unit tests for builder/utils.py module."""

import importlib.util
import os
import sys
from unittest.mock import Mock

import pytest

# Import builder/utils.py via spec to avoid path conflicts
_utils_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "builder",
    "utils.py",
)
spec = importlib.util.spec_from_file_location("builder_utils", _utils_path)
builder_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder_utils)


class TestGetTargetArch:
    """Test get_target_arch architecture detection."""

    def test_returns_board_arch_default(self):
        """Returns arch from board config when no user override."""
        env = Mock()
        board = Mock()
        board.get.return_value = "aarch64"
        env.BoardConfig.return_value = board
        env.GetProjectOption.return_value = None

        result = builder_utils.get_target_arch(env)

        assert result == "aarch64"

    def test_user_override_takes_precedence(self):
        """board_build.arch in platformio.ini overrides board default."""
        env = Mock()
        board = Mock()
        board.get.return_value = "armv7"
        env.BoardConfig.return_value = board
        env.GetProjectOption.side_effect = lambda key, default=None: (
            "aarch64" if key == "board_build.arch" else default
        )

        result = builder_utils.get_target_arch(env)

        assert result == "aarch64"

    def test_falls_back_to_armv7(self):
        """Falls back to armv7 when board has no arch defined."""
        env = Mock()
        board = Mock()
        board.get.side_effect = lambda key, default=None: default
        env.BoardConfig.return_value = board
        env.GetProjectOption.return_value = None

        result = builder_utils.get_target_arch(env)

        assert result == "armv7"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
