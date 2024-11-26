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
distance_left = 33
distance_right = 19
option = ''

# Songs:
def section_19():
    # Clear the screen:
    clear()

    # Edge Y:
    edge(y=c.EDGE_Y)
    
    # Title:
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + ' ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + ' ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '   ' + back_c('W') + '   ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ')
    print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('B') + ' ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ')

    #  XXX    XXX   X   X   XXX    XXX
    # X      X   X  XX  X  X      X  
    #  XXX   X   X  X X X  X  XX   XXX 
    #     X  X   X  X  XX  X   X      X
    #  XXX    XXX   X   X   XXX    XXX

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
    text_phrase = [front_c('G') + styles_c('N') + '1.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Figure 8' + (' ' * 33) + front_c('G') + styles_c('N') + '6.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Sky Garden',
    front_c('G') + styles_c('N') + '2.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Delfino Square' + (' ' * 27) + front_c('G') + styles_c('N') + '7.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Bowser Castle',
    front_c('G') + styles_c('N') + '3.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Waluigi Pinball / Wario Stadium' + (' ' * 10) + front_c('G') + styles_c('N') + '8.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Peach Garden',
    front_c('G') + styles_c('N') + '4.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Rainbow Road' + (' ' * 29) + front_c('G') + styles_c('N') + '9.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Yoshi Falls',
    front_c('G') + styles_c('N') + '5.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Desert Hills' + (' ' * 28) + front_c('G') + styles_c('N') + '10.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Tokyo Drift',
    front_c('G') + styles_c('N') + '11.) ' + front_c('Y') + styles_c('B') + 'Play: ' + front_c('W') + 'Main menu theme',
    front_c('G') + styles_c('N') + '12.) ' + front_c('W') + styles_c('B') + 'Return to the menu']

    # Text (options):
    for r in range(len(text_phrase)):
        if r < len(text_phrase) - 1:
            text(text_phrase[r], x=c.EDGE_X + 13, next=3)
        else:
            text(text_phrase[r], x=c.EDGE_X + 38, next=3)

    print((' ' * (c.EDGE_X + 35)), front_c('Y') + styles_c('B') + '- Select the option: ' + styles_c('N') + front_c('W'), end='', sep='')
    
    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=3)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 57, y=c.EDGE_Y + 35)

    # Select the option:
    color(f='', b='', s='', ff=False)
    option = input()

    # Try converting the value to int (this worked first time):
    try:
        option = int(option)

        if not 1 <= option <= 12:
            raise ValueError
        else:
            # Play any song:
            if option >= 1 and option <= 11:
                # Variable:
                c.CHANGE_SONG = True

                # Wario/Waluigi song:
                if option == 11:
                    # Music:
                    play_music('Main menu')

                    c.CHANGE_SONG = False
                else:
                    if option >= 8:
                        option += 1
                    
                    # Option:
                    c.TRACK = option

                    # Music:
                    play_music('Track')
            
            # Return to the menu:
            else:
                # Menu:
                c.SECTION = 1

                # SFX:
                play_sfx('Back')

                # Music:
                if c.CHANGE_SONG == True:
                    # Music:
                    play_music('Main menu')

                    # Variable:
                    c.CHANGE_SONG == False
                    c.TRACK = 1
    
    except ValueError:
        # SFX:
        play_sfx('Error')

        # Variable:
        option = ''