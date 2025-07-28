import cv2
import numpy as np

img =cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")
width = 600
height=850
dim = (width,height)
resized=cv2.resize(img,dim)

kernel = np.ones((5,5),dtype='uint8')
# erosion = cv2.erode(resized,kernel,iterations=1)
# dilation = cv2.dilate(resized,kernel,iterations=1)
# opening=cv2.morphologyEx(resized,cv2.MORPH_OPEN,kernel)
# closing = cv2.morphologyEx(resized,cv2.MORPH_CLOSE,kernel)
# gradient = cv2.morphologyEx(resized,cv2.MORPH_GRADIENT,kernel)
topht = cv2.morphologyEx(resized,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(resized,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("original",resized)
# cv2.imshow("erosion",erosion)
# cv2.imshow("dilation",dilation)
# cv2.imshow("opening",opening)
# cv2.imshow("closing",closing)
# cv2.imshow("gradient",gradient)
cv2.imshow("topht",topht)
cv2.imshow("blackhat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()