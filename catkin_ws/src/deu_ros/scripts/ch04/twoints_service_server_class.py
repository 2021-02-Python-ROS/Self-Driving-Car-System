#!/usr/bin/env python

import rospy
#here
from deu_ros.srv import TwoInts, TwoIntsResponse

class TwoIntsServiceServer:
    #here
    use_default_constructor = False

    def __init__(self):
        #here
        rospy.init_node('twoints_service_server_class')
        self.service = rospy.Service('twoints_service',TwoInts,self.service_handler)
        rospy.spin()
    def service_handler(self, request):
        print 'a =', request.a, ', b =', request.b
        if TwoIntsServiceServer.use_default_constructor:
            #here
            resp = TwoIntsResponse()
            resp.result_add = request.a + request.b
            resp.result_mult = request.a * request.b
        else:
            #here
            result_add = request.a + request.b
            result_mult = request.a * request.b
            resp = TwoIntsResponse(result_add, result_mult)
        return resp

if __name__ == "__main__":
    #here
    server = TwoIntsServiceServer()