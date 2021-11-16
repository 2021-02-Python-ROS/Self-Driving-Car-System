#!/usr/bin/env python

from abc import *
# Python Abstract Class - Extends
import cv_bridge
# OpenCV ROS library
from sensor_msgs.msg import Image
import rospy

class ScanDefault:
    __metaclass__ = ABCMeta
    
    @abstractmethod  # Abstract Method
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()  # OpenCV2 <-> ROS
        self.current_focus_pub = rospy.Publisher('current_focus_image', Image, queue_size=1)
        self.rate = rospy.Rate(20)  # Image of Event
        
    @abstractmethod # Abstract Method - 2
    # Notice Used Image Topic
    def image_callback(self, msg):
        raise NotImplementedError()
