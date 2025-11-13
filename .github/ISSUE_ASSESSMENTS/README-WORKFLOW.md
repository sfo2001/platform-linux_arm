# Issues Directory

This directory contains assessments and closure documentation for issues cloned from the original `platformio/platform-linux_arm` repository.

## Purpose

When this repository was forked and issues were cloned, many historical issues needed analysis to determine:
- Current status (resolved, open, duplicate, wontfix)
- Root cause (if resolved)
- Solution documentation
- Closure decision and rationale

This directory provides a structured approach to assess each issue systematically.

## Directory Structure

```
issues/
├── README.md                    # This file
├── TEMPLATE.md                  # Assessment template for analyzing issues
├── close-issue.sh              # Helper script for closing issues with gh CLI
├── {issue-number}/             # Per-issue directories
│   ├── assessment.md           # Full assessment (root cause, solution, testing)
│   └── closure-comment.md      # Concise comment for GitHub issue closure
```

## Workflow

### 1. Assess an Issue

For each open issue:

1. **Create issue directory**:
   ```bash
   mkdir -p issues/{issue-number}
   ```

2. **Copy template** and fill in analysis:
   ```bash
   cp issues/TEMPLATE.md issues/{issue-number}/assessment.md
   # Edit assessment.md with issue details
   ```

3. **Create closure comment** (concise version for GitHub):
   ```bash
   # Edit issues/{issue-number}/closure-comment.md
   # Focus on: Summary, Solution, Validation, Status
   ```

4. **Commit assessment**:
   ```bash
   git add issues/{issue-number}/
   git commit -m "docs(issues): assess issue #{issue-number}"
   ```

### 2. Close the Issue

Once assessment is complete and resolution verified:

**Option A: Using helper script** (recommended):
```bash
./issues/close-issue.sh {issue-number}
```

**Option B: Manual gh command**:
```bash
gh issue close {issue-number} --comment "$(cat issues/{issue-number}/closure-comment.md)"
```

**Option C: GitHub web UI**:
- Navigate to issue on GitHub
- Copy content from `issues/{issue-number}/closure-comment.md`
- Paste as comment and close issue

### 3. Track Progress

Keep a log of assessed issues:

```bash
# List all cloned issues
gh issue list --state all --limit 100

# Count resolved vs open
ls -d issues/*/ | wc -l  # Assessed issues
gh issue list --state open | wc -l  # Remaining open
```

## Assessment Template Fields

The `TEMPLATE.md` provides structure for:

1. **Executive Summary** - Quick status and key findings
2. **Issue Background** - Original problem, environment, impact
3. **Root Cause Analysis** - Technical investigation and findings
4. **Solution** - Implementation approach, code changes, validation
5. **Current Status** - What works now, remaining limitations
6. **Comparison** - Before vs after table
7. **Documentation** - Updated docs and references
8. **Related Issues** - Duplicates, dependencies
9. **Recommendations** - For users and maintainers
10. **Closure Decision** - Recommendation and rationale

## Example: Issue #32

**Directory**: `issues/32/`

**Files**:
- `assessment.md` - Full analysis (270 lines)
- `closure-comment.md` - Concise GitHub comment (80 lines)

**Usage**:
```bash
# Close issue #32
gh issue close 32 --comment "$(cat issues/32/closure-comment.md)"

# Or with script
./issues/close-issue.sh 32
```

**Status**: ✅ RESOLVED (cross-compilation now works on all platforms)

## Helper Script Usage

The `close-issue.sh` script automates closing issues:

```bash
# Basic usage
./issues/close-issue.sh {issue-number}

# With custom label
./issues/close-issue.sh {issue-number} resolved

# Dry-run (show command without executing)
./issues/close-issue.sh {issue-number} --dry-run
```

**What it does**:
1. Validates that `issues/{issue-number}/closure-comment.md` exists
2. Uses `gh issue close` with the closure comment
3. Optionally adds labels (resolved, duplicate, wontfix, etc.)
4. Confirms closure success

## Issue Status Categories

Use these categories when assessing issues:

- **✅ RESOLVED** - Issue fixed, solution implemented and validated
- **🔄 DUPLICATE** - Duplicate of another issue (link to canonical issue)
- **🚫 WONTFIX** - Valid issue but won't be fixed (explain rationale)
- **⚠️ PARTIAL** - Partially resolved with known limitations
- **❌ OPEN** - Still needs work, not resolved
- **ℹ️ NEEDS_INFO** - Insufficient information to assess

## Best Practices

1. **Be thorough but concise** - Full analysis in assessment.md, summary in closure-comment.md
2. **Link to evidence** - Code references, commits, test results
3. **Document workarounds** - Even if issue resolved, users may need migration steps
4. **Reference research** - Link to research/ docs if available
5. **Test before closing** - Validate the fix actually works
6. **Update INDEX** - If issue relates to roadmap phases, update research/00-INDEX.md

## Tips for Efficiency

**Batch assessment**:
```bash
# List all open issues
gh issue list --state open

# Create directories for batch processing
for i in 33 34 35; do mkdir -p issues/$i; done

# Use template
for i in 33 34 35; do cp issues/TEMPLATE.md issues/$i/assessment.md; done
```

**Quick status check**:
```bash
# Find issues with assessments
find issues/ -name "assessment.md" -exec dirname {} \;

# Find issues ready to close (have closure-comment.md)
find issues/ -name "closure-comment.md" -exec dirname {} \;
```

**Bulk close** (use with caution):
```bash
# Close all assessed issues in a range
for i in {32..40}; do
    if [ -f "issues/$i/closure-comment.md" ]; then
        ./issues/close-issue.sh $i
    fi
done
```

## Questions?

- **Template unclear?** - See `issues/32/assessment.md` for a complete example
- **gh CLI issues?** - Check `gh auth status` and repository access
- **Need help?** - Reference this README and TEMPLATE.md structure

---

**Last Updated**: 2025-11-09
**Issues Assessed**: 1 of N (Issue #32 complete)
**Workflow Version**: 1.0
