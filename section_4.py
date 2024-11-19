# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *
from vehicles import *

# Config:
import config as c

# Variables:
black = (color(b='B') + '  ')
white = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 19
distance_right = 19
option = ''

# Vehicles:
vehicles = ['Car', 'Motorcycle', 'Bus', 'Go kart', 'Truck', 'Monster car', 'Formula 1', 'Bicycle'] # More vehicles coming soon...

# Selection of the vehicle (2 Player):
def section_4():
    # Clear the screen:
    clear()

    # Edge Y:
    edge(y=c.EDGE_Y)
    
    # Title:
    # print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '      ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y'))
    # print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '         ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '    ' + (' ' * distance_right) + front_c('Y'))
    # print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '      ' + back_c('W') + '    ' + back_c('B') + '  ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + (' ' * distance_right) + front_c('Y'))
    # print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '     ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '        ' + back_c('W') + ' ' + back_c('B') + '    ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + '  ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + (' ' * distance_right) + front_c('Y'))
    # print(back_c('B') + front_c('Y') + (' ' * c.EDGE_X) + (' ' * distance_left) + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '    ' + back_c('W') + '   ' + back_c('B') + '      ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + '   ' + back_c('W') + '     ' + back_c('B') + '  ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + ' ' + back_c('B') + '   ' + back_c('W') + '   ' + back_c('B') + ' ' + (' ' * distance_right) + front_c('Y'))

    #  ###   #####  #      #####   ###   #####  #####   ###   #   #  
    # #      #      #      #      #        #      #    #   #  ##  #
    #  ###   ###    #      ###    #        #      #    #   #  # # #  
    #     #  #      #      #      #        #      #    #   #  #  ##  
    #  ###   #####  #####  #####   ###     #    #####   ###   #   #  

    # Banner middle:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=2)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Edge Y:
    edge(y=1)
    
    # Show the vehicle:
    show_vehicle(c.VEHICLE_PLAYER_1, 30, x=c.EDGE_X)

    # Edge Y:
    edge(y=2)
    
    # Text phrases:
    text_phrase = [front_c('Y') + '- Current vehicle of the player 2: ' + front_c('C') + f'{vehicles[c.VEHICLE_PLAYER_2]}', 'Next vehicle', 'Previous vehicle', 'Select vehicle', 'Return to menu']

    # Text (options):
    for r in range(len(text_phrase)):
        if r == 0:
            text(styles_c('B') + text_phrase[r] + styles_c('N'), x=c.EDGE_X + 25, next=3)
        else:
            text(front_c('G') + f'{r}.) ' + front_c('W') + styles_c('B') + text_phrase[r] + styles_c('N'), x=c.EDGE_X + 25, next=3)

    print((' ' * (c.EDGE_X + 28)), front_c('Y') + styles_c('B') + '- Select the option: ' + styles_c('N') + front_c('W'), end='', sep='')
    
    # Banner bottom:
    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=3)

    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
    line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

    color(f='Y', b='B', ff=False)
    line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

    # Move the cursor:
    pos(x=c.EDGE_X + 50, y=c.EDGE_Y + 29)

    # Select the option:
    color(f='', b='', s='', ff=False)
    option = input()

    # Try converting the value to int (this worked first time):
    try:
        option = int(option)

        if not 1 <= option <= 4:
            raise ValueError
        else:
            # Options:
            if option == 1:
                if c.VEHICLE_PLAYER_2 < min(c.MAX_VEHICLES, len(vehicles)) - 1:
                    c.VEHICLE_PLAYER_2 += 1
                else:
                    c.VEHICLE_PLAYER_2 = 0

                # SFX:
                play_sfx('Edit')
            
            elif option == 2:
                if c.VEHICLE_PLAYER_2 > 0:
                    c.VEHICLE_PLAYER_2 -= 1
                else:
                    c.VEHICLE_PLAYER_2 = min(c.MAX_VEHICLES, len(vehicles)) - 1

                # SFX:
                play_sfx('Edit')
            
            elif option == 3:
                c.SECTION = 13

                # SFX:
                play_sfx('Go')
            else:
                c.SECTION = 1

                # SFX:
                play_sfx('Back')
    
    except ValueError:
        # SFX:
        play_sfx('Error')

        # Variable:
        option = ''