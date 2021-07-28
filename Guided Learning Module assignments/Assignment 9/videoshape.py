import numpy as np
import cv2
video = cv2.VideoCapture('video.mp4')
while(True):
    ret, frame=video.read()
    cv2.rectangle(frame,(100,100),(400,500),(0,255,0),3)
    cv2.circle(frame,(500,500),100,(255,153,255),3)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
