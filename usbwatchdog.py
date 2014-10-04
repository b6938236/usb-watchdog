# @author b6938236
# @date 2014.10.04
# @version 1.1

import sys, os
#import xml.etree.ElementTree #for py2exe, otherwise not needed
import xml.etree.cElementTree as ET
		
def checkdevice(vid,pid,device_name,device_type,service_name,vendor_name,product_name,disablefirst):
	#build string, because instance ID is not provided by the program
	usb_instance = str(vid) + ";"
	usb_instance += str(pid) + ";"
	usb_instance += str(device_name) + ";"
	usb_instance += str(device_type) + ";"
	usb_instance += str(service_name) + ";"
	usb_instance += str(vendor_name) + ";"
	usb_instance += str(product_name) + "\n"
	
	db_devices = open("devices.db","r")
	for line in db_devices:
		if line == ("A;" + usb_instance): #check if device is in the trusted list
				db_devices.close()
				return
		elif line == ("R;" + usb_instance): #check if device is in the untrusted list
				os.system("USBDeview.exe /disable_by_pid {0};{1}".format(vid,pid))
				print "WARNING: USB DEVICE ON BLOCKLIST HAS BEEN DISCONNECTED"
				print "Device ID: {0};{1}".format(vid,pid)
				print "======================================================"
				#Future: Give the user the option to (t)emporarily or (p)ermanently ignore?
				return
	db_devices.close()
		
	if (disablefirst):
		os.system("USBDeview.exe /disable_by_pid {0};{1}".format(vid,pid))
	print "New USB device identifies itself as \"{0}\"".format(device_name)
	print "This device identifies as a {0} device".format(device_type)
	print "usb.ids identifies this device as a {0} from {1}".format(product_name,vendor_name)
	response = raw_input("Do you want to (A)ccept or (R)eject this device?")
	response = response[:1].lower()
	if (response == "a" and disablefirst): #device was disabled, user wants it back
		os.system("USBDeview.exe /enable_by_pid {0};{1}".format(vid,pid))
	if (response == "r" and not disablefirst): #user doesn't want device and it wasn't disabled
		os.system("USBDeview.exe /disable_by_pid {0};{1}".format(vid,pid))
	permanent = raw_input("Do you want to automatically apply this decision to this device in the future? (Yes/No)")
	permanent = permanent[:1].lower()
	if permanent == "y": #store the device string in the database
		if response == "a":
			usb_instance = "A;" + usb_instance
		else:
			usb_instance = "R;" + usb_instance
		db_devices = open("devices.db","a")
		db_devices.write(usb_instance)
		db_devices.close()
	
def sweep(disablefirst):
	#generate XML report of all currently connected devices, then check each one
	os.system("USBDeview.exe /sxml sweep.xml /DisplayDisconnected 0")
	tree = ET.parse("sweep.xml")
	root = tree.getroot()
	usbs = []
	if (disablefirst):
		for leaf in root:
			checkdevice(leaf[11].text,leaf[12].text,leaf[0].text,leaf[2].text,leaf[22].text,leaf[19].text,leaf[20].text, True)
	else:
		for leaf in root:
			checkdevice(leaf[11].text,leaf[12].text,leaf[0].text,leaf[2].text,leaf[22].text,leaf[19].text,leaf[20].text, False)
		
def man():
	print "Prevents against unwanted or malicious USB devices"
	print "Note: This program WILL NOT patch USB firmwares for compromised devices"
	print
	print "USBWatchdog.exe"
	print "     Displays this help dialogue"
	print
	print "USBWatchdog.exe --device [arguments]"
	print "     The --device flag should only be used by USBDeview"
	print "     Arguments:"
	print "     vid - Vendor ID"
	print "     pid - Product ID"
	print "     device_name - Device name, as reported by the device"
	print "     device_type - Device type, as reported by the device"
	print "     service_name - Service name, as reported by the OS"
	print "     vendor_name - Vendor name, translated by usb.ids"
	print "     product_name - Product name, translated by usb.ids"
	print
	print "USBWatchdog.exe --sweep"
	print "     Checks all currently connected USB devices against the database"
	print "     Will disable unknown devices first, then reactivate after user allows them"
	print
	print "USBWatchdog.exe --firstrun"
	print "     Same as --sweep, but asks user about device before disabling them"
	print "     Used to generate trusted database and keeps input devices from being disabled"
	print
	print "USB Watchdog is provided by b6938236"
	print "https://github.com/b6938236"
	print 
	print "USBDeview and related files are provided by NirSoft"
	print "http://www.nirsoft.net/utils/usb_devices_view.html"
	print 
	print "usb.ids is provided by Stephen J. Gowdy <linux.usb.ids@gmail.com>"
	print "http://www.linux-usb.org/usb.ids"

if len(sys.argv) == 1:
	man()
elif sys.argv[1] == "--sweep": #Disable unknown devices first, then re-enable them after user OK
	sweep(True) 
elif sys.argv[1] == "--firstrun": #Disable unknown devices after user has rejected them
	sweep(False) 
elif sys.argv[1] == "--device": #New device has been inserted, USBDeview is passing along details
	checkdevice(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7], sys.argv[8],True)
else:
	man()