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

# Race:
def section_15(firts_time):
    # Clear the screen:
    clear()

    # Variables:
    start_race = False
    in_race = True
    
    # Track color:
    if c.TRACK == 1:
        track_color = 'R'
    elif c.TRACK == 2:
        track_color = 'Bl'
    elif c.TRACK == 3:
        track_color = 'M'
    else:
        track_color = 'G'
    
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
    
    # Only see:
    if firts_time == True:
        # Variables:
        section = 0
        loop = True
        switch = False
        count = 0
        max_count = 3
        selected_color = 'B'

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
                
                # Append:
                if count < max_count:
                    count += 1
                else:
                    count = 0
                    max_count = 10

                    # Switch color:
                    if selected_color == 'B':
                        selected_color = 'W'
                    else:
                        selected_color = 'B'
                
                track_line.append(back_c(selected_color) + ' ')

                # Pop:
                track_line.pop(0)

                # Space:
                print(' ' * c.EDGE_X, end='')

                # Line:
                for j in range(len(track_line)):
                    print(track_line[j], end='', sep='')
                
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
                print(' ' * c.EDGE_X, end='')
                
                # Line:
                for j in range(len(track_line)):
                    print(track_line[j], end='', sep='')
                
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

                # Time:
                wait(3)

                # Variable:
                loop = False

        # Variable:
        c.SECTION = 15

    else:
        track_lines = [back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ',
                    back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ',
                    back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ',
                    back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
                    # back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
                    back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
                    back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
                    back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ',
                    back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ',
                    back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ',
                    back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('W') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ' + back_c('B') + ' ']

        # Set the same:
        if c.GAME_MODE == 0:
            c.VEHICLE_PLAYER_2 = c.VEHICLE_PLAYER_CPU
        
        # Variables:
        adjust_cars = -1
        track_line_number = 0
        distance_1 = 0
        distance_2 = 0
        switch = -1

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
            # for j in range(len(track_line_init)):
            #     print(track_line_init[j], end='', sep='')
            # back_c('B', False)

            # Line:
            print(track_lines[track_line_number], end='', sep='')
            back_c('B', False)

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

            # Race:
            if start_race == False:
                wait(1)
                start_race = True
            else:
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
                if adjust_cars < 0:
                    if c.DISTANCE_PLAYER_1 > 50 and c.DISTANCE_PLAYER_2 > 30 or c.DISTANCE_PLAYER_2 > 50 and c.DISTANCE_PLAYER_1 > 30:
                        adjust_cars = 40

                        if switch == -1:
                            switch = 0
                elif adjust_cars >= 0:
                    c.DISTANCE_PLAYER_1 -= 2
                    c.DISTANCE_PLAYER_2 -= 2
                    adjust_cars -= 2

                # Line:
                if c.DISTANCE_PLAYER_1 > 25 and c.DISTANCE_PLAYER_2 > 25 and c.ANIMATION_LINE_TRACK == True:
                    for p in range(max(round(distance_1), round(distance_2))):
                        if track_line_count < 10:
                            track_line_count += 1
                        else:
                            track_line_count = 0

                            if track_line_color == 'B':
                                track_line_color = 'W'
                            else:
                                track_line_color = 'B'
                        
                        track_line_init.append(back_c(track_line_color) + ' ')
                        track_line_init.pop(0)

                # FPS:
                wait(c.GAME_TICK)
