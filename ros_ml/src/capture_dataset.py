#!/usr/bin/env python3
import rospy
from move_robot import MoveRobot
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
import os

msg = Pose()

class RobotGo:
    def __init__(self):
        self.sub = rospy.Subscriber('/odom', Odometry, self.callback)
        self.moverobot_object = MoveRobot()
        self.i = 0
        self.flag = False

    def callback(self, msg):
        xx = msg.pose.pose.position.x
        yy = msg.pose.pose.position.y

        if(self.flag == False):
            print(xx,'::', yy)
            file1.write("%f, %f\n" %((xx),(yy)))

        linear_x = 0.25
        angular_z = 0.085
        self.moverobot_object.send_cmd(linear_x, angular_z)
        self.i = self.i+1
        if self.i > 300:
            self.flag = True
            linear_x = 0.0
            angular_z = 0.0
            self.moverobot_object.send_cmd(linear_x, angular_z)

if __name__=="__main__":
    try:
        os.mkdir('/home/ssiddharth/catkin_ws/src/ros_ml/results')
    except:
        print('folder already exists')
        pass
    file1 = open('/home/ssiddharth/catkin_ws/src/ros_ml/results/test.csv', "w+")
    rospy.init_node('node')
    stopwall_object = RobotGo()
    rospy.spin()


    