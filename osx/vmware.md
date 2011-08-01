Headless mode
====

ctrl-option-clicking the Fusion  Dock icon and Force Quitting

vusb-analyzer
====

http://vusb-analyzer.sourceforge.net/tutorial.html

Add the new debug options to its .vmx config file

    monitor = "debug"
    usb.analyzer.enable = TRUE
    usb.analyzer.maxLine = 8192
    mouse.vusb.enable = FALSE

And remove the existing virtual USB device definitions:

    usb:0.present = "TRUE"
    usb:1.present = "TRUE"
    usb:1.deviceType = "hub"
    usb:0.deviceType = "mouse"

To reduce the size of the log, we can filter out only the USBIO log entries and compress them. This is optional, vusb-analyzer can also be run directly on the vmware.log file.

    grep USBIO vmware.log | gzip > windows-storage-read.log.gz