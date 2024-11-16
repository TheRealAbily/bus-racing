# Import modules from other subfolders

from modules.carpentry import *
from modules.config import *

# Variables:
black = (back_c('B', change=False) + front_c('', change=False) + '  ')
white = (back_c('W', change=False) + front_c('', change=False) + '  ')
edge = (back_c('', change=False) + front_c('Y', change=False) + '|')

# Main menu:
def section_1():
    clear()
    front_c('Y')
    line('=', WIDHT + EXTRA_FIX, points='o', x=EDGE_X, y=EDGE_Y)
    line(black, floor(WIDHT / 2), intr=white, points=edge, x=EDGE_X, less=True)
    line(black, floor(WIDHT / 2), intr=white, points=edge, x=EDGE_X, less=True, switch=True)