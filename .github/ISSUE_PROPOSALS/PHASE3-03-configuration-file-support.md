# ⚙️ Add Configuration File Support

## Priority
**P2 - Nice to Have** (Optional Enhancement)

## Labels
`feature`, `enhancement`, `P2`

## Summary

Add support for `.platform-linux_arm.ini` configuration file to set global defaults (SSH timeout, default user, etc.) reducing platformio.ini duplication across projects.

## Motivation

**Current:** Must repeat configuration in every project
```ini
# Project 1: platformio.ini
[env]
upload_timeout = 300
upload_user = pi
upload_ssh_port = 22

# Project 2: platformio.ini
[env]
upload_timeout = 300  # Duplicated!
upload_user = pi      # Duplicated!
upload_ssh_port = 22  # Duplicated!
```

**Proposed:** Global defaults + per-project overrides
```ini
# ~/.platformio/.platform-linux_arm.ini (global)
[defaults]
upload_timeout = 300
upload_user = pi
upload_ssh_port = 22
test_timeout = 600

# Project: platformio.ini (only overrides)
[env:raspberrypi_4b]
upload_user = admin  # Override global default
```

## Implementation

1. Check for config file in:
   - `~/.platformio/.platform-linux_arm.ini`
   - `./.platform-linux_arm.ini` (project-local)

2. Load defaults from config

3. Allow platformio.ini to override

## Benefits

✅ DRY across projects
✅ User-specific defaults
✅ Less boilerplate

## Acceptance Criteria

- [ ] Config file loading implemented
- [ ] Defaults properly merged with project config
- [ ] Documentation added
- [ ] Example config provided
- [ ] Backward compatible

## Estimated Effort

**3 hours**

## References

**Analysis Report:** `research/PYTHON_CODEBASE_ANALYSIS.md` (Phase 3, Task 3.3)

---

**Created from:** Python Codebase Analysis Report (2025-11-14)
