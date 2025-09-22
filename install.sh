#!/bin/bash
set -e

echo "[*] Checking Python3 installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-venv python3-pip
fi

echo "[*] Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "[*] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[*] Installing Chomu globally..."
sudo python3 setup.py install

echo "[*] Cleaning up..."
deactivate

echo "[*] Installation complete!"
echo "You can now run the tool by typing: chomu"
