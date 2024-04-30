# we import all libraries used in our program
import cv2
import numpy
# Initialize Camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# infinite loop
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, flipCode = 1)
        mean = numpy.mean(frame)
        min = numpy.min(frame)
        max = numpy.max(frame)
        stddev = numpy.std(frame)
        print('Statistics: min, max, mean, stddev ---> ', min, max, mean, stddev)
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

