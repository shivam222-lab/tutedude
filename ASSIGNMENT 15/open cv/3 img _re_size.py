import cv2

img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")

print("dimensions of the image: ",img.shape)
# width =\ img.shape[1]
# height = 400
# width = 400
# height = img.shape[0]
width=400
height=400
dim  =(width,height)
resized =cv2.resize(img,dim)

cv2.imshow("window",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()