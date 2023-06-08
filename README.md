# Overview

This is a rough guide to capturing paired joycon events using [python-evdev](https://python-evdev.readthedocs.io/) on your [Raspberry Pi](https://raspberrypi.com/). I tested this on a the latest Raspberry Pi OS and on a Raspberry Pi 4 Model B. When I get my hands on a clean device, I'll do a more detailed step-by-step guide.

## TL;DR

You will need to install/setup `cmake`, `python3`, `python-evdev`, `hid-nintendo`, `joycond`. When you pair your joycons, two new entries - Joycon (L) / (R) - will be created in `/dev/input`. You can then simultaneously press two triggers which should create another input called Joycon (Combined).

## Rough guide

1. Update packages:

```bash
sudo apt update && sudo apt upgrade
```

2. Install cmake

```bash
sudo apt install cmake
```

3. Install python3

```bash
sudo apt install python3
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.9 /usr/bin/python
```

4. Update your kernel headers.

```bash
sudo apt install raspberrypi-kernel raspberrypi-kernel-headers
```

5. Install [python-evdev](https://python-evdev.readthedocs.io/en/latest/install.html)

```bash
sudo apt install evdev
python list_devices.py # check if evdev works
```

6. Install [dkms-hid-nintendo](https://github.com/nicman23/dkms-hid-nintendo) from source

```bash
git clone https://github.com/nicman23/dkms-hid-nintendo
cd dkms-hid-nintendo

sudo dkms add .
sudo dkms build nintendo -v 3.2
sudo dkms install nintendo -v 3.2
cd ..
```

7. Install [joycond](https://github.com/DanielOgorchock/joycond/) from source

```bash
sudo apt install libevdev-dev libudev-dev
git clone https://github.com/DanielOgorchock/joycond/
cd joycond
cmake .
sudo make install
sudo systemctl enable --now joycond
cd ..
```

8. Pair your joycons. Run `python list_devices.py` again to check if they were paired successfully. Press a single trigger on both joycons to combine them into a new input. Run `python list_devices.py` again to check for the new input.

9. The new combined joycon will have a slightly different mapping. Run `python joycon.py` to test the button mappings. You may have to change the device name at the top of the file.

## TODO

1. Calibration

2. Step-by-step guide from clean install