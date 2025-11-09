# Issue Assessment Template

**Issue Number**: #[NUMBER]
**Title**: [ISSUE_TITLE]
**Assessment Date**: YYYY-MM-DD
**Assessor**: [NAME]
**Status**: [OPEN | RESOLVED | DUPLICATE | WONTFIX | NEEDS_INFO]

---

## Executive Summary

[1-2 paragraph overview: What is the issue? What's the current status? Key findings.]

**Quick Status**:
- **Original Problem**: [Brief description]
- **Current Status**: ✅ RESOLVED | ❌ OPEN | ⚠️ PARTIAL | 🔄 DUPLICATE | 🚫 WONTFIX
- **Resolution Date**: [If resolved]
- **Solution**: [One-line summary]

---

## Issue Background

### Original Problem

**Reporter**: [GitHub username if relevant]
**Date Reported**: [Original date]
**Environment**:
- PlatformIO version: [version]
- Host OS: [OS details]
- Target board: [board]
- Framework: [framework if relevant]

**Error/Behavior**:
```
[Error message or description of unexpected behavior]
```

**Impact**:
- [Who was affected?]
- [What use cases were blocked?]
- [How many users impacted?]

### Expected vs Actual Behavior

**Expected**:
[What should have happened]

**Actual**:
[What actually happened]

---

## Root Cause Analysis

### Investigation Summary

[What was investigated? What tools/methods were used?]

### Root Cause

[Technical explanation of why the issue occurred]

**Key Findings**:
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

**Evidence**:
- Code references: [file:line]
- Related issues: #[issue numbers]
- External references: [links]

---

## Solution

### Approach

[Describe the solution strategy]

**Implementation**:
- [What was changed?]
- [Which files were modified?]
- [What's the technical approach?]

### Code References

**Modified Files**:
- `[file path]:[line numbers]` - [description of change]
- `[file path]:[line numbers]` - [description of change]

**Commits**:
- [`[commit hash]`](link) - [commit message]
- [`[commit hash]`](link) - [commit message]

### Validation

**How was the fix validated?**
- [ ] Manual testing on [platform/board]
- [ ] Automated CI/CD tests
- [ ] Community testing
- [ ] Documentation updated

**Test Results**:
[Summary of test outcomes]

---

## Current Status

### What Works Now ✅

1. [Feature/capability 1]
2. [Feature/capability 2]
3. [Feature/capability 3]

### Remaining Limitations ⚠️

1. [Limitation 1 if any]
2. [Limitation 2 if any]

### Breaking Changes 🔴

[Any breaking changes introduced by the fix, or "None"]

---

## Comparison: Before vs After

| Aspect | Before | After |
|--------|--------|-------|
| [Aspect 1] | ❌ [Status] | ✅ [Status] |
| [Aspect 2] | ⚠️ [Status] | ✅ [Status] |
| [Aspect 3] | [Status] | [Status] |

---

## Documentation

**Updated Documentation**:
- [ ] README.md
- [ ] CONTRIBUTING.md
- [ ] Code comments
- [ ] Examples
- [ ] Research docs

**Documentation Links**:
- [Link to relevant docs]
- [Link to examples]

---

## Related Issues

**Duplicates**:
- #[issue] - [brief description]

**Related**:
- #[issue] - [brief description]

**Blocks/Blocked By**:
- Blocks: #[issue]
- Blocked by: #[issue]

---

## Recommendations

### For Users

**If experiencing this issue**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Workarounds** (if issue not resolved):
[Alternative approaches]

### For Maintainers

**Immediate Actions**:
- [ ] [Action 1]
- [ ] [Action 2]

**Future Actions**:
- [ ] [Future improvement 1]
- [ ] [Future improvement 2]

---

## References

**Research Documents**:
- [Link to research/analysis docs]

**Code References**:
- [Link to relevant code]

**External References**:
- [Links to external resources, discussions, specs]

**Related Commits**:
- [Commit hashes and links]

---

## Closure Decision

**Recommendation**: [CLOSE | KEEP_OPEN | NEEDS_MORE_INFO]

**Rationale**:
[Why should this issue be closed/kept open?]

**Closure Comment**:
[See closure-comment.md in this directory for the GitHub comment text]

---

**Assessment Status**:
- [ ] Issue analyzed
- [ ] Root cause identified
- [ ] Solution documented
- [ ] Testing validated
- [ ] Documentation updated
- [ ] Closure comment prepared
- [ ] Ready for closure

---

*Template Version: 1.0*
*Last Updated: 2025-11-09*
