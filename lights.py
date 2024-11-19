# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *
from random import randint

# Config:
import config as c

# Lights:
def section_16():
    # SFX:
    play_sfx('Countdown')

    # Variable:
    distance = 0

    # Lights:
    for m in range(4):
        # Clear the screen:
        clear()

        # Spaces:
        edge(y=c.EDGE_Y)

        # Colors:
        back_c('B', False)
        if m < 2:
            front_c('R', False)
        elif m == 2:
            front_c('Y', False)
        else:
            front_c('G', False)

        # Light:
        print(m)
        print((' ' * (c.EDGE_X + distance)), '        __________________________________', sep='')
        print((' ' * (c.EDGE_X + distance)), '       /XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\\', sep='')
        print((' ' * (c.EDGE_X + distance)), '      /XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\\', sep='')
        print((' ' * (c.EDGE_X + distance)), '     /XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\\', sep='')
        print((' ' * (c.EDGE_X + distance)), '    /XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\\', sep='')
        print((' ' * (c.EDGE_X + distance)), '   /XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\\', sep='')
        print((' ' * (c.EDGE_X + distance)), '  /XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\\', sep='')
        print((' ' * (c.EDGE_X + distance)), '  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|', sep='')
        print((' ' * (c.EDGE_X + distance)), '  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|', sep='')
        print((' ' * (c.EDGE_X + distance)), '  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|', sep='')
        print((' ' * (c.EDGE_X + distance)), '  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|', sep='')
        print((' ' * (c.EDGE_X + distance)), '  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|', sep='')
        print((' ' * (c.EDGE_X + distance)), '  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|', sep='')
        print((' ' * (c.EDGE_X + distance)), '  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|', sep='')
        print((' ' * (c.EDGE_X + distance)), '  \\XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/', sep='')
        print((' ' * (c.EDGE_X + distance)), '   \\XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/', sep='')
        print((' ' * (c.EDGE_X + distance)), '    \\XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/', sep='')
        print((' ' * (c.EDGE_X + distance)), '     \\XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/', sep='')
        print((' ' * (c.EDGE_X + distance)), '      \\XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/', sep='')
        print((' ' * (c.EDGE_X + distance)), '       \\XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/', sep='')

        # Spaces:
        edge(y=c.EDGE_Y)

        # Restart colors:
        back_c('-', False)
        front_c('-', False)

        # Move the cursor:
        pos(x=c.EDGE_X + 0, y=c.EDGE_Y + 0)

        # Wait:
        if m < 3:
            # Time:
            wait(0.9)
        else:
            # Time:
            wait(1.25)

            # Variable:
            c.SECTION = 16
