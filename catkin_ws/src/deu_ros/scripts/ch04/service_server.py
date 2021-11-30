#!/usr/bin/env python

import rospy
from deu_ros.srv import WordCount, WordCountResponse


def count_words(request):
    #here
    return WordCountResponse(len(request.words.split()))

rospy.init_node('service_server')
#here
rospy.service = rospy.Service('word_count',WordCount,count_words)
rospy.spin()