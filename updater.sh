#!/bin/bash
# updater.sh - Chomu auto-updater script
# Checks for updates from the official GitHub repo and updates if a new version is available.

REPO="gl1tch0x1/chomu"
LOCAL_VERSION=$(python3 setup.py --version 2>/dev/null)
LATEST_VERSION=$(curl -s https://api.github.com/repos/$REPO/releases/latest | grep '"tag_name"' | cut -d '"' -f4)

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
    echo "[*] Updating Chomu..."
    git fetch --all && git reset --hard origin/main
    ./install.sh
    echo "[✓] Chomu has been updated to version $LATEST_VERSION."
fi
