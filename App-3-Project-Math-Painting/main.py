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


class Rectangle:
    """
    Creates a rectangle at given coordinates with width and height and filled with given color.
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """
        Changes slices of data with new values
        :param canvas: Canvas to be drawn on
        """
        canvas.data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color


class Square:
    """
    Creates a square at given coordinates with equal side lengths and filled with given color.
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw_canvas(self, canvas):
        """
            Changes slices of data with new values
            :param canvas: Canvas to be drawn on
        """
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color


_canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas=_canvas)
s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
s1.draw_canvas(canvas=_canvas)
_canvas.make('canvas.png')
