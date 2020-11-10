import pygame
import sys

pygame.init()
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("Arial", 40, True)
font2 = pygame.font.SysFont("Arial", 20, True)
white = (255, 255, 255)

mountains = pygame.image.load("pics/bg_mountains.jpg")
lobby = pygame.image.load("pics/lobby.PNG")
fight_button = pygame.image.load("pics/fight_sign.png")
fight = pygame.image.load("pics/fight.PNG")


def how_to_play():
    running = True
    while running:
        screen.blit(mountains, (0, 0))
        screen.blit(font.render("How to play!", True, (white)), (50, 20))
        screen.blit(font2.render("Press [ESCAPE] to go back", True, (white)), (530, 20))
        controls = screen.blit(font.render("Fight controls", True, (white)), (50, 120))
        betting = screen.blit(font.render("Betting in lobby", True, (white)), (50, 170))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("back")
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if event.button == 1:
                    if controls.collidepoint(mx, my):
                        controls_instructions()
                    if betting.collidepoint(mx, my):
                        lobby_instructions()

        pygame.display.update()


def controls_instructions():
    print("hello")
    running = True
    screen.blit(mountains, (0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.blit(fight, (300, 50))

        # rubrik
        screen.blit(font.render("Controls", True, (white)), (20, 20))
        # förklarande text
        screen.blit(font2.render("Left Player:", True, (white)), (10, 100))
        screen.blit(font2.render("A --- Move left", True, (white)), (10, 120))
        screen.blit(font2.render("D --- Move Right", True, (white)), (10, 140))
        screen.blit(font2.render("W --- Punch", True, (white)), (10, 160))
        screen.blit(font2.render("S --- Kick", True, (white)), (10, 180))
        screen.blit(font2.render("SPACE --- Jump", True, (white)), (10, 200))
        screen.blit(font2.render("Right Player:", True, (white)), (10, 240))
        screen.blit(font2.render("Arrow Left --- Move Left", True, (white)), (10, 260))
        screen.blit(font2.render("Arrow Right --- Move Right", True, (white)), (10, 280))
        screen.blit(font2.render("Arrow Up --- Punch", True, (white)), (10, 300))
        screen.blit(font2.render("Arrow Down --- Kick", True, (white)), (10, 320))
        screen.blit(font2.render("Right Ctrl --- Jump", True, (white)), (10, 340))

        pygame.display.update()


def lobby_instructions():
    print("hello")
    running = True
    screen.blit(mountains, (0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.blit(lobby, (350, 50))
        screen.blit(fight_button, (370, 400))
        # rubrik
        screen.blit(font.render("Betting in lobby", True, (white)), (20, 20))
        # förklarande text
        screen.blit(font2.render("To the left are the players live-score", True, (white)), (5, 100))
        screen.blit(font2.render("To bet simply read who's turn it is,", True, (white)), (5, 120))
        screen.blit(font2.render("then make your bet by clicking the ", True, (white)), (5, 140))
        screen.blit(font2.render("money. In the box below is your", True, (white)), (5, 160))
        screen.blit(font2.render("current bet displayed, below that is", True, (white)), (5, 180))
        screen.blit(font2.render("the possible amount you can win!", True, (white)), (5, 200))
        screen.blit(font2.render("To Confirm your bet, simply press", True, (white)), (5, 220))
        screen.blit(font2.render("the head of the player next to the", True, (white)), (5, 240))
        screen.blit(font2.render("money that you want to place your", True, (white)), (5, 260))
        screen.blit(font2.render("bet on.", True, (white)), (5, 280))
        screen.blit(font2.render("After you have confirmed your bet", True, (white)), (5, 300))
        screen.blit(font2.render("this fight sign will appear, when", True, (white)), (5, 320))
        screen.blit(font2.render("you both are ready, press it to", True, (white)), (5, 340))
        screen.blit(font2.render("start the epic battle!", True, (white)), (5, 360))

        pygame.display.update()


if __name__ == '__main__':
    how_to_play()


