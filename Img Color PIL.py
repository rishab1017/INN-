
# Open the grayscale image
from tkinter import Image


image = Image.open("C:\Users\archa\Pictures\Sunrise.jpg")

# Convert the image to RGB mode
image = image.convert('RGB')

# Create a color map for the image
color_map = Image.new('RGB', (256,1))
color_map.putdata([(i,i,i) for i in range(256)])

# Apply the color map to the image
image.putpalette(color_map.getpalette())

# Save the colorized image
image.print('colorized_image.jpg')
