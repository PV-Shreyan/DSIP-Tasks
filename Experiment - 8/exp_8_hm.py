import cv2
import numpy as np
import matplotlib.pyplot as plt

source_path = r"images\dsip_logo.png"
reference_path = r"images\DSIP_OPE_2.png"

source_image = cv2.imread(source_path, cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

# Check if images were loaded successfully
if source_image is None:
    print(f"Error: Could not load source image from {source_path}. Please ensure the file exists and the path is correct.")
elif reference_image is None:
    print(f"Error: Could not load reference image from {reference_path}. Please ensure the file exists and the path is correct.")
else:
    # Calculate histograms for the source and reference images for plotting
    source_hist_plot = cv2.calcHist([source_image], [0], None, [256], [0, 256])
    reference_hist_plot = cv2.calcHist([reference_image], [0], None, [256], [0, 256])
    
    # Normalize histograms to have sum equal to 1 (Required for CDF calculation)
    source_hist = source_hist_plot / source_hist_plot.sum()
    reference_hist = reference_hist_plot / reference_hist_plot.sum()

    # Calculate cumulative distribution functions (CDF) for histograms
    source_cdf = source_hist.cumsum()
    reference_cdf = reference_hist.cumsum()

    # Perform histogram matching by mapping source CDF to reference CDF
    # The interpolation should use the values 0-255 for the output range
    mapping = np.interp(source_cdf, reference_cdf, np.arange(256))
    matched_image = mapping[source_image]

    # Convert to uint8 data type
    matched_image = matched_image.astype(np.uint8)
    
    # Calculate the histogram of the final matched image for plotting
    matched_hist_plot = cv2.calcHist([matched_image], [0], None, [256], [0, 256])

    # Display the images and histograms using a 2x3 grid
    plt.figure(figsize=(15, 8))

    # Row 1: Images
    plt.subplot(2, 3, 1)
    plt.title('Source Image')
    plt.imshow(source_image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.title('Reference Image')
    plt.imshow(reference_image, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.title('Matched Image')
    plt.imshow(matched_image, cmap='gray')
    plt.axis('off')

    # Row 2: Histograms
    plt.subplot(2, 3, 4)
    plt.title('Source Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.plot(source_hist_plot)
    plt.xlim([0, 256])
    plt.grid(True)

    plt.subplot(2, 3, 5)
    plt.title('Reference Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.plot(reference_hist_plot)
    plt.xlim([0, 256])
    plt.grid(True)

    plt.subplot(2, 3, 6)
    plt.title('Matched Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.plot(matched_hist_plot)
    plt.xlim([0, 256])
    plt.grid(True)

    plt.tight_layout()
    plt.show()