# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *
from save_load import *
from vehicles import *

# Config:
import config as c

# Variables:
white = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 30
distance_right = 17

# Winner:
def section_18():
    # Track line color:
    black = (color(b=c.TRACK_LINE_COLOR) + '  ')
    
    # Clear the screen:
    clear()

    # Variable:
    if c.WINNER == 0:
        winner = 'Player 1'
        vehicle = c.VEHICLE_PLAYER_1

        if c.GAME_MODE == 0:
            c.WINS_TO_CPU += 1
    else:
        if c.GAME_MODE == 0:
            winner = 'The CPU'
        else:
            winner = 'Player 2'
        
        vehicle = c.VEHICLE_PLAYER_2

    # Volume:
    volume()
    
    # Edge Y:
    edge(y=c.EDGE_Y)

    # Text:
    print(back_c('B') + front_c('W') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + '   ')
    print(back_c('B') + front_c('W') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + '  ')
    print(back_c('B') + front_c('W') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '    ')
    print(back_c('B') + front_c('W') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ')
    print(back_c('B') + front_c('W') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ')

    # Banner top:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=c.EDGE_Y)
    
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)
    
    # Edge Y:
    edge(y=2)
    
    # Distances:
    if vehicle == 0:
        distance = 43
    elif vehicle == 1:
        distance = 45
    elif vehicle == 2:
        distance = 40
    elif vehicle == 3:
        distance = 45
    elif vehicle == 4:
        distance = 41
    else:
        distance = 41
    
    # Vehicle:
    show_vehicle(vehicle, 0, False, x=c.EDGE_X + distance)
    
    # Edge Y:
    edge(y=2)
    
    # Line text:
    print((' ' * (c.EDGE_X + 36)) + front_c('W') + styles_c('N') +  '- ' + front_c('Y') + 'The winner is: ' + front_c('G') + styles_c('B') + winner + styles_c('N') + front_c('W') + ' -', end='\n\n')
    print((' ' * (c.EDGE_X + 29)) + front_c('W') + styles_c('N') +  '- Press ' + front_c('G') + styles_c('B') + '<enter>' + styles_c('N') + front_c('W') + ' to return to the menu -')

    # Edge Y:
    edge(y=2)

    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # # Move the cursor:
    pos(x=c.EDGE_X + 70, y=c.EDGE_Y + 23)

    # Play music:
    play_music('Winning idle')

    # Pause the program:
    input()

    # Section:
    c.SECTION = 1

    # SFX:
    play_sfx('Go')

    # Play music:
    play_music('Main menu')
