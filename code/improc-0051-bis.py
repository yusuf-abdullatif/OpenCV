import cv2
import numpy

#source: https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
#ap = cv2.VideoCapture('padelpoint.mp4')
cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
ret, frame = cap.read()
sumImages = numpy.zeros(frame.shape)
nb = 0 

# Read until video is completed
while nb<300:
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

while True:
  # Capture frame-by-frame
  ret, frame = cap.read()
  cv2.imshow('Moving regions', numpy.abs(backgroundImage-frame))
  key = cv2.waitKey(10)
  if key == ord('q'):
    break
# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
