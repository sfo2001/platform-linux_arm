# 🔧 Extract Magic Values to Constants

## Priority
**P1 - High Priority** (Code Quality)

## Labels
`refactoring`, `code-quality`, `P1`, `enhancement`

## Summary

Extract hardcoded magic values (strings, numbers) to named constants for better maintainability and single source of truth.

## Examples

### SSH Defaults (appears 20+ times)
```python
# Current: Scattered throughout code
ssh_port = "22"
user = "pi"
path = "/tmp/program"
test_path = "/tmp/test_program"

# Proposed: Centralized
class SSHDefaults:
    PORT = "22"
    USER = "pi"
    UPLOAD_PATH = "/tmp/program"
    TEST_PATH = "/tmp/test_program"
    TIMEOUT = 300  # seconds
```

### Upload Protocols
```python
class UploadProtocol:
    SCP = "scp"
    RSYNC = "rsync"
    SSH = "ssh"
    MANUAL = "manual"

# Usage
if protocol == UploadProtocol.SCP:
    ...
```

### Test Transport
```python
class TestTransport:
    SSH = "ssh"
    MANUAL = "manual"
```

### Exit Code Markers
```python
# platform-test-uploader.py
class TestConstants:
    EXIT_CODE_MARKER = "__EXIT_CODE__:"
    DEFAULT_TIMEOUT = 600
```

## Benefits

✅ Single source of truth
✅ Easy to find and update defaults
✅ Self-documenting code
✅ Type-safe with enums/constants
✅ IDE autocomplete

## Acceptance Criteria

- [ ] All magic strings extracted to constants
- [ ] All magic numbers extracted to constants
- [ ] Constants grouped logically in classes
- [ ] Constants documented
- [ ] No functional changes
- [ ] Tests pass

## Estimated Effort

**2 hours**

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 2, Task 2.5)

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
