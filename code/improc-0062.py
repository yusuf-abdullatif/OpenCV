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
        #Edge-based segmentation
        #source: https://pyimagesearch.com/2015/11/02/watershed-opencv/
        shifted = cv2.pyrMeanShiftFiltering(frame, 21, 51)
        # convert the mean shift image to grayscale, then apply
        # Otsu's thresholding
        gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # we display it
        cv2.imshow("Original", frame)   
        cv2.imshow("Threshold", thresh)
   
        # we wait for a key pressed
        k = cv2.waitKey(10)
        # if it is 'q', we quit
        if k == ord('q'):
            break

# we close all windows
cv2.destroyAllWindows()

