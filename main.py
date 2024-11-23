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
import presentation as s1
import main_menu as s2
import select_player_1 as s3
import select_player_2 as s4
import options_menu as s5
import exit_menu as s6
import information as s7
import edit_edge_x as s8
import edit_edge_y as s9
import edit_volume_music as s10
import edit_volume_sfx as s11
import exit_game as s12
import select_cpu as s13
import loading as s14
import race as s15
import lights as s16
import save_load as s17
c.SECTION = 16
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

    # Exit of the game (menu):
    if c.SECTION == 5:
        s6.section_6()

    # Information:
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
    
    # Exit of the game (exit):
    if c.SECTION == 11:
        s12.section_12()
    
    # Selection of car (CPU):
    if c.SECTION == 12:
        s13.section_13()

    # Loading:
    if c.SECTION == 13:
        s14.section_14()

    # Race:
    if c.SECTION == 14:
        s15.section_15(True)

    # Lights:
    if c.SECTION == 15:
        s16.section_16()

    # Race:
    if c.SECTION == 16:
        s15.section_15(False)
    
    # Save the data:
    s17.save_data()
