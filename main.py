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

# Start the program:
while c.LOOP:
    # Presentation:
    if c.SECTION == 0:
        s1.section_1()

    # Main menu:
    if c.SECTION == 1:
        s2.section_2()