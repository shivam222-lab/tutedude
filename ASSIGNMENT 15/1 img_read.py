import cv2

img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")

cv2.imshow("window",img)

cv2.waitKey(1000)

cv2.destroyAllWindows()