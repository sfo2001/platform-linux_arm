# 🔄 Standardize Return Values Across Methods

## Priority
**P2 - Nice to Have** (Optional Improvement)

## Labels
`refactoring`, `consistency`, `P2`, `enhancement`

## Summary

Standardize return values across upload/test methods for consistency. Some methods return `0`, others return `result.returncode`, creating confusion.

## Problem

**Inconsistent returns:**
```python
# Some methods return 0
def _upload_scp(...):
    # ...
    return 0  # Always 0, even if result.returncode != 0

# Others return actual exit code
def _run_remote_command(...):
    result = subprocess.run(cmd)
    return result.returncode
```

## Solution

**Always return exit code:**
```python
def _upload_scp(...):
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise exception.PlatformioException(...)
    return 0  # Or return result.returncode

# Or use consistent pattern:
def _upload_scp(...):
    result = subprocess.run(cmd, check=True)  # Raises on error
    return 0
```

## Acceptance Criteria

- [ ] All methods return consistent values
- [ ] Documentation clarifies return value conventions
- [ ] Tests verify return values
- [ ] No functional regressions

## Estimated Effort

**2 hours**

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 3, Task 3.2)

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
