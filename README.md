# RPI Temp Monitor

## Setup

### Hardware

You will need:
- RPI Zero W with GPIO pins
- SD Card (4GB and above)
- DS18B20 temperature sensor
- 4.7K Ohm resistor
- Three GPIO jumper wires
- Breadboard

Wire up the sensor as shown in [this diagram](https://www.circuitbasics.com/wp-content/uploads/2016/03/Raspberry-Pi-DS18B20.png).

### Install OS

Use the [RPI Imager](https://www.raspberrypi.com/software/) to install Raspberry PI OS Lite (legacy or not doesn't matter) to an SD card.
During the process it will ask if you want to customize the OS settings. Do this and set up the following fields:
- Hostname
- Username/password
- Keyboard layout (set it to GB)
- SSH (enable and require password)

### Connecting to PI

Use the following command to list all the Raspberry PI devices on your network:
```bash
sudo nmap -sn 192.168.[subnet].0/24 | grep -i raspberry -B 2
```
Take the IP address from that command and plug it into ssh:
```bash
ssh [hostname]@[IP address]
```

### Software setup

On the PI, fetch the install script and run it.
```
wget https://raw.githubusercontent.com/Crozzers/rpi-temp-monitor/main/rpi-setup.sh
chmod +x rpi-setup.sh
sudo ./rpi-setup.sh
```
