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
black = (color(b='B') + '  ')
white = (color(b='W') + '  ')
edges = (front_c('Y') + back_c('B') + '|')
distance_left = 19
distance_right = 19
option = ''

# Race:
def section_15(firts_time):
    # Clear the screen:
    clear()

    # Only see:
    if firts_time == True:
        # Variable:
        section = 0
        loop = True
        switch = False

        # SFX:
        play_sfx('Show race track')

        # Loop:
        while loop == True:
            # Sections:
            if section == 0:
                # Banner top:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X, y=2)

                line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

                # Spaces:
                edge(y=7)
                
                # Line:
                line(back_c('W') + (' ' * 10), 5, intr=back_c('B') + (' ' * 10), x=c.EDGE_X, switch=True)

                # Spaces:
                edge(y=7)

                # Banner bottom:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X, y=2)

                line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

                # Time:
                wait(2)

                # Variable:
                section = 1
            
            elif 1 <= section <= 40:
                # Clear the screen:
                clear()

                # Banner top:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X, y=2)

                if switch == True:
                    line(black, floor(c.WIDHT / 2), intr=white, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(black, floor(c.WIDHT / 2), intr=white, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                else:
                    line(white, floor(c.WIDHT / 2), intr=black, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(white, floor(c.WIDHT / 2), intr=black, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)

                # Spaces:
                edge(y=7)
                
                # Line:
                line(back_c('W') + (' ' * 10), 5, intr=back_c('B') + (' ' * 10), x=c.EDGE_X, switch=True)

                # Spaces:
                edge(y=7)

                # Banner bottom:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X, y=2)

                if switch == True:
                    line(black, floor(c.WIDHT / 2), intr=white, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(black, floor(c.WIDHT / 2), intr=white, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)
                else:
                    line(white, floor(c.WIDHT / 2), intr=black, x=c.EDGE_X, less=True)
                    back_c('B', False)
                    line(white, floor(c.WIDHT / 2), intr=black, x=c.EDGE_X, less=True, switch=True)
                    back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, x=c.EDGE_X)

                # Time:
                wait(0.15) # 7.5

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

                line(black, floor(c.WIDHT / 2), intr=white, right=edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(black, floor(c.WIDHT / 2), intr=white, right=edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX, right='o', x=c.EDGE_X)

                # Spaces:
                edge(y=7)
                
                # Line:
                line(back_c('W') + (' ' * 10), 5, intr=back_c('B') + (' ' * 10), x=c.EDGE_X, switch=True)

                # Spaces:
                edge(y=7)

                # Banner bottom:
                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX + 1, right='o', x=c.EDGE_X, y=2)

                line(black, floor(c.WIDHT / 2), intr=white, right=back_c('B') + ' ' + edges, x=c.EDGE_X, less=True)
                back_c('B', False)
                line(black, floor(c.WIDHT / 2), intr=white, right=back_c('W') + ' ' + back_c('B') + edges, x=c.EDGE_X, less=True, switch=True)
                back_c('B', False)

                color(f='Y', b='B', ff=False)
                line('=', c.WIDHT + c.EXTRA_FIX + 1, right='o', x=c.EDGE_X)

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

        line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True)
        back_c('B', False)
        line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True, switch=True)
        back_c('B', False)

        color(f='Y', b='B', ff=False)
        line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)

        # Spaces:
        edge(y=7)
        
        # Line:
        line(back_c('W') + (' ' * 10), 5, intr=back_c('B') + (' ' * 10), x=c.EDGE_X, switch=True)

        # Spaces:
        edge(y=7)

        # Banner bottom:
        color(f='Y', b='B', ff=False)
        line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X, y=2)

        line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True)
        back_c('B', False)
        line(black, floor(c.WIDHT / 2), intr=white, left=edges, x=c.EDGE_X, less=True, switch=True)
        back_c('B', False)

        color(f='Y', b='B', ff=False)
        line('=', c.WIDHT + c.EXTRA_FIX, left='o', x=c.EDGE_X)
        input()