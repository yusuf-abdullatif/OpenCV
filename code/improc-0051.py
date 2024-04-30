import cv2
import numpy

#source: https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
cap = cv2.VideoCapture('padelpoint.mp4')
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
ret, frame = cap.read()
sumImages = numpy.zeros(frame.shape)
nb = 0 

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    # add the image to the sum
    sumImages += frame
    nb += 1
  else:
    break

avgImages = sumImages / nb
avgImages = avgImages.astype(numpy.uint8)
cv2.imshow('sumImages', avgImages)
key = cv2.waitKey(0)

backgroundImage = avgImages.copy()
# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
