# we import all libraries used in our program
import cv2
import numpy

# we read an image from disk to memory
img = cv2.imread('img/jonkoping-01.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgLab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
imgLuv = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
imgXYZ = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
print("---> Stats:")
print("shape, (min, max, avg) RGB: ", img.shape, ', ', numpy.min(img), numpy.max(img), numpy.mean(img))
print("shape, (min, max, avg) Gray: ", imgGray.shape, ', ', numpy.min(imgGray), numpy.max(imgGray), numpy.mean(imgGray))
print("shape, (min, max, avg) HSV: ", imgHSV.shape, ', ', numpy.min(imgHSV), numpy.max(imgHSV), numpy.mean(imgHSV))
print("shape, (min, max, avg) Lab: ", imgLab.shape, ', ', numpy.min(imgLab), numpy.max(imgLab), numpy.mean(imgLab))
print("shape, (min, max, avg) Luv: ", imgLuv.shape, ', ', numpy.min(imgLuv), numpy.max(imgLuv), numpy.mean(imgLuv))
print("shape, (min, max, avg) XYZ: ", imgXYZ.shape, ', ', numpy.min(imgXYZ), numpy.max(imgXYZ), numpy.mean(imgXYZ))
# we show the image and wait for a key to be pressed
cv2.imshow('Jonkoping original', img)
cv2.imshow('Jonkoping gray', imgGray)
cv2.imshow('Jonkoping Lab', imgLab)
cv2.imshow('Jonkoping HSV', imgHSV)
cv2.imshow('Jonkoping Luv', imgLuv)
cv2.imshow('Jonkoping XYZ', imgXYZ)
key = cv2.waitKey(0)

cv2.destroyAllWindows()
