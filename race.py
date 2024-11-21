# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *

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

    # Track color:
    if c.TRACK == 1:
        track_color = 'R'
    if c.TRACK == 2:
        track_color = 'Bl'
    if c.TRACK == 3:
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
                edge(y=7)
                print((' ' * c.EDGE_X), end='')

                # Line:
                for j in range(len(track_line)):
                    print(track_line[j], end='', sep='')
                
                # Spaces:
                edge(y=6)

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
                edge(y=7)
                
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
                edge(y=6)

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
                edge(y=7)
                print(' ' * c.EDGE_X, end='')
                
                # Line:
                for j in range(len(track_line)):
                    print(track_line[j], end='', sep='')
                
                # Spaces:
                edge(y=6)

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
        # Music:
        play_music('Track')

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
        edge(y=7)
        print((' ' * c.EDGE_X), end='')
        
        # Line:
        for j in range(len(track_line_init)):
            print(track_line_init[j], end='', sep='')

        # Spaces:
        edge(y=5)

        # Banner bottom:
        color(f='Y', b='B', ff=False)
        line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X, y=2)

        line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True)
        back_c('B', False)
        line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True, switch=True)
        back_c('B', False)

        color(f='Y', b='B', ff=False)
        line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)
        input()