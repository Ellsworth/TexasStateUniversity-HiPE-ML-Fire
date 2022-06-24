# Packaging ROS2

## Building

Clone this repository to download the `src` folding and the required
config files.

### Grab the repo

`git clone https://github.com/Ellsworth/TexasStateUniversity-HiPE-ML-Fire.git`

### Build the ROS2 Package

`make buildfull`

After performing any code modifications, it is highly reccomended to run
`make clean` to remove any build artifacts. On buildtime, ROS generates several files that reference the directory of files within the project.

## Running

Several projects are implemented within this repo. The `make` command may be used to run one of the ROS2 interfaces.

* `build` - Builds py_pubsub;
* `buildall` - Builds py_pubsub and float_package,
* `talker` - Send BME680 data to the ROS2 interface.
* `listener` - Receive BME680 from the ROS2 interface and display to screen.
* `clean` - 