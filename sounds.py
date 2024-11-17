# Import the necessary modules:

import pygame
import sys

# Config:
import config as c

# Variables:
screen_scale = 200

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

# SFX:
# sfx = pygame.mixer.Sound("resources/sfx.wav")
# sfx.set_volume(c.VOLUME_SFX)

# # Volumen:
# pygame.mixer.music.set_volume(c.VOLUME_MUSIC)

# # Volumen (SFX):
# sfx.set_volume(c.VOLUME_SFX)

# Inicializa Pygame:
pygame.init()

# Window size:
window_size = (screen_scale, screen_scale)
screen = pygame.display.set_mode(window_size)

# Caption:
pygame.display.set_caption("Music and SFX")

# Music:
def start_play_music():
    # Music:
    pygame.mixer.music.load("resources/title_screen.mp3")
    pygame.mixer.music.set_volume(c.VOLUME_MUSIC)

    # Play:
    pygame.mixer.music.play(-1)

    # Background color:
    screen.fill((255, 255, 255))

    # Show the image:
    screen.blit(image_sound_1, image_position)
    
    # Update the screen:
    pygame.display.flip()

# Close the window:
def exit_window():
    pygame.quit()
    sys.exit()
