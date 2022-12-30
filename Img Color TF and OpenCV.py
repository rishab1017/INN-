import cv2
import tensorflow as tf

# Load the grayscale image
image = cv2.imread('grayscale_image.jpg', cv2.IMREAD_GRAYSCALE)

# Convert the image to a tensor
image = tf.convert_to_tensor(image, dtype=tf.float32)

# Load a pre-trained model
model = tf.hub.load('https://tfhub.dev/deepmind/deoldify/2')

# Colorize the image
image = model(image)
image = image['output'][0]
Use OpenCV to save the colorized image:
Copy code
# Convert the image back to a numpy array
image = image.numpy()

# Save the colorized image
cv2.imwrite('colorized_image.jpg', image)

