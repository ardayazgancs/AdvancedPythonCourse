import numpy as np
from PIL import Image


class Canvas:
    """
    Creates a background where different shapes will be drawn upon (has a color as well).
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3D numpy array filled with zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user given values for color
        self.data[:] = color

    def make(self, image_path):
        """
        Converts given numpy array into image and saves it in the image_path
        :param image_path: path of save location
        """
        image = Image.fromarray(self.data, 'RGB')
        image.save(image_path)
