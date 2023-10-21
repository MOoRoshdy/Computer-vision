#عرض ابعاد الصورة والبكسلات
import cv2
img=cv2.imread('youtube\imges\car.jpg')
pix=img.size
dime=img.shape

print(f'the pixels is {pix}',f'the dimetion is {dime}')
cv2.imshow('cart',img)
cv2.waitKey(0)