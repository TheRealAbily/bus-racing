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
distance_left = 13
distance_right = 0

# Information:
def section_7():
    # Track line color:
    black = (color(b=c.TRACK_LINE_COLOR) + '  ')
    
    # Clear the screen:
    clear()

    # Spaces:
    edge(y=c.EDGE_Y)
    
    # Text:
    print(front_c('W') + (' ' * (c.EDGE_X + distance_left)) + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + (' ' * distance_right))
    print(front_c('W') + (' ' * (c.EDGE_X + distance_left)) + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + (' ' * distance_right))
    print(front_c('W') + (' ' * (c.EDGE_X + distance_left)) + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '    ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + (' ' * distance_right))
    print(front_c('W') + (' ' * (c.EDGE_X + distance_left)) + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + (' ' * distance_right))
    print(front_c('W') + (' ' * (c.EDGE_X + distance_left)) + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '       ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + '     ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + (' ' * distance_right))
    
    # Spaces:
    edge(y=2)

    # Banner middle:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)
    
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)
        
    # Spaces:
    edge(y=2)

    # Text:
    text_phrase = ['- Bus Racing is a turn-based racing game developed in Python, in which players',
                    'control buses that compete to reach the finish line before their opponents. The',
                    'game uses simple and dynamic mechanics to offer a competitive and fun experience,',
                    'ideal for both solo games against the AI ​​and playing with friends.',
                    ' ',
                    ' ',
                    '- The goal of the game is to cross the finish line before everyone else, overcoming',
                    'obstacles, taking advantage of bonuses and using strategies to advance faster.',
                    'The gameplay focuses on turns that combine elements of chance and strategic',
                    'decisions, adding a layer of excitement and unpredictability to each race.',
                    ' ',
                    ' ',
                    '- The game is designed to be accessible and easy to use, with a basic interface',
                    'that allows players to select their buses, customize them, and compete. In',
                    'addition, it has a statistics system at the end of each race that shows the',
                    'results, player times and final positions.']

    # Long text:
    for i in range(len(text_phrase)):
        print((' ' * (c.EDGE_X + 11)), front_c('W') + styles_c('B') + text_phrase[i] + front_c('W') + styles_c('N'), sep='')
    
    # Spaces:
    edge(y=2)
    
    # Line text:
    print((' ' * (c.EDGE_X + 32)), front_c('W') + '- Press ' + front_c('G') + styles_c('B') + '<enter>' + front_c('W') + styles_c('N') + ' to return the menu - ' + styles_c('N') + front_c('W'), sep='')
    
    # Spaces:
    edge(y=2)

    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)
    
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 70, y=c.EDGE_Y + len(text_phrase) + 16)

    # Pause the program:
    input()

    # SFX:
    play_sfx('Back')

    # Variable:
    c.SECTION = 1