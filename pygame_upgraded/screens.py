import sys

import pygame as pg

from Pygame.constants import WHITE, YELLOW_LIGHT, BLACK, YELLOW, RED
from pygame_upgraded import common
from pygame_upgraded.common import periodic_movement, TextBox
from pygame_upgraded.mood_score import calc_mood_score
from pygame_upgraded.music import music_lose_game_melody, music_intro, music_battle, music_win_game_melody
from pygame_upgraded.quiz import QuizStartScreen
from pygame_upgraded.quiz_api import quiz_categories
from pygame_upgraded.text_handler import text_speech, pop_up_bubbles
from pygame_upgraded.poketer1 import gunnar, ada, attack_function, special_attack, cpu_random_attack, glada_gunnar, \
    aggressive_ada, sword, crossed_sword, winning_crown_hasse_moving, winning_crown_ada_moving
from pygame_upgraded.variables import background, vs_sign1, background_win, logo, start_background, instructions_frame, \
    start_screen
from pygame_upgraded.buttons import battle_time_button, quit_button, back_button, attack_button, special_attack_button, \
    quiz_button, start_game_button, instructions_button, quit_button_start


class WinnerScreenAda:
    def __init__(self):
        music_lose_game_melody()

    def handle_keydown(self, key):
        if key == pg.K_ESCAPE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        if button == 1:
            if quit_button_rect.collidepoint((mx, my)):
                sys.exit()
        return self

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(background_win, (0, 0))
        ada_win_pic = pg.image.load("images/Pink_dragon_08.png")
        ada_win_pic = pg.transform.scale(ada_win_pic, (350, 350))
        screen.blit(ada_win_pic, (205, 285))
        winning_crown_ada_moving()
        gunnar_lose = pg.transform.scale(gunnar.image, (200, 200))
        screen.blit(gunnar_lose, (25, 355))
        tear_drop = pg.image.load("images/tear-png-20.png")
        tear_drop = pg.transform.scale(tear_drop, (25, 25))
        screen.blit(tear_drop, (90, 430))
        screen.blit(logo, (215, -55))
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, "Better luck next time,", YELLOW_LIGHT, 386, 150, True)
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, f"{ada.name} won!", YELLOW_LIGHT, 385, 200, True)
        quit_button()


class MenuStartScreen:
    def __init__(self):
        music_intro()

    def handle_keydown(self, key):
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        start_game_button_rect = pg.Rect(275, 280, 240, 65)
        instructions_button_rect = pg.Rect(275, 360, 240, 65)
        quit_game_button_rect = pg.Rect(275, 440, 240, 65)
        if button == 1:
            if start_game_button_rect.collidepoint((mx, my)):
                return StartScreen()
            if instructions_button_rect.collidepoint((mx, my)):
                return InstructionsScreen()
            if quit_game_button_rect.collidepoint((mx, my)):
                sys.exit()

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(start_background, (0, 0))
        screen.blit(logo, (215, -55))
        start_game_button()
        instructions_button()
        quit_button_start()


class InstructionsScreen:
    def handle_keydown(self, key):
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        back_button_rect = pg.Rect(30, 540, 140, 40)
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        if button == 1:
            if back_button_rect.collidepoint((mx, my)):
                return MenuStartScreen()
            if quit_button_rect.collidepoint((mx, my)):
                sys.exit()

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(start_background, (0, 0))
        screen.blit(instructions_frame, (75, 75))
        back_button()
        quit_button()


class StartScreen:
    def __init__(self):
        self.popup_state = "not clicked"
        self.gunnar_mood_score = 0
        self.ada_mood_score = 0
        #self.music = music_intro()

    def handle_keydown(self, key):
        if key == pg.K_RETURN:
            if self.popup_state == "not clicked":
                self.gunnar_mood_score = calc_mood_score(gunnar.mood, "Göteborg", live=False)
                gunnar.add_health(self.gunnar_mood_score)
                self.popup_state = "one click"
            elif self.popup_state == "one click":
                self.ada_mood_score = calc_mood_score(ada.mood, "Västerås", live=False)
                ada.add_health(self.ada_mood_score)
                self.popup_state = "two clicks"
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        battle_button_rect = pg.Rect(285, 245, 225, 70)
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        if button == 1:
            if battle_button_rect.collidepoint((mx, my)):
                music_battle()
                return BattleScreen()
            if quit_button_rect.collidepoint((mx, my)):
                sys.exit()
        return self

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        aggressive_ada(520, 300, 640, 300)
        glada_gunnar(8, 30, 122, 45)

        pop_up_bubbles(self.popup_state, self.gunnar_mood_score, self.ada_mood_score)

        battle_time_button()
        quit_button()
        text_speech(screen, "RobotoSlab-Medium.ttf", 15, "Press [enter] for moodscores", BLACK, 397, 330, True)


class BattleScreen:
    def __init__(self):
        #self.music = music_battle() #CL
        pass

    def handle_keydown(self, key):
        if key == pg.K_BACKSPACE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        back_button_rect = pg.Rect(30, 540, 140, 40)
        attack_button_rect = pg.Rect(87, 430, 150, 50)
        block_button_rect = pg.Rect(325, 430, 150, 50)
        quiz_button_rect = pg.Rect(563, 430, 150, 50)
        if button == 1:
            if quit_button_rect.collidepoint((mx, my)):
                sys.exit()
            if back_button_rect.collidepoint((mx, my)):
                return StartScreen()
            if attack_button_rect.collidepoint((mx, my)):
                return AttackScreen("user")
            if block_button_rect.collidepoint((mx, my)):
                return SpecialAttackScreen("user")
            if quiz_button_rect.collidepoint((mx, my)):
                common.next_screen = QuizStartScreen(5, quiz_categories, self, gunnar)
        return self

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        x_off, y_off = periodic_movement(1, 5)
        aggressive_ada(504, 156, 650, 550)
        glada_gunnar(24, 144 + y_off, 122, 45)

        screen.blit(vs_sign1, (300, 225))
        quit_button()
        back_button()
        attack_button()
        special_attack_button()
        quiz_button()
        textbox_gunnar = TextBox((0.5, 0.2), "RobotoSlab-Medium.ttf", 30, False, WHITE, "It's your turn!")
        textbox_gunnar.render(screen)


class AttackScreen:
    def __init__(self, turn_):
        self.turn = turn_
        self.timeout = pg.time.get_ticks()

        if self.turn == "user":
            attack_score = attack_function(gunnar, ada)
            self.text_gunnar = f"Gunnar attacked Ada! Ada took {attack_score} in damage!"
            self.text_ada = ""
        else:
            attack_score = attack_function(ada, gunnar)
            self.text_ada = f"Ada attacked Gunnar! You took {attack_score} in damage!"
            self.text_gunnar = ""

    def handle_keydown(self, key):
        if key == pg.K_ESCAPE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        back_button_rect = pg.Rect(30, 540, 140, 40)

        if button == 1:
            if back_button_rect.collidepoint((mx, my)):
                return BattleScreen()
            if quit_button_rect.collidepoint((mx, my)):
                sys.exit()
            return self

    def handle_timer(self):
        time_now = pg.time.get_ticks()
        if time_now - self.timeout > 5000 and self.timeout != 0:
            self.timeout = 0

            if ada.health <= 0:
                return WinnerScreenGunnar()
            if gunnar.health <= 0:
                return WinnerScreenAda()

            # when the users attack is finished - let cpu make a move
            if self.turn == "user":
                if cpu_random_attack():
                    return AttackScreen("cpu")
                else:
                    return SpecialAttackScreen("cpu")

            # when the cpu's attack is finished - return to Battlescreen
            if self.turn == "cpu":
                return BattleScreen()

        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        textbox_gunnar = TextBox((0.5, 0.2), "RobotoSlab-Medium.ttf", 25, False, YELLOW, self.text_gunnar)
        textbox_gunnar.render(screen)

        textbox_ada = TextBox((0.5, 0.2), "RobotoSlab-Medium.ttf", 25, False, RED, self.text_ada)
        textbox_ada.render(screen)

        x_off, y_off = periodic_movement(1, 5)
        if self.turn == "user":
            glada_gunnar(24, 144 + y_off, 122, 45)
            aggressive_ada(504, 156, 650, 550)
        else:
            glada_gunnar(24, 144, 122, 45)
            aggressive_ada(504, 156 + y_off, 650, 550)

        quit_button()
        back_button()

        # Rotate sword depending on whose turn it is
        sword(self.turn)


class SpecialAttackScreen:
    def __init__(self, turn_):
        self.turn = turn_
        self.timeout = pg.time.get_ticks()

        if self.turn == "user":
            attack_score = special_attack(gunnar, ada)
            self.text_gunnar = f"Gunnar special attacked Ada! Ada took {attack_score} in damage!"
            self.text_ada = ""
        else:
            attack_score = special_attack(ada, gunnar)
            self.text_ada = f"Ada special attacked Gunnar! You took {attack_score} in damage!"
            self.text_gunnar = ""

    def handle_keydown(self, key):
        if key == pg.K_ESCAPE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        back_button_rect = pg.Rect(30, 540, 140, 40)

        if button == 1:
            if back_button_rect.collidepoint((mx, my)):
                return BattleScreen()
            if quit_button_rect.collidepoint((mx, my)):
                sys.exit()
        return self

    def handle_timer(self):
        time_now = pg.time.get_ticks()
        if time_now - self.timeout > 5000 and self.timeout != 0:
            self.timeout = 0

            if ada.health <= 0:
                return WinnerScreenGunnar()
            if gunnar.health <= 0:
                return WinnerScreenAda()

            # when the users attack is finished - let cpu make a move
            if self.turn == "user":
                if cpu_random_attack():
                    return AttackScreen("cpu")
                else:
                    return SpecialAttackScreen("cpu")

            # when the cpu's attack is finished - return to Battlescreen
            if self.turn == "cpu":
                return BattleScreen()
        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        textbox_gunnar = TextBox((0.5, 0.2), "RobotoSlab-Medium.ttf", 25, False, YELLOW, self.text_gunnar)
        textbox_gunnar.render(screen)

        textbox_ada = TextBox((0.5, 0.2), "RobotoSlab-Medium.ttf", 25, False, RED, self.text_ada)
        textbox_ada.render(screen)

        x_off, y_off = periodic_movement(1, 5)
        if self.turn == "user":
            glada_gunnar(24, 144 + y_off, 122, 45)
            aggressive_ada(504, 156, 650, 550)
        else:
            glada_gunnar(24, 144, 122, 45)
            aggressive_ada(504, 156 + y_off, 650, 550)

        quit_button()
        back_button()
        crossed_sword()


class WinnerScreenGunnar:
    def __init__(self):
        music_win_game_melody()

    def handle_keydown(self, key):
        if key == pg.K_ESCAPE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        if button == 1:
            if quit_button_rect.collidepoint((mx, my)):
                sys.exit()
        return self

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(WHITE)
        screen.blit(background_win, (0, 0))
        x_off, y_off = periodic_movement(1, 5) #CL
        gunnar_bigger = pg.transform.scale(gunnar.image, (350, 350))
        screen.blit(gunnar_bigger, (220, 235 + y_off))
        winning_crown_hasse_moving()
        pink_dragon_sad = pg.image.load("images/Pink_dragon_05.png")
        pink_dragon_sad = pg.transform.scale(pink_dragon_sad, (204, 235))
        screen.blit(pink_dragon_sad, (25, 340))
        screen.blit(logo, (213, -55))
        tear_drop = pg.image.load("images/tear-png-20.png")
        tear_drop = pg.transform.scale(tear_drop, (25, 25))
        screen.blit(tear_drop, (120, 410))
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, "Congratulations,", YELLOW_LIGHT, 389, 150, True)
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, f"{gunnar.name} won!", YELLOW_LIGHT, 388, 200, True)
        quit_button()