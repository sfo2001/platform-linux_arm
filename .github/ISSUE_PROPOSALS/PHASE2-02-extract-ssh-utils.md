# ♻️ Extract SSH Command Building to Shared Module

## Priority
**P1 - High Priority** (Code Quality - DRY Principle)

**SHOULD FIX for v1.8.0**

## Labels
`enhancement`, `refactoring`, `P1`, `code-quality`

## Summary

Extract duplicated SSH/SCP command building logic into a shared utility module to eliminate code duplication, centralize security fixes, and improve maintainability.

## Problem

**Current State:**
- SSH command building logic duplicated across **6+ methods**
- Nearly identical code in `platform.py` and `platform-test-uploader.py`
- Security fixes must be applied to multiple locations
- Inconsistent error handling
- Harder to test in isolation

**Duplication Examples:**
- `platform.py`: `_upload_scp()`, `_upload_rsync()`, `_upload_ssh()`, `_run_remote_command()`
- `platform-test-uploader.py`: `build_ssh_command()`, `build_scp_command()`

## Solution

Create `ssh_utils.py` module with reusable SSH command builders.

### Implementation

#### New File: `ssh_utils.py`

```python
"""
Shared utilities for SSH/SCP command construction.

This module provides secure, reusable builders for SSH and SCP commands
with proper shell escaping and error handling.
"""

import os
import shlex
from typing import List, Optional

class SSHConnectionConfig:
    """Configuration for SSH connections."""

    def __init__(
        self,
        user: str,
        host: str,
        port: str = "22",
        key: Optional[str] = None,
        strict_host_check: bool = False
    ):
        self.user = user
        self.host = host
        self.port = port
        self.key = key
        self.strict_host_check = strict_host_check

    def validate(self) -> None:
        """Validate configuration."""
        if not self.user or not self.host:
            raise ValueError("User and host are required")

        if self.key:
            key_path = os.path.expanduser(self.key)
            if not os.path.exists(key_path):
                raise FileNotFoundError(f"SSH key not found: {key_path}")


class SSHCommandBuilder:
    """Build SSH commands with proper escaping and security."""

    def __init__(self, config: SSHConnectionConfig):
        self.config = config
        self.config.validate()

    def build_ssh_command(
        self,
        remote_command: Optional[str] = None,
        extra_opts: Optional[List[str]] = None
    ) -> List[str]:
        """
        Build SSH command.

        Args:
            remote_command: Command to execute on remote host
            extra_opts: Additional SSH options

        Returns:
            Command as list of arguments
        """
        cmd = ["ssh"]

        # Port
        cmd.extend(["-p", str(self.config.port)])

        # SSH key
        if self.config.key:
            key_path = os.path.expanduser(self.config.key)
            cmd.extend(["-i", key_path])

        # Host key verification
        if not self.config.strict_host_check:
            cmd.extend(["-o", "StrictHostKeyChecking=no"])
            cmd.extend(["-o", "UserKnownHostsFile=/dev/null"])
            cmd.extend(["-o", "LogLevel=ERROR"])

        # Extra options
        if extra_opts:
            cmd.extend(extra_opts)

        # Target
        cmd.append(f"{self.config.user}@{self.config.host}")

        # Remote command (properly escaped)
        if remote_command:
            cmd.append(remote_command)

        return cmd

    def build_scp_command(
        self,
        local_path: str,
        remote_path: str,
        extra_flags: Optional[List[str]] = None
    ) -> List[str]:
        """
        Build SCP command.

        Args:
            local_path: Local file path
            remote_path: Remote file path (will be shell-escaped)
            extra_flags: Additional SCP flags

        Returns:
            Command as list of arguments
        """
        cmd = ["scp"]

        # Port (note: SCP uses -P, SSH uses -p)
        cmd.extend(["-P", str(self.config.port)])

        # SSH key
        if self.config.key:
            key_path = os.path.expanduser(self.config.key)
            cmd.extend(["-i", key_path])

        # Host key verification
        if not self.config.strict_host_check:
            cmd.extend(["-o", "StrictHostKeyChecking=no"])
            cmd.extend(["-o", "UserKnownHostsFile=/dev/null"])
            cmd.extend(["-o", "LogLevel=ERROR"])

        # Extra flags
        if extra_flags:
            cmd.extend(extra_flags)

        # Source and destination
        cmd.append(local_path)
        # Remote path is shell-escaped
        cmd.append(f"{self.config.user}@{self.config.host}:{shlex.quote(remote_path)}")

        return cmd

    def build_rsync_command(
        self,
        local_path: str,
        remote_path: str,
        flags: str = "-avz"
    ) -> List[str]:
        """
        Build rsync command with SSH transport.

        Args:
            local_path: Local file path
            remote_path: Remote file path
            flags: Rsync flags (default: -avz)

        Returns:
            Command as list of arguments
        """
        cmd = ["rsync"]

        # Flags
        if flags:
            cmd.extend(flags.split())

        # SSH options
        ssh_opts = ["-p", str(self.config.port)]
        if self.config.key:
            key_path = os.path.expanduser(self.config.key)
            ssh_opts.extend(["-i", key_path])

        # Build SSH command string (for rsync -e option)
        ssh_cmd = "ssh " + " ".join(shlex.quote(opt) for opt in ssh_opts)
        cmd.extend(["-e", ssh_cmd])

        # Source and destination
        cmd.append(local_path)
        cmd.append(f"{self.config.user}@{self.config.host}:{shlex.quote(remote_path)}")

        return cmd


def parse_upload_port(
    upload_port: str,
    default_user: str = "pi",
    default_path: str = "/tmp/program"
) -> tuple[str, str, str]:
    """
    Parse upload_port into components.

    Supported formats:
      - user@host:/path
      - user@host
      - host:/path
      - host

    Args:
        upload_port: Upload port string
        default_user: Default user if not specified
        default_path: Default path if not specified

    Returns:
        Tuple of (user, host, path)

    Raises:
        ValueError: If upload_port is invalid
    """
    if not upload_port:
        raise ValueError("upload_port is required")

    user = default_user
    path = default_path

    # Parse user@host:path format
    if "@" in upload_port:
        user, host_part = upload_port.split("@", 1)
    else:
        host_part = upload_port

    # Parse host:path
    if ":" in host_part:
        host, path = host_part.split(":", 1)
    else:
        host = host_part

    return user, host, path
```

### Usage Example

#### In `platform.py`:

```python
from ssh_utils import SSHConnectionConfig, SSHCommandBuilder, parse_upload_port

def _upload_scp(self, target, source, env):
    """Upload binary using SCP."""
    upload_port = env.GetProjectOption("upload_port", None)
    user, host, path = parse_upload_port(upload_port, "pi", "/tmp/program")

    # Create SSH config
    config = SSHConnectionConfig(
        user=user,
        host=host,
        port=env.GetProjectOption("upload_ssh_port", "22"),
        key=env.GetProjectOption("upload_ssh_key", None),
        strict_host_check=env.GetProjectOption("upload_strict_host_check", False)
    )

    # Build SCP command
    builder = SSHCommandBuilder(config)
    flags = env.GetProjectOption("upload_flags", "").split() if env.GetProjectOption("upload_flags", "") else None
    cmd = builder.build_scp_command(str(source[0]), path, extra_flags=flags)

    # Execute
    result = subprocess.run(cmd, timeout=timeout)
    # ... rest of implementation
```

## Benefits

✅ **DRY (Don't Repeat Yourself)**
- Single source of truth for SSH command building
- Eliminates 200+ lines of duplicate code

✅ **Centralized Security**
- Security fixes applied once, affect all callers
- Consistent shell escaping everywhere

✅ **Easier Testing**
- Utility functions can be unit tested in isolation
- Mock SSH commands for testing

✅ **Better Maintainability**
- Changes to SSH logic in one place
- Consistent behavior across upload/test/debug

✅ **Type Safety**
- Strongly typed configuration objects
- Clear interface boundaries

## Refactoring Plan

### Phase 1: Create ssh_utils.py
- [ ] Implement `SSHConnectionConfig`
- [ ] Implement `SSHCommandBuilder`
- [ ] Implement `parse_upload_port()`
- [ ] Add comprehensive docstrings
- [ ] Add type hints

### Phase 2: Refactor platform.py
- [ ] Update `_upload_scp()` to use ssh_utils
- [ ] Update `_upload_rsync()` to use ssh_utils
- [ ] Update `_upload_ssh()` to use ssh_utils
- [ ] Update `_run_remote_command()` to use ssh_utils
- [ ] Remove duplicate `_parse_upload_port()` method

### Phase 3: Refactor platform-test-uploader.py
- [ ] Update `build_ssh_command()` to use ssh_utils
- [ ] Update `build_scp_command()` to use ssh_utils
- [ ] Update `parse_test_port()` to use common parser

### Phase 4: Testing & Validation
- [ ] Add unit tests for ssh_utils
- [ ] Test all upload protocols
- [ ] Test all test transport modes
- [ ] Verify no regressions

## Testing Strategy

### Unit Tests (New)

```python
# test_ssh_utils.py
import pytest
from ssh_utils import SSHConnectionConfig, SSHCommandBuilder, parse_upload_port

def test_parse_upload_port():
    user, host, path = parse_upload_port("pi@raspberrypi:/tmp/prog")
    assert user == "pi"
    assert host == "raspberrypi"
    assert path == "/tmp/prog"

def test_build_ssh_command():
    config = SSHConnectionConfig("pi", "raspberrypi", "22")
    builder = SSHCommandBuilder(config)
    cmd = builder.build_ssh_command("ls -la")

    assert "ssh" in cmd
    assert "pi@raspberrypi" in cmd
    assert "ls -la" in cmd

def test_shell_escaping():
    config = SSHConnectionConfig("pi", "host")
    builder = SSHCommandBuilder(config)
    cmd = builder.build_scp_command("/local/file", "/tmp/file; rm -rf /")

    # Remote path should be shell-escaped
    assert "'/tmp/file; rm -rf /'" in " ".join(cmd)
```

### Integration Tests

- Test all upload protocols with ssh_utils
- Test test execution with ssh_utils
- Verify backward compatibility

## Acceptance Criteria

- [ ] `ssh_utils.py` module created with full implementation
- [ ] All SSH command building logic uses ssh_utils
- [ ] No code duplication remains
- [ ] Unit tests added and passing
- [ ] Integration tests passing
- [ ] All existing functionality preserved
- [ ] Type hints on all new code
- [ ] Docstrings on all public APIs
- [ ] Security improvements maintained (shlex.quote)
- [ ] Code reviewed

## Related Issues

- Depends on: #[Phase 1 Issue 1] - Command injection fixes (should use consistent escaping)
- Part of: Python Code Quality Improvement Initiative (Phase 2)
- Related to: #[Phase 2 Issue 1] - Add type hints
- Related to: #[Phase 2 Issue 3] - Add docstrings

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 2, Task 2.2)

**Files Affected:**
- `ssh_utils.py` (new)
- `platform.py` (refactored)
- `platform-test-uploader.py` (refactored)
- `tests/test_ssh_utils.py` (new)

## Estimated Effort

**4-5 hours** (includes testing)

- Create ssh_utils.py: 2 hours
- Refactor platform.py: 1 hour
- Refactor test-uploader.py: 0.5 hour
- Testing: 1 hour
- Documentation: 0.5 hour

## Implementation Notes

1. Create ssh_utils.py first with full test coverage
2. Refactor one file at a time (start with platform.py)
3. Test thoroughly after each refactoring
4. Consider backward compatibility (can introduce gradually)
5. Update import statements in all files

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
**Analysis:** research/PYTHON_CODEBASE_ANALYSIS.md
