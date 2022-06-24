# Jetson Nano Setup

## Custom Xubuntu Setup

### Install Custom Xubuntu 20.04 Image

Download the Xubuntu 20.04 image. This is a custom Xubuntu 20.04 install created by Chris Mitchells. This is required a NVIDIA does not currently provide a Ubuntu 20.04 install for the Jetson Nano.

[https://forums.developer.nvidia.com/t/xubuntu-20-04-focal-fossa-l4t-r32-3-1-custom-image-for-the-jetson-nano/121768](https://forums.developer.nvidia.com/t/xubuntu-20-04-focal-fossa-l4t-r32-3-1-custom-image-for-the-jetson-nano/121768)

### Extract Image

* On Unix, the command `tar -xf Xubuntu-20.04-l4t-r32.3.1.tar.tbz2`

* On Windows, use 7-Zip or WinRar to extract .img file.

### Download Balena Etcher

Download and install Balena Ethcher to the flash SD Card. Other programs will work as well however this is the one we used.

[https://www.balena.io/etcher/](https://www.balena.io/etcher/)

### Flash Custom Xubuntu Image with Balena

Flash image on to SD card this will get the SD card ready to be used. We recommend 64GB SD cards for optimal storage.

---
## Getting Ready for Install

### Getting the Jetson Ready

The SD card slot is located on the bottom side of the Jetson Daughter board. It is inserted with the pins facing in the upwards direction.

Make sure to plug in the Jetson using a barrel jack connector for optimal power usage. The barrel jack connector requires the Jetson to close the jumper. These can be purchased online or with female-female jumper cables. A mouse and keyboard and monitor will also be needed for intial setup.

### Setting up Xubuntu

Follow the on screen instructions to setup the install. When prompted for the partition size, be sure that the default size is used.

Next is the power management config. The two options are MAX and 5W. The MAX setting with use aproximately 15W at max usage, whilst the 5W setting reduces the SOC's maximum clock speed and voltage to reduce the max power consumption to 5W.

### Fix date and time

The Jetson does not have an onboard clock configuration. We must fix this issue as it can cause problems with the browser and ROS. Follow the instructions below.

[https://github.com/justsoft/jetson-nano-date-sync](https://github.com/justsoft/jetson-nano-date-sync)

---