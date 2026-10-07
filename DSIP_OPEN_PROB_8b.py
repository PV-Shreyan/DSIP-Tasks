import cv2
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms

img_beans = cv2.imread (r'C:\Users\PV shreyan\OneDrive\Pictures\IMP\DSIP_OPE_1.png', cv2.IMREAD_GRAYSCALE)
ref_pollen = cv2.imread (r'C:\Users\PV shreyan\OneDrive\Pictures\IMP\DSIP_OPE_3.png', cv2.IMREAD_GRAYSCALE)
ref_darker = cv2.imread (r'C:\Users\PV shreyan\OneDrive\Pictures\IMP\DSIP_OPE_3.png', cv2.IMREAD_GRAYSCALE)

# Perform Histogram Matching
matched_pollen = match_histograms (img_beans, ref_pollen)
matched_darker = match_histograms (img_beans, ref_darker)

plt.figure (figsize = (15, 10))

# Row 1: Matching Beans to Pollen
plt.subplot (2, 3, 1)
plt.imshow (img_beans, cmap = 'gray')
plt.title ('Target: Beans')

plt.subplot (2, 3, 2)
plt.imshow (ref_pollen, cmap = 'gray')
plt.title ('Reference: Pollen')

plt.subplot (2, 3, 3)
plt.imshow (matched_pollen, cmap = 'gray')
plt.title ('Matched Output (to Pollen)')

# Row 2: Matching Beans to Darker Beans
plt.subplot (2, 3, 4)
plt.imshow (img_beans, cmap = 'gray')
plt.title ('Target: Beans')

plt.subplot (2, 3, 5)
plt.imshow (ref_darker, cmap = 'gray')
plt.title ('Reference: Darker Beans')

plt.subplot (2, 3, 6)
plt.imshow (matched_darker, cmap = 'gray')
plt.title ('Matched Output (to Darker Beans)')

plt.tight_layout()
plt.show()