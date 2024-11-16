# Import the modules to use the colors

import colorama
from colorama import Fore, Back, Style

# Initialize Colorama:
colorama.init()

# Style:
def styles_c(style):
    if style == 'N':
        return style.NORMAL
    elif style == 'D':
        return style.DIM
    elif style == 'B':
        return style.BRIGHT
    else:
        return style.RESET_ALL

# Text color:
def front_c(color):
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

# Background color:
def back_c(color):
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