import textwrap

import pygame
import pygame as pg

from Pygame.constants import BLACK
from pygame_upgraded.variables import screen, screen_size, BLACK


def text_speech(screen, font: str, size: int, text: str, color, x, y, bold: bool):
    font = pg.font.Font(font, size)
    font.set_bold(bold)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def left_chat_bubble(mood_score):
    left_bubble = pg.image.load("images/Chat_bubble_left.png")
    left_bubble = pg.transform.scale(left_bubble, (300, 170))
    screen.blit(left_bubble, (250, 50))
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, f"Moodscore: {mood_score}", BLACK, 390, 135, True)


def right_chat_bubble(mood_score):
    right_bubble = pg.image.load("images/Chat_bubble_right.png")
    right_bubble = pg.transform.scale(right_bubble, (300, 170))
    screen.blit(right_bubble, (260, 350))
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, f"Moodscore: {mood_score}", BLACK, 370, 435, True)


def pop_up_bubbles(state, gunnar_mood_score, ada_mood_score):
    if state == "one click":
        left_chat_bubble(gunnar_mood_score)
        right_chat_bubble(ada_mood_score)

    # if state == "two clicks":
    #     left_chat_bubble(gunnar_mood_score)
    #


class TextBox:
    def __init__(self, rel_pos, font_name, font_size, font_bold, color, text, line_width=100):
        self.position = (screen_size[0] * rel_pos[0], screen_size[1] * rel_pos[1])
        self.font_size = font_size
        self.font = pygame.font.Font(font_name, font_size)
        self.font.set_bold(font_bold)
        self.color = color
        self.text_lines = []
        self.text_lines_shadow = []
        self.line_width = line_width
        self.set_text(text)

    def set_text(self, text):
        lines_specified_width = textwrap.fill(text, self.line_width)
        chopped_lines = lines_specified_width.split('\n')
        self.text_lines = []
        self.text_lines_shadow = []
        for line in chopped_lines:
            line_surface = self.font.render(line, True, self.color)
            self.text_lines.append(line_surface)
            line_surface_shadow = self.font.render(line, True, BLACK)
            self.text_lines_shadow.append(line_surface_shadow)

    def render(self, screen):
        # shadow
        for idx, text_surface_shadow in enumerate(self.text_lines_shadow):
            text_rect_shadow = text_surface_shadow.get_rect()
            text_rect_shadow.center = self.position[0] + 1, self.position[1] + 2 + idx * (self.font_size + 15)
            screen.blit(text_surface_shadow, text_rect_shadow)

        for idx, text_surface in enumerate(self.text_lines):
            text_rect = text_surface.get_rect()
            text_rect.center = self.position[0], self.position[1] + idx * (self.font_size + 15)
            screen.blit(text_surface, text_rect)