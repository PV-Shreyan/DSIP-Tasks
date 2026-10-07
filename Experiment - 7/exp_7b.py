import cv2
import matplotlib.pyplot as plt

img = cv2.imread (r"images\dsip_logo.png")

img_gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

plt.figure (figsize = (6, 6))
plt.imshow (img_gray, cmap = 'gray')
plt.title ("Grayscale Image")
plt.axis ("off")
plt.show ()