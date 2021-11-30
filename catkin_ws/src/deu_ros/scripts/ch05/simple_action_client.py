#!/usr/bin/env python

import rospy

import actionlib
from deu_ros.msg import TimerAction, TimerGoal, TimerResult

rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()

goal = TimerGoal()
# goal.time_to_wait = rospy.Duration.from_sec(5.0)
goal.time_to_wait = rospy.Duration(5)
client.send_goal(goal)

finished = client.wait_for_result()
if finished:
    print('Time elapsed: %f' % (client.get_result().time_elapsed.to_sec()))
    #rospy.loginfo('Time elapsed: %f', client.get_result().time_elapsed.to_sec())
else:
    rospy.loginfo("Not finished")