#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
echo "Run this in WSL Ubuntu terminal. Script installs dependencies and runs buildozer setup.",
read -p "Press ENTER to continue or CTRL-C to abort..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3.11 python3.11-venv python3.11-dev build-essential git zip unzip libffi-dev libssl-dev libsqlite3-dev zlib1g-dev libbz2-dev libreadline-dev libncursesw5-dev libgdbm-dev libnss3-dev liblzma-dev openjdk-17-jdk
mkdir -p ~/projects
echo "Ensure your project is copied to ~/projects/Kilimo360_ready or edit script."
rm -rf ~/.buildozer ~/.android || true
echo "Create venv and install python packages"
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel cython packaging build appdirs jinja2 colorama
pip install kivy==2.2.0 kivymd==1.1.1 kivy_garden.mapview plyer buildozer python-for-android
echo "Run buildozer android setup now (may prompt)"
buildozer android setup || true
SDK_DIR="$HOME/.buildozer/android/platform/android-sdk"
if [ -d "$SDK_DIR" ]; then
    cd "$SDK_DIR" || true
    mkdir -p cmdline-tools
    shopt -s nullglob
    if compgen -G "cmdline-tools-*" > /dev/null; then
        mv cmdline-tools-* cmdline-tools/latest 2>/dev/null || true
    fi
    if [ ! -e "tools" ]; then ln -s cmdline-tools/latest tools || true; fi
fi
echo "Setup complete; edit buildozer.spec as needed and run: buildozer android debug"
