import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = r"images\dsip_logo.png" 
image = cv2.imread (image_path)

if image is None:
    print (f"Error: Could not load image from {image_path}. Please check the path.")
else:
    # Convert BGR (OpenCV default) to RGB for Matplotlib
    image_rgb = cv2.cvtColor (image, cv2.COLOR_BGR2RGB)

    # Define the size of the median filter kernel (should be an odd number) & adjust the size based on the desired smoothing level
    kernel_size = 5
    
    # Apply the Median filter for smoothing
    smoothed_image = cv2.medianBlur (image_rgb, kernel_size)

    plt.figure (figsize = (10, 5))

    plt.subplot (1, 2, 1)
    plt.title ('Original Image')
    plt.imshow (image_rgb)
    plt.axis ('off')

    plt.subplot (1, 2, 2)
    plt.title ('Median Filtered Image')
    plt.imshow (smoothed_image)
    plt.axis ('off')

    plt.tight_layout()
    plt.show()