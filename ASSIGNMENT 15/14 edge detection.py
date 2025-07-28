#canny edge detection
#noise reduction
#intenstity of the qradient of the image
#non-maximum suppression
#thresholding

import cv2

img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/bired img.jpeg",0)
resize = cv2.resize(img,(520,520))
min_thresh = 100
max_thresh = 200
edges = cv2.Canny(resize,min_thresh,max_thresh)
cv2.imshow("oeiginal",resize)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()