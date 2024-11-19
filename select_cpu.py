# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *
from vehicles import *
from random import randint

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

# Selection of the vehicle (CPU):
def section_13():
    # Variables:
    selected = 0
    spin = 0
    max_spin = 17
    c.VEHICLE_PLAYER_CPU = randint(0, min(c.MAX_VEHICLES, len(vehicles)) - 1)
    loop = True

    # Loop:
    while loop == True:
        # Clear the screen:
        clear()

        # Edge Y:
        edge(y=c.EDGE_Y)

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
        show_vehicle(c.VEHICLE_PLAYER_CPU, 30, x=c.EDGE_X)

        # Edge Y:
        edge(y=2)
        
        # Text:
        text(styles_c('B') + front_c('Y') + '- Current vehicle of the CPU: ' + front_c('C') + f'{vehicles[c.VEHICLE_PLAYER_CPU]}' + styles_c('N'), x=c.EDGE_X + 25, next=3)

        # Banner bottom:
        color(f='Y', b='B', ff=False)
        line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X, y=2)

        line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True)
        line(black, floor(c.WIDHT / 2), intr=white, points=edges, x=c.EDGE_X, less=True, switch=True)

        color(f='Y', b='B', ff=False)
        line('=', c.WIDHT + c.EXTRA_FIX, points='o', x=c.EDGE_X)

        # Select the option:
        color(f='', b='', s='', ff=False)
        if selected == 1:
            # SFX:
            play_sfx('Selected')

            # Move the cursor:
            pos(y=c.EDGE_Y + 17)

            # Text:
            print((' ' * (c.EDGE_X + 28)), front_c('W') + styles_c('D') + '- Press' + front_c('G') + ' <enter> ' + front_c('W') + 'to continue - ' + front_c('W'), end='', sep='')
            input()

            # Loop:
            loop = False

            # Variable:
            c.SECTION = 13
        elif selected == 0:
            # SFX:
            play_sfx('Random')
            
            # Variable:
            selected = 2
        else:
            # Wait:
            wait(0.25)

            # Random:
            if c.VEHICLE_PLAYER_CPU < min(c.MAX_VEHICLES, len(vehicles)) - 1:
                c.VEHICLE_PLAYER_CPU += 1
            else:
                c.VEHICLE_PLAYER_CPU = 0

            # Spins:
            if spin < max_spin:
                spin += 1

                # Move the cursor:
                pos(x=c.EDGE_X + 40, y=c.EDGE_Y + 14)
            else:
                selected = True
