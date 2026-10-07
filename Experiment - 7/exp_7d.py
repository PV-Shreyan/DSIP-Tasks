import cv2
import matplotlib.pyplot as plt

img = cv2.imread (r"images\dsip_logo.png")

img_gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

img_thresh = cv2.adaptiveThreshold (img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.figure (figsize = (6, 6))
plt.imshow (img_thresh, cmap = 'gray')
plt.title ("Adaptive Thresholded Image")
plt.axis ("off")
plt.show ()
