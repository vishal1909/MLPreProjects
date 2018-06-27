#!/usr/bin/python3

import cv2
import numpy as np
import random 

cam=cv2.VideoCapture(0)

while(1):
	print("camera is running")
	status,frame=cam.read()
	#vid=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow("slot 1" , img)
	x=np.random.random()
	y=str(x)[3:6]
	cv2.imwrite("img"+y+".jpg", frame)

cam.release()


