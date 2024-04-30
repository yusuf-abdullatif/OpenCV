# we import all libraries used in our program
import cv2
import datetime
print("---> OpenCV version : {0}".format(cv2.__version__))
# Initialize Camera
cap = cv2.VideoCapture(0)
# infinite loop
while True:
    # we read an image from the camera
    ret, frame = cap.read()
    # there is an image
    if ret:
        frame = cv2.flip(frame, flipCode = 1)
        # we display it
        cv2.imshow('Camera image', frame)
        # we wait for a key pressed
        k = cv2.waitKey(10)
        # if it is 'q', we quit
        if k == ord('q'):
            break
        if k == ord('s'):
            x = datetime.datetime.now()
            filenameRGB = 'outRGB'+str(x.year)+str(x.month)+str(x.day)+str(x.hour)+str(x.minute)+str(x.second)+'.png'
            cv2.imwrite(filenameRGB, frame)
            print('Image ', filenameRGB, ' saved...')
    # there is no image
    else:
        print('ERROR ---> Camera not found!')

# we close all windows
cv2.destroyAllWindows()

