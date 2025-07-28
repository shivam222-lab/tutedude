import cv2

img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")

width=600
height= 850
dim =(width,height)

resized=cv2.resize(img,dim)
print("size in bytes",img.size)
cv2.imshow("original",resized)

flip =cv2.flip(resized,1)
cv2.imshow("horizontal",flip)

flip2=cv2.flip(resized,0)
cv2.imshow('vertical',flip2)

flip3 = cv2.flip(resized,-1)
cv2.imshow("horizontal & vertical",flip3)

cv2.waitKey(0)
cv2.destroyAllWindows()
