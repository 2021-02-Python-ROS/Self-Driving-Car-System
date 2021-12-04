#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist

# tutlebot drive class
# linear velocity, angular velocity change class
class BotDrive:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
        self.twist = Twist()
        self._linear = 0
        self._angular = 0
        
    def set_linear(self, linear):
        # linear velocity setting (speed)
        self._linear = linear
        
    def set_angular(self, angular):
        # angular velocity setting (rotate)
        self._angular = angular
        
    def bot_drive(self):
        self.twist.linear.x = self._linear
        self.twist.angular.z = self._angular
        self.cmd_vel_pub.publish(self.twist)
        
# main
if __name__ == "__main__":
    rospy.init_node('bot_drive_controller')
    botDrive = BotDrive()
    botDrive.set_linear(1) # linear velocity set 1m/s
    botDrive.bot_drive() # drive start
    rospy.spin()
