# 🟡 Add Timeout Protection to Subprocess Calls

## Priority
**P0 - CRITICAL** (Security & Reliability)

**MUST FIX before next release (v1.7.1 or v1.8.0)**

## Labels
`security`, `reliability`, `P0`, `enhancement`

## Summary

Multiple `subprocess.run()` and `subprocess.Popen()` calls lack timeout protection, creating potential DoS vulnerabilities where hung SSH connections can block PlatformIO indefinitely.

## Impact

**Security Risk:**
- **CVSS Score:** 5.0 (Medium) - Denial of Service
- Hung SSH connections can block CI/CD pipelines indefinitely
- No way to recover from network failures without killing process
- Affects upload, test, and debug operations

**User Impact:**
- Users must manually kill PlatformIO on network issues
- CI/CD pipelines can hang indefinitely
- Poor user experience with no timeout feedback

## Affected Code

### Files with Missing Timeouts

**platform.py:**
- Line 175: `subprocess.run()` in `_upload_scp()`
- Line 238: `subprocess.run()` in `_upload_rsync()`
- Line 295: `subprocess.run()` in `_upload_ssh()`
- Line 337: `subprocess.run()` in `_run_remote_command()`

**platform-test-uploader.py:**
- Line 164: `subprocess.run()` in `upload_test_binary()` (SCP upload)
- Line 175: `subprocess.run()` in `upload_test_binary()` (chmod)
- Line 200: `subprocess.Popen()` in `execute_test_binary()` (needs special handling)

## Solution

Add configurable timeout to all subprocess operations with proper error handling.

### Implementation

#### 1. Define Default Timeout Constant

```python
# At top of platform.py
class SubprocessDefaults:
    """Default values for subprocess operations."""
    UPLOAD_TIMEOUT = 300  # 5 minutes
    TEST_TIMEOUT = 600    # 10 minutes (tests may run longer)
    DEBUG_TIMEOUT = 300   # 5 minutes
```

#### 2. Add Timeout to Subprocess Calls

```python
# Example: platform.py line 175 (_upload_scp)
timeout = env.GetProjectOption("upload_timeout", SubprocessDefaults.UPLOAD_TIMEOUT)

try:
    result = subprocess.run(cmd, capture_output=False, text=True, timeout=timeout)
except subprocess.TimeoutExpired:
    raise exception.PlatformioException(
        f"SCP upload timed out after {timeout} seconds. "
        f"Check network connection or increase timeout with 'upload_timeout' option in platformio.ini"
    )
```

#### 3. Configuration Options

Add to `platformio.ini`:
```ini
[env:raspberrypi_4b]
# Timeout for upload operations (seconds)
upload_timeout = 300

# Timeout for test operations (seconds)
test_timeout = 600

# Timeout for debug operations (seconds)
debug_timeout = 300
```

## Testing Requirements

**Test Cases:**
- [ ] Normal operations complete within default timeout
- [ ] Timeout properly triggered on slow connections
- [ ] Helpful error message displayed on timeout
- [ ] Custom timeout values respected
- [ ] No timeout on `Popen()` with streaming output (tests)
- [ ] All upload protocols tested: SCP, rsync, SSH
- [ ] Test upload and execution with timeouts
- [ ] Remote command execution with timeouts

**Simulated Timeout Testing:**
```bash
# Add artificial delay to test timeout
# In platformio.ini:
upload_flags = -o ConnectTimeout=1
upload_timeout = 5
upload_port = pi@nonexistent.host.local:/tmp/program

pio run --target upload
# Should timeout after 5 seconds with helpful error
```

## Acceptance Criteria

- [ ] All `subprocess.run()` calls have timeout parameter
- [ ] Configurable timeout options documented
- [ ] Timeout exceptions properly handled with user-friendly messages
- [ ] Default timeouts are reasonable (5-10 minutes)
- [ ] Tests pass with normal timeouts
- [ ] Timeout behavior tested and validated
- [ ] Documentation updated (README, UPLOAD.md, TESTING.md)
- [ ] No regression in existing functionality

## Implementation Details

### Files to Modify

1. **platform.py**
   - Add `SubprocessDefaults` class
   - Add timeout to 4 `subprocess.run()` calls
   - Add exception handling for `TimeoutExpired`
   - Extract timeout from project options

2. **platform-test-uploader.py**
   - Add `SubprocessDefaults` or import from platform
   - Add timeout to 2 `subprocess.run()` calls
   - Special handling for `Popen()` (consider per-line timeout or total timeout)
   - Add timeout configuration to `RemoteTestUploader`

3. **Documentation**
   - Update `docs/UPLOAD.md` with timeout options
   - Update `REMOTE_TESTING.md` with test timeout options
   - Add troubleshooting section for timeout issues

### Special Considerations

**For `subprocess.Popen()` (test execution):**
- Streaming output makes simple timeout tricky
- Consider using `threading.Timer` or `signal.alarm` (Unix)
- Or implement per-line timeout (fail if no output for N seconds)
- Or add overall test timeout option

**Recommended approach for tests:**
```python
# Option 1: Overall timeout with threading
import threading

def timeout_handler():
    process.kill()
    raise TimeoutError("Test execution timed out")

timer = threading.Timer(timeout, timeout_handler)
timer.start()
try:
    # Stream output...
finally:
    timer.cancel()
```

## Related Issues

- Depends on: #[Phase 1 Issue 1] - Command injection fixes (should be fixed first)
- Depends on: #[Phase 1 Issue 2] - Test uploader command injection
- Part of: Python Codebase Security Audit
- Related to: #[Phase 1 Issue 4] - Security documentation

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 1, Task 1.3)

**Affected Files:**
- `platform.py` (4 locations)
- `platform-test-uploader.py` (3 locations)

**External References:**
- [Python subprocess timeouts](https://docs.python.org/3/library/subprocess.html#subprocess.run)
- [TimeoutExpired exception](https://docs.python.org/3/library/subprocess.html#subprocess.TimeoutExpired)

## Estimated Effort

**2-3 hours** (implementation + testing + documentation)

## Implementation Notes

1. Fix command injection issues first (Issues #1, #2)
2. Add timeout constants/defaults
3. Update all subprocess calls
4. Add exception handling
5. Test with various timeout scenarios
6. Update documentation
7. Consider adding progress indicators for long operations

## Future Enhancement

Consider adding progress feedback for long-running operations:
- Show elapsed time during upload
- Display transfer rate/progress
- Warn user if operation is taking longer than expected

This can be deferred to Phase 3 (Optional Improvements).

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
**Analysis:** research/PYTHON_CODEBASE_ANALYSIS.md
