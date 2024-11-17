# Import the modules to use the colors

import colorama
from colorama import Fore, Back, Style

# Initialize Colorama:
colorama.init()

# Colors (back and front), and styles:
def color(**options):
    # Front color:
    front_color = options.get('f', 0)

    # Back color:
    back_color = options.get('b', 0)

    # Style:
    select = options.get('s', 0)

    # Use like function:
    function = options.get('ff', True)

    # Apply the changes:

    # Text:
    if front_color != 0:
        if function == True:
            if front_color == 'B':
                return Fore.BLACK
            elif front_color == 'R':
                return Fore.RED
            elif front_color == 'G':
                return Fore.GREEN
            elif front_color == 'Y':
                return Fore.YELLOW
            elif front_color == 'Bl':
                return Fore.BLUE
            elif front_color == 'M':
                return Fore.MAGENTA
            elif front_color == 'C':
                return Fore.CYAN
            elif front_color == 'W':
                return Fore.WHITE
            else:
                return Fore.RESET
        else:
            if front_color == 'B':
                print(Fore.BLACK, end='')
            elif front_color == 'R':
                print(Fore.RED, end='')
            elif front_color == 'G':
                print(Fore.GREEN, end='')
            elif front_color == 'Y':
                print(Fore.YELLOW, end='')
            elif front_color == 'Bl':
                print(Fore.BLUE, end='')
            elif front_color == 'M':
                print(Fore.MAGENTA, end='')
            elif front_color == 'C':
                print(Fore.CYAN, end='')
            elif front_color == 'W':
                print(Fore.WHITE, end='')
            else:
                print(Fore.RESET, end='')
    
    # Background:
    if back_color != 0:
        if function == True:
            if back_color == 'B':
                return Back.BLACK
            elif back_color == 'R':
                return Back.RED
            elif back_color == 'G':
                return Back.GREEN
            elif back_color == 'Y':
                return Back.YELLOW
            elif back_color == 'Bl':
                return Back.BLUE
            elif back_color == 'M':
                return Back.MAGENTA
            elif back_color == 'C':
                return Back.CYAN
            elif back_color == 'W':
                return Back.WHITE
            else:
                return Back.RESET
        else:
            if back_color == 'B':
                print(Back.BLACK, end='')
            elif back_color == 'R':
                print(Back.RED, end='')
            elif back_color == 'G':
                print(Back.GREEN, end='')
            elif back_color == 'Y':
                print(Back.YELLOW, end='')
            elif back_color == 'Bl':
                print(Back.BLUE, end='')
            elif back_color == 'M':
                print(Back.MAGENTA, end='')
            elif back_color == 'C':
                print(Back.CYAN, end='')
            elif back_color == 'W':
                print(Back.WHITE, end='')
            else:
                print(Back.RESET, end='')
    
    # Style:
    if select != 0:
        if function == True:
            if select == 'N':
                return Style.NORMAL
            elif select == 'D':
                return Style.DIM
            elif select == 'B':
                return Style.BRIGHT
            else:
                return Style.RESET_ALL
        else:
            if select == 'N':
                print(Style.NORMAL, end='')
            elif select == 'D':
                print(Style.DIM, end='')
            elif select == 'B':
                print(Style.BRIGHT, end='')
            else:
                print(Style.RESET_ALL, end='')

# Style:
def styles_c(select, function=True):
    if function == True:
        if select == 'N':
            return Style.NORMAL
        elif select == 'D':
            return Style.DIM
        elif select == 'B':
            return Style.BRIGHT
        else:
            return Style.RESET_ALL
    else:
        if select == 'N':
            print(Style.NORMAL, end='')
        elif select == 'D':
            print(Style.DIM, end='')
        elif select == 'B':
            print(Style.BRIGHT, end='')
        else:
            print(Style.RESET_ALL, end='')

# Text color:
def front_c(color, function=True):
    if function == True:
        if color == 'B':
            return Fore.BLACK
        elif color == 'R':
            return Fore.RED
        elif color == 'G':
            return Fore.GREEN
        elif color == 'Y':
            return Fore.YELLOW
        elif color == 'Bl':
            return Fore.BLUE
        elif color == 'M':
            return Fore.MAGENTA
        elif color == 'C':
            return Fore.CYAN
        elif color == 'W':
            return Fore.WHITE
        else:
            return Fore.RESET
    else:
        if color == 'B':
            print(Fore.BLACK, end='')
        elif color == 'R':
            print(Fore.RED, end='')
        elif color == 'G':
            print(Fore.GREEN, end='')
        elif color == 'Y':
            print(Fore.YELLOW, end='')
        elif color == 'Bl':
            print(Fore.BLUE, end='')
        elif color == 'M':
            print(Fore.MAGENTA, end='')
        elif color == 'C':
            print(Fore.CYAN, end='')
        elif color == 'W':
            print(Fore.WHITE, end='')
        else:
            print(Fore.RESET, end='')

# Background color:
def back_c(color, function=True):
    if function == True:
        if color == 'B':
            return Back.BLACK
        elif color == 'R':
            return Back.RED
        elif color == 'G':
            return Back.GREEN
        elif color == 'Y':
            return Back.YELLOW
        elif color == 'Bl':
            return Back.BLUE
        elif color == 'M':
            return Back.MAGENTA
        elif color == 'C':
            return Back.CYAN
        elif color == 'W':
            return Back.WHITE
        else:
            return Back.RESET
    else:
        if color == 'B':
            print(Back.BLACK, end='')
        elif color == 'R':
            print(Back.RED, end='')
        elif color == 'G':
            print(Back.GREEN, end='')
        elif color == 'Y':
            print(Back.YELLOW, end='')
        elif color == 'Bl':
            print(Back.BLUE, end='')
        elif color == 'M':
            print(Back.MAGENTA, end='')
        elif color == 'C':
            print(Back.CYAN, end='')
        elif color == 'W':
            print(Back.WHITE, end='')
        else:
            print(Back.RESET, end='')
