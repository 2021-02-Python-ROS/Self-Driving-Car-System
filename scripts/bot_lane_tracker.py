#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
from scan_with_camera import ScanWithCamera
from bot_drive_controller import BotDrive


# lane mid driving
class BotLaneTracker:
    def __init__(self, image_topic_name):
        self.bridge = cv_bridge.CvBridge()

        self.image_sub = rospy.Subscriber(image_topic_name, Image, self.image_callback)
        self.image_pub = rospy.Publisher(image_topic_name + "/trace_image", Image, queue_size=1)

        self.cx = 0
        self.err = 0
        self.t = image_topic_name

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')  # img -> bgr8 cv2
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # bgr -> hsv

        # h, s, v = cv2.split(hsv_image)  # image HSV split
        _, _, v = cv2.split(hsv_image)
        v = cv2.inRange(v, 220, 255)  # V Image, Low Value, High Value
        # 210, 220 or 220, 255

        # height, width, _ = hsv_image.shape
        # hsv_image[height/2:0, 0:width] = 0

        M = cv2.moments(v)  # weight mid

        if M['m00'] > 0:
            self.cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(image, (self.cx, cy), 20, (0, 0, 255), -1)
            # center pos(cx, cy), radius(20), color(B, G, R), thickness(-1: fill)
            self.cx = self.cx - 320

        image = self.bridge.cv2_to_imgmsg(image)
        self.image_pub.publish(image)


if __name__ == '__main__':
    rospy.init_node('Bot_Lane_Tracker')
    left_line = BotLaneTracker('my_left_camera/rgb/image_raw')
    right_line = BotLaneTracker('my_right_camera/rgb/image_raw')
    botDrive = BotDrive()
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        cx = (left_line.cx + right_line.cx + 0.3) / 2
        err = -float(cx) / 80
        print err

        if abs(err) > 0.14:
            botDrive.set_linear(0.4)
            botDrive.set_angular(err)
        elif abs(err) < 0.14:
            botDrive.set_linear(1)
            botDrive.set_angular(err)
        botDrive.bot_drive()
        rate.sleep()






