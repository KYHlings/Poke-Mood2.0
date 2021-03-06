import sys
from random import choice

import pygame as pg

from Pygame.constants import WHITE, YELLOW_LIGHT,  YELLOW, RED
from pygame_upgraded import global_stuff
from pygame_upgraded.Textbased_Pygame.cards_helper import get_cities
from pygame_upgraded.global_stuff import periodic_movement
from pygame_upgraded.mood_score import calc_mood_score
from pygame_upgraded.music import music_lose_game_melody, music_intro, music_battle, music_win_game_melody
from pygame_upgraded.quiz import QuizStartScreen
from pygame_upgraded.quiz_api import quiz_categories
from pygame_upgraded.text_handler import text_speech, TextBox
from pygame_upgraded.poketer1 import gunnar, ada, attack_function, special_attack, cpu_random_attack, glada_gunnar, \
    aggressive_ada, sword, crossed_sword, winning_crown_hasse_moving, winning_crown_ada_moving, block_function, shield
from pygame_upgraded.variables import background, vs_sign1, background_win, logo, start_background, instructions_frame, \
    start_screen, QUIZ_TRANSP_GREEN, QUIZ_TRANSP_GREEN_HIGHL, QUIZ_TRANSP_GREEN_LIGHT, screen, BLACK
from pygame_upgraded.buttons import battle_time_button, quit_button, back_button, attack_button, special_attack_button, \
    quiz_button, start_game_button, instructions_button, quit_button_start, Button, choose_city_button, block_button
from pygame_upgraded.run import main


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
                main()

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
                main()

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

    def handle_mouse_button(self, button):
        city = choice(get_cities())
        city2 = choice(get_cities())
        mx, my = pg.mouse.get_pos()
        battle_button_rect = pg.Rect(285, 245, 225, 70)
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        choose_city_button_rect = pg.Rect(285, 400, 225, 70)
        if button == 1:
            if quit_button_rect.collidepoint((mx, my)):
                main()
            if choose_city_button_rect.collidepoint((mx, my)):
                city = MoodScreen()
                return city
            if battle_button_rect.collidepoint((mx, my)):
                if self.gunnar_mood_score == 0:
                    if self.popup_state == "not clicked":
                        self.gunnar_mood_score = calc_mood_score(gunnar.mood, city, live=False)
                        gunnar.add_health(self.gunnar_mood_score)
                        gunnar.add_max_health(self.gunnar_mood_score)
                        self.ada_mood_score = calc_mood_score(ada.mood, city2, live=False)
                        ada.add_health(self.ada_mood_score)
                        ada.add_max_health(self.ada_mood_score)
                        self.popup_state = "one click"
                show_city_score(city, city2)
                music_battle()
                return BattleScreen()
        return self

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.blit(background, (0, 0))

        # aggressive_ada(520, 300, 640, 300)
        # glada_gunnar(8, 30, 122, 45)
        choose_city_button()
        battle_time_button()
        quit_button()
        text_speech(screen, "RobotoSlab-Medium.ttf", 25, "Press battle to get a random mood score, or choose a city!",
                    BLACK, 400, 200,True)
        pg.display.update()


def show_city_score(city, city2):
    clock = pg.time.Clock()
    waiting = True
    time = 5
    while waiting:
        dt = clock.tick(1) / 1000
        time -= dt
        print(time)
        if time <= 0:
            waiting = False
        screen.blit(background, (0, 0))
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, f"Gunnar got {calc_mood_score(mood=gunnar.mood, city=city, live=False)} added to its health!", BLACK, 389, 150, True)
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, f"Gunnar got his moodscore from {city}", BLACK, 389, 180, True)
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, f"Ada got {calc_mood_score(mood=ada.mood, city=city2, live=False)} added to its health!", BLACK, 389, 300, True)
        text_speech(screen, "RobotoSlab-Medium.ttf", 30, f"Ada got her moodscore from {city2}", BLACK, 389, 330, True)
        pg.display.update()


class MoodScreen:
    def __init__(self):
        self.popup_state = "not clicked"
        self.city_buttons = []
        self.gunnar_mood_score = 0
        self.ada_mood_score = 0
        self.button_positions = [(0.3, 0.4),
                                 (0.7, 0.4),
                                 (0.3, 0.6),
                                 (0.7, 0.6),
                                 (0.3, 0.8),
                                 (0.7, 0.8)]
        self.cities = get_cities()
        for idx, city in enumerate(self.cities[:6]):
            self.city_button = Button(rel_pos=self.button_positions[idx], rel_size=(0.4, 0.2),
                                 color=QUIZ_TRANSP_GREEN, highlight=QUIZ_TRANSP_GREEN_HIGHL,
                                 font_size=22, font_color=WHITE, text=city)
            self.city_buttons.append(self.city_button)

    def handle_mouse_button(self, mouse_button):
        city2 = choice(get_cities())
        clicked_button_idx = None
        for city_button in self.city_buttons:
            if city_button.handle_mouse_button(mouse_button):
                clicked_button_idx = self.city_buttons.index(city_button)
                break

        if clicked_button_idx is not None:
            quiz_button.color = QUIZ_TRANSP_GREEN_LIGHT
            print(clicked_button_idx)
            city = self.cities[clicked_button_idx]
            if self.gunnar_mood_score == 0:
                if self.popup_state == "not clicked":
                    self.gunnar_mood_score = calc_mood_score(gunnar.mood, city, live=False)
                    gunnar.add_health(self.gunnar_mood_score)
                    gunnar.add_max_health(self.gunnar_mood_score)
                    self.ada_mood_score = calc_mood_score(ada.mood, city2, live=False)
                    ada.add_health(self.ada_mood_score)
                    ada.add_max_health(self.ada_mood_score)
                    self.popup_state = "one click"
            show_city_score(city, city2)
            music_battle()
            return BattleScreen()

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.blit(background, (0, 0))
        for city in self.city_buttons:
            city.render(screen)


class BattleScreen:
    def __init__(self):
        #self.music = music_battle() #CL
        self.is_block = None

    def handle_keydown(self, key):
        if key == pg.K_BACKSPACE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        attack_button_rect = pg.Rect(57, 430, 150, 50)
        block_button_rect = pg.Rect(222, 430, 150, 50)
        sp_attack_button_rect = pg.Rect(390, 430, 150, 50)
        quiz_button_rect = pg.Rect(563, 430, 150, 50)

        if button == 1:
            if quit_button_rect.collidepoint((mx, my)):
                main()
            if block_button_rect.collidepoint((mx, my)):
                return BlockScreen("user")
            if attack_button_rect.collidepoint((mx, my)):
                return AttackScreen("user",self.is_block)
            if sp_attack_button_rect.collidepoint((mx, my)):
                return SpecialAttackScreen("user",self.is_block)
            if quiz_button_rect.collidepoint((mx, my)):
                global_stuff.next_screen = QuizStartScreen(5, quiz_categories, self, gunnar)
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
        block_button()
        attack_button()
        special_attack_button()
        quiz_button()
        textbox_gunnar = TextBox((0.5, 0.2), "RobotoSlab-Medium.ttf", 30, False, WHITE, "It's your turn!")
        textbox_gunnar.render(screen)


class AttackScreen:
    def __init__(self, turn_,is_block):
        self.turn = turn_
        self.timeout = pg.time.get_ticks()
        self.is_block = is_block

        if self.turn == "user":
            attack_score = attack_function(gunnar, ada,is_block)
            self.text_gunnar = f"Gunnar attacked Ada! Ada took {attack_score} in damage!"
            self.text_ada = ""
        else:
            attack_score = attack_function(ada, gunnar,is_block)
            self.text_ada = f"Ada attacked Gunnar! You took {attack_score} in damage!"
            self.text_gunnar = ""

    def handle_keydown(self, key):
        if key == pg.K_ESCAPE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        #back_button_rect = pg.Rect(30, 540, 140, 40)

        if button == 1:
            # if back_button_rect.collidepoint((mx, my)):
            #     return BattleScreen()
            if quit_button_rect.collidepoint((mx, my)):
                main()
            return self

    def handle_timer(self):
        time_now = pg.time.get_ticks()
        if time_now - self.timeout > 2000 and self.timeout != 0:
            self.timeout = 0

            if ada.health <= 0:
                return WinnerScreenGunnar()
            if gunnar.health <= 0:
                return WinnerScreenAda()

            # when the users attack is finished - let cpu make a move
            if self.turn == "user":
                if cpu_random_attack():
                    return AttackScreen("cpu",self.is_block)
                else:
                    return SpecialAttackScreen("cpu",self.is_block)

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
        # back_button()

        # Rotate sword depending on whose turn it is
        sword(self.turn)


class BlockScreen:
    def __init__(self, turn_):
        self.turn = turn_
        self.timeout = pg.time.get_ticks()
        self.is_block = block_function()

        if self.turn == "user":
            #is_block = block_function(gunnar, ada)
            if self.is_block == True:
                self.text_gunnar = f"Gunnar blocked!"
            else:
                self.text_gunnar =f"Failed block!"
            self.text_ada = ""
        else:
            attack_score = special_attack(ada, gunnar,self.is_block)
            self.text_ada = f"Ada special attacked Gunnar! You took {attack_score} in damage!"
            self.text_gunnar = ""


    def handle_keydown(self, key):
        if key == pg.K_ESCAPE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)

        if button == 1:
            if quit_button_rect.collidepoint((mx, my)):
                main()
        return self

    def handle_timer(self):
        time_now = pg.time.get_ticks()
        if time_now - self.timeout > 2000 and self.timeout != 0:
            self.timeout = 0

            if ada.health <= 0:
                return WinnerScreenGunnar()
            if gunnar.health <= 0:
                return WinnerScreenAda()

            # when the users attack is finished - let cpu make a move
            if self.turn == "user":
                if cpu_random_attack():
                    return AttackScreen("cpu",self.is_block)
                else:
                    return SpecialAttackScreen("cpu",self.is_block)

            # when the cpu's attack is finished - return to Battlescreen
            if self.turn == "cpu":
                return BattleScreen()
        return self

    def render(self, screen):
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
        shield()

class SpecialAttackScreen:
    def __init__(self, turn_,is_block):
        self.turn = turn_
        self.timeout = pg.time.get_ticks()
        self.is_block = is_block

        if self.turn == "user":
            attack_score = special_attack(gunnar, ada,is_block)
            self.text_gunnar = f"Gunnar special attacked Ada! Ada took {attack_score} in damage!"
            self.text_ada = ""
        else:

            attack_score = special_attack(ada, gunnar,is_block)
            self.text_ada = f"Ada special attacked Gunnar! You took {attack_score} in damage!"
            self.text_gunnar = ""

    def handle_keydown(self, key):
        if key == pg.K_ESCAPE:
            return start_screen
        return self

    def handle_mouse_button(self, button):
        mx, my = pg.mouse.get_pos()
        quit_button_rect = pg.Rect(650, 30, 140, 40)

        if button == 1:
            if quit_button_rect.collidepoint((mx, my)):
                main()
        return self

    def handle_timer(self):
        time_now = pg.time.get_ticks()
        if time_now - self.timeout > 2000 and self.timeout != 0:
            self.timeout = 0

            if ada.health <= 0:
                return WinnerScreenGunnar()
            if gunnar.health <= 0:
                return WinnerScreenAda()

            # when the users attack is finished - let cpu make a move
            if self.turn == "user":
                if cpu_random_attack():
                    return AttackScreen("cpu",self.is_block)
                else:
                    return SpecialAttackScreen("cpu",self.is_block)

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
        # back_button()
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
                main()
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