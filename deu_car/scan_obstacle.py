#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from bot_drive_controller import BotDrive

class scan_obstacle():
    def __init__(self):
        self.g_range_ahead = 1
        self.scan_sub = rospy.Subscriber('scan', LaserScan, self.scan_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
        rospy.init_node('wander')
        self.rate = rospy.Rate(10)
        self.botDrive = BotDrive()

    def scan_callback(self, msg):
        self.g_range_ahead = min(msg.ranges)
        print 'g_range_ahead = %.2f' % self.g_range_ahead
        self.rate.sleep()
        if self.g_range_ahead < 2:
            self.botDrive.set_linear(0)
            print ('stop!')
        else:
            self.botDrive.set_linear(1)
            print ('moving again')

if __name__ == "__main__":
    detect_obstacle = scan_obstacle()
    while not rospy.is_shutdown():
        detect_obstacle.rate.sleep()

"""
	unused code
    def __init__(self):
        self.LIDAR_ERR = 0.05  # Lidar sensor scan distance minimum set
        msg = rospy.wait_for_message("/scan", LaserScan)
        self.g_range_ahead = 1
        self.scanned_distance = []
        rospy.init_node('Scan_Obstacle')
        self.rate = rospy.Rate(10)
        self.botDrive = BotDrive()

    def scan_callback(self, msg):
        for i in range(360):
            if i <= 45 or i > 315:
                if msg.ranges[i] >= self.LIDAR_ERR:
                    self.scanned_distance.append(msg.ranges[i])
                    if min(self.scanned_distance) <= 0.09:
                        self.botDrive.set_linear(0)
                        self.botDrive.bot_drive()
                        rospy.loginfo('stop')
                        break
                    else:
                        self.botDrive.set_linear(1)
                        rospy.loginfo('distance from obstacle : %f', min(self.scanned_distance))
                        self.botDrive.bot_drive()
"""





