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
        # Set the same:
        c.VEHICLE_PLAYER_2 = c.VEHICLE_PLAYER_CPU
        
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
            line_player_1 = [[(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 0), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 1), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 2), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 3), ' ' * c.REMAINING_DISTANCE_PLAYER_1],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_1 + adjust_player_1)), draw_vehicle(c.VEHICLE_PLAYER_1, 4), ' ' * c.REMAINING_DISTANCE_PLAYER_1]]

            # Vehicles:
            line_player_2 = [[(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 0), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 1), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 2), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 3), ' ' * c.REMAINING_DISTANCE_PLAYER_2],
                            [(' ' * (c.EDGE_X + c.DISTANCE_PLAYER_2 + adjust_player_2)), draw_vehicle(c.VEHICLE_PLAYER_2, 4), ' ' * c.REMAINING_DISTANCE_PLAYER_2]]

            # Clear the screen:
            clear()

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
            for j in range(len(track_line_init)):
                print(track_line_init[j], end='', sep='')

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
            color(f='Y', b='B', ff=False)
            line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

            line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True)
            back_c('B', False)
            line(firts_color, floor(c.WIDHT / 2), intr=second_color, left=edges, x=c.EDGE_X, less=True, switch=True)
            back_c('B', False)

            color(f='Y', b='B', ff=False)
            line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

            # Race:
            if start_race == False:
                wait(1)
                start_race = True
            else:
                # Run cars:
                c.DISTANCE_PLAYER_1 += 1
                c.DISTANCE_PLAYER_2 += 1
                
                # FPS:
                wait(1 / c.FPS)