# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *

# Config:
import config as c

# Variables:
black = (color(b='B') + '  ')
white = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 31
distance_right = 30
option = ''

# Edit edge Y:
def section_9():
    # Clear the screen:
    clear()

    # Edge Y:
    edge(y=c.EDGE_Y)
    
    # Title:
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + '    ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '     ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + '  ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '          ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '  ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + '   ' + back_c('B') + '         ' + back_c('W') + ' ' + back_c('B') + '   ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + '  ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '           ' + back_c('W') + ' ' + back_c('B') + '   ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + '    ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '       ' + back_c('W') + ' ' + back_c('B') + '   ' + (' ' * distance_right) + front_c('Y'))

    # Banner middle:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=2)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Edge Y:
    edge(y=2)

    # Text:
    text(front_c('W') + styles_c('B') + '- Enter the new value of the' + front_c('Y') + ' Y axis ' + front_c('W') + '( ' + front_c('C') + 'Current: ' + front_c('Y') + f'{round(c.EDGE_Y)}' + front_c('W') + ' )' + styles_c('N'), x=c.EDGE_X + 25, next=3)

    print((' ' * (c.EDGE_X + 28)), front_c('W') + styles_c('B') + '- ' + front_c('G') + 'New value ' + front_c('W') + '( ' + front_c('C') + 'Min: ' + front_c('Y') + '0' + front_c('W') + ' - ' + front_c('C') + 'Max: ' + front_c('Y') + '20' + front_c('W') + ' ): ' + styles_c('N') + front_c('W'), end='', sep='')
    
    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=3)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 63, y=c.EDGE_Y + 17)

    # Select the option:
    color(f='', b='', s='', ff=False)
    option = input()

    # Try converting the value to int (this worked first time):
    try:
        option = int(option)

        if not 0 <= option <= 20:
            raise ValueError
        else:
            # Edit value:
            c.EDGE_Y = option

            # Back to the options:
            c.SECTION = 4

            # SFX:
            play_sfx('Edit')
    
    except ValueError:
        # SFX:
        play_sfx('Error')

        # Variable:
        option = ''