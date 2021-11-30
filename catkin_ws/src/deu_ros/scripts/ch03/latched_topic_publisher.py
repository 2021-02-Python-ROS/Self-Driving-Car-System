#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')

# pub = rospy.Publisher('counter', Int32)
pub = rospy.Publisher('counter', Int32, queue_size=1, latch= True)
pub.publish(100)

rate=rospy.Rate(2)
count = 0

while not rospy.is_shutdown():
    if count ==20: # after 10 seconds
        break
    count += 1
    print 'count =', count
    rate.sleep()