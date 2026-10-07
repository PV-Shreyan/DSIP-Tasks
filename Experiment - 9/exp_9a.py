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

    # Define Gaussian kernel for smoothing
    kernel_size = (5, 5)
    sigma = 1.5
    gaussian_kernel = cv2.getGaussianKernel (kernel_size[0], sigma)
    gaussian_kernel = np.outer (gaussian_kernel, gaussian_kernel)

    # Apply Gaussian smoothing
    smoothed_image = cv2.filter2D (image_rgb, -1, gaussian_kernel)

    # Define sharpening kernel
    sharpening_kernel = np.array ([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])

    # Apply sharpening
    sharpened_image = cv2.filter2D (image_rgb, -1, sharpening_kernel)

    # Display all three images side-by-side
    plt.figure (figsize = (15, 5))

    plt.subplot (1, 3, 1)
    plt.title ('Original Image')
    plt.imshow (image_rgb)
    plt.axis ('off')

    plt.subplot (1, 3, 2)
    plt.title ('Smoothed Image')
    plt.imshow (smoothed_image)
    plt.axis ('off')

    plt.subplot (1, 3, 3)
    plt.title ('Sharpened Image')
    plt.imshow (sharpened_image)
    plt.axis ('off')

    plt.tight_layout()
    plt.show()