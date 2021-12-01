#!/usr/bin/env python

# Move Turtlebot 1m forward
# cf. pp.231-232

import rospy
from actionlib import SimpleActionClient
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionFeedback

def feedback_cb(msg):
    x = msg.base_position.pose.position.x
    y = msg.base_position.pose.position.y
    print 'x = %.2f y = %.2f'%(x,y)

def done_cb(status, result):
    print 'status =', status
    print 'result =', result, '(NOTHING)'
    if status == GoalStatus.SUCCEEDED:
        print '>>> move succeeded!'
    elif status == GoalStatus.REJECTED:
        print '>>> move rejected!'
    else:
        print 'fine the status in /opt/ros/kinetic/share/actionlib_msgs/msg/GoalStatus.msg'


rospy.init_node('move_one_meter')
client = SimpleActionClient('move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "base_footprint" # default: base_link
goal.target_pose.header.stamp = rospy.get_rostime()

goal.target_pose.pose.position.x = 1.0
goal.target_pose.pose.position.y = 0.0
goal.target_pose.pose.orientation.w = 1.0
client.send_goal(goal, done_cb = done_cb, feedback_cb = feedback_cb)

client.wait_for_result()