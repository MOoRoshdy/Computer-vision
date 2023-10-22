#حفظ الصورة بالرمادي عند الضغط علي زر معين
import cv2
img=cv2.imread('youtube/imges/baby.jpg',0) #==>0= to gray
# img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray imge',img)
k=cv2.waitKey(0)

if k==27:   #27==> asci code= q or Esc or use ""ord('q)""
    cv2.destroyAllWindows()
    
elif k==ord('s'): #save imge when prees 's'
    
    cv2.imwrite('D:\\new_imge.jpg',img)
    # cv2.destroyAllWindows()