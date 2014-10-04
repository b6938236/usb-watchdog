usb-watchdog
============

USB device management to prevent against BadUSB attacks (Python 2.7)

usbwatchdog.py
--------------
Detect unknown USB devices: present the user the device identifiers and have them allow/reject the drive
Create an (un)trusted device store to recognize commonly used devices (on a per user basis)

USBDeview.cfg
-------------
Config file for USBDeview, adds the required command needed to launch usbwatchdog

Prerequisites
-------------
USBDeview - http://www.nirsoft.net/utils/usb_devices_view.html
This must be architecture specifc, otherwise you will be unable to (de)activate USB devices

usb.ids - http://www.linux-usb.org/usb.ids
For additional manufacturer info and device names

First-Run Warning
-----------------
Because unknown devices are automatically disabled, you may want to have an on-screen or secondary keyboard ready for when your USB keyboard is disabled.

Issues
------
USBDeview does not seem to launch commands when USB device is inserted on Windows 8.1 (64 bit).  The author has been contacted.
