# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *

import config as c

# Show the vehicles:
def show_vehicle(vehicle, distance = 0, show_stats = True, **options):
    # Edge X:
    if 'x' in options:
        edge_x = options.get('x', 0)

        # Convert the variable to int:
        if not isinstance(edge_x, int):
            try:
                edge_x = int(edge_x)
            except ValueError:
                edge_x = 0
    else:
        edge_x = 0
    
    # Colors:
    front_c('-', False)
    back_c('-', False)
    styles_c('B', False)

    # Variable:
    distance_stats = 7

    # Car:
    if vehicle == 0:
        print((' ' * (edge_x + distance)), "", front_c('-'), sep='')

        print((' ' * (edge_x + distance)), front_c('R') + "  ______", front_c('-'), sep='')

        print((' ' * (edge_x + distance)), front_c('R') + " /", front_c('C') + "|_||_\\", front_c('R') + "`.__", front_c('-'), end='', sep='')

        # Speed:
        if show_stats == True:
            print((' ' * (distance_stats + 8)), front_c('W') + 'Speed: ' + front_c('R') + back_c('B') + ('X' * c.STATS[0][0]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('R') + "(   ", front_c('W') + "_    _ ", front_c('R') + "_", front_c('Y') + "\\", front_c('-'), end='', sep='')

        # Acceleration:
        if show_stats == True:
            print((' ' * distance_stats), front_c('W') + 'Acceleration: ' + front_c('Y') + back_c('B') + ('X' * c.STATS[0][1]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('W') + "=", front_c('R') + "`-", front_c('W') + "(_)", front_c('R') + "--", front_c('W') + "(_)", front_c('R') + "-", front_c('W') + "'", front_c('-'), end='', sep='')

        # Weight:
        if show_stats == True:
            print((' ' * (distance_stats + 6)), front_c('W') + 'Weight: ' + front_c('C') + back_c('B') + ('X' * c.STATS[0][2]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
    # Motorcycle:
    if vehicle == 1:
        print((' ' * (edge_x + distance)), "", sep='')

        print((' ' * (edge_x + distance)), "", sep='')

        print((' ' * (edge_x + distance)), front_c('M') + "     ,", front_c('-'), end='', sep='')

        # Speed:
        if show_stats == True:
            print((' ' * (distance_stats + 10)), front_c('W') + 'Speed: ' + front_c('R') + back_c('B') + ('X' * c.STATS[1][0]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('M') + "::,.->\-", front_c('Y') + ".", front_c('-'), end='', sep='')

        # Acceleration:
        if show_stats == True:
            print((' ' * distance_stats), front_c('W') + 'Acceleration: ' + front_c('Y') + back_c('B') + ('X' * c.STATS[1][1]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('W') + "(_)", front_c('M') + "'==", front_c('W') + "(_)", front_c('-'), end='', sep='')
    
        # Weight:
        if show_stats == True:
            print((' ' * (distance_stats + 6)), front_c('W') + 'Weight: ' + front_c('C') + back_c('B') + ('X' * c.STATS[1][2]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
    # Bus:
    if vehicle == 2:
        print((' ' * (edge_x + distance)), front_c('C') + "_______________", front_c('-'), sep='')

        print((' ' * (edge_x + distance)), front_c('C') + "| ", front_c('BL') + "[][][][][] ", front_c('C') + "|_\_", front_c('-'), sep='')

        print((' ' * (edge_x + distance)), front_c('C') + "| ", front_c('W') + ",-.       ,-. ", front_c('Y') + ".", front_c('C') + "|", front_c('-'), end='', sep='')

        # Speed:
        if show_stats == True:
            print((' ' * (distance_stats + 7)), front_c('W') + 'Speed: ' + front_c('R') + back_c('B') + ('X' * c.STATS[2][0]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('C') + "`", front_c('W') + "( ", front_c('Y') + "o", front_c('W') + " )", front_c('C') + "-----", front_c('W') + "( ", front_c('Y') + "o", front_c('W') + " )", front_c('C') + "-'", front_c('-'), end='', sep='')

        # Acceleration:
        if show_stats == True:
            print((' ' * distance_stats), front_c('W') + 'Acceleration: ' + front_c('Y') + back_c('B') + ('X' * c.STATS[2][1]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('W') + "  `-'       `-'", front_c('-'), end='', sep='')
    
        # Weight:
        if show_stats == True:
            print((' ' * (distance_stats + 9)), front_c('W') + 'Weight: ' + front_c('C') + back_c('B') + ('X' * c.STATS[2][2]), front_c('W') + back_c('B'), sep='')
        else:
            print()
    
    # Go kart:
    if vehicle == 3:
        print((' ' * (edge_x + distance)), sep='')

        print((' ' * (edge_x + distance)), sep='')

        print((' ' * (edge_x + distance)), front_c('Y') + "__", front_c('-'), end='', sep='')

        # Speed:
        if show_stats == True:
            print((' ' * (distance_stats + 14)), front_c('W') + 'Speed: ' + front_c('R') + back_c('B') + ('X' * c.STATS[3][0]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('Y') + ".-'--", front_c('C') + "`", front_c('Y') + "-._", front_c('-'), end='', sep='')

        # Acceleration:
        if show_stats == True:
            print((' ' * distance_stats), front_c('W') + 'Acceleration: ' + front_c('Y') + back_c('B') + ('X' * c.STATS[3][1]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('Y') + "'-", front_c('W') + "O", front_c('Y') + "---", front_c('W') + "O", front_c('Y') + "--", front_c('R') + "'", front_c('-'), end='', sep='')
    
        # Weight:
        if show_stats == True:
            print((' ' * (distance_stats + 5)), front_c('W') + 'Weight: ' + front_c('C') + back_c('B') + ('X' * c.STATS[3][2]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
    # Truck:
    if vehicle == 4:
        print((' ' * (edge_x + distance)), sep='')

        print((' ' * (edge_x + distance)), front_c('G') + "         ___", front_c('-'), sep='')

        print((' ' * (edge_x + distance)), front_c('G') + "_________|", front_c('C') + "[_\\", front_c('G') + "___", front_c('-'), end='', sep='')

        # Speed:
        if show_stats == True:
            print((' ' * (distance_stats + 9)), front_c('W') + 'Speed: ' + front_c('R') + back_c('B') + ('X' * c.STATS[4][0]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('G') + "|", front_c('R') + "o  ", front_c('W') + "_   ", front_c('G') + "|-  | ", front_c('W') + "_ ", front_c('Y') + "o", front_c('G') + ")", front_c('-'), end='', sep='')

        # Acceleration:
        if show_stats == True:
            print((' ' * distance_stats), front_c('W') + 'Acceleration: ' + front_c('Y') + back_c('B') + ('X' * c.STATS[4][1]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('G') + "'--", front_c('W') + "(_)", front_c('G') + "-------", front_c('W') + "(_)", front_c('G') + "´", front_c('-'), end='', sep='')
    
        # Weight:
        if show_stats == True:
            print((' ' * (distance_stats + 7)), front_c('W') + 'Weight: ' + front_c('C') + back_c('B') + ('X' * c.STATS[4][2]), front_c('W') + back_c('B'), sep='')
        else:
            print()
    
    # Monster truck:
    if vehicle == 5:
        print((' ' * (edge_x + distance)), "", sep='')

        print((' ' * (edge_x + distance)), front_c('R') + " _/\______", front_c('C') + "\\", front_c('R') + "__", front_c('-'), sep='')

        print((' ' * (edge_x + distance)), front_c('R') + "/ ", front_c('W') + ",-.", front_c('R') + " -|-  ", front_c('W') + ",-.", front_c('R') + "`-", front_c('Y') + ".", front_c('-'), end='', sep='')

        # Speed:
        if show_stats == True:
            print((' ' * (distance_stats + 7)), front_c('W') + 'Speed: ' + front_c('R') + back_c('B') + ('X' * c.STATS[5][0]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('R') + "`", front_c('W') + "( ", front_c('Y') +  "o", front_c('W') + " )", front_c('R') + "----", front_c('W') + "( ", front_c('Y') + "o", front_c('W') + " )", front_c('R') + "-'", front_c('-'), end='', sep='')

        # Acceleration:
        if show_stats == True:
            print((' ' * distance_stats), front_c('W') + 'Acceleration: ' + front_c('Y') + back_c('B') + ('X' * c.STATS[5][1]), front_c('W') + back_c('B'), sep='')
        else:
            print()
        
        print((' ' * (edge_x + distance)), front_c('W') + "  `-'      `-'", end='', sep='')
    
        # Weight:
        if show_stats == True:
            print((' ' * (distance_stats + 9)), front_c('W') + 'Weight: ' + front_c('C') + back_c('B') + ('X' * c.STATS[5][2]), front_c('W') + back_c('B'), sep='')
        else:
            print()
    
    # Reset colors:
    front_c('-', False)
    back_c('-', False)
    styles_c('-', False)
