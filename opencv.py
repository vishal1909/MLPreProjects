#!/usr/bin/python3


import cv2


a=cv2.imread("vishal.jpg")
b=cv2.imread("im.jpg")
c=cv2.imread("vishal.jpg",0)    # 0 for grayscale
d=cv2.imread("im.jpg",0)   	#1 for color image
				# -1 for unchanged image

print(a.shape)
print(b.shape)
e=print(a[600][500])

a[600][500]=[0,0,0]
print( " new value:", a[600][500])

cv2.imshow("slot1",a)
cv2.imshow("slot2",b)
cv2.imshow("slot3",c)
cv2.imshow("slot4",d)

cv2.imshow("slot5",a[600][500])
cv2.imshow("slot6",a[297][383])


cv2.imwrite("copy.jpg",c)

cv2.waitKey(0)


cv2.destroyALLWindows()




