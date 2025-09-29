#!/bin/bash
# updater.sh - Chomu auto-updater script
# Checks for updates from the official GitHub repo and updates if a new version is available.


REPO="gl1tch0x1/chomu"
LOCAL_VERSION=$(python3 setup.py --version 2>/dev/null)

# Use a GitHub token if available to avoid rate limits
if [ -n "$GITHUB_TOKEN" ]; then
    AUTH_HEADER="-H \"Authorization: token $GITHUB_TOKEN\""
    LATEST_VERSION=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/$REPO/releases/latest | grep '"tag_name"' | cut -d '"' -f4)
else
    LATEST_VERSION=$(curl -s https://api.github.com/repos/$REPO/releases/latest | grep '"tag_name"' | cut -d '"' -f4)
fi

if [ -z "$LATEST_VERSION" ]; then
    echo "[!] Could not fetch latest version info. Check your internet connection or GitHub API limits."
    exit 1
fi

echo "[*] Local version: $LOCAL_VERSION"
echo "[*] Latest version: $LATEST_VERSION"

if [ "$LOCAL_VERSION" = "$LATEST_VERSION" ]; then
    echo "[✓] Chomu is already up to date."
    exit 0
else
    echo "[!] Update available: $LOCAL_VERSION → $LATEST_VERSION"
    echo "[*] Stashing local changes (if any)..."
    git stash || true
    echo "[*] Fetching and resetting to latest main..."
    git fetch --all && git reset --hard origin/main
    echo "[*] Running install.sh to update dependencies and code..."
    ./install.sh
    echo "[✓] Chomu has been updated to version $LATEST_VERSION."
fi
