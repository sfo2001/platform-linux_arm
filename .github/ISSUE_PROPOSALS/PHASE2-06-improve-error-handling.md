# 🔍 Improve Error Handling Specificity

## Priority
**P1 - High Priority** (Code Quality & Reliability)

## Labels
`enhancement`, `error-handling`, `P1`, `code-quality`

## Summary

Replace generic `except Exception` with specific exception types for better error diagnosis and debugging.

## Problem

**platform-test-uploader.py:255**
```python
except Exception as e:
    print(f"\nERROR: {str(e)}", file=sys.stderr)
    return 1
```

**Issues:**
- Catches all exceptions (even `KeyboardInterrupt`, `SystemExit`)
- No stack trace for debugging
- Hard to diagnose root cause

## Solution

```python
except subprocess.CalledProcessError as e:
    print(f"\nERROR: Remote command failed: {e}", file=sys.stderr)
    print(f"Exit code: {e.returncode}", file=sys.stderr)
    return e.returncode
except subprocess.TimeoutExpired as e:
    print(f"\nERROR: Operation timed out after {e.timeout} seconds", file=sys.stderr)
    return 1
except OSError as e:
    print(f"\nERROR: File operation failed: {e}", file=sys.stderr)
    return 1
except KeyboardInterrupt:
    print("\nERROR: Operation cancelled by user", file=sys.stderr)
    return 130
except Exception as e:
    print(f"\nERROR: Unexpected error: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    return 1
```

## Benefits

✅ Better error messages
✅ Appropriate exit codes
✅ Stack traces for unexpected errors
✅ Won't catch `KeyboardInterrupt`/`SystemExit`
✅ Easier debugging

## Acceptance Criteria

- [ ] All `except Exception` reviewed
- [ ] Specific exceptions caught where possible
- [ ] Stack traces for unexpected errors
- [ ] Appropriate exit codes
- [ ] Tests for error cases
- [ ] Code reviewed

## Estimated Effort

**1-2 hours**

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 2, Task 2.6)

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
