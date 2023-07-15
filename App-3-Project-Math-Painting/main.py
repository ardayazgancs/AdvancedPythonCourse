from canvas import Canvas
from shapes import Rectangle, Square
import os

# Get canvas width and height from the user
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))

# Make a dictionary of color codes and prompt for color
colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter canvas color (white or black): ')

# Create a canvas with user input
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input('What do you like to draw? Enter quit to quit. ')
    # Create rectangle if user typed rectangle:
    if shape_type.lower() == 'quit':
        break
    else:
        x = int(input(f'Enter x of {shape_type.lower()}: '))
        y = int(input(f'Enter y of {shape_type.lower()}: '))
        red = int(input(f'How much red should the {shape_type.lower()} have? '))
        green = int(input(f'How much green? '))
        blue = int(input(f'How much blue? '))
        if shape_type.lower() == 'rectangle':
            width = int(input(f'Enter width of {shape_type.lower()}: '))
            height = int(input(f'Enter height of {shape_type.lower()}: '))
            r1 = Rectangle(x=x, y=y, width=width, height=height, color=(red, green, blue))
            r1.draw(canvas)
        else:
            side = int(input(f'Enter side length of {shape_type.lower()}: '))
            s1 = Square(x=x, y=y, side=side, color=(red, green, blue))

os.chdir('./files')
canvas.make('canvas.png')
