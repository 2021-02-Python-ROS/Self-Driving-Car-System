#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from bot_drive_controller import BotDrive

class Scan_Obstacle():
    def __init__(self):
        self.g_range_ahead = 1
        self.scan_sub = rospy.Subscriber('scan', LaserScan, self.scan_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
        self.rate = rospy.Rate(10)
        self.botDrive = BotDrive()

    def scan_callback(self, msg):
        self.g_range_ahead = min(msg.ranges)
        print 'obstacle_ahead = %.2f' % self.g_range_ahead
        self.rate.sleep()

if __name__ == "__main__":
    scan_obstacle = Scan_Obstacle()
    while not rospy.is_shutdown():
        scan_obstacle.rate.sleep()




