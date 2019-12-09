#!/bin/sh
echo "This script will set up the raspberry pi as SUNBEAM"

echo "Installing binaries to /usr/local/bin" && stow -Rt /usr/local bin
echo "Installing systemd services to /etc/systemd/system" && stow -Rt /etc/systemd/system system
# ln -sT  monitor.py /usr/local/bin/monitor.py ||
# ln -sT  ./etc/systemd/system/monitor_voltage.service /etc/systemd/system/monitor_voltage.service ||
# ln -sT  ./etc/systemd/system/sunbeam_php_server.service /etc/systemd/system/sunbeam_php_server.service

