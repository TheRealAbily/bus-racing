# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *
from random import randint

# Config:
import config as c

# Lights:
def section_16():
    # SFX:
    play_sfx('Pre start')

    # Variable:
    distance = 27
    light_c1 = front_c('W')
    light_c2 = front_c('W')
    light_c3 = front_c('W')
    light_c4 = front_c('W')

    # Lights:
    for m in range(5):
        # Clear the screen:
        clear()
        
        # Spaces:
        edge(y=c.EDGE_Y + 5)

        # Colors:
        back_c('B', False)
        
        if m == 1:
            light_c1 = front_c('R')

            # SFX:
            play_sfx('Countdown')
        elif m == 2:
            light_c2 = (front_c('R') + styles_c('B'))
        elif m == 3:
            light_c3 = (front_c('Y') + styles_c('B'))
        elif m == 4:
            light_c4 = (front_c('G') + styles_c('B'))

        # Light:
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '       _____________        _____________ ', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c1 + ' _______ ',  styles_c('N'), front_c('W') + '  |      |  ', light_c1 + ' _______ ',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c1 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |      |  ', light_c1 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c1 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c1 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c1 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c1 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c1 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |------|  ', light_c1 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c2 + ' _______ ',  styles_c('N'), front_c('W') + '  |------|  ', light_c2 + ' _______ ',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c2 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |      |  ', light_c2 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c2 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c2 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c2 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c2 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c2 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |      |  ', light_c2 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c3 + ' _______ ',  styles_c('N'), front_c('W') + '  |      |  ', light_c3 + ' _______ ',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c3 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |      |  ', light_c3 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c3 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c3 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c3 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c3 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c3 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |------|  ', light_c3 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c4 + ' _______ ',  styles_c('N'), front_c('W') + '  |------|  ', light_c4 + ' _______ ',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c4 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |      |  ', light_c4 + '/XXXXXXX\\', styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c4 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c4 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c4 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |      |  ', light_c4 + '|XXXXXXX|',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |  ', light_c4 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |      |  ', light_c4 + '\XXXXXXX/',  styles_c('N'), front_c('W') + '  |', sep='')
        print((' ' * (c.EDGE_X + distance)), front_c('W') + styles_c('N') + '      |_____________|      |___________', front_c('W') + '__|', sep='')

        # Spaces:
        edge(y=c.EDGE_Y)

        # Restart colors:
        back_c('-', False)
        front_c('-', False)

        # Move the cursor:
        pos(x=c.EDGE_X + 0, y=c.EDGE_Y + 0)

        # Wait:
        if m == 0:
            wait(2.65)
        elif m < 4:
            # Time:
            wait(0.9)
        else:
            # Time:
            wait(1.5)

            # Variable:
            c.SECTION = 16
