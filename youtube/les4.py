#تغير حجم الصورة واالنافزة
import cv2
img=cv2.imread('youtube\imges\car.jpg')
new_imge=cv2.resize(img,(500,200))
cv2.imshow("car",img)
cv2.imshow('car cut',new_imge)
cv2.waitKey(0)
