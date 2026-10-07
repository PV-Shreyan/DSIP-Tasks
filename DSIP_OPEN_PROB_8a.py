import cv2
import matplotlib.pyplot as plt

img_med = cv2.imread (r'C:\Users\PV shreyan\OneDrive\Pictures\IMP\DSIP_OPE_5.png', cv2.IMREAD_GRAYSCALE)

# Global Histogram Equalization
ghe_med = cv2.equalizeHist (img_med)

# CLAHE
clahe = cv2.createCLAHE (clipLimit = 2.0, tileGridSize = (8, 8))
clahe_med = clahe.apply (img_med)

plt.figure (figsize = (12, 4))
plt.subplot (1, 3, 1), plt.imshow (img_med, cmap = 'gray'), plt.title ("Original Image")
plt.subplot (1, 3, 2), plt.imshow (ghe_med, cmap = 'gray'), plt.title ("GHE Output")
plt.subplot (1, 3, 3), plt.imshow (clahe_med, cmap = 'gray'), plt.title ("CLAHE Output")
plt.show()