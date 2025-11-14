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

"""
Platform Constants

Centralized constants for Linux ARM platform to maintain single source of truth
and improve code maintainability.
"""


class SSHDefaults:
    """Default values for SSH connections and operations."""

    # Default SSH port
    PORT = "22"

    # Default SSH username for Raspberry Pi and similar SBCs
    USER = "pi"

    # Default upload destination path on remote target
    UPLOAD_PATH = "/tmp/program"

    # Default test binary path on remote target
    TEST_PATH = "/tmp/test_program"


class UploadProtocol:
    """Supported upload protocols for deploying binaries to remote targets."""

    # Secure Copy Protocol - simple file transfer
    SCP = "scp"

    # Rsync - efficient incremental file transfer
    RSYNC = "rsync"

    # SSH with piped input - transfer via SSH with cat
    SSH = "ssh"

    # Manual - display instructions to user
    MANUAL = "manual"

    # List of all valid protocols
    ALL = [SCP, RSYNC, SSH, MANUAL]


class TestTransport:
    """Supported transport methods for test execution."""

    # Execute tests via SSH
    SSH = "ssh"

    # Manual test execution (display instructions)
    MANUAL = "manual"

    # List of all valid transports
    ALL = [SSH, MANUAL]


class Timeouts:
    """Timeout values in seconds for various operations."""

    # Upload operation timeout (SCP, rsync, SSH)
    UPLOAD = 300

    # Remote command execution timeout after upload
    UPLOAD_RUN = 300

    # Test binary upload timeout
    TEST_UPLOAD = 300

    # Test execution timeout
    TEST_EXECUTION = 600

    # Chmod operation timeout
    CHMOD = 30


class TestConstants:
    """Constants for test execution and output parsing."""

    # Marker string for extracting exit code from test output
    EXIT_CODE_MARKER = "__EXIT_CODE__:"


class DebugTools:
    """Debug tool identifiers and configurations."""

    # GDB server over SSH tunnel
    GDBSERVER_SSH = "gdbserver-ssh"

    # Direct GDB remote connection
    GDB_REMOTE = "gdb-remote"

    # Default debug tool
    DEFAULT = GDBSERVER_SSH

    # Default debug port for direct TCP connection
    DEFAULT_PORT = "localhost:2345"


class ToolchainPrefix:
    """Toolchain prefixes for cross-compilation."""

    # 64-bit ARM (ARMv8/AArch64) toolchain prefix
    AARCH64 = "aarch64-linux-gnu-"

    # 32-bit ARM (ARMv7) toolchain prefix
    ARMV7 = "arm-linux-gnueabihf-"


class GDBExecutable:
    """GDB executable names for different architectures."""

    # Native GDB (when running on ARM Linux)
    NATIVE = "gdb"

    # 64-bit ARM GDB
    AARCH64 = "aarch64-linux-gnu-gdb"

    # 32-bit ARM GDB
    ARMV7 = "arm-linux-gnueabihf-gdb"


class Architecture:
    """Target architecture identifiers."""

    # 64-bit ARM (ARMv8)
    AARCH64 = "aarch64"

    # 32-bit ARM (ARMv7) - default for backward compatibility
    ARMV7 = "armv7"


class SystemType:
    """System type identifiers for platform detection."""

    # 32-bit ARM Linux
    LINUX_ARM = "linux_arm"

    # 64-bit ARM Linux
    LINUX_AARCH64 = "linux_aarch64"

    # macOS x86_64 (only platform with PlatformIO toolchain package)
    DARWIN_X86_64 = "darwin_x86_64"


class PackageName:
    """PlatformIO package names."""

    # Cross-compilation toolchain package
    TOOLCHAIN_GCC_ARM = "toolchain-gccarmlinuxgnueabi"


class Framework:
    """Framework identifiers."""

    # WiringPi GPIO library
    WIRINGPI = "wiringpi"


class SSHOptions:
    """SSH command-line options for security and reliability."""

    # Disable strict host key checking (for automated deployments)
    STRICT_HOST_KEY_CHECKING_NO = "StrictHostKeyChecking=no"

    # Don't save host keys (for automated deployments)
    USER_KNOWN_HOSTS_FILE_NULL = "UserKnownHostsFile=/dev/null"

    # Reduce SSH output verbosity
    LOG_LEVEL_ERROR = "LogLevel=ERROR"


class RsyncDefaults:
    """Default values for rsync operations."""

    # Default rsync flags: archive mode, verbose, compress
    FLAGS = "-avz"


class UIConstants:
    """Constants for user interface and display."""

    # Width of separator lines in terminal output
    SEPARATOR_WIDTH = 60

    # Separator character
    SEPARATOR_CHAR = "="
