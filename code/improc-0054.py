import cv2
import numpy

#source: https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
cap = cv2.VideoCapture('bridgeRGB2023414161111.avi')
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
ret, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
sumImages = numpy.zeros(frame.shape)
nb = 0 

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    # add the image to the sum
    sumImages += cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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

cap = cv2.VideoCapture('bridgeRGB2023414161111.avi')
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
  diff = (((backgroundImage-cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))<200)*255).astype(numpy.uint8)
  print(diff)
  cv2.imshow('Moving regions', diff)
  key = cv2.waitKey(10)
  if key == ord('q'):
    break

# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
