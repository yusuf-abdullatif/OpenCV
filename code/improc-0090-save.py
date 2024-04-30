import cv2
import datetime

# Initialize Camera
cap = cv2.VideoCapture(1)
ret, frame = cap.read()

x = datetime.datetime.now()

filenameRGB = 'outRGB'+str(x.year)+str(x.month)+str(x.day)+str(x.hour)+str(x.minute)+str(x.second)+'.avi'
print("---> filenames: ", filenameRGB)
outRGB = cv2.VideoWriter(filenameRGB,cv2.VideoWriter_fourcc(*'MJPG'), 30, ( frame.shape[1], frame.shape[0] ))


print(" ")
print(" ")
print("----------------------------------")
print("----------------------------------")
print(str(datetime.datetime.now()) + " ---> ENTERING VIDEO LOOP...")
print("----------------------------------")
print("----------------------------------")
print(" ")
print(" ")

numberOfImagesInVideo = 600

nb = 0
# Main loop of the program: getting all the images forever... until ESC in fact.
while nb<numberOfImagesInVideo:
    ret, frame = cap.read()
    if ret==True:
        outRGB.write(frame)
    else:
        print('ERROR ---> Camera not found!')
    nb += 1


print(" ")
print("---> Hej då - Goodbye - Au revoir")
print(" ")
print(str(datetime.datetime.now()) + " --- The End ---")
print(" ")
print(" ")

outRGB.release()
