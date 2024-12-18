# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *
from save_load import *

# Config:
import config as c

# Variables:
white = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 17
distance_right = 17

# Presentation:
def section_1():
    # Load the data:
    load_data()
    
    # Track line color:
    black = (color(b=c.TRACK_LINE_COLOR) + '  ')

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
    text(color(f='W', b='B', s='B') + '- Press ' + front_c('G') + styles_c('B') + '<enter>' + styles_c('N') + front_c('W') + ' to start -', points=color(f='Y', b='B', s='N') + '||', intr=' ', distance=c.WIDHT - (32 * 2), distance_1=-1, distance_2=-1, x=c.EDGE_X)

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
    pos(x=c.EDGE_X + 65, y=c.EDGE_Y + 16)

    # Play music:
    play_music('Main menu')

    # Pause the program:
    input()

    # Section:
    c.SECTION = 1

    # SFX:
    play_sfx('Go')
