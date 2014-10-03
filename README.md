usb-watchdog
============

USB device management to prevent against BadUSB attacks

usbwatchdog.py
--------------
Detect unknown USB devices: present the user the device identifiers and have them allow/reject the drive
Create an (un)trusted device store to recognize commonly used devices (on a per user basis)

Prerequisites
-------------
USBDeview - http://www.nirsoft.net/utils/usb_devices_view.html
This must be architecture specifc, otherwise you will be unable to (de)activate USB devices

usb.ids - http://www.linux-usb.org/usb.ids
For additional manufacturer info and device names

First-Run Warning
-----------------
Because unknown devices are automatically disabled, you may want to have an on-screen or secondary keyboard ready for when your USB keyboard is disabled.
