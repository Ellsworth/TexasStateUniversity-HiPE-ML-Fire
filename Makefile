SHELL := /bin/bash

all:
	rosdep install -i --from-path src --rosdistro foxy -y
	colcon build --packages-select py_pubsub
	chmod +x ./install/setup.bash
	. install/setup.bash

talker:
	. install/setup.bash
	ros2 run py_pubsub talker

listener:
	. install/setup.bash
	ros2 run py_pubsub listener
