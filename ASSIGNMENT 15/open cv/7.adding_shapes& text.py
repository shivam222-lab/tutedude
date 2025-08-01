import cv2
import numpy as np

# img = cv2.imread("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/img.jpg")
img=np.zeros(shape=[600,800,3],dtype='uint8')
# img.fill(255)
cv2.line(img,(0,0),(150,150),(255,0,0),2)

cv2.rectangle(img,(200,150),(250,300),(0,255,0),3)
cv2.circle(img,(300,75),70,(255,0,255),3)

pts_polygon = np.array([[100,50],[100,300],[500,50],[500,300]], np.int32)
cv2.polylines(img,[pts_polygon],True,(0,255,255),3)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'HELLO',(0,500),font,3,(200,255,255),8,cv2.LINE_AA)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()