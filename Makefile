SHELL := /bin/bash
.PHONY: build

build:
	rosdep install -i --from-path src --rosdistro foxy -y
	
	colcon build --packages-select py_pubsub


talker:
	. install/setup.bash
	ros2 run py_pubsub talker

listener:
	. install/setup.bash
	ros2 run py_pubsub listener
