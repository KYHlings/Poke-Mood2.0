import pygame


def music(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)