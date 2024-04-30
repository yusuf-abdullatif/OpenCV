# we import all libraries used in our program
import cv2

# we read an image from disk to memory
img = cv2.imread('img/jonkoping-01.jpg')

# we change some pixels values
img[0:100, 0:200, :] = 0

# we print the information concerning this image
print('---> Shape: ', img.shape)
print('---> Image nd-array: ', img)

# we show the image and wait for a key to be pressed
cv2.imshow('Jonkoping', img)
key = cv2.waitKey(0)

cv2.destroyAllWindows()
