# CMD screen control functions

from os import system
from time import sleep

# Clear the screen:
def clear():
    system('cls')

# Pause the program:
def pause():
    system('pause')

# Pause the program for X time:
def wait(my_time):
    sleep(my_time)
