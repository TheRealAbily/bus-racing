# Import the necessary modules

# Carpentry:
from colors import *
from line import *
from move import *
from screen import *
from text import *

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
