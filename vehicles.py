# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *

# Show the vehicles:
def show_vehicle(vehicle, distance, **options):
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
    
    # Car:
    if vehicle == 0:
        print((' ' * (edge_x + distance)), "", sep='')
        print((' ' * (edge_x + distance)), front_c('R') + " _/\______", front_c('C') + "\\", front_c('R') + "__", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('R') + "/ ", front_c('W') + ",-.", front_c('R') + " -|-  ", front_c('W') + ",-.", front_c('R') + "`-", front_c('Y') + ".", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('R') + "`", front_c('W') + "( ", front_c('Y') +  "o", front_c('W') + " )", front_c('R') + "----", front_c('W') + "( ", front_c('Y') + "o", front_c('W') + " )", front_c('R') + "-'", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('W') + "  `-'      `-'", sep='')
        
    # Motorcycle:
    if vehicle == 1:
        print((' ' * (edge_x + distance)), "", sep='')
        print((' ' * (edge_x + distance)), "", sep='')
        print((' ' * (edge_x + distance)), front_c('M') + "     ,", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('M') + "::,.->\-", front_c('Y') + ".", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('W') + "(_)", front_c('M') + "'==", front_c('W') + "(_)", front_c('-'), sep='')
    
    # Bus:
    if vehicle == 2:
        print((' ' * (edge_x + distance)), front_c('C') + "_______________", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('C') + "| ", front_c('BL') + "[][][][][] ", front_c('C') + "|_\_", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('C') + "| ", front_c('W') + ",-.       ,-. ", front_c('Y') + ".", front_c('C') + "|", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('C') + "`", front_c('W') + "( ", front_c('Y') + "o", front_c('W') + " )", front_c('C') + "-----", front_c('W') + "( ", front_c('Y') + "o", front_c('W') + " )", front_c('C') + "-'", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('W') + "  `-'       `-'", front_c('-'), sep='')
    
    # Go kart:
    if vehicle == 3:
        print((' ' * (edge_x + distance)), sep='')
        print((' ' * (edge_x + distance)), sep='')
        print((' ' * (edge_x + distance)), front_c('Y') + "__", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('Y') + ".-'--", front_c('C') + "`", front_c('Y') + "-._", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('Y') + "'-", front_c('W') + "O", front_c('Y') + "---", front_c('W') + "O", front_c('Y') + "--", front_c('R') + "'", front_c('-'), sep='')
    
    # Truck:
    if vehicle == 4:
        print((' ' * (edge_x + distance)), sep='')
        print((' ' * (edge_x + distance)), front_c('G') + "         ___", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('G') + "_________|", front_c('C') + "[_\\", front_c('G') + "___", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('G') + "|", front_c('R') + "o  ", front_c('W') + "_   ", front_c('G') + "|-  | ", front_c('W') + "_ ", front_c('Y') + "o", front_c('G') + ")", front_c('-'), sep='')
        print((' ' * (edge_x + distance)), front_c('G') + "'--", front_c('W') + "(_)", front_c('G') + "-------", front_c('W') + "(_)", front_c('G') + "´", front_c('-'), sep='')
    
    # Reset colors:
    front_c('-', False)
    back_c('-', False)
    styles_c('-', False)
