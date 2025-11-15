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
Remote SSH Test Uploader for Linux ARM Platform

This script uploads test binaries to a remote Linux ARM target via SSH,
executes them, and streams the output back to PlatformIO's test framework.
"""

import os
import shlex
import shutil
import subprocess
import sys
import time

from ssh_utils import SSHConnectionConfig, SSHCommandBuilder, parse_upload_port


class RemoteTestUploader:
    """
    Handles uploading and executing test binaries on remote Linux ARM targets via SSH.
    """

    def __init__(self, target, source, env):
        self.target = target
        self.source = source
        self.env = env
        self.upload_port = None
        self.user = None
        self.host = None
        self.remote_path = None
        self.ssh_port = "22"
        self.ssh_key = None

    def parse_test_port(self):
        """
        Parse test_port configuration.
        Supported formats:
          - user@host:/path/to/test_binary
          - user@host
          - host:/path
          - host
        """
        # Get test_port (preferred) or fallback to upload_port
        self.upload_port = self.env.GetProjectOption("test_port", None)
        if not self.upload_port:
            self.upload_port = self.env.GetProjectOption("upload_port", None)

        if not self.upload_port:
            raise Exception(
                "test_port or upload_port is not configured. Add to platformio.ini:\n"
                "  test_port = user@hostname:/path/to/test_binary\n"
                "  or\n"
                "  upload_port = user@hostname:/path/to/test_binary"
            )

        # Get defaults from project options
        default_user = self.env.GetProjectOption("test_username", "pi")
        default_path = self.env.GetProjectOption("test_path", "/tmp/test_program")

        # Use shared parser
        try:
            self.user, self.host, self.remote_path = parse_upload_port(
                self.upload_port,
                default_user=default_user,
                default_path=default_path
            )
        except ValueError as e:
            raise Exception(str(e))

        # Get SSH configuration
        self.ssh_port = self.env.GetProjectOption("test_ssh_port", "22")
        if not self.ssh_port:
            self.ssh_port = self.env.GetProjectOption("upload_ssh_port", "22")

        self.ssh_key = self.env.GetProjectOption("test_ssh_key", None)
        if not self.ssh_key:
            self.ssh_key = self.env.GetProjectOption("upload_ssh_key", None)

    def check_ssh_available(self):
        """Check if SSH is available on the system."""
        if not shutil.which("ssh"):
            raise Exception(
                "SSH is not installed. Please install it using your system package manager:\n"
                "  Linux: sudo apt install openssh-client\n"
                "  macOS: SSH is pre-installed"
            )
        if not shutil.which("scp"):
            raise Exception(
                "SCP is not installed. Please install it using your system package manager:\n"
                "  Linux: sudo apt install openssh-client\n"
                "  macOS: SCP is pre-installed"
            )

    def build_ssh_command(self, remote_command=None):
        """Build SSH command with proper authentication."""
        # Create SSH config
        try:
            config = SSHConnectionConfig(
                user=self.user,
                host=self.host,
                port=self.ssh_port,
                key=self.ssh_key,
                strict_host_check=False
            )
        except (ValueError, FileNotFoundError) as e:
            raise Exception(str(e))

        # Build SSH command using shared builder
        builder = SSHCommandBuilder(config)
        return builder.build_ssh_command(remote_command)

    def build_scp_command(self, local_file, remote_file):
        """Build SCP command for file upload."""
        # Create SSH config
        try:
            config = SSHConnectionConfig(
                user=self.user,
                host=self.host,
                port=self.ssh_port,
                key=self.ssh_key,
                strict_host_check=False
            )
        except (ValueError, FileNotFoundError) as e:
            raise Exception(str(e))

        # Build SCP command using shared builder
        builder = SSHCommandBuilder(config)
        return builder.build_scp_command(local_file, remote_file)

    def upload_test_binary(self):
        """Upload test binary to remote target via SCP."""
        source_file = str(self.source[0])

        print(f"\nUploading test binary to {self.user}@{self.host}:{self.remote_path}")

        # Upload the binary with timeout protection
        upload_timeout = self.env.GetProjectOption("test_upload_timeout", 300)
        cmd = self.build_scp_command(source_file, self.remote_path)
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=upload_timeout)
        except subprocess.TimeoutExpired:
            raise Exception(
                f"Test upload timeout after {upload_timeout} seconds. "
                "Increase timeout with 'test_upload_timeout' option in platformio.ini"
            )

        if result.returncode != 0:
            raise Exception(
                f"Failed to upload test binary:\n"
                f"Command: {' '.join(cmd)}\n"
                f"Error: {result.stderr}"
            )

        # Make it executable (use shlex.quote to prevent command injection)
        chmod_cmd = self.build_ssh_command(f"chmod +x {shlex.quote(self.remote_path)}")
        try:
            result = subprocess.run(chmod_cmd, capture_output=True, text=True, timeout=30)
        except subprocess.TimeoutExpired:
            raise Exception("Timeout while setting executable permission on remote test binary")

        if result.returncode != 0:
            raise Exception(
                f"Failed to make test binary executable:\n"
                f"Error: {result.stderr}"
            )

        print(f"Upload successful: {self.remote_path}")

    def _build_test_command(self) -> str:
        """
        Build remote test execution command with exit code capture.

        Returns:
            Remote shell command string
        """
        # Use shlex.quote to prevent command injection via remote_path
        return f"{shlex.quote(self.remote_path)}; echo \"__EXIT_CODE__:$?\""

    def _stream_test_output(self, process, test_timeout: int) -> int:
        """
        Stream test output from remote process and extract exit code.

        Args:
            process: subprocess.Popen instance
            test_timeout: Timeout in seconds

        Returns:
            Exit code from test execution

        Raises:
            Exception: If test execution times out
        """
        exit_code = 0

        try:
            # Stream output line by line
            for line in iter(process.stdout.readline, ""):
                if not line:
                    break

                # Check for exit code marker
                if "__EXIT_CODE__:" in line:
                    exit_code = self._extract_exit_code(line)
                else:
                    # Print to console (PlatformIO captures this)
                    print(line, end="")

            # Wait for process to complete with timeout
            process.wait(timeout=test_timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
            raise Exception(
                f"Test execution timeout after {test_timeout} seconds. "
                "Increase timeout with 'test_timeout' option in platformio.ini"
            )

        return exit_code

    def _extract_exit_code(self, line: str) -> int:
        """
        Extract exit code from marker line.

        Args:
            line: Output line containing exit code marker

        Returns:
            Extracted exit code, or 0 if extraction fails
        """
        try:
            return int(line.split("__EXIT_CODE__:")[1].strip())
        except (IndexError, ValueError):
            return 0

    def execute_test_binary(self) -> int:
        """
        Execute test binary on remote target and stream output.

        Returns:
            Exit code from test execution
        """
        print(f"\nExecuting tests on {self.user}@{self.host}...")
        print("=" * 80)

        # Build and execute test command
        test_command = self._build_test_command()
        cmd = self.build_ssh_command(test_command)
        test_timeout = self.env.GetProjectOption("test_timeout", 600)

        # Start process
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        # Stream output and get exit code
        try:
            exit_code = self._stream_test_output(process, test_timeout)
        finally:
            print("=" * 80)

        return exit_code

    def run(self):
        """Main entry point for the test uploader."""
        try:
            # Parse configuration
            self.parse_test_port()

            # Check prerequisites
            self.check_ssh_available()

            # Upload test binary
            self.upload_test_binary()

            # Execute tests and return exit code
            exit_code = self.execute_test_binary()

            if exit_code == 0:
                print("\n✓ Tests PASSED")
            else:
                print(f"\n✗ Tests FAILED (exit code: {exit_code})")

            return exit_code

        except subprocess.TimeoutExpired as e:
            print(f"\nERROR: Operation timed out after {e.timeout} seconds", file=sys.stderr)
            print("Increase timeout with 'test_timeout' or 'test_upload_timeout' option in platformio.ini", file=sys.stderr)
            return 1
        except subprocess.CalledProcessError as e:
            print(f"\nERROR: Remote command failed: {e}", file=sys.stderr)
            print(f"Exit code: {e.returncode}", file=sys.stderr)
            if e.stderr:
                print(f"Error output: {e.stderr}", file=sys.stderr)
            return e.returncode
        except (OSError, FileNotFoundError) as e:
            print(f"\nERROR: File operation failed: {e}", file=sys.stderr)
            return 1
        except ValueError as e:
            print(f"\nERROR: Configuration error: {e}", file=sys.stderr)
            return 1
        except KeyboardInterrupt:
            print("\nERROR: Operation cancelled by user", file=sys.stderr)
            return 130
        except Exception as e:
            print(f"\nERROR: Unexpected error: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            return 1


def upload_test(target, source, env):
    """
    Entry point called by PlatformIO test framework.
    This function is registered as the upload handler for tests.
    """
    uploader = RemoteTestUploader(target, source, env)
    return uploader.run()


# Allow this script to be run standalone for testing
if __name__ == "__main__":
    print("This script is designed to be called by PlatformIO test framework.")
    print("Use 'pio test' to run tests with this uploader.")
    sys.exit(1)
