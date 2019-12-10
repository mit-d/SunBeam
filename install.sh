#!/bin/sh
echo "This script will set up the raspberry pi as SUNBEAM"

[ "$UID" -eq 0 ] || exec sudo "$0" "$@"

echo "Installing binaries to /usr/local/bin" && stow -Rt /usr/local/bin bin
echo "Installing files to /usr/local/share" && stow -Rt /usr/local/share share
echo "Installing systemd services to /etc/systemd/system" && stow -Rt /etc/systemd/system system

