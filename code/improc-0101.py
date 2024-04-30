# we import all libraries used in our program
import cv2
import datetime
print("---> OpenCV version : {0}".format(cv2.__version__))
#source: https://thinkinfi.com/detect-mouse-click-events-with-python-opencv/
listPoints = []
def mousePoints(event,x,y,flags,params):
    global listPoints
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        listPoints.append([x, y])
        print(listPoints)
# Initialize Camera
cap = cv2.VideoCapture(0)
# infinite loop
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, flipCode = 1)
        cv2.imshow('Camera image', frame)
        cv2.setMouseCallback("Camera image", mousePoints)
        k = cv2.waitKey(10)
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
