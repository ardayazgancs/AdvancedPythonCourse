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
