#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2, cv_bridge

class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')

        cv2.imshow("window",image)
        img = cv2.imread("window", cv2.IMREAD_GRAYSCALE)
        (x, y), (w, h) = (200, 200), (30, 20)
        roi_img = img[y:y + h, x:x + w]
        print(roi_img)
        cv2.waitKey(3)

rospy.init_node('follower')
follower = Follower()
rospy.spin()