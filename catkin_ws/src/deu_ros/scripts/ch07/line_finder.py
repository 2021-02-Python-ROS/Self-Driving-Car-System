#!/usr/bin/env python
# coding=utf-8

import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image
from robot_drive_controller import RobotDriveController
import numpy

class LineTracer:
    def __init__(self, image_topic):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window",1)
        self.image_pub = rospy.Publisher(image_topic + "/circle", Image, queue_size=1)
        self.image_sub = rospy.Subscriber(image_topic, Image, self.image_callback)
        self.t = image_topic
        self.cx = 0

        self.stop_count = 0
        self.stop_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback2)
        self.area = 0

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_gray = numpy.array([0, 0, 200])
        upper_gray = numpy.array([0, 0, 255])
        mask = cv2.inRange(hsv, lower_gray, upper_gray)

        h, w, d = image.shape
        search_top = 3*h/4
        search_bot = 3 * h / 4 + 20
        mask[0:search_top, 0:w] = 0
        mask[search_bot:h, 0:w] = 0

        M = cv2.moments(mask)
        if M['m00'] > 0:
            self.cx = int(M['m10'] / M['m00'])

            cy = int(M['m01'] / M['m00'])
            cv2.circle(image, (self.cx, cy), 20, (0, 0, 255), -1)
            self.cx = self.cx - 320

if __name__ == '__main__':
    rospy.init_node('lane_trace')
    main_line = LineTracer('camera/rgb/image_raw')
    stop_line = LineTracer('camera/rgb/image_raw')
    drive_controller = RobotDriveController()
    rate = rospy.Rate(20)
    count = 0
    while not rospy.is_shutdown():
        cx = main_line / 2
        err = -float(cx) / 100

        if stop_line.area > 9000.0:
            drive_controller.set_velocity(0)
            drive_controller.set_angular(0)
            count = count + 1
            print('stop!')
            print(count)
            rospy.sleep(3)

        if count == 4:
            drive_controller.set_velocity(1)
            drive_controller.set_angular(0)
            drive_controller.drive()

        if abs(err) > 0.20 and stop_line.area < 9000.0:
            drive_controller.set_velocity(0.4)
            drive_controller.set_angular(err)
            drive_controller.drive()

        elif abs(err) <= 0.20 and stop_line.area < 9000.0:
            drive_controller.set_velocity(1)
            drive_controller.set_angular(err)
            drive_controller.drive()

        rate.sleep()

    rospy.spin()