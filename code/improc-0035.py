import cv2
import datetime

#source: https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
cap = cv2.VideoCapture('outRGB2023414131958.avi')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

x = datetime.datetime.now()
ret, frame = cap.read()
fileRGB = 'noiseRGB'+str(x.year)+str(x.month)+str(x.day)+str(x.hour)+str(x.minute)+str(x.second)+'.avi'
outRGB = cv2.VideoWriter(fileRGB,cv2.VideoWriter_fourcc(*'MJPG'), 30, (frame.shape[1],frame.shape[0]))

ret, oldFrame = cap.read()
oldFrame = cv2.blur(oldFrame, (5,5))

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, newFrame = cap.read()

  if ret == True:
    # Display the resulting frame
    newFrame = cv2.blur(newFrame, (5,5))
    cv2.imshow('Video', newFrame-oldFrame)
    outRGB.write(newFrame-oldFrame)

    oldFrame = newFrame.copy()
    # Press Q on keyboard to  exit
    k = cv2.waitKey(25)
    if k == ord('q'):
      break
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
outRGB.release()
 
# Closes all the frames
cv2.destroyAllWindows()
