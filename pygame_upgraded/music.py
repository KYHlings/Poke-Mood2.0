import pygame as pg
from pygame import mixer



def sound_ambient_hover_quizz_btn():
    sound = mixer.Sound("music/ambient_quizz_c2_short.mp3")
    sound.play()
    sound.set_volume(0.1)


def sound_ambient_hover_over_attack_btn():
    sound = mixer.Sound("music/ambient_attack_c_short.mp3")
    sound.play(1)
    sound.set_volume(0.1)


def sound_ambient_hover_over_special_attack_btn():
    sound = mixer.Sound("music/ambient_special_attack_c1_short.mp3")
    sound.play()
    sound.set_volume(0.1)


def music_lose_game_melody():
    pg.mixer.init()
    pg.mixer.music.load("music/lose_game_melody.mp3")
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.2)


def music_win_game_melody():
    pg.mixer.init()
    pg.mixer.music.load("music/vinnar_låt_utkast.mp3")
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.3)


def music_battle():
    pg.mixer.init()
    pg.mixer.music.load("music/battle_time_1.mp3")
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.1)


def music_intro():
    pg.mixer.init()
    pg.mixer.music.load("music/intro_song_1.mp3")
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.1)


def sound(filename):
    sound = mixer.Sound(filename)
    sound.play()
    sound.set_volume(0.2)