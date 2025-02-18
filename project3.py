import cv2
import numpy as np

image = cv2.imread("cat.jpg")

# Taking dimensions
(h, w) = image.shape[:2]

# Applying Rotation
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Scaling image
scaled_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Applying Translation
translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))

# Advanced Image Enhancements

# Adjust Brightness and Contrast
alpha = 1.2 # Contrast control (1.0-3.0)
beta = 50 # Brightness control (0-100)
bright_contrast_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Sharpness (using unsharp masking)
gaussian_blur = cv2.GaussianBlur(image, (0, 0), 5)
sharp_image = cv2.addWeighted(image, 1.5, gaussian_blur, -0.5, 0)

# Applying Blur
blur_image = cv2.GaussianBlur(image, (15, 15), 0)

# Displaying images with Transformations and Enhancements
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Scaled Image", scaled_image)
cv2.imshow("Translated Image", translated_image)
cv2.imshow("Brightness and Contrast", bright_contrast_image)
cv2.imshow("Sharpness", sharp_image)
cv2.imshow("Blur", blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
