#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

# === CONFIGURATION ===
SOURCE_REPO="platformio/platform-linux_arm"
TARGET_REPO="sfo2001/platform-linux_arm"
DRY_RUN="${DRY_RUN:-false}"  # Set DRY_RUN=true to test without creating

# === VALIDATE REQUIREMENTS ===
if ! command -v gh &> /dev/null; then
    echo "Error: gh CLI is not installed"
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed"
    exit 1
fi

# === FETCH AND CREATE ISSUES ===
echo "Fetching open issues from $SOURCE_REPO..."

gh issue list -R "$SOURCE_REPO" --state open --limit 1000 --json number,title,body,labels | \
jq -c '.[]' | while IFS= read -r issue; do
    # Extract issue details
    NUMBER=$(echo "$issue" | jq -r '.number')
    TITLE=$(echo "$issue" | jq -r '.title')
    BODY=$(echo "$issue" | jq -r '.body // ""')  # Handle null body
    LABELS=$(echo "$issue" | jq -r '[.labels[].name] | join(",")')

    # Check if issue already exists (search by title prefix)
    SEARCH_TITLE="[#$NUMBER]"
    if gh issue list -R "$TARGET_REPO" --search "\"$SEARCH_TITLE\" in:title" --json title --limit 1 | jq -e '.[0]' > /dev/null 2>&1; then
        echo "⏭️  Skipping #$NUMBER (already exists): $TITLE"
        continue
    fi

    # Prepend original issue reference to body
    FULL_BODY="**Cloned from original repository: $SOURCE_REPO#$NUMBER**

$BODY"

    echo "📝 Creating issue #$NUMBER: $TITLE"

    if [ "$DRY_RUN" = "true" ]; then
        echo "   [DRY RUN] Would create with labels: $LABELS"
        continue
    fi

    # Create issue using stdin for body (avoids escaping issues)
    if [ -n "$LABELS" ]; then
        echo "$FULL_BODY" | gh issue create -R "$TARGET_REPO" \
            --title "[#$NUMBER] $TITLE" \
            --body-file - \
            --label "$LABELS" || echo "⚠️  Warning: Failed to create issue #$NUMBER"
    else
        echo "$FULL_BODY" | gh issue create -R "$TARGET_REPO" \
            --title "[#$NUMBER] $TITLE" \
            --body-file - || echo "⚠️  Warning: Failed to create issue #$NUMBER"
    fi

    # Rate limiting: small delay between requests
    sleep 0.5
done

echo "✅ Issue cloning process completed!"
