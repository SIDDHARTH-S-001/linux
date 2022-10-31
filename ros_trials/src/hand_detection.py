#!/usr/bin/env python
import rospy
import mediapipe as mp
import cv2
import math
from geometry_msgs.msg import Twist
import sys
import time

cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
rospy.init_node('hand_gesture_control',anonymous=True)
velocity_publisher=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

def turnLeft(velocity_publisher,lmList):
    velocity_message=Twist()
    loop_rate = rospy.Rate(10)
    x1,y1=lmList[20][1],lmList[20][2]
    x2,y2=lmList[0][1],lmList[0][2]
    lenght=math.hypot(x1-x2,y1-y2)
    while True:
        if lenght<150:
           velocity_message.angular.z=-0.01
           velocity_publisher.publish(velocity_message)
        else:
            break
    velocity_message.angular.z=0
    velocity_publisher.publish(velocity_message)

def turnRight(velocity_publisher,lmList):
    velocity_message=Twist()
    loop_rate = rospy.Rate(10)
    x11,y11=lmList[8][1],lmList[8][2]
    x21,y21=lmList[0][1],lmList[0][2]
    lenght=math.hypot(x11-x21,y11-y21)
    while True:
        if lenght<150:
           velocity_message.angular.z=0.01
           velocity_publisher.publish(velocity_message)
        else:
            break
    velocity_message.angular.z=0
    velocity_publisher.publish(velocity_message)

def forward(velocity_publisher,lmList):
    velocity_message=Twist()
    loop_rate = rospy.Rate(10)
    x12,y12=lmList[12][1],lmList[12][2]
    x22,y22=lmList[0][1],lmList[0][2]
    lenght=math.hypot(x12-x22,y12-y22)
    while True:
        if lenght<150:
           velocity_message.linear.y=0.01
           velocity_publisher.publish(velocity_message)
        else:
            break
    velocity_message.linear.y=0
    velocity_publisher.publish(velocity_message)

while True:
    ret,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('rame',frame)
    results=hands.process(imgRGB)
    lmList=[]
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append((id,cx,cy))
            mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            turnLeft(velocity_publisher,lmList)
            forward(velocity_publisher,lmList)
            turnRight(velocity_publisher,lmList)
    time.sleep(2)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
