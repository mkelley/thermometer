
Requires: python3-w1thermsensor

Notes
-----
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20

add "dtoverlay=w1-gpio" to /boot/config.txt
reboot
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls
cd 28-xxxx (change this to match what serial number pops up)
cat w1_slave

raspberrypi .../devices/28-021564e8b8ff $ cat w1_slave
24 01 4b 46 7f ff 0c 10 48 : crc=48 YES
24 01 4b 46 7f ff 0c 10 48 t=18250

The temperature is 18.250 C

-------------------------------------

Ambient probe ID: 021564e8b8ff
Waterproof probe ID: 0000075d075a
