# we import all libraries used in our program
import cv2
import numpy
from matplotlib import pyplot as plt
# we load the image
img = cv2.imread('penna.bmp')
print('Shape: ', img.shape)
# infinite loop
frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(frame.ravel(),256,[0,256])
plt.show()

frameThreshold = ((frame>56).astype(numpy.uint8))*255
print(frameThreshold)
# we display it
cv2.imshow('Image', frame)
cv2.imshow('Image with threshold', frameThreshold)

# we wait for a key pressed
k = cv2.waitKey(0)

# we close all windows
cv2.destroyAllWindows()

