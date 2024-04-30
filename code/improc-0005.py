# we import all libraries used in our program
import cv2
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
# we read an image from disk to memory
img = cv2.imread('img/jonkoping-01.jpg')
# we flip the image to get the good view during 3d projection
img2 = cv2.flip(src = img, flipCode = 1)
# we show the image and wait for a key to be pressed
cv2.imshow('Jonkoping', img)
key = cv2.waitKey(0)
# 3d mesh grid of an image
#source: https://www.geeksforgeeks.org/3d-surface-plotting-in-python-using-matplotlib/
# we make the data from our image
X = np.arange(img2.shape[1])
Y = np.arange(img2.shape[0])
X, Y = np.meshgrid(X, Y)
# we plot the surface
fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})
fig2, ax2 = plt.subplots(subplot_kw={"projection": "3d"})
fig3, ax3 = plt.subplots(subplot_kw={"projection": "3d"})
ax1.plot_surface(X, Y, img2[:,:,0], vmin = img2[:,:,0].min() * 2, cmap = cm.Blues)
ax2.plot_surface(X, Y, img2[:,:,1], vmin = img2[:,:,1].min() * 2, cmap = cm.Greens)
ax3.plot_surface(X, Y, img2[:,:,2], vmin = img2[:,:,2].min() * 2, cmap = cm.Reds)
# we show the surfaces
plt.show()
cv2.destroyAllWindows()

