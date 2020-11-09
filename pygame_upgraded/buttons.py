import pygame
import pygame as pg

from Pygame.constants import BLACK, COLOR_LIGHT_SELECTED, COLOR_LIGHT_UNSELECTED, LIGHT_RED_SELECTED, \
    LIGHT_RED_UNSELECTED, LIGHT_BLUE_SELECTED, LIGHT_BLUE_UNSELECTED, LIGHT_GREEN_SELECTED, LIGHT_GREEN_UNSELECTED
from pygame_upgraded.music import sound_ambient_hover_over_attack_btn, sound_ambient_hover_over_special_attack_btn, \
    sound_ambient_hover_quizz_btn
from pygame_upgraded.text_handler import text_speech, TextBox
from pygame_upgraded.variables import width, height, screen, screen_size, FONT_ROBOTO, QUIZ_DARKGREEN


def battle_time_button():
    mouse = pg.mouse.get_pos()
    if 275 <= mouse[0] <= 275 + 240 and 245 <= mouse[1] <= 225 + 100:
        pg.draw.rect(screen, BLACK, (285, 245, 225, 70), 3)
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, (287, 247, 221, 66))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Battle time!", BLACK, width / 2.02,
                    height / 2.15, True)
    else:
        pg.draw.rect(screen, BLACK, (285, 245, 225, 70), 3)
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, (287, 247, 221, 66))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Battle time!", BLACK, width / 2.02,
                    height / 2.15, True)


def quit_button():
    mouse = pg.mouse.get_pos()
    if 650 <= mouse[0] <= 650 + 140 and 30 <= mouse[1] <= 30 + 40:
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, [652, 32, 137, 37])
        pg.draw.rect(screen, BLACK, [650, 30, 140, 40], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "QUIT", BLACK, 715, 48, True)
    else:
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, [650, 30, 140, 40])
        pg.draw.rect(screen, BLACK, [650, 30, 140, 40], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "QUIT", BLACK, 715, 48, True)


def back_button():
    mouse = pg.mouse.get_pos()
    if 30 <= mouse[0] <= 30 + 140 and 540 <= mouse[1] <= 540 + 40:
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, [32, 542, 137, 37])
        pg.draw.rect(screen, BLACK, [30, 540, 140, 40], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "BACK", BLACK, 97, 558, True)
    else:
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, [32, 542, 137, 37])
        pg.draw.rect(screen, BLACK, [30, 540, 140, 40], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "BACK", BLACK, 97, 558, True)


def attack_button():
    mouse = pg.mouse.get_pos()
    if 87 <= mouse[0] <= 87 + 150 and 430 <= mouse[1] <= 430 + 50:
        pg.draw.rect(screen, LIGHT_RED_SELECTED, [89, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [87, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Attack", BLACK, 162, 453, True)
        sound_ambient_hover_over_attack_btn()
    else:
        pg.draw.rect(screen, LIGHT_RED_UNSELECTED, [89, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [87, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Attack", BLACK, 162, 453, True)


def special_attack_button():
    mouse = pg.mouse.get_pos()
    if 325 <= mouse[0] <= 325 + 150 and 430 <= mouse[1] <= 430 + 50:
        pg.draw.rect(screen, LIGHT_BLUE_SELECTED, [327, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [325, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Special", BLACK, 400, 453, True)
        sound_ambient_hover_over_special_attack_btn()
    else:
        pg.draw.rect(screen, LIGHT_BLUE_UNSELECTED, [327, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [325, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Special", BLACK, 400, 453, True)


def quiz_button():
    mouse = pg.mouse.get_pos()
    if 563 <= mouse[0] <= 563 + 150 and 430 <= mouse[1] <= 430 + 50:
        pg.draw.rect(screen, LIGHT_GREEN_SELECTED, [565, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [563, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Quiz", BLACK, 638, 453, True)
        sound_ambient_hover_quizz_btn()
    else:
        pg.draw.rect(screen, LIGHT_GREEN_UNSELECTED, [565, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [563, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Quiz", BLACK, 638, 453, True)


def start_game_button():
    mouse = pg.mouse.get_pos()
    if 275 <= mouse[0] <= 275 + 225 and 280 <= mouse[1] <= 280 + 65:
        pg.draw.rect(screen, BLACK, (275, 280, 240, 65), 3)
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, (277, 282, 236, 61))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Start Game", BLACK, width / 2.025,
                    height / 1.93, True)
    else:
        pg.draw.rect(screen, BLACK, (275, 280, 240, 65), 3)
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, (277, 282, 236, 61))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Start Game", BLACK, width / 2.025,
                    height / 1.93, True)


def instructions_button():
    mouse = pg.mouse.get_pos()
    if 275 <= mouse[0] <= 275 + 240 and 360 <= mouse[1] <= 360 + 65:
        pg.draw.rect(screen, BLACK, (275, 360, 240, 65), 3)
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, (277, 362, 236, 61))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "How To Play", BLACK, width / 2.025,
                    height / 1.54, True)
    else:
        pg.draw.rect(screen, BLACK, (275, 360, 240, 65), 3)
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, (277, 362, 236, 61))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "How To Play", BLACK, width / 2.025,
                    height / 1.54, True)


def quit_button_start():
    mouse = pg.mouse.get_pos()
    if 275 <= mouse[0] <= 275 + 225 and 440 <= mouse[1] <= 440 + 65:
        pg.draw.rect(screen, BLACK, (275, 440, 240, 65), 3)
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, (277, 442, 236, 61))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Quit Game", BLACK, width / 2.025,
                    height / 1.27, True)
    else:
        pg.draw.rect(screen, BLACK, (275, 440, 240, 65), 3)
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, (277, 442, 236, 61))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Quit Game", BLACK, width / 2.025,
                    height / 1.27, True)


class Button:
    def __init__(self, rel_pos, rel_size, color, highlight, font_size, font_color, text):
        self.position = (int(screen_size[0] * rel_pos[0]) ,int( screen_size[1] * rel_pos[1]))
        self.size = (screen_size[0] * rel_size[0], screen_size[1] * rel_size[1])
        self.color = color
        self.highlight = highlight
        self.text = TextBox(rel_pos=rel_pos, font_name=FONT_ROBOTO,
                            font_size=font_size, font_bold=False, color=font_color, text=text, line_width=28)
        self.button_rect = pygame.Rect(self.position[0], self.position[1], self.size[0] - 3, self.size[1] - 3)
        self.button_rect.center = self.position[0], self.position[1]
        self.button_frame_rect = pygame.Rect(0, 0, self.size[0], self.size[1])  # x, y, width, height
        self.button_frame_rect.center = self.position[0], self.position[1]
        self.enabled = True

    def handle_keydown(self, key):
        pass

    def handle_mouse_button(self, mouse_button):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos) and mouse_button == 1 and self.enabled:
            return True
        else:
            return False

    def render(self, screen):
        pygame.draw.rect(screen, QUIZ_DARKGREEN, self.button_frame_rect, 4)  # button frame

        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos) and self.enabled:  # If mouse on button - highlight button
            if len(self.highlight) == 4:
                s = pygame.Surface((self.button_rect.width, self.button_rect.height),
                                   pygame.SRCALPHA)  # per-pixel alpha
                s.fill(self.highlight)  # notice the alpha value in the color
                screen.blit(s, self.button_rect)
            else:
                pygame.draw.rect(screen, self.highlight, self.button_rect)
        else:
            if len(self.color) == 4:
                s = pygame.Surface((self.button_rect.width, self.button_rect.height),
                                   pygame.SRCALPHA)  # per-pixel alpha
                s.fill(self.color)  # notice the alpha value in the color
                screen.blit(s, self.button_rect)
            else:
                pygame.draw.rect(screen, self.color, self.button_rect)

        self.text.render(screen)