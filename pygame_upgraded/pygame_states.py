import pygame as pg


from TextToPygame import start_game

#print("Lets use your new stats, press [Enter] to ge in to the World of Poketeers")
import pygame_upgraded.variables
from pygame_upgraded import common
from pygame_upgraded.screens import MenuStartScreen, StartScreen
from pygame_upgraded.variables import screen

pg.init()


def mainloop(screen):
    # To be able to go back to startscreen and run popups if not run before
    pygame_upgraded.variables.start_screen = StartScreen()

    state = MenuStartScreen()

    clock = pg.time.Clock()
    while True:
        # Event handling
        ev = pg.event.poll()

        if ev.type == pg.KEYDOWN:
            state = state.handle_keydown(ev.key)

        if ev.type == pg.MOUSEBUTTONDOWN:
            temp_state = state.handle_mouse_button(ev.button)
            if temp_state is not None:
                state = temp_state

        elif ev.type == pg.QUIT:
            break

        if common.next_screen is not None:
            #print("changing frames to", type(common.next_screen))
            state = common.next_screen
            common.next_screen = None

        state = state.handle_timer()
        state.render(screen)

        pg.display.update()
        clock.tick(30)


if __name__ == '__main__':
    start_game(False)
    common.common_init()
    pg.display.set_caption("PokeMood")
    mainloop(screen)
    pg.quit()
