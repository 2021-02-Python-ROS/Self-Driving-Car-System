#!/usr/bin/env python

import rospy
from deu_ros.srv import WordCount, WordCountRequest
import sys

rospy.init_node('service_client')
rospy.wait_for_service('word_count')
#here
word_counter = rospy.ServiceProxy('word_count',WordCount)

words = ' '.join(sys.argv[1:])
#here
word_count = word_counter(words)
print words, '-> ', word_count.count

