import math
import pygame

from pygame_upgraded.variables import *

# https://stackoverflow.com/questions/13034496/using-global-variables-between-files
# Deklarer global variabel mellan filer.

def common_init():
    global next_screen
    next_screen = None


def periodic_movement(frequency, amplitude):
    time = pygame.time.get_ticks()
    x_off = amplitude * math.cos(frequency * time * math.pi / 1000)
    y_off = amplitude * math.sin(frequency * time * math.pi / 1000)
    return x_off, y_off


def rel_to_pix(rel_pos):
    x = rel_pos[0] * screen_size[0]
    y = rel_pos[1] * screen_size[1]
    pix_pos = (x, y)
    return pix_pos


