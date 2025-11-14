# ✅ Add Unit Tests for Python Codebase

## Priority
**P2 - Nice to Have** (Optional Improvement)

## Labels
`testing`, `P2`, `enhancement`

## Summary

Add unit test infrastructure and tests for Python modules to improve code quality, catch regressions, and enable confident refactoring.

## Current State

- **No unit tests** for Python code
- Manual testing only
- Refactoring is risky (no safety net)
- Hard to verify bug fixes

## Proposed Solution

### Test Infrastructure

```bash
# Install testing tools
pip install pytest pytest-cov pytest-mock

# Run tests
pytest tests/
pytest --cov=. --cov-report=html
```

### Test Coverage Goals

**Priority 1:**
- `ssh_utils.py` - 90%+ (if created in Phase 2)
- `platform.py` - Core methods (50%+)

**Priority 2:**
- `platform-test-uploader.py` - Key methods (50%+)

**Priority 3:**
- Framework scripts - Basic smoke tests

### Example Tests

```python
# tests/test_ssh_utils.py
import pytest
from ssh_utils import parse_upload_port, SSHConnectionConfig

def test_parse_upload_port_full():
    user, host, path = parse_upload_port("pi@raspberrypi:/tmp/prog")
    assert user == "pi"
    assert host == "raspberrypi"
    assert path == "/tmp/prog"

def test_parse_upload_port_defaults():
    user, host, path = parse_upload_port("192.168.1.100")
    assert user == "pi"  # default
    assert host == "192.168.1.100"
    assert path == "/tmp/program"  # default

def test_ssh_config_validation():
    with pytest.raises(ValueError):
        config = SSHConnectionConfig("", "host")
        config.validate()
```

```python
# tests/test_platform.py
import pytest
from unittest.mock import Mock, patch
from platform import Linux_armPlatform

def test_is_native_on_arm():
    with patch('platform.get_systype', return_value='linux_arm'):
        assert Linux_armPlatform._is_native() == True

def test_is_native_on_x86():
    with patch('platform.get_systype', return_value='linux_x86_64'):
        assert Linux_armPlatform._is_native() == False

def test_parse_upload_port_invalid():
    platform = Linux_armPlatform()
    env = Mock()
    with pytest.raises(Exception):
        platform._parse_upload_port(None, env)
```

## Acceptance Criteria

- [ ] pytest infrastructure set up
- [ ] Tests for ssh_utils (if created) - 90%+
- [ ] Tests for platform core methods - 50%+
- [ ] Tests for test uploader - 50%+
- [ ] CI/CD integration
- [ ] Coverage reports generated
- [ ] Documentation on running tests

## Benefits

✅ Catch regressions early
✅ Confident refactoring
✅ Living documentation
✅ Faster debugging
✅ Better code quality

## Estimated Effort

**8-10 hours**

- Infrastructure: 1 hour
- ssh_utils tests: 2 hours
- platform.py tests: 3 hours
- test-uploader tests: 2 hours
- CI/CD integration: 1 hour
- Documentation: 1 hour

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 3, Task 3.1)

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
