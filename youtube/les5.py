#نظام الاوان في الصورة
import cv2
img=cv2.imread('youtube/imges/baby.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#new size gry
new_size=cv2.resize(gray,(500,500))
#------------------------------------
cv2.imshow('baby',img)
cv2.imshow('new gry',new_size)
cv2.waitKey(0)