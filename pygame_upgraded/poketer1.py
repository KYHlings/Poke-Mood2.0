import time
from random import randint
from termcolor import colored
#from prints_module import atk_txt, delay_print, successful_block, unsuccessful_block
from pygame_upgraded.Textbased_Pygame.print_module import atk_txt
from pygame_upgraded.global_stuff import periodic_movement


class Poketer1:
    def __init__(self, name, mood, color, health, max_health, attack, catchword):
        self.name = name
        self.mood = mood
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.color = color
        self.catchword = catchword

    def attack_fnc(self, opponent_pokemon):
        miss_chance = randint(1, 6)
        if miss_chance <= 5:
            opponent_pokemon.health -= self.attack
            atk_txt(self.name, opponent_pokemon.name, "3 2 1...")
            self.healtcheck_color(opponent_pokemon)
            # self.healthcheck(opponent_pokemon, opponent.name)
            # self.healthcheck(opponent_pokemon, opponent.name)
        else:
            print("Attacken missade...")

        # opponent_pokemon.health -= self.attack
        # atk_txt(self.name, opponent_pokemon.name, "3 2 1...")
        # self.healtcheck_color(opponent_pokemon)

    def healtcheck_color(self, opponent_pokemon):

        if opponent_pokemon.health >= opponent_pokemon.max_health / 2:
            print(f"{opponent_pokemon.name} hälsa: {colored(opponent_pokemon.health, 'green')}\n")
        elif opponent_pokemon.max_health / 4 <= opponent_pokemon.health <= opponent_pokemon.max_health / 2:
            print(f"{opponent_pokemon.name} hälsa: {colored(opponent_pokemon.health, 'yellow')}\n")
        elif opponent_pokemon.health <= opponent_pokemon.max_health / 4:
            print(f"{opponent_pokemon.name} hälsa: {colored(opponent_pokemon.health, 'red')}\n")

    def healthcheck(self, opponent_pokemon, opponent_name):
        if self.health <= 0 or opponent_pokemon.health <= 0:
            if opponent_pokemon.health <= 0:
                print(f'*** {opponent_name} Poketer {opponent_pokemon.name} svimmade. Du vann! ***')
            if self.health <= 0:
                print(f'*** Din poketer {self.name} svimmade. {opponent_name} vann! ***')
            alive = False
            return alive

    def block(self, opponent_pokemon):
        misschans = randint(1, 6)
        critchance = randint(1, 6)
        dmg_modifier = randint(-3, 3)
        if misschans <= 5:
            if critchance >= 4:
                opponent_pokemon.health -= (self.attack + dmg_modifier) * 2
                atk_txt(self.name, opponent_pokemon.name, "3 2 1...")
                self.healthcheck(opponent_pokemon,opponent_name)
            elif critchance < 4:
                opponent_pokemon.health -= (self.attack + dmg_modifier)
                atk_txt(self.name, opponent_pokemon.name, "3 2 1...")
                self.healthcheck(opponent_pokemon)
        else:
            print(f"{opponent_pokemon.name} missade sin attack...")

    def add_attack(self, attack_score):
        self.attack += attack_score

    def add_health(self, health_score):
        self.health += health_score

    def add_max_health(self, max_health_score):
        self.max_health += max_health_score

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_stats(self):
        return f"{self.name} har {self.health} i hälsa och {self.attack} i attack."

    def set_attack(self, attack_score):
        self.attack = attack_score

    def __repr__(self):
        return f'Poketer: {self.name}. Mood: {self.mood}. Health: {self.health}. Max health: {self.max_health}. Attack: {self.attack}.'

from random import randint

import pygame as pg

from Pygame.constants import WHITE
from pygame_upgraded.text_handler import text_speech
from pygame_upgraded.variables import screen


class Poketer:
    def __init__(self, name, mood, color, health, max_health, attack, catchword, img_name):
        self.name = name
        self.mood = mood
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.color = color
        self.catchword = catchword
        self.image = pg.image.load(img_name).convert_alpha()

    def add_health(self, health_score):
        self.health += health_score

    def add_max_health(self, health_score):
        self.max_health += health_score
gunnar = Poketer("Glada Gunnar", 'happy', 'yellow', 50, 50, 45, catchword="#YOLO", img_name="images/Green_monster_resized.png")
ada = Poketer("Aggressiva Ada", 'angry', 'red', 50, 50, 45, catchword="#FTW", img_name="images/Pink_dragon_01.png")


def attack_function(attacker, defender):
    defender.add_health(-attacker.attack)
    return attacker.attack


def special_attack(attacker, defender):
    misschans = randint(1, 6)
    if misschans <= 2:
        defender.add_health(-attacker.attack * 2)
        return attacker.attack * 2
    return 0


def cpu_random_attack():
    random_number = randint(1, 11)
    if random_number <= 7:
        return True
    if random_number >= 8:
        return False


def glada_gunnar(x, y, a, b):
        screen.blit(gunnar.image, (x, y))
        text_speech(screen, "RobotoSlab-Medium.ttf", 15, f"{gunnar.name}", gunnar.color, a, b, True)
        text_speech(screen, "RobotoSlab-Medium.ttf", 15,
                    f"Stats: HP: {gunnar.health}/{gunnar.max_health}, Attack: {gunnar.attack}, Mood: {gunnar.mood}",
                    WHITE, 170, 20, True)
        bg_bar1 = pg.Rect(200, 50, gunnar.max_health, 50)
        hp_bar1 = pg.Rect(200, 50, 200 * (gunnar.health * 0.01), 50)
        if gunnar.health > 0:
            pg.draw.rect(screen, (255, 0, 0), bg_bar1)
            pg.draw.rect(screen, (0, 255, 0), hp_bar1)


def aggressive_ada(x, y, a, b):
    screen.blit(ada.image, (x, y))
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, f"{ada.name}", ada.color, a, b, True)
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, f"Stats: HP: {ada.health} Attack: {ada.attack} Mood: {ada.mood}",
                WHITE, 630, 575, True)
    bg_bar1 = pg.Rect(50, 530, ada.max_health, 50)
    hp_bar1 = pg.Rect(50, 530, 200 * (ada.health * 0.01), 50)
    if ada.health > 0:
        pg.draw.rect(screen, (255, 0, 0), bg_bar1)
        pg.draw.rect(screen, (0, 255, 0), hp_bar1)


def sword(turn):
    sword = pg.image.load("images/sword_resized.png")
    x_off, y_off = periodic_movement(1, 5)
    if turn == "user":
        rotate_image = pg.transform.rotozoom(sword, 0 + x_off, 1)
    else:
        rotate_image = pg.transform.rotozoom(sword, 70 + x_off, 1)
    new_rect = rotate_image.get_rect(center=(400, 300))
    screen.blit(rotate_image, new_rect)


def crossed_sword():
    double_sword = pg.image.load("images/Sword_crossed_01.PNG")
    double_sword = pg.transform.smoothscale(double_sword, (230, 230))

    x_off, y_off = periodic_movement(1, 7)
    rect = double_sword.get_rect()
    shield = pg.transform.smoothscale(double_sword, (rect.width + int(x_off), rect.height + int(x_off)))
    blit_rect = shield.get_rect()
    blit_rect.center = (420, 280)
    screen.blit(shield, blit_rect)


def winning_crown_hasse_moving():
    winning_crown = pg.image.load("images/crown.png")
    winning_crown = pg.transform.scale(winning_crown, (170, 140))
    x_off, y_off = periodic_movement(1, 5)
    screen.blit(winning_crown, (270, 180 + y_off))


def winning_crown_ada_moving():
    winning_crown = pg.image.load("images/crown.png")
    winning_crown = pg.transform.scale(winning_crown, (151, 124))
    x_off, y_off = periodic_movement(1, 5)
    screen.blit(winning_crown, (340, 245 + y_off))
