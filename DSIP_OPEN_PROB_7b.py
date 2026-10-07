import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r"images\DSIP_OPE_7(5).png"
img = cv2.imread (img_path, cv2.IMREAD_GRAYSCALE)

# Logarithmic Transformation
c = 255 / np.log (1 + np.max (img))
img_log = c * (np.log (1 + img.astype (np.float32)))
img_log = np.array (img_log, dtype = np.uint8)

# Plotting
plt.figure (figsize = (10, 4))
plt.subplot (1, 2, 1)
plt.imshow (img, cmap = 'gray')
plt.title ("Original Image")

plt.subplot (1, 2, 2)
plt.imshow (img_log, cmap = 'gray')
plt.title ("Logarithmic Transform")
plt.show ()