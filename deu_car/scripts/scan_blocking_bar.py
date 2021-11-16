#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from bot_drive_controller import BotDrive
from scan_default import ScanDefault

class ScanBar(ScanDefault):
    # Scan Blocking Bar
    def __init__(self):
        super(ScanBar, self).__init__()
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)
        self.image_pub = rospy.Publisher('detect/blocking_bar', Image, queue_size=1)
        self.scan_blockingbar = rospy.Publisher('detect/is_block', Bool, queue_size=1)
        self.len_contour = 0
        self.botDrive = BotDrive()
        
    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        #lower_red = np.array([0, 0, 90])
        #upper_red = np.array([5, 5, 110])
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([5, 255, 255])
        gray_img = cv2.inRange(image, lower_red, upper_red)
        h, w = gray_img.shape
        block_bar_mask = gray_img
        
        block_bar_mask[h/2:h, 0:w] = 0
        contours, hierarchy = cv2.findContours(block_bar_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        block_bar_mask = self.bridge.cv2_to_imgmsg(block_bar_mask, "passthrough")
        self.len_contour = len(contours)
        
        if contours:
            self.image_pub.publish(block_bar_mask)
            if len(contours) >= 3:
                self.scan_blockingbar.publish(True)
            else:
                self.scan_blockingbar.publish(False)
                
                
if __name__ == "__main__":
    rospy.init_node('test_node')
    scaner = ScanBar()
    botDrive = BotDrive
    while not rospy.is_shutdown():
        print scaner.len_contour  #debuging
        
        if scaner.len_contour < 2:
            scaner.botDrive.set_linear(1)
            scaner.botDrive.bot_drive()
        else:
            scaner.botDrive.set_linear(0)
            scaner.botDrive.bot_drive()
        scaner.rate.sleep()
