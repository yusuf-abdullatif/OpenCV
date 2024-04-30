# we import all libraries used in our program
import cv2
import numpy
# Initialize Camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print("Shape: ", frame.shape)
nb = 0
# infinite loop
while True:
    # we read an image from the camera
    ret, frame = cap.read()
    # there is an image
    if ret:
        frame = cv2.flip(frame, flipCode = 1)
        frame1 = frame[0:frame.shape[0]//2, 0:frame.shape[1]//2]
        frame2 = frame[frame.shape[0]//2:frame.shape[0], 0:frame.shape[1]//2]
        frame3 = frame[0:frame.shape[0]//2, frame.shape[1]//2:frame.shape[1]]
        frame4 = frame[frame.shape[0]//2:frame.shape[0], frame.shape[1]//2:frame.shape[1]]
        if nb==0:
            print("shapes 1,2,3,4: ", frame1.shape, frame2.shape, frame3.shape, frame4.shape)
        nb += 1
        frame1 = cv2.Canny(frame1, 100, 200)
        frame2 = ((frame2>127)*255).astype(numpy.uint8)
        frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
        frame4 = 255 - frame4
        # we display it
        cv2.imshow('Camera image', frame)
        cv2.imshow('subimage 1', frame1)
        cv2.imshow('subimage 2', frame2)
        cv2.imshow('subimage 3', frame3)
        cv2.imshow('subimage 4', frame4)
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

