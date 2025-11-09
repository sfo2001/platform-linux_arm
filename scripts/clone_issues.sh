#!/bin/bash

# === CONFIGURATION ===
# Set the source and target repositories
SOURCE_REPO="platformio/platform-linux_arm"  # Replace with the original repo
TARGET_REPO="sfo2001/platform-linux_arm" # Replace with your fork

# === FETCH AND CREATE ISSUES ===
echo "Fetching open issues from $SOURCE_REPO..."

# Use gh to list issues, get JSON, and process each one
gh issue list -R "$SOURCE_REPO" --state open --limit 1000 --json number,title,body,labels | jq -c '.[]' | while read -r issue; do
    # Extract issue details using jq
    TITLE=$(echo "$issue" | jq -r '.title')
    BODY=$(echo "$issue" | jq -r '.body')
    LABELS=$(echo "$issue" | jq -r '[.labels[].name] | join(",")')

    # Check if the issue has any labels
    if [ "$LABELS" = "" ]; then
        LABEL_ARG=""
    else
        LABEL_ARG="--label \"$LABELS\""
    fi

    # Create the issue in the target repository
    echo "Creating issue: $TITLE"
    # Use eval to handle the optional label argument correctly
    eval "gh issue create -R \"$TARGET_REPO\" --title \"$TITLE\" --body \"$BODY\" $LABEL_ARG"
done

echo "Issue cloning process completed!"
