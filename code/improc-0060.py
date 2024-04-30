# we import all libraries used in our program
import cv2

# Initialize Camera
cap = cv2.VideoCapture(0)

# infinite loop
while True:
    # we read an image from the camera
    ret, frame = cap.read()
    # there is an image
    if ret:
        frame = cv2.flip(frame, flipCode = 1)
        frameBlur = cv2.GaussianBlur(frame, (3, 3), 0)
        frameGray = cv2.cvtColor(frameBlur, cv2.COLOR_BGR2GRAY)
        frameEdges = cv2.Laplacian(frameGray, cv2.CV_16S, ksize=3)
        frameFinalEdges = cv2.convertScaleAbs(frameEdges)
        # we display it
        cv2.imshow('Camera image', frame)
        cv2.imshow('Laplacian edges', frameFinalEdges)
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

