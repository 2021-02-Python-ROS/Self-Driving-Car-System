#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist


class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
        self.p2_image_pub = rospy.Publisher('camera/rgb/image_raw/p2', Image, queue_size=1)
        self.twist = Twist()
        self.count = 0

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_yellow = numpy.array([25, 20, 50])
        upper_yellow = numpy.array([35, 255, 255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        h, w, d = image.shape
        search_top = 3 * h / 4
        search_bot = 3 * h / 4 + 20
        mask[0:search_top, 0:w] = 0
        mask[search_bot:h, 0:w] = 0
        M = cv2.moments(mask)
        if M['m00'] > 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(image, (cx, cy), 20, (0, 0, 255), -1)
            err = cx - w / 2
            self.twist.linear.x = 1.0
            self.twist.angular.z = -float(err) / 300  # 400: 0.1, 300: 0.15, 250, 0.2
            self.cmd_vel_pub.publish(self.twist)

        cv2.imshow("window", image)
        cv2.imshow("mask", mask)
        cv2.imwrite('image.jpg', image)
        cv2.imwrite('mask.jpg', mask)

        image_msg = self.bridge.cv2_to_imgmsg(image, 'bgr8')
        self.p2_image_pub.publish(image_msg)
        rospy.loginfo('count = %d', self.count)
        self.count += 1
        cv2.waitKey(3)


rospy.init_node('follower')
follower = Follower()
rospy.spin()