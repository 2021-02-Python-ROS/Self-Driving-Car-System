#!/usr/bin/env python

import rospy
#here
from deu_ros.srv import TwoInts, TwoIntsRequest
import sys


class TwoIntsServiceClient:
    def __init__(self):
        #here
        rospy.init_node('twoints_service_client_class')
        rospy.wait_for_service('twoints_service')
        self.service = rospy.ServiceProxy('twoints_service',TwoInts)
    def get_result(self, a, b):
        #here
        request = TwoIntsRequest(a,b)
        resp = self.service(request)
        return resp.result_add, resp.result_mult

if __name__ == "__main__":
    #here

    if len(sys.argv) <3:
        print "Two arguments of int type is required."
        sys.exit(-1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    for i in range(3):
        #here

        print 'result_add =', result_add, ', result_mult =', result_mult
        rospy.sleep(1)