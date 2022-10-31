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

while True:
    ret,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    lmList=[]
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append((id,cx,cy))
            mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            x1,y1=lmList[20][1],lmList[20][2]
            x2,y2=lmList[0][1],lmList[0][2]
            lenght=math.hypot(x1-x2,y1-y2)
            if lenght<150:
                print('yes')
            else:
                print('no')
    cv2.imshow('rame',frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()