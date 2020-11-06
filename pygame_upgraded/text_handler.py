import pygame as pg

from Pygame.constants import BLACK
from pygame_upgraded.variables import screen


def main():
    pass


if __name__ == '__main__':
    main()


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