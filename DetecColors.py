import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ORANGE_MIN = np.array([5, 50, 50])
ORANGE_MAX = np.array([15, 255, 255])

while True:
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, ORANGE_MIN, ORANGE_MAX)
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()