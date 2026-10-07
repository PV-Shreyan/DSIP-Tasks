import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread (r"images\dsip_logo.png")

img_gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

gamma = 0.5
img_gamma = np.array (255 * (img_gray / 255) ** gamma, dtype = np.uint8)

plt.figure (figsize = (6, 6))
plt.imshow (img_gamma, cmap = 'gray')
plt.title ("Gamma Transformed Image")
plt.axis ("off")
plt.show ()
