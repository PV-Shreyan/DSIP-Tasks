import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r"images\DSIP_OPE_7(5).png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Piecewise-Linear (Contrast Stretching)
# Maps the min intensity to 0 and max to 255
min_val = np.min (img)
max_val = np.max (img)
img_stretched = ((img - min_val) / (max_val - min_val)) * 255
img_stretched = np.uint8 (img_stretched)

# Plotting
plt.figure (figsize = (10, 4))

plt.subplot (1, 2, 1)
plt.imshow (img, cmap = 'gray')
plt.title ("Original Image")

plt.subplot (1, 2, 2)
plt.imshow (img_stretched, cmap = 'gray')
plt.title ("Piecewise-Linear (Contrast Stretch)")

plt.show()