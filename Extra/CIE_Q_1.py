import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread(r"C:\Users\RANGUNWALA\Downloads\1.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Normalize the histogram so that the sum of all bins equals 1
hist_normalized = hist / hist.sum()

# Calculate the percentage of pixels in dark and bright regions
dark_pixels_percentage = np.sum(hist_normalized[:128]) * 100  # Pixels below intensity 128 are considered dark
bright_pixels_percentage = np.sum(hist_normalized[128:]) * 100  # Pixels above intensity 128 are considered bright

# Calculate the mean and standard deviation of pixel intensities
mean_intensity = np.mean(gray_image)
std_dev = np.std(gray_image)

# Check for uniform images (like fully black or fully white)
if std_dev == 0:
    if mean_intensity == 0:
        brightness_category = "very dark"
    elif mean_intensity == 255:
        brightness_category = "very bright"
    else:
        brightness_category = "uniform gray"
    contrast_category = "no contrast"
else:
    # Determine brightness based on dark and bright pixel percentages
    threshold_margin = 10  # Margin to determine 'balanced' category
    if abs(dark_pixels_percentage - bright_pixels_percentage) <= threshold_margin:
        brightness_category = "balanced"
    elif dark_pixels_percentage > 80:
        brightness_category = "very dark"
    elif bright_pixels_percentage > 80:
        brightness_category = "very bright"
    elif dark_pixels_percentage > bright_pixels_percentage:
        brightness_category = "dark"
    elif bright_pixels_percentage > dark_pixels_percentage:
        brightness_category = "bright"

    # Define dynamic thresholds for contrast based on the standard deviation
    low_contrast_threshold = 30  # Set your own percentage for low contrast
    high_contrast_threshold = 60 # Set your own percentage for high contrast

    # Determine contrast category dynamically
    if std_dev < low_contrast_threshold:
        contrast_category = "low contrast"
    elif low_contrast_threshold <= std_dev < high_contrast_threshold:
        contrast_category = "moderate contrast"
    else:
        contrast_category = "high contrast"

# Print results
print(f"The image is {brightness_category}.")
print(f"The image has {contrast_category}.")

# Plot the histogram for visualization
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.plot(hist_normalized)
plt.xlim([0, 256])
plt.show()

# Print out the percentages and standard deviation for reference
print(f"Dark pixels: {dark_pixels_percentage:.2f}%")
print(f"Bright pixels: {bright_pixels_percentage:.2f}%")
print(f"Standard Deviation of Pixel Intensities: {std_dev:.2f}")
