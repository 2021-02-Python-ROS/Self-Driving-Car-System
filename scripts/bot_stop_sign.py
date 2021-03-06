#! /usr/bin/env python
# coding=utf-8

import rospy
import cv2, cv_bridge
import numpy as np
from bot_drive_controller import BotDrive
from sensor_msgs.msg import Image
from std_msgs.msg import Bool


class ScanStopSign:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)
        self.block_pub = rospy.Publisher('detect/stop_sign', Bool, queue_size=1)

        self.drive_controller = BotDrive()
        self.contours = []
        self.stop = False

    def image_callback(self, msg):

        origin_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 0, 90])
        upper_red = np.array([5, 5, 110])
        gray_img = cv2.inRange(hsv, lower_red, upper_red)

        h, w = gray_img.shape
        block_bar_mask = gray_img
        block_bar_mask[0:h, 0: w- w/9] = 0
        block_bar_mask[h/2:h, 0:w] = 0
        block_bar_mask[0:h/10, 0:w] = 0

        block_bar_mask, self.contours, hierarchy = cv2.findContours(block_bar_mask, cv2.RETR_TREE,
                                                                    cv2.CHAIN_APPROX_SIMPLE)

        # rospy.loginfo(len(self.contours))  debug code
        if len(self.contours) >= 7:
            self.stop = True
        else:
            self.stop = False


if __name__ == '__main__':
    rospy.init_node('image_converter')
    ic = ScanStopSign()
    rospy.spin()