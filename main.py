# Import the necessary modules

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *
from sounds import *

# Config:
import config as c

# Program:
import section_1 as s1
import section_2 as s2
import section_3 as s3
import section_4 as s4
import section_5 as s5
import section_6 as s6
import section_7 as s7
import section_8 as s8
import section_9 as s9
import section_10 as s10
import section_11 as s11
import section_12 as s12
import section_13 as s13
c.SECTION = 12
# Start the program:
while c.LOOP:
    # Presentation:
    if c.SECTION == 0:
        s1.section_1()

    # Main menu:
    if c.SECTION == 1:
        s2.section_2()

    # Selection of car (1 Player):
    if c.SECTION == 2:
        s3.section_3()

    # Selection of car (2 Player):
    if c.SECTION == 3:
        s4.section_4()

    # Options:
    if c.SECTION == 4:
        s5.section_5()

    # Exit of the game:
    if c.SECTION == 5:
        s6.section_6()

    # Last page:
    if c.SECTION == 6:
        s7.section_7()

    # Edit edge X:
    if c.SECTION == 7:
        s8.section_8()

    # Edit edge Y:
    if c.SECTION == 8:
        s9.section_9()

    # Edit volume (Music):
    if c.SECTION == 9:
        s10.section_10()

    # Edit volume (SFX):
    if c.SECTION == 10:
        s11.section_11()
    
    # Exit:
    if c.SECTION == 11:
        s12.section_12()
    
    # Selection of car (CPU):
    if c.SECTION == 12:
        s13.section_13()
