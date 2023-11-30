# RPI Temp Monitor

A super simple project for setting up a temperature monitor using a Raspberry Pi.

## Setup

### Hardware

You will need:
- RPi Zero W with GPIO pins
- SD Card (4GB and above)
- DS18B20 temperature sensor
- 4.7K Ohm resistor
- Three GPIO jumper wires
- Breadboard

Wire up the sensor as shown in [this diagram](https://www.circuitbasics.com/wp-content/uploads/2016/03/Raspberry-Pi-DS18B20.png) taken from
[this article](https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/).

### Install OS

Use the [RPI Imager](https://www.raspberrypi.com/software/) to install Raspberry Pi OS Lite (legacy or not doesn't matter) to an SD card.
During the process it will ask if you want to customize the OS settings. Do this and set up the following fields:
- Hostname
- Username/password
- Wifi (see [WiFi setup section](#wifi-setup))
- Keyboard layout (set it to GB)
- SSH (enable and require password)

### Connecting to Pi

Use the following command to list all the Raspberry Pi devices on your network:
```bash
sudo nmap -sn 192.168.[subnet].0/24 | grep -i raspberry -B 2
```
Take the IP address from that command and plug it into ssh:
```bash
ssh [username]@[IP address]
```

### WiFi Setup

The RPi imager gives you the option to configure 1 wifi network for the Pi. If you're deploying this in a location with a different WiFi network,
you'll want to configure an additional WiFi network so that you can SSH into it at that location.
Follow [these steps](https://github.com/Brisso/Raspberry-Pi-Documentation/blob/master/configuration/wireless/wireless-cli.md#adding-the-network-details-to-the-raspberry-pi)
from the RPI networking documentation. See also the section on
[adding multiple wireless networks](https://github.com/Brisso/Raspberry-Pi-Documentation/blob/master/configuration/wireless/wireless-cli.md#adding-multiple-wireless-network-configurations).

You can also use this command to add the network to your `wpa_supplicant` file:
```bash
echo "[wifi password]" | wpa_passphrase "[SSID]" | grep -v "#" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
```

### Software setup

On the Pi, fetch the install script and run it.
```
wget https://raw.githubusercontent.com/Crozzers/rpi-temp-monitor/main/rpi-setup.sh
chmod +x rpi-setup.sh
sudo ./rpi-setup.sh
```
This will update the system, install requirements, fetch the monitoring script and modify `/etc/rc.local` to launch the script on boot.
