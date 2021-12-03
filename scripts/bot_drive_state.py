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
from bot_stop_sign import ImageConverter
from scan_obstacle import Scan_Obstacle
class BotReady(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        # self.botDrive = BotDrive()

    def execute(self, ud):
        start = self.choose_lane()
        # rospy.loginfo("Ready? Wait for 3 seconds.")
        # rospy.sleep(rospy.Duration(3))
        return 'success'

    def choose_lane(self):
        lane_changer = ScanBar()
        self.starting_lane = int(input("Choose your departure lane. (enter 1 or 2)"))
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
                                lane_changer.botDrive.set_angular(self.angular_v)
                                lane_changer.botDrive.bot_drive()
                                if time.time() - start_time > 0:
                                    rospy.sleep(1)
                                    return 2



class ScanBlockBar(State):
    # Scanning To Blocking Bar
    # Drive Start or Stop
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        # self.blocking_bar = ScanBar()
        self.starting_lane = 0
        self.angular_v = math.pi / 2

    def execute(self, ud):
            blocking_bar = ScanBar()
            while not rospy.is_shutdown():
                if blocking_bar.go_sign:
                    blocking_bar.botDrive.set_linear(1)
                    # rospy.loginfo("Blocking Bar Openned!")
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
        self.scan_stop_sign = ImageConverter()
        self.scan_obstacle =  ScanObstacle()

        self.is_stop_line = rospy.Subscriber('detect/is_stop_line', Bool, self.stop_line_callback)

        self.left_line = BotLaneTracker('my_left_camera/rgb/image_raw')
        self.right_line = BotLaneTracker('my_right_camera/rgb/image_raw')  # changed
        self.is_success = False
        self.is_stop_line = False
        self.count1 = 0


    def stop_line_callback(self, msg):
        if msg.data:
            self.is_stop_line = True
        else:
            self.is_stop_line = False

    def execute(self, ud):
        rospy.loginfo("Now Driving")

        print(self.count1)
        while True:
            # Transition Start
            if self.is_stop_line:
                return 'scan_stop_line'

            if self.scan_stop_sign.ko and self.count1 == 7:
                self.count1 += 1
                return 'scan_stop_sign'
            elif self.count1 == 8:
                time_now = int(rospy.Time.now().to_sec())
                target_time = time_now + 11.5  # 3 second wait

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
                rospy.sleep(2)
                self.count1 += 1
                return 'scan_obstacle'
            elif self.count1 == 9:
                if self.is_stop_line:
                    return 'end_line'
            # if self.is_success:
            #     return 'end_line'
            # Transition End

            cx = (self.left_line.cx + self.right_line.cx + 10) / 2
            err = -float(cx) / 100  # 80 or 100

            if abs(err) > 0.16:   # 0.14 is original
                self.botDrive.set_linear(0.4)
                self.botDrive.set_angular(err)
            elif abs(err) < 0.16:
                self.botDrive.set_linear(0.57)  # 1 or 0.5
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
        self.count = 0

    def stop_line_callback(self, msg):
        self.cs = msg.data

    def execute(self, ud):
        rospy.loginfo("Stop Line Scanned")
        self.count += 1
        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 3  # 3 second wait

        while target_time > int(rospy.Time.now().to_sec()):
            self.botDrive.set_linear(0)
            self.rate.sleep()

        if self.count == 4 or self.count == 7:    # original count is 4 6
            if self.count == 4:
                self.botDrive.set_angular(-0.1)
                self.botDrive.bot_drive()
                return 'go_straight'
            elif self.count == 7:
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
        target_time = time_now + 3  # 4 second drive

        while target_time > int(rospy.Time.now().to_sec()):
            continue

        self.botDrive.set_angular(0)
        self.botDrive.bot_drive()
        rospy.sleep(3)
        return 'success'


class GoStraight(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, ud):
        self.botDrive = BotDrive()
        while not rospy.is_shutdown():
            start_time = time.time() + 7 # after done this, count few seconds, set variable, angular z 0.x ?
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
            start_time = time.time() + 7 # after done this, count few seconds, set variable, angular z 0.x ?
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
        self.right_line = BotLaneTracker('my_right_camera/rgb/image_raw')  # changed

        self.rate = rospy.Rate(4)

    def execute(self, ud):
        rospy.loginfo("Now Driving 2")

        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 15.5  # 4 second drive

        while target_time > int(rospy.Time.now().to_sec()):
            cx = (self.left_line.cx + self.right_line.cx + 10) / 2
            err = -float(cx) / 100  # 80 or 100

            if abs(err) > 0.17:  # 0.14 is original
                self.botDrive.set_linear(0.4)
                self.botDrive.set_angular(err)
            elif abs(err) < 0.17:
                self.botDrive.set_linear(0.5)  # 1 or 0.5
                self.botDrive.set_angular(err)
            self.botDrive.bot_drive()
            # self.rate.sleep()

        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 1  # 3 second wait

        while target_time > int(rospy.Time.now().to_sec()):
            self.botDrive.set_linear(0.8)
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
        print("hi")
        start_time = time.time() + 3  # after done this, count few seconds, set variable, angular z 0.x ?
        self.scan_obstacle = Scan_Obstacle()
        while True:
            if time.time() - start_time > 0:
                return 'success'


class EndLine(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        self.botDrive = BotDrive()

    def execute(self, ud):
        rospy.loginfo("End Project")
        self.drive_controller.set_velocity(0)
        self.drive_controller.drive()
        return 'success'
