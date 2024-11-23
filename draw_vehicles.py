# Import modules from other subfolders

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *

import config as c

# Draw the vehicles:
def draw_vehicle(vehicle, line):
    # Colors:
    front_c('-', False)
    back_c('-', False)
    styles_c('B', False)

    # Car:
    if vehicle == 0:
        if line == 0:
            part = ''
        elif line == 1:
            part = f'{front_c('R')}  ______ {front_c('-')}'
        elif line == 2:
            part = f'{front_c('R')} /{front_c('C')}|_||_\\{front_c('R')}`.__{front_c('-')}'
        elif line == 3:
            part = f'{front_c('R')}(   {front_c('W')}_    _ {front_c('R')}_{front_c('Y')}\\{front_c('-')}'
        else:
            part = f'{front_c('W')}={front_c('R')}`-{front_c('W')}(_){front_c('R')}--{front_c('W')}(_){front_c('R')}-{front_c('W')}\'{front_c('-')}'

    # Motorcycle:
    elif vehicle == 1:
        if line == 0:
            part = ''
        elif line == 1:
            part = ''
        elif line == 2:
            part = f'{front_c('M')}     ,{front_c('-')}'
        elif line == 3:
            part = f'{front_c('M')}::,.->\-{front_c('Y')}.{front_c('-')}'
        else:
            part = f'{front_c('W')}(_){front_c('M')}\'=={front_c('W')}(_){front_c('-')}'

    # Bus:
    elif vehicle == 2:
        if line == 0:
            part = f'{front_c('C')}_______________{front_c('-')}'
        elif line == 1:
            part = f'{front_c('C')}| {front_c('BL')}[][][][][] {front_c('C')}|_\_{front_c('-')}'
        elif line == 2:
            part = f'{front_c('C')}| {front_c('W')},-.       ,-. {front_c('Y')}.{front_c('C')}|{front_c('-')}'
        elif line == 3:
            part = f'{front_c('C')}`{front_c('W')}( {front_c('Y')}o{front_c('W')} ){front_c('C')}-----{front_c('W')}( {front_c('Y')}o{front_c('W')} ){front_c('C')}-\'{front_c('-')}'
        else:
            part = f'{front_c('W')}  `-\'       `-\'{front_c('-')}'

    # Go kart:
    elif vehicle == 3:
        if line == 0:
            part = ''
        elif line == 1:
            part = ''
        elif line == 2:
            part = f'{front_c('Y')}__{front_c('-')}'
        elif line == 3:
            part = f'{front_c('Y')}.-\'--{front_c('C')}`{front_c('Y')}-._{front_c('-')}'
        else:
            part = f'{front_c('Y')}\'-{front_c('W')}O{front_c('Y')}---{front_c('W')}O{front_c('Y')}--{front_c('R')}\'{front_c('-')}'

    # Truck:
    elif vehicle == 4:
        if line == 0:
            part = ''
        elif line == 1:
            part = f'{front_c('G')}         ___{front_c('-')}'
        elif line == 2:
            part = f'{front_c('G')}_________|{front_c('C')}[_\\{front_c('G')}___{front_c('-')}'
        elif line == 3:
            part = f'{front_c('G')}|{front_c('R')}o  {front_c('W')}_   {front_c('G')}|-  | {front_c('W')}_ {front_c('Y')}o{front_c('G')}){front_c('-')}'
        else:
            part = f'{front_c('G')}\'--{front_c('W')}(_){front_c('G')}-------{front_c('W')}(_){front_c('G')}´{front_c('-')}'

    # Monster car:
    else:
        if line == 0:
            part = ''
        elif line == 1:
            part = f'{front_c('R')} _/\______{front_c('C')}\\{front_c('R')}__{front_c('-')}'
        elif line == 2:
            part = f'{front_c('R')}/ {front_c('W')},-.{front_c('R')} -|-  {front_c('W')},-.{front_c('R')}`-{front_c('Y')}.{front_c('-')}'
        elif line == 3:
            part = f'{front_c('R')}`{front_c('W')}( {front_c('Y')}o{front_c('W')} ){front_c('R')}----{front_c('W')}( {front_c('Y')}o{front_c('W')} ){front_c('R')}-\'{front_c('-')}'
        else:
            part = f'{front_c('W')}  `-\'      `-\''
    
    # Return the part of the vehicle:
    return part
    
    # Reset colors:
    front_c('-', False)
    back_c('-', False)
    styles_c('-', False)
