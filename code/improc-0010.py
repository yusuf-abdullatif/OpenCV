import cv2
import math

# Initialize Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Camera image', frame)
        k = cv2.waitKey(100)
        if k == ord('q'):
            break
    else:
        print('ERROR ---> Camera not found!')

cv2.destroyAllWindows()

