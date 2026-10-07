import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path =  r"images\DSIP_OPE_7(4).png"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Power-Law (Gamma) Transformation
gamma = 0.5 # Change gamma to >1 to darken, <1 to brighten
img_normalized = img / 255.0
img_gamma = np.power (img_normalized, gamma)
img_gamma = np.uint8 (img_gamma * 255)

# Plotting
plt.figure (figsize = (10, 4))

plt.subplot (1, 2, 1)
plt.imshow (img, cmap = 'gray')
plt.title ("Original Image")

plt.subplot (1, 2, 2)
plt.imshow (img_gamma, cmap = 'gray')
plt.title (f"Power-Law (Gamma = {gamma})")

plt.show ()