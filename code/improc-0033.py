import cv2
import numpy as np

#source: https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
cap = cv2.VideoCapture('outRGB2023414131958.avi')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

ret, oldFrame = cap.read()

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, newFrame = cap.read()
  if ret == True:
    # Display the resulting frame
    cv2.imshow('Video', newFrame-oldFrame)
    oldFrame = newFrame.copy()
    # Press Q on keyboard to  exit
    k = cv2.waitKey(25)
    if k == ord('q'):
      break
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
