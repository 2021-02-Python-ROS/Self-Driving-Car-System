#!/usr/bin/env python

import rospy
import math
import time
from smach import State
from bot_drive_controller import BotDrive
from std_msgs.msg import Bool, Float32
from sensor_msgs.msg import LaserScan
from scan_blocking_bar import ScanBar
# state : http://wiki.ros.org/smach/Tutorials/Getting%20Started
from bot_lane_tracker import BotLaneTracker
from scan_stop_line import ScanStopLine
from bot_stop_sign import ScanStopSign
from scan_obstacle import Scan_Obstacle
class BotReady(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        self.angular_v = math.pi / 2
    def execute(self, ud):
        start = self.select_lane()
        return 'success'

    def select_lane(self):
        lane_changer = ScanBar()
        self.starting_lane = int(input("Select the lane (1 or 2): "))
        start_time = time.time() + 0.5
        while not rospy.is_shutdown():
            if self.starting_lane == 1:
                return 1
            elif self.starting_lane == 2:
                lane_changer.botDrive.set_angular(-self.angular_v)
                lane_changer.botDrive.bot_drive()
                if time.time() - start_time > 0:
                    rospy.sleep(1)
                    start_time = time.time() + 0.7
                    while True:
                        lane_changer.botDrive.set_linear(1.0)
                        lane_changer.botDrive.set_angular(0)
                        lane_changer.botDrive.bot_drive()
                        if time.time() - start_time > 0:
                            rospy.sleep(1)
                            start_time = time.time() + 0.5
                            while True:
                                lane_changer.botDrive.set_linear(0.1)
                                lane_changer.botDrive.set_angular(self.angular_v - 0.11)
                                lane_changer.botDrive.bot_drive()
                                if time.time() - start_time > 0:
                                    rospy.sleep(1)
                                    return 2




class ScanBlockBar(State):
    # Scanning To Blocking Bar and Drive
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        # self.blocking_bar = ScanBar()

    def execute(self, ud):
            blocking_bar = ScanBar()
            while not rospy.is_shutdown():
                if blocking_bar.go_sign:
                    blocking_bar.botDrive.set_linear(1)
                    # rospy.loginfo("Blocking Bar Opened!")
                else:
                    blocking_bar.botDrive.set_linear(0)
                    # rospy.loginfo("Blocking Bar is Closed")
                blocking_bar.botDrive.bot_drive()
                if time.time() - blocking_bar.start_time > 0:
                    return 'success'


class BotLaneTrack(State):
    # default Driving state
    # Scanning Event
    def __init__(self):
        State.__init__(self, outcomes=['success', 'scan_stop_line', 'scan_stop_sign', 'scan_obstacle', 'end_line'])
        self.botDrive = BotDrive()

        self.scan_stop_line = ScanStopLine()
        self.scan_stop_sign = ScanStopSign()
        self.scan_obstacle =  ScanObstacle()

        self.is_stop_line = rospy.Subscriber('detect/is_stop_line', Bool, self.stop_line_callback)

        self.left_line = BotLaneTracker('my_left_camera/rgb/image_raw')
        self.right_line = BotLaneTracker('my_right_camera/rgb/image_raw')
        self.is_stop_line = False
        self.stop_count = 0


    def stop_line_callback(self, msg):
        if msg.data:
            self.is_stop_line = True
        else:
            self.is_stop_line = False

    def execute(self, ud):
        rospy.loginfo("Now Driving")

        print(self.stop_count)
        while True:
            # Transition Start
            if self.is_stop_line:
                self.stop_count += 1

                return 'scan_stop_line'

            if self.scan_stop_sign.stop and self.stop_count == 0:
                self.stop_count += 1

                return 'scan_stop_sign'
            elif self.stop_count == 1:  # Before transition to obstacle scan state, wait time and keep lane tracing 9
                self.scan_stop_sign.stop = False
                time_now = int(rospy.Time.now().to_sec())
                target_time = time_now + 12.8

                while target_time > int(rospy.Time.now().to_sec()):
                    cx = (self.left_line.cx + self.right_line.cx + 10) / 2
                    err = -float(cx) / 100  # 80 or 100

                    if abs(err) > 0.16:  # 0.14 is original
                        self.botDrive.set_linear(0.4)
                        self.botDrive.set_angular(err)
                    elif abs(err) < 0.16:
                        self.botDrive.set_linear(0.6)  # 1 or 0.5
                        self.botDrive.set_angular(err)
                    self.botDrive.bot_drive()
                self.stop_count += 1

                return 'scan_obstacle'
            elif self.stop_count == 11:  # due to scan too many contours, we have to ignore red color for few seconds
                time_now = int(rospy.Time.now().to_sec())
                target_time = time_now + 7  # 7 seconds ignore

                while target_time > int(rospy.Time.now().to_sec()):
                    cx = (self.left_line.cx + self.right_line.cx + 10) / 2
                    err = -float(cx) / 100  # 80 or 100

                    if abs(err) > 0.15:
                        self.botDrive.set_linear(0.4)
                        self.botDrive.set_angular(err)
                    elif abs(err) < 0.15:
                        self.botDrive.set_linear(0.5)
                        self.botDrive.set_angular(err)
                    self.botDrive.bot_drive()
                if self.scan_stop_sign.stop == True:
                    time_now2 = int(rospy.Time.now().to_sec())
                    target_time2 = time_now2 + 3.7
                    while target_time2 > int(rospy.Time.now().to_sec()):
                        cx = (self.left_line.cx + self.right_line.cx + 10) / 2
                        err = -float(cx) / 100  # 80 or 100

                        if abs(err) > 0.15:
                            self.botDrive.set_linear(0.4)
                            self.botDrive.set_angular(err)
                        elif abs(err) < 0.15:
                            self.botDrive.set_linear(0.5)
                            self.botDrive.set_angular(err)
                        self.botDrive.bot_drive()
                    return 'end_line'
                    # Transition End

            cx = (self.left_line.cx + self.right_line.cx + 10) / 2
            err = -float(cx) / 100 # 80 or 100

            if abs(err) > 0.15:   # 0.14 is original
                self.botDrive.set_linear(0.4)
                self.botDrive.set_angular(err)
            elif abs(err) < 0.15:
                self.botDrive.set_linear(0.5)  # 1 or 0.5
                self.botDrive.set_angular(err)
            self.botDrive.bot_drive()


class ScannedStopLine(State):
    # Scanning To Stop Line
    # Drive Start or Stop
    def __init__(self):
        State.__init__(self, outcomes=['success', 'go_straight', 'go_straight2'])
        self.botDrive = BotDrive()
        self.stop_line_sub = rospy.Subscriber('detect/stop_line_cx', Float32, self.stop_line_callback)
        self.rate = rospy.Rate(4)  # 20
        self.stop_line_count = 0

    def stop_line_callback(self, msg):
        self.cs = msg.data

    def execute(self, ud):
        rospy.loginfo("Stop Line Scanned")
        self.stop_line_count += 1
        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 3  # 3 second wait

        while target_time > int(rospy.Time.now().to_sec()):
            self.botDrive.set_linear(0)
            self.rate.sleep()

        if self.stop_line_count == 4 or self.stop_line_count == 7:
            if self.stop_line_count == 4:
                self.botDrive.set_angular(-0.1)
                self.botDrive.bot_drive()
                return 'go_straight'
            elif self.stop_line_count == 7:
                self.botDrive.set_angular(-0.3)
                self.botDrive.bot_drive()
                return 'go_straight2'
        return 'success'


class ScannedStopSign(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        self.botDrive = BotDrive()

    def execute(self, ud):
        rospy.loginfo("Stop Sign Scanned")
        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 3
        while target_time > int(rospy.Time.now().to_sec()):
            continue
        self.botDrive.set_angular(0)
        self.botDrive.bot_drive()
        return 'success'


class GoStraight(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, ud):
        self.botDrive = BotDrive()
        while not rospy.is_shutdown():
            start_time = time.time() + 7
            while True:
                self.botDrive.set_angular(0.0)
                self.botDrive.set_linear(0.8)
                self.botDrive.bot_drive()
                if time.time() - start_time > 0:
                    return 'success'

class GoStraight2(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, ud):
        self.botDrive = BotDrive()
        while not rospy.is_shutdown():
            start_time = time.time() + 7
            while True:
                self.botDrive.set_angular(0.0)
                self.botDrive.set_linear(0.8)
                self.botDrive.bot_drive()
                if time.time() - start_time > 0:
                    return 'success'


class BotLaneTrack2(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        self.botDrive = BotDrive()

        self.left_line = BotLaneTracker('my_left_camera/rgb/image_raw')
        self.right_line = BotLaneTracker('my_right_camera/rgb/image_raw')

        self.rate = rospy.Rate(4)

    def execute(self, ud):
        rospy.loginfo("Now Driving 2")

        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 15.5  # Time Delay to insert second curve course

        while target_time > int(rospy.Time.now().to_sec()):
            cx = (self.left_line.cx + self.right_line.cx + 10) / 2
            err = -float(cx) / 100  # 80 or 100

            if abs(err) > 0.17:
                self.botDrive.set_linear(0.43)
                self.botDrive.set_angular(err)
            elif abs(err) < 0.17:
                self.botDrive.set_linear(0.5)
                self.botDrive.set_angular(err)
            self.botDrive.bot_drive()

        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 1

        while target_time > int(rospy.Time.now().to_sec()):
            self.botDrive.set_linear(0.81)
            self.botDrive.set_angular(-0.8)
            self.botDrive.bot_drive()

        return 'success'

class ScanObstacle(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        self.botDrive = BotDrive()
        self.detect_obstacle_sub = rospy.Subscriber('detect/is_obstacle', LaserScan, callback=self.scan_callback)

    def scan_callback(self, msg):
        pass

    def execute(self, ud):
        rospy.loginfo("obstacle")
        start_time = time.time() + 4
        self.scan_obstacle = Scan_Obstacle()
        if self.scan_obstacle.g_range_ahead < 2:
            self.botDrive.set_linear(0)
        else:
            self.botDrive.set_linear(1)
        self.botDrive.bot_drive()
        while True:
            if time.time() - start_time > 0:
                return 'success'


class EndLine(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        self.botDrive = BotDrive()

    def execute(self, ud):
        rospy.loginfo("End Project")
        self.botDrive.set_linear(0)
        self.botDrive.bot_drive()
        return 'success'

