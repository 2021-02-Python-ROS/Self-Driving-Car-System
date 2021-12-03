#!/usr/bin/env python
import cv2
import cv_bridge
import rospy
from sensor_msgs.msg import Image

import bot_drive_state
from smach import StateMachine
import smach_ros

class BotStateMachine(object):
    def __init__(self):
        self.autonomous_drive = StateMachine(outcomes=['success'])
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)
        self.bridge = cv_bridge.CvBridge()

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        #cv2.imshow("Driving screen", image)
        #cv2.waitKey(3)

    def drive_bot(self):
        with self.autonomous_drive:
            StateMachine.add('BOT_READY', bot_drive_state.BotReady(), transitions={'success':'SCAN_BAR'})
            StateMachine.add('SCAN_BAR', bot_drive_state.ScanBlockBar(), transitions={'success':'LANE_TRACK'})
            StateMachine.add('LANE_TRACK', bot_drive_state.BotLaneTrack(), transitions={'success':'END_LINE', 'scan_stop_line':'SCAN_STOP_LINE', 'scan_stop_sign':'SCAN_STOP_SIGN',
                                                                                        'scan_obstacle' : 'SCAN_OBSTACLE', 'end_line' : 'END_LINE'})
            StateMachine.add('SCAN_OBSTACLE', bot_drive_state.ScanObstacle(), transitions={'success': 'LANE_TRACK'})
            StateMachine.add('SCAN_STOP_SIGN', bot_drive_state.ScannedStopSign(), transitions={'success':'LANE_TRACK'})
            StateMachine.add('SCAN_STOP_LINE', bot_drive_state.ScannedStopLine(), transitions={'success':'LANE_TRACK', 'go_straight':'GO_STRAIGHT', 'go_straight2':'GO_STRAIGHT2'})
            StateMachine.add('GO_STRAIGHT', bot_drive_state.GoStraight(), transitions={'success':'LANE_TRACK2'})
            StateMachine.add('GO_STRAIGHT2', bot_drive_state.GoStraight2(), transitions={'success': 'LANE_TRACK'})
            StateMachine.add('LANE_TRACK2', bot_drive_state.BotLaneTrack2(), transitions={'success':'LANE_TRACK'})
            StateMachine.add('END_LINE', bot_drive_state.EndLine(), transitions={'success': 'success'})
            # StateMachine.add('') ....

        sis = smach_ros.IntrospectionServer('test', self.autonomous_drive, '/SM_ROOT')
        sis.start()
        self.autonomous_drive.execute()
        sis.stop()


if __name__ == "__main__":
    rospy.init_node('autonomous_car_test_drive')
    bot_state_machine = BotStateMachine()
    bot_state_machine.drive_bot()
    while not rospy.is_shutdown():
        rospy.spin()