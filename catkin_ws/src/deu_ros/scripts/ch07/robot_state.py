#!/usr/bin/env python
# coding=utf-8

import rospy
from smach import State
from detect_blocking_bar import BlockDetector
from lane_follower import LineTracer
from robot_drive_controller import RobotDriveController
import time
import math
from std_msgs.msg import Bool, Float32
from detect_stop_sign import ImageConverter
from obstacle_stop import DetectObstacle
from detect_stop_line import DetectStopLine

class SettingLane(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        self.drive_controller = RobotDriveController()

    def execute(self, ud):
        rospy.loginfo("wait...")
        #rospy.sleep(rospy.Duration(3))
        return 'success'


class DetectBlockingBar(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, ud):
        block_finder = BlockDetector()
        countfloor = 0
        while True:
            print(len(block_finder.contours))

            if len(block_finder.contours) == 0 and countfloor > 2: #3
                block_finder.drive_controller.set_velocity(1)

                print('go!')

                start_time = time.time() +3

                while True:
                    block_finder.drive_controller.drive()
                    if time.time() - start_time > 0:
                        break

                block_finder.drive_controller.set_velocity(0)

                return 'success'

            elif len(block_finder.contours) != 0 and countfloor > 3: #3
                block_finder.drive_controller.set_velocity(0)
                print('stop')

            else:
                print('!!detecting!!')

            countfloor = countfloor + 1
            rospy.sleep(0.1)

class DetectStopLine(State):
    def __init__(self):

        State.__init__(self, outcomes=['success'])
        self.drive_controller = RobotDriveController()
        self.stop_line_sub = rospy.Subscriber('detect/stop_line_cx', Float32, self.stop_line_callback)
        self.rate = rospy.Rate(20)
        self.count = 0


    def stop_line_callback(self, msg):
        self.cx = msg.data

    def execute(self, ud):
        rospy.loginfo("stopLine_check...")

        time_now = int(rospy.Time.now().to_sec())
        target_time = time_now + 3

        while target_time > int(rospy.Time.now().to_sec()):
            self.drive_controller.set_velocity(0)
            self.rate.sleep()
        return 'success'

class LaneTrace(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.stop_line = DetectStopLine()
        self.stop_line = False


    def execute(self, ud):
        left_line = LineTracer('my_left_camera/rgb/image_raw')
        right_line = LineTracer('my_right_camera/rgb/image_raw')
        main_line = LineTracer('camera/rgb/image_raw')
        stop_line = LineTracer('camera/rgb/image_raw')
        drive_controller = RobotDriveController()
        detect_obstacle = DetectObstacle()
        rate = rospy.Rate(10)
        count = 0
        self.Tcount = 0
        obs = 0
        test = ImageConverter()
        oob = AvoidObstacle()

        while not rospy.is_shutdown():

            cx = (left_line.cx + right_line.cx)  / 2
            err = -float(cx) / 100
            self.stop_line = True
            print(stop_line.area)
            print('aaaaaaaaaaaa')
            #print(self.Tcount)
            #print('bbbbbbbbbbbbbbb')

            if test.ko == True:
                obs += 1
                return 'success'

            if  obs == 1:
                if detect_obstacle.range_ahead > 2 or detect_obstacle.range_right > 2 or \
                        ((math.isnan(detect_obstacle.range_ahead)) and math.isnan(detect_obstacle.range_right)):

                    value = False
                    detect_obstacle.stop_pub.publish(value)
                    print('go~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                    return 'success'
                else:
                    value = True
                    detect_obstacle.stop_pub.publish(value)
                    drive_controller.set_velocity(0)
                    print('stop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                obs += 1


            if stop_line.area > 5000.0:

                drive_controller.set_velocity(0)
                drive_controller.set_angular(0)
                count = count + 1
                print('stop!')
                print(count)
                rospy.sleep(3)

            if count == 1:
                if stop_line.area > 3000.0:

                    drive_controller.set_velocity(0)
                    drive_controller.set_angular(0)
                    count = count + 1
                    print('stop!')
                    print(count)
                    rospy.sleep(3)
                    self.Tcount += 1


            if count == 3:
                drive_controller.set_velocity(1)
                drive_controller.set_angular(0)
                drive_controller.drive()
                count += 1


            if count == 5:
                drive_controller.set_velocity(0)
                drive_controller.set_angular(-0.2)  #-0.2, 0

                #start_time = time.time() + 1.5
                start_time = time.time() + 1
                while True:
                    drive_controller.drive()
                    if time.time() - start_time > 0:
                        count = count + 1
                        break

                drive_controller.set_velocity(0.5) #1
                drive_controller.set_angular(0)
                drive_controller.drive()

                start_time = time.time() + 5

                while True:
                    drive_controller.drive()
                    if time.time() - start_time > 0:
                        count = count + 1
                        break
                print("end")
                drive_controller.set_velocity(0)
                #return 'success'

            # if self.Tcount == 1:
            #     drive_controller.set_velocity(1)
            #     drive_controller.set_angular(0.27)
            #     drive_controller.drive()
            #     if start_time + 4.5 < time.time():
            #         drive_controller.set_velocity(0)
            #         drive_controller.set_angular(0)
            #         drive_controller.drive()
            #         start_time = time.time()
            #         self.Tcount += 1
            #
            #     elif self.Tcount == 2:
            #         if start_time + 1.0 > time.time():
            #             drive_controller.set_velocity(0)
            #             drive_controller.set_angular(-2.3)
            #             rospy.loginfo('turnning')
            #             drive_controller.drive()
            #     else:
            #         start_time = time.time()
            #         self.Tcount += 1
            #
            # elif self.Tcount == 3:
            #     rospy.loginfo('T_course_pass')

            if abs(err) > 0.17: #0.14
                drive_controller.set_velocity(0.4)
                drive_controller.set_angular(err)
                drive_controller.drive()
                #print(err)
            elif abs(err) < 0.17: #0.14
                #drive_controller.set_velocity(1)
                drive_controller.set_velocity(0.5)
                drive_controller.set_angular(err)
                drive_controller.drive()
                #print(err)
            rate.sleep()
        #return 'success'




class AvoidObstacle(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, ud):
        detect_obstacle = DetectObstacle()
        drive_controller = RobotDriveController()

        while not rospy.is_shutdown():
            rospy.sleep(1)
            if detect_obstacle.range_ahead > 2 or detect_obstacle.range_right > 2 or \
                    ((math.isnan(detect_obstacle.range_ahead)) and math.isnan(detect_obstacle.range_right)):
                rospy.sleep(3)
                value = False
                detect_obstacle.stop_pub.publish(value)
                print('go')

                return 'success'
            else:
                value = True
                detect_obstacle.stop_pub.publish(value)
                drive_controller.set_velocity(0)
                print('stop')

            #return 'success'


class DetectStopSign(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, ud):
        drive_controller = RobotDriveController()
        stop_sign_finder = ImageConverter()
        countfloor = 0
        if len(stop_sign_finder.contours) == 0:
            stop_sign_finder.drive_controller.set_velocity(0)
            print('stop')
        rospy.sleep(3)
        print('go!')
        stop_sign_finder.drive_controller.set_velocity(1)
        return "success"


