# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from save_load import *
from sounds import *
from text import *

# Config:
import config as c

# Adjust screen:
def section_0():
    # Load the data:
    load_data()

    # Change the section:
    if c.ADJUST_SCREEN == 1:
        c.SECTION = 0
    else:
        # Clear the screen:
        clear()

        # Variable:
        distance_x = 20
        distance_y = 26
        lines = 10
        
        # Corner:
        print(back_c('B') + (' ' * c.EDGE_X) + back_c('W') + (' ' * (lines + 1)), sep='')

        for t in range(lines - 4):
            print(back_c('B') + (' ' * c.EDGE_X) + back_c('W') + (' \n') + back_c('B'), end='', sep='')

        # Spaces:
        edge(y=round(distance_y/2))
        
        # Text:
        print((' ' * (c.EDGE_X + distance_x + 2)) + front_c('W') + back_c('B') + styles_c('N') + '- Expand the ' + front_c('Y') + 'CMD window' + front_c('G') + ' completely ' + front_c('W') + 'before starting to play -', end='', sep='')
        print(('\n' * 2) + (' ' * (c.EDGE_X + distance_x)) + front_c('W') + back_c('B') + styles_c('N') + '- Use' + front_c('G') + styles_c('B') + ' \'Y\' ' + front_c('W') + styles_c('N') + 'to play,' + front_c('R') + styles_c('B') + ' \'N\' ' + front_c('W') + styles_c('N') + 'to reload this screen until it\'s right -', end='', sep='')
        
        print(('\n' * 3) + (' ' * (c.EDGE_X + distance_x + 20)) + front_c('Y') + back_c('B') + styles_c('N') + '- Select the option: ', sep='')
        
        # Reset the colors:
        color(f='-', b='-', s='-', ff=False)

        # Spaces:
        edge(y=round(distance_y/2))

        # Corner:
        for i in range(lines - 4):
            print((' ' * c.EDGE_X) + back_c('B') + (' ' * (c.WIDHT + 5)) + back_c('W') + ' ', sep='')
            print(back_c('B'), end='', sep='')
        print((' ' * c.EDGE_X) + back_c('B') + (' ' * (c.WIDHT - lines + 5)) + back_c('W') + (' ' * (lines + 1)), end='', sep='')
        back_c('B', False)
        
        # Move the cursor:
        pos(x=c.EDGE_X + distance_x + 42, y=round(distance_y/2) + 13)

        # Reset the colors:
        color(f='-', b='-', s='-', ff=False)

        # Select the option:
        option = input()

        # Move the cursor:
        pos(x=c.EDGE_X + distance_x + 43, y=round(distance_y/2) + 13)

        # Check the option:
        try:
            if option.upper() != 'Y' and option.upper() != 'N':
                raise ValueError
            else:
                # 1 Player:
                if option.upper() == 'Y':
                    c.SECTION = 0
                    c.ADJUST_SCREEN = 1
                    play_sfx('Go')
                    save_data()
                else:
                    wait(0.25)
                    play_sfx('Edit')

        except ValueError:
            # SFX:
            play_sfx('Error')

            # Variable:
            option = ''
