usb-watchdog
============

USB device management to prevent against BadUSB attacks (Python 2.7)

usbwatchdog.py
--------------
Detect unknown USB devices: present the user the device identifiers and have them allow/reject the drive

Create an (un)trusted device store to recognize commonly used devices (on a per user basis)

USBDeview.cfg
-------------
Config file for USBDeview, adds the required command needed to launch usbwatchdog.py

usbwatchdog-1.1.zip
-------------------
py2exe compiled script, unzip and drop the architecture specific version of USBDeview.

usb.ids ver 2014.08.25, usbdeview.cfg provided within archive

Config file has been updated to launch usbwatchdog.exe instead of .py

Prerequisites
-------------
USBDeview - http://www.nirsoft.net/utils/usb_devices_view.html

This must be architecture specific, otherwise you will be unable to (de)activate USB devices

usb.ids - http://www.linux-usb.org/usb.ids

For additional manufacturer info and device names

Installation
------------
Copy usbwatchdog.py, USBDeview.exe, USBDeview.cfg, and usb.ids into the same folder.

The config file will be suitable if you have added python to your system path, else you need to edit it to reflect python's location.

Because USBDeview.exe needs Administrator privileges to enable and disable devices, usbwatchdog.py also needs to be ran as administrator.

Issues
------
USBDeview does not seem to launch commands when USB device is inserted on Windows 8.1 (64 bit).  The author has been contacted.
