#!/usr/bin/python3
import  cv2
import numpy as np    # importing required modules
import random
face_cascade = cv2.CascadeClassifier('a.xml')    # detecting face we have xml file which contain trained data.
eye_cascade=cv2.CascadeClassifier('b.xml')
cap=cv2.VideoCapture(0)		# capture video


"""
x=np.random.random()
y=str(x)[3:6]
cv2.imwrite("adhoc"+y+".jpg", img)
"""
		

while True:
    ret, img = cap.read()      # frame running from webcam
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)   # 1.3 scaling factor # 5 no. of neighbors in one rectangle

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]    # eyes are within faces so its range where they can found
        roi_color = img[y:y+h, x:x+w]
	
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)   

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break





	
cap.release()
cv2.destroyAllWindows()




