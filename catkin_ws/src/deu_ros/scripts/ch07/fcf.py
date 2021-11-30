#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge, numpy
import sys


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)
        self.len_contour = 0
    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        lower_red = numpy.array([0, 0, 90])
        upper_red = numpy.array([5, 5, 110])
        gray_img = cv2.inRange(image, lower_red, upper_red)
        h, w = gray_img.shape
        block_bar_mask = gray_img

        block_bar_mask[h / 2:h, 0:w] = 0
        cv2.imshow("window", gray_img)
        cv2.waitKey(3)
        block_bar_mask, contours, hierarchy = cv2.findContours(block_bar_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.len_contour = len(contours)

rospy.init_node('follower')
follower = Follower()
rospy.spin()

