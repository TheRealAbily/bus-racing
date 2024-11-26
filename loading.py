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

    # Distance:
    c.DISTANCE_PLAYER_1 = 0
    c.DISTANCE_PLAYER_2 = 0
    probability = 0

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
    text(color(f='W', b='B', s='B') + ' - Loading. Wait a minute... -  ', points=color(f='Y', b='B', s='N') + '||', intr=' ', distance=c.WIDHT - (34 * 2), distance_1=0, distance_2=0, x=c.EDGE_X)

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
    wait(randint(15, 25) / 10)
    
    # Move the cursor:
    pos(x=0, y=c.EDGE_Y + 16)

    # Line text:
    text(color(f='W', b='B', s='B') + ' - Press ' + front_c('G') + styles_c('B') + '<enter>' + front_c('W') + styles_c('N') + ' to continue -  ', points=color(f='Y', b='B', s='N') + '||', intr=' ', distance=c.WIDHT - (34 * 2), distance_1=0, distance_2=0, x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 66, y=c.EDGE_Y + 16)

    # Pause the program:
    input()

    # Move the cursor:
    pos(x=c.EDGE_X + 66, y=c.EDGE_Y + 16)

    # SFX:
    play_sfx('Car passing')
    
    # Less volume:
    less = c.VOLUME_MUSIC / 20

    # Turn down the volume:
    for i in range(20):
        c.VOLUME_MUSIC -= less
        volume()    
        wait(0.1)

    # Stop the music:
    stop_music()

    # Original volume:
    c.VOLUME_MUSIC = less * 20
    volume()

    # Random track:
    c.TRACK = 11 # randint(1, c.MAX_TRACKS_COUNT)

    # Clear:
    clear()
    
    # Time:
    wait(2)

    # Section:
    c.SECTION = 14
