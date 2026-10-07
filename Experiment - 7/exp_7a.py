import cv2
import matplotlib.pyplot as plt

img = cv2.imread (r"images\dsip_logo.png")

img_rgb = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)

plt.figure (figsize = (6, 6))
plt.imshow (img_rgb)
plt.title ("Input Image")
plt.axis ("off")
plt.show ()