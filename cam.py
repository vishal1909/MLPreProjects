#!/usr/bin/python3

import numpy as np
import cv2
import os

cap=cv2.VideoCapture(0)

"""
if cap.isOpened()==True:
	print("camera is success")
else:
	print("else nothing to do")


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""

while(1):
	print("camera is running ...")
	ret,frame=cap.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("slot1",frame)
	if cv2.waitKey(2) & 0xFF == ord('/s'):
		break
cap.release()
cv2.destroyAllWindows()


