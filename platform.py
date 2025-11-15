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

import os
import shlex
import shutil
import subprocess
import sys

from platformio import exception
from platformio.public import PlatformBase, get_systype

# Add platform directory to sys.path for platform_constants import
# This is necessary because during platform installation via symlink://,
# the platform directory is not yet in Python's path
_PLATFORM_DIR = os.path.dirname(os.path.realpath(__file__))
if _PLATFORM_DIR not in sys.path:
    sys.path.insert(0, _PLATFORM_DIR)


class Linux_armPlatform(PlatformBase):

    @staticmethod
    def _is_native():
        # Lazy import to avoid breaking platform loading
        from platform_constants import SystemType

        systype = get_systype()
        return SystemType.LINUX_ARM in systype or SystemType.LINUX_AARCH64 in systype

    @property
    def packages(self):
        # Lazy import to avoid breaking platform loading
        from platform_constants import SystemType, PackageName

        packages = PlatformBase.packages.fget(self)
        systype = get_systype()
        # PlatformIO's toolchain package only works on macOS x86_64
        # All other platforms use system-installed toolchains
        if systype != SystemType.DARWIN_X86_64 and PackageName.TOOLCHAIN_GCC_ARM in packages:
            del packages[PackageName.TOOLCHAIN_GCC_ARM]
        return packages

    def configure_default_packages(self, variables, targets):
        # Lazy import to avoid breaking platform loading
        from platform_constants import Framework

        if not self._is_native() and Framework.WIRINGPI in variables.get(
                "pioframework", []):
            raise exception.PlatformioException(
                "PlatformIO temporary does not support cross-compilation "
                "for WiringPi framework. Please use PIO Core directly on "
                "Raspberry Pi")
        return super().configure_default_packages(variables, targets)

    def _get_upload_protocol(self, env) -> str:
        """
        Get and validate upload protocol from environment.

        Args:
            env: PlatformIO environment

        Returns:
            Upload protocol name

        Raises:
            PlatformioException: If protocol is not supported
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import UploadProtocol

        protocol = env.GetProjectOption("upload_protocol", UploadProtocol.MANUAL)
        valid_protocols = UploadProtocol.ALL

        if protocol not in valid_protocols:
            raise exception.PlatformioException(
                f"Unknown upload protocol '{protocol}'. "
                f"Supported protocols: {', '.join(valid_protocols)}"
            )

        return protocol

    def _show_manual_upload_instructions(self, source) -> int:
        """
        Display manual upload instructions to user.

        Args:
            source: List of source files (binary path)

        Returns:
            Exit code (0 for success)
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import UIConstants

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("MANUAL UPLOAD REQUIRED")
        print(separator)
        print("\nCompiled binary location:")
        print(f"  {source[0]}")
        print("\nTo deploy to your target device, use one of:")
        print(f"  scp {source[0]} user@host:/path/to/destination")
        print(f"  rsync -avz {source[0]} user@host:/path/to/destination")
        print("\nTo configure automatic upload, add to platformio.ini:")
        print("  upload_protocol = scp")
        print("  upload_port = user@hostname:/path/to/destination")
        print("\nSee documentation for more upload options.")
        print(separator + "\n")
        return 0

    def on_upload(self, target, source, env):
        """
        Custom upload handler for Linux ARM platform.
        Supports multiple upload protocols: scp, rsync, ssh, manual.

        Args:
            target: Build target
            source: List of source files (binary path)
            env: PlatformIO environment

        Returns:
            Exit code (0 for success, non-zero for failure)
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import UploadProtocol

        upload_protocol = self._get_upload_protocol(env)

        upload_handlers = {
            UploadProtocol.SCP: self._upload_scp,
            UploadProtocol.RSYNC: self._upload_rsync,
            UploadProtocol.SSH: self._upload_ssh,
            UploadProtocol.MANUAL: lambda t, s, e: self._show_manual_upload_instructions(s)
        }

        handler = upload_handlers[upload_protocol]
        return handler(target, source, env)

    def _check_upload_tool(self, tool_name):
        """Check if required upload tool is available."""
        if not shutil.which(tool_name):
            raise exception.PlatformioException(
                f"Upload tool '{tool_name}' is not installed. "
                f"Please install it using your system package manager:\n"
                f"  Linux: sudo apt install {tool_name}\n"
                f"  macOS: brew install {tool_name}"
            )

    def _parse_upload_port(self, upload_port, env):
        """
        Parse upload_port into components.
        Supported formats:
          - user@host:/path/to/destination
          - user@host
          - host:/path
          - host
        Returns: (user, host, path)
        """
        # Lazy import to avoid breaking platform loading
        from ssh_utils import parse_upload_port
        from platform_constants import SSHDefaults

        if not upload_port:
            raise exception.PlatformioException(
                "upload_port is not configured. Add to platformio.ini:\n"
                "  upload_port = user@hostname:/path/to/destination"
            )

        # Get defaults from project options
        default_user = env.GetProjectOption("upload_user", SSHDefaults.USER)
        default_path = env.GetProjectOption("upload_path", SSHDefaults.UPLOAD_PATH)

        # Use shared parser
        try:
            return parse_upload_port(upload_port, default_user, default_path)
        except ValueError as e:
            raise exception.PlatformioException(str(e))

    def _upload_scp(self, target, source, env):
        """Upload binary using SCP (Secure Copy Protocol)."""
        # Lazy import to avoid breaking platform loading
        from ssh_utils import SSHConnectionConfig, SSHCommandBuilder
        from platform_constants import SSHDefaults, Timeouts, UIConstants

        self._check_upload_tool("scp")

        upload_port = env.GetProjectOption("upload_port", None)
        user, host, path = self._parse_upload_port(upload_port, env)

        ssh_port = env.GetProjectOption("upload_ssh_port", SSHDefaults.PORT)
        ssh_key = env.GetProjectOption("upload_ssh_key", None)
        upload_flags = env.GetProjectOption("upload_flags", "")

        # Create SSH config
        try:
            config = SSHConnectionConfig(
                user=user,
                host=host,
                port=ssh_port,
                key=ssh_key,
                strict_host_check=False
            )
        except (ValueError, FileNotFoundError) as e:
            raise exception.PlatformioException(str(e))

        # Build SCP command using shared builder
        builder = SSHCommandBuilder(config)
        extra_flags = upload_flags.split() if upload_flags else None
        cmd = builder.build_scp_command(str(source[0]), path, extra_flags=extra_flags)

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("UPLOADING VIA SCP")
        print(separator)
        print(f"Source:      {source[0]}")
        print(f"Destination: {user}@{host}:{path}")
        print(f"SSH Port:    {ssh_port}")
        if ssh_key:
            print(f"SSH Key:     {ssh_key}")
        print(separator + "\n")

        # Execute SCP command with timeout protection
        upload_timeout = env.GetProjectOption("upload_timeout", Timeouts.UPLOAD)
        try:
            result = subprocess.run(cmd, capture_output=False, text=True, timeout=upload_timeout)
        except subprocess.TimeoutExpired:
            raise exception.PlatformioException(
                f"SCP upload timeout after {upload_timeout} seconds. "
                "Increase timeout with 'upload_timeout' option in platformio.ini"
            )

        if result.returncode != 0:
            raise exception.PlatformioException(
                f"SCP upload failed with exit code {result.returncode}"
            )

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("UPLOAD SUCCESSFUL")
        print(separator + "\n")

        # Post-upload execution if configured
        if env.GetProjectOption("upload_run_after", False):
            return self._run_remote_command(user, host, ssh_port, ssh_key, path, env)

        return 0

    def _upload_rsync(self, target, source, env):
        """Upload binary using rsync (efficient incremental transfer)."""
        # Lazy import to avoid breaking platform loading
        from ssh_utils import SSHConnectionConfig, SSHCommandBuilder
        from platform_constants import SSHDefaults, RsyncDefaults, UIConstants

        self._check_upload_tool("rsync")

        upload_port = env.GetProjectOption("upload_port", None)
        user, host, path = self._parse_upload_port(upload_port, env)

        ssh_port = env.GetProjectOption("upload_ssh_port", SSHDefaults.PORT)
        ssh_key = env.GetProjectOption("upload_ssh_key", None)
        upload_flags = env.GetProjectOption("upload_flags", RsyncDefaults.FLAGS)

        # Create SSH config
        try:
            config = SSHConnectionConfig(
                user=user,
                host=host,
                port=ssh_port,
                key=ssh_key,
                strict_host_check=False
            )
        except (ValueError, FileNotFoundError) as e:
            raise exception.PlatformioException(str(e))

        # Build rsync command using shared builder
        builder = SSHCommandBuilder(config)
        cmd = builder.build_rsync_command(str(source[0]), path, flags=upload_flags)

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("UPLOADING VIA RSYNC")
        print("="*60)
        print(f"Source:      {source[0]}")
        print(f"Destination: {user}@{host}:{path}")
        print(f"SSH Port:    {ssh_port}")
        if ssh_key:
            print(f"SSH Key:     {ssh_key}")
        print(f"Flags:       {upload_flags}")
        print(separator + "\n")

        # Execute rsync command with timeout protection
        upload_timeout = env.GetProjectOption("upload_timeout", 300)
        try:
            result = subprocess.run(cmd, capture_output=False, text=True, timeout=upload_timeout)
        except subprocess.TimeoutExpired:
            raise exception.PlatformioException(
                f"Rsync upload timeout after {upload_timeout} seconds. "
                "Increase timeout with 'upload_timeout' option in platformio.ini"
            )

        if result.returncode != 0:
            raise exception.PlatformioException(
                f"Rsync upload failed with exit code {result.returncode}"
            )

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("UPLOAD SUCCESSFUL")
        print(separator + "\n")

        # Post-upload execution if configured
        if env.GetProjectOption("upload_run_after", False):
            return self._run_remote_command(user, host, ssh_port, ssh_key, path, env)

        return 0

    def _upload_ssh(self, target, source, env):
        """
        Upload binary using SSH with piped input.
        This method uses SSH with cat to transfer the file.
        """
        # Lazy import to avoid breaking platform loading
        from ssh_utils import SSHConnectionConfig, SSHCommandBuilder
        from platform_constants import SSHDefaults, UIConstants

        self._check_upload_tool("ssh")

        upload_port = env.GetProjectOption("upload_port", None)
        user, host, path = self._parse_upload_port(upload_port, env)

        ssh_port = env.GetProjectOption("upload_ssh_port", SSHDefaults.PORT)
        ssh_key = env.GetProjectOption("upload_ssh_key", None)

        # Create SSH config
        try:
            config = SSHConnectionConfig(
                user=user,
                host=host,
                port=ssh_port,
                key=ssh_key,
                strict_host_check=False
            )
        except (ValueError, FileNotFoundError) as e:
            raise exception.PlatformioException(str(e))

        # Build SSH command using shared builder
        # Use shlex.quote to prevent command injection via path
        remote_command = f"cat > {shlex.quote(path)} && chmod +x {shlex.quote(path)}"
        builder = SSHCommandBuilder(config)
        cmd = builder.build_ssh_command(remote_command)

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("UPLOADING VIA SSH")
        print("="*60)
        print(f"Source:      {source[0]}")
        print(f"Destination: {user}@{host}:{path}")
        print(f"SSH Port:    {ssh_port}")
        if ssh_key:
            print(f"SSH Key:     {ssh_key}")
        print(separator + "\n")

        # Execute SSH command with file as stdin and timeout protection
        upload_timeout = env.GetProjectOption("upload_timeout", 300)
        try:
            with open(str(source[0]), "rb") as f:
                result = subprocess.run(cmd, stdin=f, capture_output=False, text=False, timeout=upload_timeout)
        except subprocess.TimeoutExpired:
            raise exception.PlatformioException(
                f"SSH upload timeout after {upload_timeout} seconds. "
                "Increase timeout with 'upload_timeout' option in platformio.ini"
            )

        if result.returncode != 0:
            raise exception.PlatformioException(
                f"SSH upload failed with exit code {result.returncode}"
            )

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("UPLOAD SUCCESSFUL")
        print(separator + "\n")

        # Post-upload execution if configured
        if env.GetProjectOption("upload_run_after", False):
            return self._run_remote_command(user, host, ssh_port, ssh_key, path, env)

        return 0

    def _run_remote_command(self, user, host, ssh_port, ssh_key, remote_path, env):
        """Run the uploaded program on the remote target."""
        # Lazy import to avoid breaking platform loading
        from ssh_utils import SSHConnectionConfig, SSHCommandBuilder
        from platform_constants import UIConstants, Timeouts

        # Create SSH config
        try:
            config = SSHConnectionConfig(
                user=user,
                host=host,
                port=ssh_port,
                key=ssh_key,
                strict_host_check=False
            )
        except (ValueError, FileNotFoundError) as e:
            raise exception.PlatformioException(str(e))

        # Get custom run command or use default
        # Use shlex.quote to prevent command injection
        run_command = env.GetProjectOption("upload_run_command", None)
        if run_command:
            # For custom commands, use as-is
            remote_command = run_command
        else:
            # For simple path execution, quote the path
            remote_command = shlex.quote(remote_path)

        # Build SSH command using shared builder
        builder = SSHCommandBuilder(config)
        cmd = builder.build_ssh_command(remote_command)

        separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
        print("\n" + separator)
        print("RUNNING REMOTE PROGRAM")
        print("="*60)
        print(f"Target: {user}@{host}")
        print(f"Command: {run_command if run_command else remote_path}")
        print(separator + "\n")

        # Execute remote command with timeout protection (interactive - shows output directly)
        run_timeout = env.GetProjectOption("upload_run_timeout", Timeouts.UPLOAD_RUN)
        try:
            result = subprocess.run(cmd, timeout=run_timeout)
        except subprocess.TimeoutExpired:
            raise exception.PlatformioException(
                f"Remote command execution timeout after {run_timeout} seconds. "
                "Increase timeout with 'upload_run_timeout' option in platformio.ini"
            )

        return result.returncode

    def _determine_gdb_executable(self, target_arch: str) -> str:
        """
        Determine GDB executable path based on target architecture.

        Args:
            target_arch: Target architecture (e.g., 'aarch64', 'armv7')

        Returns:
            Path to appropriate GDB executable
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import GDBExecutable, Architecture

        if self._is_native():
            return GDBExecutable.NATIVE

        if target_arch == Architecture.AARCH64:
            return GDBExecutable.AARCH64

        return GDBExecutable.ARMV7

    def _parse_debug_connection_info(self, debug_config: dict) -> tuple:
        """
        Parse debug connection information from configuration.

        Args:
            debug_config: Debug configuration dictionary

        Returns:
            Tuple of (user, host, prog_path, ssh_port, ssh_key)

        Raises:
            PlatformioException: If connection info cannot be parsed
        """
        # Lazy import to avoid breaking platform loading
        from ssh_utils import parse_upload_port
        from platform_constants import SSHDefaults

        upload_port = debug_config.get("upload_port")
        ssh_port = debug_config.get("ssh_port", SSHDefaults.PORT)
        ssh_key = debug_config.get("ssh_key")
        prog_path = debug_config.get("prog_path", SSHDefaults.UPLOAD_PATH)
        user = SSHDefaults.USER
        host = None

        if upload_port:
            try:
                user, host, prog_path = parse_upload_port(
                    upload_port,
                    default_user=SSHDefaults.USER,
                    default_path=prog_path
                )
            except ValueError:
                # Fallback: simple extraction
                if "@" in upload_port:
                    user_host = upload_port.split(":")[0]
                    user, host = user_host.split("@", 1)
                else:
                    host = upload_port.split(":")[0]

        return user, host, prog_path, ssh_port, ssh_key

    def _configure_gdbserver_ssh(
        self,
        debug_config: dict,
        user: str,
        host: str,
        ssh_port: str,
        ssh_key: str,
        prog_path: str
    ) -> None:
        """
        Configure SSH-tunneled gdbserver.

        Args:
            debug_config: Debug configuration dictionary (modified in place)
            user: SSH username
            host: SSH hostname
            ssh_port: SSH port number
            ssh_key: Path to SSH key file (optional)
            prog_path: Remote program path

        Raises:
            PlatformioException: If SSH configuration is invalid
        """
        # Lazy import to avoid breaking platform loading
        from ssh_utils import SSHConnectionConfig, SSHCommandBuilder

        if not host:
            raise exception.PlatformioException(
                "debug_port or upload_port must be configured for SSH debugging.\n"
                "Add to platformio.ini:\n"
                "  debug_port = user@hostname\n"
                "  or use existing upload_port configuration"
            )

        # Create SSH config
        try:
            config = SSHConnectionConfig(
                user=user,
                host=host,
                port=ssh_port,
                key=ssh_key,
                strict_host_check=False
            )
        except (ValueError, FileNotFoundError) as e:
            raise exception.PlatformioException(str(e))

        # Build SSH command for GDB remote target
        remote_command = "gdbserver - " + shlex.quote(prog_path)
        builder = SSHCommandBuilder(config)
        ssh_cmd_parts = builder.build_ssh_command(remote_command, extra_opts=["-T"])
        ssh_cmd = " ".join(shlex.quote(part) for part in ssh_cmd_parts)

        debug_config["server_executable"] = None
        debug_config["server_arguments"] = []
        debug_config["port"] = f"| {ssh_cmd}"

    def _configure_gdb_remote(self, debug_config: dict) -> None:
        """
        Configure direct TCP connection to gdbserver.

        Args:
            debug_config: Debug configuration dictionary (modified in place)
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import DebugTools

        debug_port = debug_config.get("port", DebugTools.DEFAULT_PORT)
        debug_config["port"] = debug_port

    def _build_debug_init_commands(
        self,
        debug_tool: str,
        debug_config: dict,
        prog_path: str
    ) -> list:
        """
        Build GDB initialization commands.

        Args:
            debug_tool: Debug tool name ('gdbserver-ssh' or 'gdb-remote')
            debug_config: Debug configuration dictionary
            prog_path: Remote program path

        Returns:
            List of GDB initialization commands
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import DebugTools

        init_cmds = []

        if debug_tool == DebugTools.GDBSERVER_SSH:
            init_cmds.extend([
                f"target extended-remote {debug_config['port']}",
                f"set remote exec-file {prog_path}",
                "set sysroot /",
            ])
        else:
            init_cmds.append(f"target extended-remote {debug_config['port']}")

        # Add custom init commands from config
        custom_init = debug_config.get("init_cmds", [])
        if custom_init:
            init_cmds.extend(custom_init)

        return init_cmds

    def configure_debug_session(self, debug_config: dict) -> dict:
        """
        Configure remote debugging session for ARM Linux targets.
        Supports GDB/gdbserver over SSH for remote debugging.

        Args:
            debug_config: Debug configuration dictionary

        Returns:
            Updated debug configuration dictionary
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import DebugTools

        # Get board configuration and determine GDB executable
        board_config = self.board_config(debug_config.get("env_name"))
        target_arch = board_config.get("build.arch", "armv7")
        gdb_path = self._determine_gdb_executable(target_arch)

        # Parse connection information
        user, host, prog_path, ssh_port, ssh_key = self._parse_debug_connection_info(debug_config)

        # Get debug tool
        debug_tool = debug_config.get("tool", DebugTools.GDBSERVER_SSH)

        # Configure debug server based on tool
        if debug_tool == DebugTools.GDBSERVER_SSH:
            self._configure_gdbserver_ssh(debug_config, user, host, ssh_port, ssh_key, prog_path)
        elif debug_tool == DebugTools.GDB_REMOTE:
            self._configure_gdb_remote(debug_config)

        # Set GDB configuration
        debug_config["executable"] = gdb_path
        debug_config["prog_path"] = prog_path
        debug_config["init_cmds"] = self._build_debug_init_commands(debug_tool, debug_config, prog_path)

        return debug_config

    def get_boards(self, id_=None):
        """
        Return board configurations.
        Overridden to add debug configuration to board definitions.
        """
        result = super().get_boards(id_)
        if not result:
            return result

        # Add debug tool support to all boards
        if id_:
            # Single board
            return self._add_debug_to_board(result)
        else:
            # All boards
            return {key: self._add_debug_to_board(value)
                    for key, value in result.items()}

    def _add_debug_to_board(self, board):
        """Add debug configuration to a board definition."""
        # Lazy import to avoid breaking platform loading
        from platform_constants import DebugTools

        debug = board.manifest.get("debug", {})

        # Set default debug tools
        debug["tools"] = {
            "gdbserver-ssh": {
                "server": {
                    "package": None,
                    "executable": None,
                    "arguments": []
                },
                "init_cmds": [
                    "target extended-remote $DEBUG_PORT",
                    "set remote exec-file $PROG_PATH",
                    "set sysroot /"
                ],
                "extra_cmds": [
                    "break main",
                    "continue"
                ]
            },
            "gdb-remote": {
                "server": {
                    "package": None,
                    "executable": None,
                    "arguments": []
                },
                "init_cmds": [
                    "target extended-remote $DEBUG_PORT"
                ],
                "extra_cmds": [
                    "break main",
                    "continue"
                ]
            }
        }

        # Set default debug tool
        if "default" not in debug:
            debug["default"] = DebugTools.DEFAULT

        board.manifest["debug"] = debug
        return board

    def on_test_upload(self, target, source, env):
        """
        Custom test upload handler for Linux ARM platform.
        Uploads test binaries to remote target via SSH and executes them.
        """
        # Lazy import to avoid breaking platform loading
        from platform_constants import TestTransport, UIConstants

        test_transport = env.GetProjectOption("test_transport", TestTransport.SSH)

        if test_transport == TestTransport.SSH:
            # Load and execute the SSH test uploader
            uploader_path = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "platform-test-uploader.py"
            )

            # Import the uploader module
            import importlib.util
            spec = importlib.util.spec_from_file_location("test_uploader", uploader_path)
            uploader_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(uploader_module)

            # Execute the upload_test function
            return uploader_module.upload_test(target, source, env)

        elif test_transport == TestTransport.MANUAL:
            separator = UIConstants.SEPARATOR_CHAR * UIConstants.SEPARATOR_WIDTH
            print("\n" + separator)
            print("MANUAL TEST EXECUTION REQUIRED")
            print(separator)
            print("\nCompiled test binary location:")
            print(f"  {source[0]}")
            print("\nTo run tests on your target device:")
            print(f"  1. Upload the binary: scp {source[0]} user@host:/path/to/test")
            print(f"  2. Make it executable: ssh user@host 'chmod +x /path/to/test'")
            print(f"  3. Run the tests: ssh user@host '/path/to/test'")
            print("\nTo configure automatic test execution, add to platformio.ini:")
            print("  test_transport = ssh")
            print("  test_port = user@hostname:/path/to/test")
            print(separator + "\n")
            return 0

        else:
            raise exception.PlatformioException(
                f"Unknown test_transport '{test_transport}'. "
                f"Supported transports: {', '.join(TestTransport.ALL)}"
            )
