#!/ur/bin/python3

import cv2

img=cv2.imread("vishal.jpg")
print (img.shape)
print (img.dtype)
print (img.size)

pic=cv2.imread("im.jpg")
#PADDING action
# to make the borders we have cv2.copyMakeBorder()
# argument( src, left,right ,top,bottom ,type of border)
#type of border: BORDER_CONSTANT,BORDER_REFLECT,BORDER_REPLICATE


ball = pic[280:340, 330:390]
print(ball)
image=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT)
picture=cv2.copyMakeBorder(pic,10,10,10,10,cv2.BORDER_REFLECT)
cv2.imshow("plot1:", image)
cv2.imshow("plot2:",picture)
#cv2.imshow("plot3",ball)
cv2.waitKey(0)





