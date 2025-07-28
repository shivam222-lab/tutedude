import cv2

img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")

resize = cv2.resize(img,(520,520))
kernel =3
blur =cv2.medianBlur(resize,kernel)

cv2.imshow("input",resize)
cv2.imshow("output",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()