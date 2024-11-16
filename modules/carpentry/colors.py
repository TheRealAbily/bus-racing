# Import the modules to use the colors

import colorama
from colorama import Fore, Back, Style

# Initialize Colorama:
colorama.init()

# Style:
def styles_c(style):
    if style == 'N':
        style.NORMAL
    elif style == 'D':
        style.DIM
    elif style == 'B':
        style.BRIGHT
    else:
        style.RESET_ALL

# Text color:
def front_c(color):
    if color == 'B':
        Fore.BLACK
    elif color == 'R':
        Fore.RED
    elif color == 'G':
        Fore.GREEN
    elif color == 'Y':
        Fore.YELLOW
    elif color == 'Bl':
        Fore.BLUE
    elif color == 'M':
        Fore.MAGENTA
    elif color == 'C':
        Fore.CYAN
    elif color == 'W':
        Fore.WHITE
    else:
        Fore.RESET

# Background color:
def back_c(color):
    if color == 'B':
        Back.BLACK
    elif color == 'R':
        Back.RED
    elif color == 'G':
        Back.GREEN
    elif color == 'Y':
        Back.YELLOW
    elif color == 'Bl':
        Back.BLUE
    elif color == 'M':
        Back.MAGENTA
    elif color == 'C':
        Back.CYAN
    elif color == 'W':
        Back.WHITE
    else:
        Back.RESET
