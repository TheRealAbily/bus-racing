# Import the necessary modules:

import pygame
import sys
from random import randint

# Config:
import config as c

# Inicializa Pygame:
pygame.init()

# Variables:
screen_scale = 300

# Images:
image_sound_1 = pygame.image.load('resources/images/sound_1.png')
image_sound_2 = pygame.image.load('resources/images/sound_2.png')

# Scale:
image_sound_1 = pygame.transform.scale(image_sound_1, ((screen_scale/5) * 4, (screen_scale/5) * 4))
image_sound_2 = pygame.transform.scale(image_sound_2, ((screen_scale/5) * 4, (screen_scale/5) * 4))

# Get the scale:
edge_x, edge_y = image_sound_1.get_size()

# Position:
image_position = (screen_scale/2 - (edge_x/2), screen_scale/2 - (edge_y/2))

# Window size:
window_size = (screen_scale, screen_scale)
screen = pygame.display.set_mode(window_size)

# Caption:
pygame.display.set_caption("Music and SFX")

# Icon:
icon = pygame.image.load("resources/images/icon.png")

# Show the icon:
pygame.display.set_icon(icon)

# Background color:
screen.fill((255, 255, 255))

# Show the image:
screen.blit(image_sound_1, image_position)

# Update the screen:
pygame.display.flip()

# Music:
def play_music(music):
    # Stop the music:
    pygame.mixer.music.stop()

    # Music:
    if music == 'Main menu':
        pygame.mixer.music.load("resources/sounds/title_screen.mp3")
    elif music == 'Track':
        if c.TRACK == 1:
            # 8
            pygame.mixer.music.load("resources/sounds/track_1.mp3")

        elif c.TRACK == 2:
            # Delfino
            pygame.mixer.music.load("resources/sounds/track_2.mp3")

        elif c.TRACK == 3:
            # Pinball
            pygame.mixer.music.load("resources/sounds/track_3.mp3")

        else:
            # Rainbow road
            pygame.mixer.music.load("resources/sounds/track_4.mp3")
        
    # Volume:
    pygame.mixer.music.set_volume(c.VOLUME_MUSIC)

    # Play:
    pygame.mixer.music.play(-1)

# Stop:
def stop_music():
    # Stop the music:
    pygame.mixer.music.stop()

# Close the window:
def exit_window():
    pygame.quit()
    sys.exit()

# SFX:
def play_sfx(sfx):
    # SFX:
    if sfx == 'Back':
        effect = pygame.mixer.Sound("resources/sounds/back.wav")
    elif sfx == 'Countdown':
        effect = pygame.mixer.Sound("resources/sounds/countdown.wav")
    elif sfx == 'Go':
        effect = pygame.mixer.Sound("resources/sounds/go.wav")
    elif sfx == 'Edit':
        effect = pygame.mixer.Sound("resources/sounds/edit.wav")
    elif sfx == 'Error':
        effect = pygame.mixer.Sound("resources/sounds/error.wav")
    elif sfx == 'Random':
        effect = pygame.mixer.Sound("resources/sounds/random.wav")
    elif sfx == 'Selected':
        effect = pygame.mixer.Sound("resources/sounds/selected.wav")
    elif sfx == 'Car passing':
        effect = pygame.mixer.Sound("resources/sounds/car_passing.wav")
    elif sfx == 'Show race track':
        selection = randint(1, 2)

        if selection == 1:
            effect = pygame.mixer.Sound("resources/sounds/show_race_track_1.wav")
        else:
            effect = pygame.mixer.Sound("resources/sounds/show_race_track_2.wav")
    elif sfx == 'Pre start':
        selection = randint(1, 2)

        if selection == 1:
            effect = pygame.mixer.Sound("resources/sounds/pre_start_1.wav")
        else:
            effect = pygame.mixer.Sound("resources/sounds/pre_start_2.wav")
    
    # Volume:
    effect.set_volume(c.VOLUME_SFX)

    # Play:
    effect.play()

# Change volume (Music):
def volume():
    pygame.mixer.music.set_volume(c.VOLUME_MUSIC)

    # Change the image:
    if c.VOLUME_MUSIC > 0:
        screen.blit(image_sound_1, image_position)
    else:
        screen.blit(image_sound_2, image_position)

    # Update the screen:
    pygame.display.flip()
