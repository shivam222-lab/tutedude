import cv2

video = cv2.VideoCapture("C:/Users/ozash/OneDrive/Pictures/Camera imports/Desktop/video.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("output.mp4",fourcc,59.94,(1280,720))

while video.isOpened():
    ret,frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow("frame",frame)

        if cv2.waitKey(10)==ord('s'):
            break
    else:
         break
cv2.destroyAllWindows()