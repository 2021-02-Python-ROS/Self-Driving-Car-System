#!/usr/bin/env python


import rospy
import bot_drive_state
from smach import StateMachine
import smach_ros

class BotStateMachine(object):
    def __init__(self):
        self.autonomous_drive = StateMachine(outcomes=['success'])

    def drive_bot(self):
        with self.autonomous_drive:
            StateMachine.add('BOT_READY', bot_drive_state.BotReady(), transitions={'success':'SCAN_BAR'})
            StateMachine.add('SCAN_BAR', bot_drive_state.ScannedBar(), transitions={'success':'LANE_TRACK'})
            StateMachine.add('LANE_TRACK', bot_drive_state.BotLaneTrack(), transitions={'success':'success', 'scan_stop_line':'SCAN_STOP_LINE'})
            StateMachine.add('SCAN_STOP_LINE', bot_drive_state.ScannedStopLine(), transitions={'success':'LANE_TRACK'})
            #StateMachine.add('PROJECT_END', bot_drive_state.ProjectEnd().BotLaneTrack(), transitions={'success':'success'})
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
