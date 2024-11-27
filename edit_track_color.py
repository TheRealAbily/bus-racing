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
white = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 15
distance_right = 30
option = ''

# Edit track line color:
def section_20():
    # Track line color:
    black = (color(b=c.TRACK_LINE_COLOR) + '  ')
    
    # Clear the screen:
    clear()

    # Edge Y:
    edge(y=c.EDGE_Y)
    
    # Title:
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + '   ' + back_c('B') + '     ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '       ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '       ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '   ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '       ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') +  ' ' + back_c('W') + '  ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + '    ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + '   ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '    ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '       ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '       ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ')

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
    text(front_c('W') + styles_c('B') + '- Enter the new' + front_c('Y') + ' track line color ' + front_c('W') + 'value ( ' + front_c('C') + 'Current: ' + front_c('Y') + f'{c.TRACK_LINE_COLOR}' + front_c('W') + ' )' + styles_c('N'), x=c.EDGE_X + 22, next=3)

    # Text phrases:
    text_phrase = [front_c('R') + styles_c('B') + 'R: ' + front_c('W') + 'Red' + (' ' * 23) + front_c('G') + styles_c('B') + 'G: ' + front_c('W') + 'Green',
                    front_c('Y') + styles_c('B') + 'Y: ' + front_c('W') + 'Yellow' + (' ' * 20) + front_c('Bl') + styles_c('B') + 'Bl: ' + front_c('W') + 'Blue',
                    front_c('M') + styles_c('B') + 'M: ' + front_c('W') + 'Magenta' + (' ' * 19) + front_c('C') + styles_c('B') + 'C: ' + front_c('W') + 'Cyan',
                    front_c('W') + styles_c('B') + 'W: ' + front_c('W') + 'White' + (' ' * 21) + front_c('W') + styles_c('B') + 'B: ' + front_c('W') + 'Black']

    # Text (options):
    for r in range(len(text_phrase)):
        text(text_phrase[r], x=c.EDGE_X + 30, next=3)

    print((' ' * (c.EDGE_X + 41)), front_c('W') + styles_c('B') + '- ' + front_c('G') + 'New value: ' + styles_c('N') + front_c('W'), end='', sep='')
    
    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=3)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 55, y=c.EDGE_Y + 29)

    # Select the option:
    color(f='', b='', s='', ff=False)
    option = input()
    option = option.upper()
    
    # Try converting the value to int (this worked first time):
    try:
        if option != 'R' and option != 'G' and option != 'Y' and option != 'BL' and option != 'M' and option != 'C' and option != 'B' and option != 'W':
            raise ValueError
        else:
            # Edit value:
            c.TRACK_LINE_COLOR = option

            # Back to the options:
            c.SECTION = 4

            # SFX:
            play_sfx('Edit')
    
    except ValueError:
        # SFX:
        play_sfx('Error')

        # Variable:
        option = ''
