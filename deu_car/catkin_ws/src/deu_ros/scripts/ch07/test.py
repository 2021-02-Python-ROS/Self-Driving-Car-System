#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from robot_drive_controller import RobotDriveController

drive_controller = RobotDriveController()

drive_controller.set_velocity(1)
drive_controller.drive()
