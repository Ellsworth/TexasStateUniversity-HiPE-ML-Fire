# ROS2 Foxy Fitzroy Installation

## Disclaimer

The following documentation and instructions are sourced from the link below, the offical ROS2 Foxy Documentation. Pieces have been taken out or changed to fit the needs of this project. If installation issues occur please visit the link below.

[https://docs.ros.org/en/foxy/Installation.html](https://docs.ros.org/en/foxy/Installation.html)

---

## Ubuntu Debian Installation

### Setup Sources

You will need to add the ROS2 apt repositories to your system. First make sure that the Ubuntu Universe repository is enabled by checking the output of this command.

```bash
apt-chace policy | grep universe
```

If you see a line similar to the following continue to the Install ROS2 Packages porition.

```bash
500 http://us.archive.ubuntu.com/ubuntu focal/universe amd64 Packages
    release v=20.04,o=Ubuntu,a=focal,n=focal,l=Ubuntu,c=universe,b=amd64
```

If you don't see an ouput line like the one aobve, then enable to Universe repository with these instructions.

```bash
sudo apt install software-properities-common
sudo add-apt-repository universe
```

Now add the ROS2 apt repository to your system.

```bash
sudo aptupdate && sudo apt install curl gnupg2 lsg-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Then add the repository to your sources list.

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

---

## Install ROS2 Packages

Update your apt repository caches after setting up the repositories. It is recommened to ensure your system is up to date before installing new packages.

```bash
sudo apt update
sudo apt upgrade
sudo apt install ros-foxy-desktop
```

---

## Environment Setup

Run the following command to edit the bashrc.

```bash
nano ~/.bashrc
```

Add the following line at the end of the file to setup your enviornment.

```bash
source /opt/ros/foxy/setup.bash
```

---
