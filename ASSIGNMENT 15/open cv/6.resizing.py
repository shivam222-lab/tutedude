import cv2

img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")

print("dimensions of original imgae",img.shape)


scale = 50
width = int(img.shape[1]*scale/100)
height = int(img.shape[0]*scale/100)

dim = (width,height)

resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print("dimensions of resied image :",resized.shape)

cv2.imshow('resized',resized)
cv2.imshow('original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()