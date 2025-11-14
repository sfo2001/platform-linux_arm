# 🔴 CRITICAL: Fix Command Injection Vulnerabilities in platform.py

## Priority
**P0 - CRITICAL SECURITY** 🚨

**MUST FIX before next release (v1.7.1 or v1.8.0)**

## Labels
`security`, `critical`, `P0`, `bug`

## Summary

Three critical command injection vulnerabilities exist in `platform.py` that could allow remote code execution on target devices through unsanitized user input in SSH/SCP operations.

## Security Impact

**CVSS Scores:**
- Line 281 (SSH upload): **9.0 Critical**
- Line 220 (rsync SSH options): **8.0 High**
- Line 406 (debug session): **8.0 High**

**Attack Vector:** Malicious input in `upload_port`, `ssh_key`, or `prog_path` configuration could execute arbitrary commands on remote targets.

**Example Attack:**
```ini
# In platformio.ini
upload_port = pi@host:/tmp/program; rm -rf /
```

## Affected Code

### Vulnerability 1: SSH Upload Path (Line 281)
```python
# VULNERABLE CODE
cmd.append(f"cat > {path} && chmod +x {path}")
```

**Risk:** `path` is user-controlled and not shell-escaped.

### Vulnerability 2: Rsync SSH Options (Line 220)
```python
# VULNERABLE CODE
ssh_opts = f"-p {ssh_port}"
if ssh_key:
    ssh_opts += f" -i {key_path}"
cmd.extend(["-e", f"ssh {ssh_opts}"])
```

**Risk:** Shell metacharacters in `ssh_key` path will be interpreted.

### Vulnerability 3: Debug Session Path (Line 406)
```python
# VULNERABLE CODE
ssh_cmd_parts.append("gdbserver - " + prog_path)
```

**Risk:** `prog_path` is not shell-escaped.

## Solution

Use `shlex.quote()` to properly escape all user-controlled shell arguments.

### Implementation

```python
import shlex

# Fix 1: Line 281 (_upload_ssh)
cmd.append(f"cat > {shlex.quote(path)} && chmod +x {shlex.quote(path)}")

# Fix 2: Line 220 (_upload_rsync)
ssh_args = ["-p", str(ssh_port)]
if ssh_key:
    ssh_args.extend(["-i", key_path])
cmd.extend(["-e", "ssh " + " ".join(shlex.quote(arg) for arg in ssh_args)])

# Fix 3: Line 406 (configure_debug_session)
ssh_cmd_parts.append("gdbserver - " + shlex.quote(prog_path))
```

## Testing Requirements

**Test Cases:**
- [ ] Normal paths work: `/tmp/program`
- [ ] Paths with spaces work: `/tmp/my program`
- [ ] Malicious input is escaped: `/tmp/program; rm -rf /tmp/test`
- [ ] Special characters handled: `$HOME/program`, `~/program`, `./program`
- [ ] All upload protocols tested: SCP, rsync, SSH
- [ ] Debug session with various paths
- [ ] Cross-compilation and native builds

**Manual Testing:**
```bash
# Test with malicious path
echo 'upload_port = pi@host:/tmp/program; echo "EXPLOITED"' >> platformio.ini
pio run --target upload
# Should NOT see "EXPLOITED" in output
```

## Acceptance Criteria

- [x] All three vulnerabilities fixed with `shlex.quote()`
- [ ] Tests pass with normal paths
- [ ] Tests pass with paths containing spaces
- [ ] Malicious input is properly escaped (no command execution)
- [ ] All upload protocols work correctly
- [ ] Debug sessions work correctly
- [ ] Documentation updated with security notes
- [ ] Code reviewed by security-conscious developer

## Related Issues

- Blocks: All other security work (must fix first)
- Related: #[Phase 1 Issue 2] - Command injection in test uploader
- Part of: Python Codebase Security Audit

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 1, Task 1.1)

**Affected Files:**
- `platform.py:220` (_upload_rsync)
- `platform.py:281` (_upload_ssh)
- `platform.py:406` (configure_debug_session)

**External References:**
- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html)
- [Python shlex.quote() documentation](https://docs.python.org/3/library/shlex.html#shlex.quote)

## Estimated Effort

**2 hours** (straightforward fix, but requires thorough testing)

## Implementation Notes

1. Add `import shlex` at top of `platform.py`
2. Apply fixes to all three locations
3. Run comprehensive test suite
4. Test on actual hardware (Raspberry Pi)
5. Verify no regression in existing functionality

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
**Analysis:** research/PYTHON_CODEBASE_ANALYSIS.md
