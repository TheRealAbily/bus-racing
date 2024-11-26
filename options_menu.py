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
distance_left = 26
distance_right = 19
option = ''

# Options:
def section_5():
    # Clear the screen:
    clear()

    # Edge Y:
    edge(y=c.EDGE_Y)
    
    # Title:
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + ' ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '    ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '  ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '     ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '    ' + back_c('B') + '     ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y'))
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + ' ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + '     ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '  ' + (' ' * distance_right) + front_c('Y'))

    # Banner middle:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=2)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Edge Y:
    edge(y=2)

    # Text phrases:
    text_phrase = [front_c('W') + 'Adjust the X axis ( ' + front_c('C') + 'Current: ' + front_c('Y') + f'{round(c.EDGE_X)}' + front_c('W') + ' )',
    front_c('W') + 'Adjust the Y axis ( ' + front_c('C') + 'Current: ' + front_c('Y') + f'{round(c.EDGE_Y)}' + front_c('W') + ' )',
    front_c('W') + 'Music volume ( ' + front_c('C') + 'Current: ' + front_c('Y') + f'{round(c.VOLUME_MUSIC * 100)}%' + front_c('W') + ' )',
    front_c('W') + 'SFX volume ( ' + front_c('C') + 'Current: ' + front_c('Y') + f'{round(c.VOLUME_SFX * 100)}%' + front_c('W') + ' )',
    front_c('W') + 'Information of the program',
    front_c('W') + 'Restore default settings',
    front_c('W') + 'Return to menu']

    # Text (options):
    for r in range(len(text_phrase)):
        text(front_c('G') + f'{r + 1}.) ' + front_c('W') + styles_c('B') + text_phrase[r] + styles_c('N'), x=c.EDGE_X + 25, next=3)

    print((' ' * (c.EDGE_X + 28)), front_c('Y') + styles_c('B') + '- Select the option: ' + styles_c('N') + front_c('W'), end='', sep='')
    
    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=3)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 50, y=c.EDGE_Y + 34)

    # Select the option:
    color(f='', b='', s='', ff=False)
    option = input()

    # Try converting the value to int (this worked first time):
    try:
        option = int(option)

        if not 1 <= option <= 7:
            raise ValueError
        else:
            if option == 1:
                # Edit edge X:
                c.SECTION = 7

                # SFX:
                play_sfx('Go')
    
            elif option == 2:
                # Edit edge Y:
                c.SECTION = 8

                # SFX:
                play_sfx('Go')
            
            elif option == 3:
                # Edit volumen (Music):
                c.SECTION = 9

                # SFX:
                play_sfx('Go')

            elif option == 4:
                # Edit volumen (SFX):
                c.SECTION = 10

                # SFX:
                play_sfx('Go')

            elif option == 5:
                # Information:
                c.SECTION = 6

                # SFX:
                play_sfx('Go')

            elif option == 6:
                # Restore default settings:
                c.VOLUME_MUSIC = 0.75
                c.VOLUME_SFX = 0.75
                c.EDGE_X = 4
                c.EDGE_Y = 2

                # SFX:
                play_sfx('Edit')

            else:
                # Menu:
                c.SECTION = 1

                # SFX:
                play_sfx('Back')
    
    except ValueError:
        # SFX:
        play_sfx('Error')

        # Variable:
        option = ''