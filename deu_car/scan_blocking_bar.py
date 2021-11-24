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
        self.count = 0
        rospy.Rate(20)
        self.isBlockbarFinish = False

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        lower_red = np.array([0, 0, 90])
        upper_red = np.array([0, 0, 255])
        gray_img = cv2.inRange(image, lower_red, upper_red)
        h, w = gray_img.shape
        block_bar_mask = gray_img

        block_bar_mask[h / 2:h, 0:w] = 0
        #  Tested OpenCV version is 3.4.2.x
        block_bar_mask, contours, hierarchy = cv2.findContours(block_bar_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        block_bar_mask = self.bridge.cv2_to_imgmsg(block_bar_mask, "passthrough")
        self.len_contour = len(contours)

        if contours:
            self.image_pub.publish(block_bar_mask)
            if self.len_contour <= 3:  # block_bar is shut downed
                self.scan_blockingbar.publish(False)  # to check
                while(self.count <= 30):
                    self.botDrive.set_linear(1)
                    self.botDrive.bot_drive()
                    # rospy.loginfo('gogo') # test code
                    self.count += 1
                    # rospy.loginfo("%d", self.count)
                    break
                if(self.count > 30):
                    self.isBlockbarFinish = True


            else:  # is open
                self.scan_blockingbar.publish(True)  # to check
                self.botDrive.set_linear(0)
                self.botDrive.bot_drive()
                self.count = 0

                # rospy.loginfo('Stop') # test code
        else:
            self.botDrive.set_linear(1)
            self.botDrive.bot_drive()


#   Stand-alone test code
if __name__ == "__main__":
    rospy.init_node('test_node')
    scanner = ScanBar()
    botDrive = BotDrive()
    while not rospy.is_shutdown():
        print scanner.len_contour  # debugging

        if scanner.len_contour < 2:
            scanner.botDrive.set_linear(1)
            scanner.botDrive.bot_drive()
        else:
            scanner.botDrive.set_linear(0)
            scanner.botDrive.bot_drive()
        scanner.rate.sleep()
