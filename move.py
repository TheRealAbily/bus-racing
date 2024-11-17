# Import the modules to use the colors

import sys
from colorama import init, Cursor

# Initialize Colorama:
init()

# Move the cursor:
def move(**options):
    # Up:
    if 'up' in options:
        up = options.get('up', 0)

        if not isinstance(up, int):
            try:
                up = int(up)
            except ValueError:
                up = 0
    else:
        up = 0

    # Right:
    if 'right' in options:
        right = options.get('right', 0)

        if not isinstance(right, int):
            try:
                right = int(right)
            except ValueError:
                right = 0
    else:
        right = 0
    
    # Down:
    if 'down' in options:
        down = options.get('down', 0)

        if not isinstance(down, int):
            try:
                down = int(down)
            except ValueError:
                down = 0
    else:
        down = 0

    # Left:
    if 'left' in options:
        left = options.get('left', 0)

        if not isinstance(left, int):
            try:
                left = int(left)
            except ValueError:
                left = 0
    else:
        left = 0

    # Move the cursor:
    sys.stdout.write(Cursor.UP(up) + Cursor.FORWARD(right) + Cursor.BACK(left) + Cursor.DOWN(down))

    # Update the screen:
    sys.stdout.flush()

# Set the position of the cursor:
def pos(**options):
    # Edge X:
    if 'x' in options:
        x = options.get('x', 0)

        if not isinstance(x, int):
            try:
                x = int(x)
            except ValueError:
                x = 0
    else:
        x = 0
    
    # Edge Y:
    if 'y' in options:
        y = options.get('y', 0)

        if not isinstance(y, int):
            try:
                y = int(y)
            except ValueError:
                y = 0
    else:
        y = 0

    # Set the position:
    sys.stdout.write(Cursor.POS(x, y))

    # Update the screen:
    sys.stdout.flush()
