#!/usr/bin/env python

import rospy
from smach import StateMachine
import robot_state
import smach_ros
import cv2
if __name__ == "__main__":
    rospy.init_node('test_node')
    driving_test_site = StateMachine(outcomes=['success'])
    with driving_test_site:
        StateMachine.add('SETTING_LANE', robot_state.SettingLane(), transitions={'success': 'DETECT_BLOCKING_BAR'})
        StateMachine.add('DETECT_BLOCKING_BAR', robot_state.DetectBlockingBar(),transitions={'success': 'LANE_TRACE1'})
        StateMachine.add('LANE_TRACE1', robot_state.LaneTrace(), transitions={'success': 'DETECT_STOP_SIGN1'})
        StateMachine.add('DETECT_STOP_SIGN1', robot_state.DetectStopSign(), transitions={'success': 'LANE_TRACE2'})
        # StateMachine.add('RIGHT_ANGLE_PARKING', RightAngleParking(), transitions={'success': 'DETECT_OBSTACLE'})
       # StateMachine.add('DETECT_STOP_SIGN1', robot_state.DetectStopSign(), transitions={'success': 'LANE_TRACE2'})

        StateMachine.add('LANE_TRACE2', robot_state.LaneTrace(), transitions={'success': 'LANE_TRACE3'})

        StateMachine.add('DETECT_OBSTACLE', robot_state.AvoidObstacle(), transitions={'success': 'LANE_TRACE3'})
        StateMachine.add('LANE_TRACE3', robot_state.LaneTrace(), transitions={'success': 'LANE_TRACE4'})
        StateMachine.add('LANE_TRACE4', robot_state.LaneTrace(), transitions={'success': 'success'})
        # StateMachine.add('PARALLEL_PARKING', ParallelParking(), transitions={'success': 'DETECT_STOP_SIGN'})
        #StateMachine.add('DETECT_STOP_SIGN2', robot_state.DetectStopSign(), transitions={'success': 'success'})
        # StateMachine.add('') ....

    sis = smach_ros.IntrospectionServer('test', driving_test_site, '/SM_ROOT')
    sis.start()
    driving_test_site.execute()
    sis.stop()
    rospy.spin()
