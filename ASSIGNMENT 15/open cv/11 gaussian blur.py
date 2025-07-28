import cv2
 
img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")

resize = cv2.resize(img,(640,640))
ksize = (7,7)
sigmax=0
sigmay=0

blur = cv2.GaussianBlur(resize,ksize,sigmax)

cv2.imshow("input",resize)
cv2.imshow("output",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()