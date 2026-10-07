import cv2
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms

img_med = cv2.imread (r'C:\Users\PV shreyan\OneDrive\Pictures\IMP\DSIP_OPE_5.png', cv2.IMREAD_GRAYSCALE)
img_darker = cv2.imread (r'C:\Users\PV shreyan\OneDrive\Pictures\IMP\DSIP_OPE_3.png', cv2.IMREAD_GRAYSCALE)

# Perform Histogram Matching
matched_med = match_histograms (img_med, img_darker)

plt.figure (figsize = (12, 4))

# Row 1: Matching Car to Pollen
plt.subplot (1, 3, 1)
plt.imshow (img_med, cmap = 'gray')
plt.title ('Target: Med Scan')

plt.subplot (1, 3, 2)
plt.imshow (img_darker, cmap = 'gray')
plt.title ('Reference: Beans')

plt.subplot (1, 3, 3)
plt.imshow (matched_med, cmap = 'gray')
plt.title ('Matched Output (to Beans)')

plt.tight_layout()
plt.show()