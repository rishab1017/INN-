import cv2

# Load the grayscale image
image = cv2.imread('grayscale_image.jpg', cv2.IMREAD_GRAYSCALE)

# Convert the image to RGB mode
image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

# Save the colorized image
cv2.imwrite('colorized_image.jpg', image)
