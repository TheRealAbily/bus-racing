# Import modules from other subfolders

from modules.carpentry import *
from modules.config import *

# Variables:
black = (color(b='B') + '  ')
white = (color(b='W') + '  ')
edge = (front_c('Y') + back_c('B') + '|')

# Main menu:
def section_1():
    # Clear the screen:
    clear()

    # Banner top:
    color(f='Y', b='B', ff=False)
    line('=', WIDHT + EXTRA_FIX, points='o', x=EDGE_X, y=EDGE_Y)

    for i in range(2):
        line(black, floor(WIDHT / 2), intr=white, points=edge, x=EDGE_X, less=True)
        line(black, floor(WIDHT / 2), intr=white, points=edge, x=EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', WIDHT + EXTRA_FIX, points='o', x=EDGE_X)

    # Spaces:
    for m in range(4):
        line(' ', WIDHT + EXTRA_FIX - 2, points=(color(f='Y') + '||'), x=EDGE_X)
    
    # Text:
    # print(back_c('B') + front_c('W') + 'XXX   X   X   XXX      XXX    XXX    XXX   XXXXX  X   X   XXX ')
    # print(back_c('B') + front_c('W') + 'X  X  X   X  X         X  X  X   X  X   X    X    XX  X  X    ')
    # print(back_c('B') + front_c('W') + 'XXX   X   X   XXX      XXX   XXXXX  X        X    X X X  X  XX')
    # print(back_c('B') + front_c('W') + 'X  X  X   X      X     X X   X   X  X   X    X    X  XX  X   X')
    # print(back_c('B') + front_c('W') + 'XXX    XXX    XXX      X  X  X   X   XXX   XXXXX  X   X   XXX ')

    # Line text:
    text(color(f='W', b='B', s='B') + '- Press <enter> to start -', points=color(f='Y', b='B', s='N') + '||', intr=' ', distance=WIDHT - (32 * 2), distance_1=-1, distance_2=-1, x=EDGE_X)

    # Spaces:
    for m in range(4):
        line(' ', WIDHT + EXTRA_FIX - 2, points=(color(f='Y') + '||'), x=EDGE_X)

    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', WIDHT + EXTRA_FIX, points='o', x=EDGE_X)

    for c in range(2):
        line(black, floor(WIDHT / 2), intr=white, points=edge, x=EDGE_X, less=True)
        line(black, floor(WIDHT / 2), intr=white, points=edge, x=EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', WIDHT + EXTRA_FIX, points='o', x=EDGE_X)