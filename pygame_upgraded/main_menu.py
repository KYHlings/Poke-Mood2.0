import pygame
import sys
from pygame_upgraded.lobby import lobby
from pygame_upgraded.how_to_play import how_to_play


def main_menu():
    pygame.init()
    pygame.mixer.init()
    font = pygame.font.SysFont("Arial", 40, True)
    # running gör så att programmet fortsätter köra för alltid tills running = False
    running = True
    while running:


        pygame.mixer.music.load("music_fight/menu_music.ogg")
        pygame.mixer.music.play(-1)
        screen = pygame.display.set_mode((800, 600))

        logo = pygame.image.load('pics/logga.png')
        play_sign = pygame.image.load('pics/play_game_logga.png')
        quit_sign = pygame.image.load('pics/Quitknapp.png')

        how_to = screen.blit(font.render("How to play", True, (255, 0, 0)), (250, 350))

        play_button = pygame.Rect(250, 250, 300, 100)
        quit_button = pygame.Rect(250, 450, 300, 100)

        pygame.draw.rect(screen, (0, 0, 0), play_button)
        pygame.draw.rect(screen, (0, 0, 0), quit_button)


        screen.blit(play_sign, (250, 250))
        screen.blit(quit_sign, (250, 450))
        screen.blit(logo, (50, 50))



        # loopar igenom en lista med pygame.events (knapptryckningar)
        for event in pygame.event.get():
            # kollar om användaren trycker på det röda krysset
            if event.type == pygame.QUIT:
                # stänger programmet
                sys.exit()
            # kollar om det sker knapptryck på musen
            if event.type == pygame.MOUSEBUTTONDOWN:
                #
                mx, my = pygame.mouse.get_pos()
                # kollar vilken knapp på musen som tryckts ned
                if event.button == 1:
                    # kollar om musens position vid knapptryckningen kolliderar med playbutton
                    if play_button.collidepoint(mx, my):
                        # starta en lobby
                        lobby()
                    if how_to.collidepoint(mx, my):
                        how_to_play()
                    if quit_button.collidepoint(mx, my):
                        sys.exit()

        # uppdaterar displayen
        pygame.display.update()