import os
from PIL import Image
import numpy as np

# Set the path to the folder containing your handwriting images
path_to_images = '/Users/Ben/Desktop/Handwriting'

# Create an empty list to store the images as arrays
images = []

# Loop through each image file in the folder
for filename in os.listdir(path_to_images):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image using Pillow
        image = Image.open(os.path.join(path_to_images, filename))
        
        # Resize the image to a standard size (e.g. 64x64)
        image = image.resize((64, 64))
        
        # Convert the image to a NumPy array
        image_array = np.asarray(image)
        
        # Normalize the pixel values to be between -1 and 1
        image_array = (image_array / 127.5) - 1
        
        # Add the image array to the list of images
        images.append(image_array)
        
# Convert the list of images to a NumPy array
images = np.array(images)
print(images)
# Save the NumPy array to disk in a format that TensorFlow can read (e.g. HDF5 or TFRecord)
# You can use TensorFlow's dataset API to load the data during training
