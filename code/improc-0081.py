# we import all libraries used in our program
import cv2
import numpy
from matplotlib import pyplot as plt
# Initialize Camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# infinite loop
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, flipCode = 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plt.hist(frame.ravel(),256,[0,256])
        plt.show()
        # we display it
        cv2.imshow('Camera image', frame)
        # we wait for a key pressed
        k = cv2.waitKey(10)
        # if it is 'q', we quit
        if k == ord('q'):
            break
    # there is no image
    else:
        print('ERROR ---> Camera not found!')

# we close all windows
cv2.destroyAllWindows()

