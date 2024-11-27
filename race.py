# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *
from draw_vehicles import *
from random import randint

# Config:
import config as c

# Variables:
firts_color = (color(b='B') + '  ')
second_color = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 19
distance_right = 19
option = ''

# Point distance:
def point_distance(point_a, point_b):
    if point_a < point_b:
        point_b -= point_a

        return abs(round(point_b / 2))
    else:
        point_a -= point_b

        return abs(round(point_a / 2))

# Clamp:
def clamp(var, min, max):
    if var < min:
        var = min
    
    if var > max:
        var = max
    
    return var

# Race:
def section_15(firts_time):
    # Clear the screen:
    clear()

    # Variables:
    start_race = False
    in_race = True

    # Track color:
    if c.TRACK == 1:
        # Figure 8:
        track_color = 'R'
    elif c.TRACK == 2:
        # Delfino Square:
        track_color = 'Bl'
    elif c.TRACK == 3:
        # Waluigi Pinball:
        track_color = 'M'
    elif c.TRACK == 4:
        # Rainbow Road:
        track_color = 'G'
    elif c.TRACK == 5:
        # Desert Hills:
        track_color = 'Y'
    elif c.TRACK == 6:
        # Sky Garden:
        track_color = 'C'
    elif c.TRACK == 7:
        # Bowser Castle:
        track_color = 'B'
    elif c.TRACK == 8:
        # Wario Stadium:
        track_color = 'Y'
    elif c.TRACK == 9:
        # Peach Gardens:
        track_color = 'G'
    elif c.TRACK == 10:
        # Yoshi Falls:
        track_color = 'Bl'
    else:
        # Tokyo Drift:
        track_color = 'R'
    
    firts_color = (color(b=track_color) + '  ')
    
    # Track:
    track_line = [back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ',
        back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ',
        back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ',
        back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ',
        back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ',
        back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ',
        back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ',
        back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ',
        back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ', back_c('W') + ' ',
        back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ', back_c('B') + ' ']
    track_line_init = track_line
    
    # Lines:
    track_lines = [back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ',
        back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ',
        back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ',
        back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
        back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
        back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
        back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
        back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ',
        back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ',
        back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ']

    # Names:
    track_names = ['Figure 8', 'Delfino Square', 'Waluigi Painball', 'Rainbow Road', 'Desert Hills', 'Sky Garden', 'Bowser Castle', 'Wario Stadium', 'Peach Garden', 'Yoshi Falls', 'Tokyo Drift']
    
    # Only see:
    if firts_time == True:
        # Variables:
        section = 0
        loop = True
        switch = False
        count = 0
        max_count = 3
        selected_color = 'B'
        track_line_number = 0

        # SFX:
        play_sfx('Show race track')

        # Loop:
        while loop == True:
            # Sections:
            if section == 0:
                # Banner top:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X, y=2)

                line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

                # Spaces:
                edge(y=8)
                print((' ' * c.EDGE_X), end='')

                # Line:
                for j in range(len(track_line)):
                    print(track_line[j], end='', sep='')
                
                # Spaces:
                edge(y=7)

                # Banner bottom:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X, y=2)

                line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

                # Track name:
                edge(y=2)
                print((' ' * (c.EDGE_X + 36)), front_c('Y') + styles_c('B') + '- Track: ' + front_c('W') + track_names[c.TRACK - 1] + ' - ', end='', sep='')

                # Time:
                wait(2)

                # Variable:
                section = 1
            
            elif 1 <= section <= 80:
                # Clear the screen:
                clear()

                # Banner top:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X, y=2)

                if switch == True:
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                else:
                    line(second_color, floor(c.WIDHT / 2), intr=firts_color, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(second_color, floor(c.WIDHT / 2), intr=firts_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)

                # Spaces:
                edge(y=8)

                # Line:
                print(' ' * c.EDGE_X, track_lines[track_line_number], end='', sep='')
                back_c('B', False)

                if switch >= 0:
                    if track_line_number < len(track_lines) - 1:
                        track_line_number += 1
                    else:
                        track_line_number = 0
                
                # Spaces:
                edge(y=7)

                # Banner bottom:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X, y=2)

                if switch == True:
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                else:
                    line(second_color, floor(c.WIDHT / 2), intr=firts_color, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(second_color, floor(c.WIDHT / 2), intr=firts_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)

                # Track name:
                edge(y=2)
                print((' ' * (c.EDGE_X + 36)), front_c('Y') + styles_c('B') + '- Track: ' + front_c('W') + track_names[c.TRACK - 1] + ' - ', end='', sep='')

                # Time:
                wait(0.075) # 7.5

                # Variable:
                section += 1

                # Switch:
                if switch == True:
                    switch = False
                else:
                    switch = True
            else:
                # Clear the screen:
                clear()

                # Banner top:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X, y=2)

                line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)

                # Spaces:
                edge(y=8)

                # Line:
                print(' ' * c.EDGE_X, track_lines[track_line_number], end='', sep='')
                back_c('B', False)
                
                # Spaces:
                edge(y=7)

                # Banner bottom:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X, y=2)

                line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)

                # Track name:
                edge(y=2)
                print((' ' * (c.EDGE_X + 36)), front_c('Y') + styles_c('B') + '- Track: ' + front_c('W') + track_names[c.TRACK - 1] + ' - ', end='', sep='')
                        
                # Goal:
                back_c('B', False)
                switch_goal = False

                for r in range(17):
                    pos(x=c.EDGE_X + 95, y=c.EDGE_Y + 5 + r)

                    if switch_goal == False:
                        print(front_c('W') + back_c('B') + '|' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + front_c('W') + back_c('B') + '|', end='', sep='')
                        switch_goal = True
                    else:
                        print(front_c('W') + back_c('B') + '|' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + front_c('W') + back_c('B') + '|', end='', sep='')
                        switch_goal = False
                
                pos(x=c.EDGE_X, y=c.EDGE_Y + 28)

                # Time:
                wait(3)

                # Variable:
                loop = False

        # Variable:
        c.SECTION = 15

    else:
        # Set the same:
        if c.GAME_MODE == 0:
            c.VEHICLE_PLAYER_2 = c.VEHICLE_PLAYER_CPU
        
        # Variables:
        adjust_cars = -1
        track_line_number = 0
        distance_1 = 0
        distance_2 = 0
        switch = -1
        stop_adjust = False
        stop_animation = False
        stop_move = False
        spaces_delete = 0
        switch_spaces_delete = 0
        ticks = 0

        # Reset time:
        c.RACE_TIME = 0
        
        # Adjust player 1:
        if c.VEHICLE_PLAYER_1 == 0:
            adjust_player_1 = 7
        elif c.VEHICLE_PLAYER_1 == 1:
            adjust_player_1 = 11
        elif c.VEHICLE_PLAYER_1 == 2:
            adjust_player_1 = 2
        elif c.VEHICLE_PLAYER_1 == 3:
            adjust_player_1 = 10
        elif c.VEHICLE_PLAYER_1 == 4:
            adjust_player_1 = 2
        else:
            adjust_player_1 = 3
        
        # Adjust player 2:
        if c.VEHICLE_PLAYER_2 == 0:
            adjust_player_2 = 7
        elif c.VEHICLE_PLAYER_2 == 1:
            adjust_player_2 = 11
        elif c.VEHICLE_PLAYER_2 == 2:
            adjust_player_2 = 2
        elif c.VEHICLE_PLAYER_2 == 3:
            adjust_player_2 = 10
        elif c.VEHICLE_PLAYER_2 == 4:
            adjust_player_2 = 2
        else:
            adjust_player_2 = 3
        
        # Music:
        if c.VEHICLE_PLAYER_1 == 2 and c.VEHICLE_PLAYER_2 == 2:
            if randint(0, 100) <= c.EASTER_EGG_PROBABILITY_1:
                play_music('Easter egg')
            else:
                play_music('Track')
        else:
            play_music('Track')

        while in_race == True:
            # Vehicles:
            line_player_1 = [[(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 0), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 1), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 2), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 3), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 4), ' ' * c.REMAINING_DISTANCE_PLAYER_1]]

            # Vehicles:
            line_player_2 = [[(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 0), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 1), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 2), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 3), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * round(c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 4), ' ' * c.REMAINING_DISTANCE_PLAYER_2]]

            # Clear the screen:
            clear()

            # Banner top:
            if stop_animation == False:
                if switch == -1:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X, y=2)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)
                elif switch == 0:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X, y=2)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)
                else:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X, y=2)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)
            else:
                if switch == 0:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X, y=2)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)
                else:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X, y=2)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)

            # Spaces:
            edge(y=1)
            
            # Show the player 1:
            for p in range(len(line_player_1)):
                for t in range(len(line_player_1[0])):
                    print(line_player_1[p][t], end='', sep='')
                print()

            # Spaces:
            edge(y=1)
            print((' ' * c.EDGE_X), end='')

            # Line:
            print(track_lines[track_line_number], end='', sep='')
            back_c('B', False)

            if stop_animation == False:
                if switch >= 0:
                    if track_line_number < len(track_lines) - 1:
                        track_line_number += 1
                    else:
                        track_line_number = 0

            # Spaces:
            edge(y=2)
            
            # Show the player 2:
            for p in range(len(line_player_2)):
                for t in range(len(line_player_2[0])):
                    print(line_player_2[p][t], end='', sep='')
                print()

            # Spaces:
            edge(y=1)

            # Banner bottom:
            if stop_animation == False:
                if switch == -1:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)
                elif switch == 0:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)
                else:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)

                # Switch:
                if switch == 1:
                    switch = 0
                else:
                    switch = 1
            else:
                if switch == 0:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)
                else:
                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)

                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(firts_color, floor(c.WIDHT / 2), intr=second_color, right=edges, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                    color(f='Y', b='B', ff=False)
                    line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)

            # Race:
            if start_race == False:
                wait(1)
                start_race = True
            else:
                if stop_move == False:
                    # Run player 1:
                    if 1 <= randint(1, c.MAX_ACCELERATION) <= c.STATS[c.VEHICLE_PLAYER_1][1]:
                        if 1 <= randint(1, c.STATS[c.VEHICLE_PLAYER_1][2]) <= c.MAX_WEIGHT:
                            c.DISTANCE_PLAYER_1 += (c.STATS[c.VEHICLE_PLAYER_1][0] / 2)
                            distance_1 = (c.STATS[c.VEHICLE_PLAYER_1][0] / 2)
                        else:
                            c.DISTANCE_PLAYER_1 += c.STATS[c.VEHICLE_PLAYER_1][0]
                            distance_1 = c.STATS[c.VEHICLE_PLAYER_1][0]

                    # Run player 2:
                    if 1 <= randint(1, c.MAX_ACCELERATION) <= c.STATS[c.VEHICLE_PLAYER_2][1]:
                        if 1 <= randint(1, c.STATS[c.VEHICLE_PLAYER_2][2]) <= c.MAX_WEIGHT:
                            c.DISTANCE_PLAYER_2 += (c.STATS[c.VEHICLE_PLAYER_2][0] / 2)
                            distance_2 = (c.STATS[c.VEHICLE_PLAYER_2][0] / 2)
                        else:
                            c.DISTANCE_PLAYER_2 += c.STATS[c.VEHICLE_PLAYER_2][0]
                            distance_2 = c.STATS[c.VEHICLE_PLAYER_2][0]
                    
                    # Adjust:
                    if stop_adjust == False:
                        if adjust_cars < 0:
                            for l in range(5):
                                distance = (5 - l) * 10
                                adjust_cars = -1
                                
                                if c.DISTANCE_PLAYER_1 > distance and c.DISTANCE_PLAYER_2 > distance:
                                    if distance == 10 and switch_spaces_delete < 3:
                                        switch_spaces_delete += 1
                                        adjust_cars = distance + 5

                                    elif distance == 20 and 3 <= switch_spaces_delete < 5:
                                        switch_spaces_delete += 1
                                        adjust_cars = distance + 10

                                    elif distance == 30 and switch_spaces_delete == 5:
                                        switch_spaces_delete = 0
                                        adjust_cars = distance + 25
                                    break
                                    
                                if ticks == 10 and 3 <= switch_spaces_delete < 5:
                                    switch_spaces_delete = 0
                                elif ticks == 15 and switch_spaces_delete == 5:
                                    switch_spaces_delete = 0

                            if switch == -1:
                                switch = 0
                        
                        elif adjust_cars >= 0:
                            if (c.DISTANCE_PLAYER_1 - 3) >= 0 and (c.DISTANCE_PLAYER_2 - 3) >= 0:
                                c.DISTANCE_PLAYER_1 -= 3
                                c.DISTANCE_PLAYER_2 -= 3
                                adjust_cars -= 2
                            else:
                                adjust_cars = -1
                        else:
                            adjust_cars = -1
                        
                        # Limits:
                        c.DISTANCE_PLAYER_1 = clamp(c.DISTANCE_PLAYER_1, 0, 74)
                        c.DISTANCE_PLAYER_2 = clamp(c.DISTANCE_PLAYER_2, 0, 74)

                # Time:
                if c.RACE_TIME + c.GAME_TICK < c.MAX_RACE_TIME:
                    c.RACE_TIME += c.GAME_TICK
                else:
                    if track_line_number == 0:
                        c.RACE_TIME = c.MAX_RACE_TIME
                        stop_adjust = True
                        
                        # Spaces deleted:
                        if spaces_delete < 15:
                            # Distance:
                            if (c.DISTANCE_PLAYER_1 - 3) >= 0:
                                c.DISTANCE_PLAYER_1 -= 3
                            
                            if (c.DISTANCE_PLAYER_2 - 3) >= 0:
                                c.DISTANCE_PLAYER_2 -= 3
                            
                            # Limits:
                            c.DISTANCE_PLAYER_1 = clamp(c.DISTANCE_PLAYER_1, 0, 74)
                            c.DISTANCE_PLAYER_2 = clamp(c.DISTANCE_PLAYER_2, 0, 74)
                            
                            spaces_delete += 3
                        else:
                            stop_animation = True
                            
                            # Limits:
                            c.DISTANCE_PLAYER_1 = clamp(c.DISTANCE_PLAYER_1, 0, 74)
                            c.DISTANCE_PLAYER_2 = clamp(c.DISTANCE_PLAYER_2, 0, 74)

                            # Stop the race:
                            if c.DISTANCE_PLAYER_1 == 74 or c.DISTANCE_PLAYER_2 == 74:
                                stop_move = True

                                if c.DISTANCE_PLAYER_1 == 74:
                                    c.WINNER = 0
                                else:
                                    c.WINNER = 1
                            
                            # Goal:
                            back_c('B', False)
                            switch_goal = False

                            for r in range(15):
                                pos(x=c.EDGE_X + 95, y=c.EDGE_Y + 5 + r)

                                if switch_goal == False:
                                    print(front_c('W') + back_c('B') + '|' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + front_c('W') + back_c('B') + '|', end='', sep='')
                                    switch_goal = True
                                else:
                                    print(front_c('W') + back_c('B') + '|' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + front_c('W') + back_c('B') + '|', end='', sep='')
                                    switch_goal = False

                # FPS:
                if stop_move == False:
                    wait(c.GAME_TICK)
                    ticks += 1
                else:
                    # Position:
                    pos(x=c.EDGE_X, y=c.EDGE_Y + 25)
                    
                    # Volume:
                    volume_backup = c.VOLUME_MUSIC
                    c.VOLUME_MUSIC = 0
                    volume()
                    
                    # SFX:
                    play_sfx('Winning start')

                    # Time:
                    wait(7)

                    # Volume:
                    c.VOLUME_MUSIC = volume_backup
                    
                    # Variable:
                    c.SECTION = 17

                    # Break the loop:
                    break
