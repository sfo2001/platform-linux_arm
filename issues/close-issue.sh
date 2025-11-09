#!/bin/bash
# close-issue.sh - Helper script to close GitHub issues with assessments
# Usage: ./issues/close-issue.sh {issue-number} [label] [--dry-run]

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Parse arguments
ISSUE_NUMBER="$1"
LABEL="${2:-}"
DRY_RUN=false

if [[ "$2" == "--dry-run" ]] || [[ "$3" == "--dry-run" ]]; then
    DRY_RUN=true
fi

# Validate input
if [ -z "$ISSUE_NUMBER" ]; then
    echo -e "${RED}Error: Issue number required${NC}"
    echo "Usage: $0 {issue-number} [label] [--dry-run]"
    echo ""
    echo "Examples:"
    echo "  $0 32                    # Close issue #32 with default comment"
    echo "  $0 32 resolved           # Close and add 'resolved' label"
    echo "  $0 32 --dry-run          # Show command without executing"
    echo "  $0 32 duplicate --dry-run"
    exit 1
fi

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}Error: gh CLI not found${NC}"
    echo "Install with: https://cli.github.com/manual/installation"
    exit 1
fi

# Validate closure comment exists
COMMENT_FILE="issues/${ISSUE_NUMBER}/closure-comment.md"
if [ ! -f "$COMMENT_FILE" ]; then
    echo -e "${RED}Error: Closure comment not found${NC}"
    echo "Expected: $COMMENT_FILE"
    echo ""
    echo "Create the closure comment first:"
    echo "  mkdir -p issues/${ISSUE_NUMBER}"
    echo "  cp issues/TEMPLATE.md issues/${ISSUE_NUMBER}/assessment.md"
    echo "  # Edit assessment.md and create closure-comment.md"
    exit 1
fi

# Show what will be done
echo -e "${YELLOW}Preparing to close issue #${ISSUE_NUMBER}${NC}"
echo ""
echo "Comment file: $COMMENT_FILE"
if [ -n "$LABEL" ]; then
    echo "Label: $LABEL"
fi
echo ""

# Preview comment (first 10 lines)
echo -e "${YELLOW}Comment preview (first 10 lines):${NC}"
echo "---"
head -n 10 "$COMMENT_FILE"
echo "..."
echo "---"
echo ""

# Build gh command
GH_CMD="gh issue close ${ISSUE_NUMBER} --comment \"\$(cat ${COMMENT_FILE})\""
if [ -n "$LABEL" ]; then
    GH_CMD="${GH_CMD} --label ${LABEL}"
fi

# Show command
echo -e "${YELLOW}Command to execute:${NC}"
echo "$GH_CMD"
echo ""

# Execute or dry-run
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}[DRY-RUN] Would execute the above command${NC}"
    echo "Remove --dry-run to actually close the issue"
    exit 0
fi

# Confirm before closing
read -p "Close issue #${ISSUE_NUMBER}? [y/N] " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Cancelled${NC}"
    exit 0
fi

# Execute
echo -e "${GREEN}Closing issue #${ISSUE_NUMBER}...${NC}"
COMMENT_TEXT=$(cat "$COMMENT_FILE")

if [ -n "$LABEL" ]; then
    gh issue close "$ISSUE_NUMBER" --comment "$COMMENT_TEXT" --label "$LABEL"
else
    gh issue close "$ISSUE_NUMBER" --comment "$COMMENT_TEXT"
fi

# Verify closure
if gh issue view "$ISSUE_NUMBER" --json state --jq .state | grep -q "CLOSED"; then
    echo -e "${GREEN}✓ Issue #${ISSUE_NUMBER} closed successfully${NC}"
    echo ""
    echo "View on GitHub:"
    gh issue view "$ISSUE_NUMBER" --web 2>/dev/null || echo "  https://github.com/$(gh repo view --json nameWithOwner -q .nameWithOwner)/issues/${ISSUE_NUMBER}"
else
    echo -e "${RED}✗ Issue may not be closed, check manually${NC}"
    exit 1
fi
