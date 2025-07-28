import cv2

img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg",0)

cv2.imshow("window",img)

cv2.imwrite("car.jpg",img)

cv2.waitKey(1000)

cv2.destroyAllWindows()