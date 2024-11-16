# Import the modules to use the colors

import colorama
from colorama import Fore, Back, Style

# Initialize Colorama:
colorama.init()

# Style:
def styles_c(style, change=True):
    if change == False:
        if style == 'N':
            return style.NORMAL
        elif style == 'D':
            return style.DIM
        elif style == 'B':
            return style.BRIGHT
        else:
            return style.RESET_ALL
    else:
        if style == 'N':
            print(style.NORMAL, end='')
        elif style == 'D':
            print(style.DIM, end='')
        elif style == 'B':
            print(style.BRIGHT, end='')
        else:
            print(style.RESET_ALL, end='')

# Text color:
def front_c(color, change=True):
    if change == False:
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
def back_c(color, change=True):
    if change == False:
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
