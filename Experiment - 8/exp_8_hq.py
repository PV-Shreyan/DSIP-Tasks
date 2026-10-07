import cv2
import matplotlib.pyplot as plt

image_path = r"images\dsip_logo.png"
image = cv2.imread (image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image from {image_path}. Please ensure the file exists and the path is correct.")
else:
    # Calculate the histogram
    histogram_original = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Calculate the histogram of the equalized image
    histogram_equalized = cv2.calcHist ([equalized_image], [0], None, [256], [0, 256])

    # Display the original and equalized images & histogram
    plt.figure (figsize = (10, 8))

    plt.subplot (2, 2, 1)
    plt.title ('Original Image')
    plt.imshow (image, cmap = 'gray')
    plt.axis ('off')

    plt.subplot (2, 2, 2)
    plt.title ('Equalized Image')
    plt.imshow (equalized_image, cmap = 'gray')
    plt.axis ('off')

    # Plot the histogram of Image
    plt.subplot (2, 2, 3)
    plt.title ('Histogram')
    plt.xlabel ('Pixel Value')
    plt.ylabel ('Frequency')
    plt.plot (histogram_original)
    plt.xlim ([0, 256])
    plt.grid (True)

    # Plot the histogram of Equalized Image
    plt.subplot (2, 2, 4)
    plt.title ('Histogram of Equalized Image')
    plt.xlabel ('Pixel Value')
    plt.ylabel ('Frequency')
    plt.plot (histogram_equalized)
    plt.xlim ([0, 256])
    plt.grid (True)

    plt.tight_layout()
    plt.show()