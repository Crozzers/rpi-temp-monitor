#!/bin/bash

# Updates
sudo apt update && sudo apt upgrade -y
# Disable bluetooth
sudo apt purge bluez -y
sudo apt autoremove -y

# Install pip
sudo apt install python3-pip -y
# Install thermal sensor lib
pip install w1thermsensor
# Enable w1 therm kernel modules
echo "dtoverlay=w1-gpio" | sudo tee -a /boot/config.txt

# Make program dir
mkdir -p ~/sensor && cd ~/sensor
# Fetch program
wget https://raw.githubusercontent.com/Crozzers/rpi-temp-monitor/main/temp-monitor.py

# Edit rc.local to add as startup script
echo "python $HOME/sensor/temp-monitor.py &" | sudo tee -a /etc/rc.local

sudo reboot
