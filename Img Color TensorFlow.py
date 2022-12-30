import tensorflow as tf

# Load the DeOldify model
model = tf.hub.load('https://tfhub.dev/deepmind/deoldify/2')

# Load the grayscale image
image = tf.io.read_file('grayscale_image.jpg')
image = tf.image.decode_image(image, channels=1)

# Colorize the image
image = model(image)
image = image['output'][0]

# Save the colorized image
tf.keras.preprocessing.image.save_img('colorized_image.jpg', image)
