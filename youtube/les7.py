#رسم الاشكال والكتابة علي الصور
import cv2
import numpy as np  #==>to drow
img=cv2.imread('youtube/imges/baby.jpg')
#line-rectangle-text
#startline,endlin,color,thikness line

# cv2.line(img,(10,10),(100,10),(0,233,0),6)
# cv2.rectangle(img,(300,10),(100,300),(0,233,0),6)
# cv2.putText(img,'baby face',(200,90),cv2.FONT_ITALIC,2,(0,255,0),5)

cv2.imshow('car',img)

cv2.waitKey(0)