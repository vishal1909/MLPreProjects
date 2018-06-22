#!/usr/bin/python3

import cv2
import os

""" 
image=cv2.imread("im.jpg",0)
pic=cv2.copyMakeBorder(image,15,15,15,15,cv2.BORDER_CONSTANT)
cv2.imshow("slot1",pic)
cv2.waitKey(0)

"""


print ("IMAGE OPERATIONS AND EDITING")


x="""
Press1:  To draw a line
Press2:  To draw a circle
Press3:  To draw a rectangle
Press4:  To draw a ellipse
Press5:  To make border on image
Press6:	 To exit from menu...
  """

print(x)
choice=int(input("Enter the choice"))
if choice==1:
	print (" Available images:")
	os.system( " ls  | grep .jpg")
	image=input("enter the image name")
	img=cv2.imread("{0}".format(image))
	pic=cv2.line(img,(0,0),(100,200),(100,255,255),2) #arguments(src,starting,ending,(color channel),line width)
	cv2.imshow("slot1",pic)
	cv2.waitKey(0)
if choice==2:
	print (" Available images:")
	os.system( " ls  | grep .jpg")
	image=input("enter the image name")
	img=cv2.imread("{0}".format(image))
	pic=cv2.circle(img,(100,150),(20),(100,255,255),2) #arguments(src,center,radius,(color channel),line width)
	cv2.imshow("slot1",pic)
	cv2.waitKey(0)
if choice==3:
	print (" Available images:")
	os.system( " ls  | grep .jpg")
	image=input("enter the image name")
	img=cv2.imread("{0}".format(image))
	pic=cv2.rectangle(img,(100,50),(400,300),(100,255,255),2) #arguments(src,starting,ending,(color channel),line width)
	cv2.imshow("slot1",pic)
	cv2.waitKey(0)
if choice==4:
	print (" Available images:")
	os.system( " ls  | grep .jpg")
	image=input("enter the image name")
	img=cv2.imread("{0}".format(image))
	pic = cv2.ellipse(img,(100,100),(100,50),0,0,180,(255,255,255),-1) #arguments(src,center,length of axes,rotation ,start angle,ending    										angle,(color channel),filling)
	cv2.imshow("slot1",pic)
	cv2.waitKey(0)
if choice==5:
	print (" Available images:")
	os.system( " ls  | grep .jpg")
	image=input("enter the image name")
	img=cv2.imread("{0}".format(image))
	pic = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT)  #arguments(src,top,left,bottom,right, type of border)
	cv2.imshow("slot1",pic)
	cv2.waitKey(0)
if choice==6:
	print("Goodbye...")
	exit()
	

	



