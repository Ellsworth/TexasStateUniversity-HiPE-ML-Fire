# Intel Depth Sensor Jetson Nano Setup

## Sources

https://jetsonhacks.com/2019/12/22/install-realsense-camera-in-5-minutes-jetson-nano/
https://jfrog.com/connect/post/installing-cuda-on-nvidia-jetson-nano/
https://github.com/jetsonhacks/buildLibrealsense2TX/issues/13


## The Issue With Using Intel's Installation on Jetson

Intel does not provide binaries for arm64 therefore we must compile it.

---

## Install Git

Use the following command to install git

```bash
sudo apt install git
```

---

## Clone the repository

```bash
git clone https://github.com/JetsonHacksNano/installLibrealsense
cd installLibrealsense
```

## Install CUDA 

Execute the following commands to install the CUDA toolkit:

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/sbsa/cuda-ubuntu1804.pin

sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_arm64.deb

sudo dpkg -i cuda-repo-ubuntu1804-11-0-local_11.0.2-450.51.05-1_arm64.deb

sudo apt-key add /var/cuda-repo-ubuntu1804-11-0-local/7fa2af80.pub

sudo apt-get update

sudo apt-get -y install cuda
```

## Update .bashrc

Run the following command.

```bash
nano ~/.bashrc
```

Add the following to the end of the file and restart the terminal.

```bash
export CUDA_HOME=/usr/local/cuda-11.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.0/lib64:/usr/local/cuda-11.0/extras/CUPTI/lib64
export PATH=$PATH:$CUDA_HOME/bin
```

## Update CMakeLists.txt

Edit the file `~/librealsense/CMakeLists.txt` and add the following `set` line in between the `cmake_minimum_required` and `project` lines.

```bash
cmake_minimum_required(VERSION 3.21)
set(CMAKE_CUDA_COMPILER /usr/local/cuda/bin/nvcc) # Add this line
project(my_project_name CUDA)
```

## Build from source

Finally, we can build the RealSense SDK from source. Navigate back to where your orignally cloned the github repository and run:

```bash
./buildLibrealsense.sh
```

DISCLAIMER: This can take over an hour to complete