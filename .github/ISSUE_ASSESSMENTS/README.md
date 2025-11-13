# Issue Assessments

This directory contains systematic assessments of issues cloned from the original `platformio/platform-linux_arm` repository.

## Purpose

When this repository was forked, many historical issues were cloned and needed thorough analysis to determine their current status. This directory provides structured documentation of:

- Issue root cause analysis
- Resolution status and validation
- Closure decisions and rationale
- Solution documentation for future reference

## Location

Moved from `issues/` (root) to `.github/ISSUE_ASSESSMENTS/` to:
- Clearly indicate this is internal project management
- Align with PlatformIO platform standards (no root-level issues/ directory)
- Maintain accessibility while decluttering the main repository view

## Contents

- `README-WORKFLOW.md` - Complete workflow documentation for assessing issues
- `TEMPLATE.md` - Assessment template for analyzing new issues
- `close-issue.sh` - Helper script for closing issues via GitHub CLI
- `{issue-number}/` - Per-issue assessment directories with:
  - `assessment.md` - Comprehensive analysis
  - `closure-comment.md` or `status-comment.md` - GitHub comment text
- `ASSESSMENT_SUMMARY.md` - Summary of all assessed issues

## Quick Reference

**View assessment workflow**: See `README-WORKFLOW.md`

**Assess a new issue**:
```bash
cd .github/ISSUE_ASSESSMENTS
mkdir {issue-number}
cp TEMPLATE.md {issue-number}/assessment.md
# Edit assessment, then create closure-comment.md
```

**Close an assessed issue**:
```bash
./close-issue.sh {issue-number}
# Or manually: gh issue close {issue-number} --comment "$(cat {issue-number}/closure-comment.md)"
```

## Why This Exists

This systematic assessment approach:
- **Documents resolution rationale** - Future contributors can understand why issues were closed
- **Validates fixes** - Each closure includes testing validation
- **Maintains transparency** - All decisions are documented and version-controlled
- **Enables batch processing** - Standardized format allows efficient issue triage

## Examples

See these directories for complete assessment examples:
- `20/` - Cross-compilation on macOS issue
- `32/` - Thread support assessment
- `38/` - WiringPi cross-compilation limitation

---

**Moved from**: `issues/` (repository root)
**Date**: 2025-11-13
**Reason**: Align with PlatformIO platform standards while preserving issue assessment work
