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

    # Define the size of the Averaging filter kernel & adjust the size based on the desired smoothing level
    kernel_size = (5, 5)
    
    # Create the Averaging filter kernel
    kernel = np.ones (kernel_size, dtype = np.float32) / (kernel_size[0] * kernel_size[1])
    
    # Apply the Averaging filter for smoothing
    smoothed_image = cv2.filter2D (image_rgb, -1, kernel)

    plt.figure (figsize = (10, 5))

    plt.subplot (1, 2, 1)
    plt.title ('Original Image')
    plt.imshow (image_rgb)
    plt.axis ('off')

    plt.subplot (1, 2, 2)
    plt.title ('Averaged (Smoothed) Image')
    plt.imshow (smoothed_image)
    plt.axis ('off')

    plt.tight_layout()
    plt.show()