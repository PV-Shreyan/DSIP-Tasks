import cv2
import matplotlib.pyplot as plt

img_path = r"images\DSIP_OPE_7(5).png" 
img = cv2.imread (img_path, cv2.IMREAD_GRAYSCALE)

# Linear Transformation (Negative)
img_negative = 255 - img

# Plotting
plt.figure (figsize = (10, 4))
plt.subplot (1, 2, 1)
plt.imshow (img, cmap = 'gray')
plt.title ("Original Image")

plt.subplot (1, 2, 2)
plt.imshow (img_negative, cmap = 'gray')
plt.title ("Linear Transform (Negative)")

plt.show ()