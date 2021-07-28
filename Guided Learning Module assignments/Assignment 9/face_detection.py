import cv2
import os

cap = cv2.VideoCapture(0)
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
cascade_classifier = cv2.CascadeClassifier(haar)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    detections = cascade_classifier.detectMultiScale(frame, 1.5, 3)
    if (len(detections)>0):
        (x,y,w,h) = detections[0]
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('Frame', frame)
    if (cv2.waitKey(10) & 0xFF == ord('q')):
        break
    cv2.destroyAllWindows()

cap.release()