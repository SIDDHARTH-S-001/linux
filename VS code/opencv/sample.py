#import numpy as np
#import matplotlib.pyplot as plt
#import PIL
import cv2
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('img', img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break