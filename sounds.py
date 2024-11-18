# Import the necessary modules:

import pygame
import sys

# Config:
import config as c

# Inicializa Pygame:
pygame.init()

# Variables:
screen_scale = 300

# Images:
image_sound_1 = pygame.image.load('resources/sound_1.png')
image_sound_2 = pygame.image.load('resources/sound_2.png')

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
icon = pygame.image.load("resources/icon.png")

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
        pygame.mixer.music.load("resources/title_screen.mp3")

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
        effect = pygame.mixer.Sound("resources/back.wav")
    elif sfx == 'Countdown':
        effect = pygame.mixer.Sound("resources/countdown.wav")
    elif sfx == 'Go':
        effect = pygame.mixer.Sound("resources/go.wav")
    elif sfx == 'Edit':
        effect = pygame.mixer.Sound("resources/edit.wav")

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
