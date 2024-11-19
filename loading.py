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

# Variables:
black = (color(b='B') + '  ')
white = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 17
distance_right = 17

# Loading:
def section_14():
    # Clear the screen:
    clear()

    # Banner top:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=c.EDGE_Y)

    for i in range(2):
        line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
        line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Spaces:
    for m in range(2):
        line(' ', c.WIDHT + c.EXTRA_FIX - 2, points=(color(f='Y') + '||'), x=c.EDGE_X)
    
    # Text:
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + '||' + (' ' * distance_left) + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '      ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y') + '||')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + '||' + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '         ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + (' ' * distance_right) + front_c('Y') + '||')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + '||' + (' ' * distance_left) + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '      ' + back_c('W') + '    ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + (' ' * distance_right) + front_c('Y') + '||')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + '||' + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '     ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + (' ' * distance_right) + front_c('Y') + '||')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + '||' + (' ' * distance_left) + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y') + '||')

    # Spaces:
    for n in range(2):
        line(' ', c.WIDHT + c.EXTRA_FIX - 2, points=(color(f='Y') + '||'), x=c.EDGE_X)
    
    # Line text:
    text(color(f='W', b='B', s='B') + ' - Loading. ' + front_c('G') + 'Wait a minute...' + front_c('W') + ' -  ', points=color(f='Y', b='B', s='N') + '||', intr=' ', distance=c.WIDHT - (34 * 2), distance_1=0, distance_2=0, x=c.EDGE_X)

    # Spaces:
    line(' ', c.WIDHT + c.EXTRA_FIX - 2, points=(color(f='Y') + '||'), x=c.EDGE_X)

    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    for k in range(2):
        line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
        line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 66, y=c.EDGE_Y + 16)

    # Wait:
    wait(randint(2, 4))
    
    # Move the cursor:
    pos(x=0, y=c.EDGE_Y + 16)

    # Line text:
    text(color(f='W', b='B', s='B') + ' - Press ' + front_c('G') + '<enter>' + front_c('W') + ' to continue -  ', points=color(f='Y', b='B', s='N') + '||', intr=' ', distance=c.WIDHT - (34 * 2), distance_1=0, distance_2=0, x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 66, y=c.EDGE_Y + 16)

    # SFX:
    play_sfx('Car_passing')

    # Pause the program:
    input()

    # Section:
    c.SECTION = 1

    # SFX:
    play_sfx('Go')