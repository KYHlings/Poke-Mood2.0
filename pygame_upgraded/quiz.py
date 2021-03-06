import math
import pygame

from pygame_upgraded import global_stuff
from pygame_upgraded.global_stuff import rel_to_pix
from pygame_upgraded.text_handler import TextBox
from pygame_upgraded.buttons import Button
from pygame_upgraded.variables import *


from pygame_upgraded.music import music, sound
from pygame_upgraded.quiz_api import get_quiz, quiz_categories


return_screen = None
poketer = None


class QuizStartScreen:
    def __init__(self, number_of_quiz_questions, quiz_categories, return_screen_, poketer_):
        global poketer
        #self.music = music_battle() #cl
        poketer = poketer_

        global return_screen
        return_screen = return_screen_
        music("music/quizz_music.mp3")
        background_image_raw = pygame.image.load("images/Background_forest.jpg").convert()
        self.background_image = pygame.transform.scale(background_image_raw, screen_size)
        self.title = TextBox(rel_pos=(0.5, 0.1), font_name=FONT_ROBOTO,
                             font_size=30, font_bold=False, color=WHITE, text="It's quiz time!")

        quiz_start_text = f"""You will now get to try your luck with {number_of_quiz_questions} tricky questions. If you get at least
{number_of_quiz_questions - 1} correct answers you win a health bonus. Which category do you choose?"""

        self.info_text = TextBox(rel_pos=(0.5, 0.25), font_name=FONT_ROBOTO,
                                 font_size=25, font_bold=False, color=WHITE, text=quiz_start_text, line_width=55)
        self.category_buttons = []
        self.button_positions = [(0.3, 0.6),
                                 (0.7, 0.6),
                                 (0.3, 0.8),
                                 (0.7, 0.8)]

        self.categories = list(quiz_categories.keys())
        for idx, category in enumerate(self.categories):
            quiz_button = Button(rel_pos=self.button_positions[idx], rel_size=(0.4, 0.2),
                                 color=QUIZ_TRANSP_GREEN, highlight=QUIZ_TRANSP_GREEN_HIGHL,
                                 font_size=22, font_color=WHITE, text=category)
            self.category_buttons.append(quiz_button)

    def handle_keydown(self, key):
        if key == pygame.K_SPACE:
            return QuizScreen()
        return self

    def handle_mouse_button(self, mouse_button):
        clicked_button_idx = None

        for category_button in self.category_buttons:
            if category_button.handle_mouse_button(mouse_button):
                clicked_button_idx = self.category_buttons.index(category_button)
                sound("music/cartoon_cymbal_hit.mp3")
                break

        if clicked_button_idx is not None:
            for category_button in self.category_buttons:
                category_button.enabled = False
            global_stuff.next_screen = QuizScreen(self.categories[clicked_button_idx])

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(BLACK)
        screen.blit(self.background_image, (0, 0))
        self.title.render(screen)
        self.info_text.render(screen)

        for category_button in self.category_buttons:
            category_button.render(screen)


class QuizScreen:

    def __init__(self, quiz_category):
        background_image_raw = pygame.image.load("images/Background_forest.jpg").convert()
        self.background_image = pygame.transform.scale(background_image_raw, screen_size)
        self.title = None
        self.question_text = None
        self.quiz_answer_buttons = []
        self.current_question = 0

        self.number_of_quiz_questions = 5

        category, questions, correct_answers, answer_options = get_quiz(self.number_of_quiz_questions, quiz_category)
        self.category = category
        self.questions = questions
        self.correct_answers = correct_answers
        self.answer_options = answer_options
        self.correct_answer_idx = None
        self.num_of_correct_ans = 0
        self.button_positions = [(0.3, 0.6),
                                 (0.7, 0.6),
                                 (0.3, 0.8),
                                 (0.7, 0.8)]
        self.set_question()
        self.next_question_timeout = 0

    def set_question(self):

        self.next_question_timeout = 0
        self.current_question += 1

        if self.current_question == self.number_of_quiz_questions + 1:
            global_stuff.next_screen = QuizFinishedScreen(self.num_of_correct_ans, self.number_of_quiz_questions)
            return

        self.correct_answer_idx = self.answer_options[self.current_question - 1].index(
            self.correct_answers[self.current_question - 1])

        self.title = TextBox(rel_pos=(0.5, 0.1), font_name=FONT_ROBOTO,
                             font_size=25, font_bold=False, color=WHITE,
                             text=f"{self.category} - Question {self.current_question}")

        self.question_text = TextBox(rel_pos=(0.5, 0.25), font_name=FONT_ROBOTO,
                                     font_size=25, font_bold=False, color=WHITE,
                                     text=self.questions[self.current_question - 1], line_width=55)
        self.quiz_answer_buttons = []
        for idx, answer_option in enumerate(self.answer_options[self.current_question - 1]):
            quiz_button = Button(rel_pos=self.button_positions[idx], rel_size=(0.4, 0.2),
                                 color=QUIZ_TRANSP_GREEN, highlight=QUIZ_TRANSP_GREEN_HIGHL,
                                 font_size=22, font_color=WHITE, text=answer_option)
            self.quiz_answer_buttons.append(quiz_button)

    def handle_keydown(self, key):
        if key == pygame.K_SPACE:
            pass
            #self.set_question()
        return self

    def handle_timer(self):
        return self

    def handle_mouse_button(self, mouse_button):
        clicked_button_idx = None
        quiz_button = None
        for quiz_button in self.quiz_answer_buttons:
            if quiz_button.handle_mouse_button(mouse_button):
                clicked_button_idx = self.quiz_answer_buttons.index(quiz_button)
                break

        if clicked_button_idx is not None:

            self.next_question_timeout = pygame.time.get_ticks()

            if clicked_button_idx == self.correct_answer_idx:
                quiz_button.color = QUIZ_TRANSP_GREEN_LIGHT
                self.num_of_correct_ans += 1
                sound("music/kids_cheering.mp3")
            else:
                quiz_button.color = QUIZ_TRANSP_RED
                self.quiz_answer_buttons[self.correct_answer_idx].color = QUIZ_TRANSP_GREEN_LIGHT
                sound("music/dinosaur_growl.mp3")

            for quiz_button in self.quiz_answer_buttons:
                quiz_button.enabled = False

    def handle_timer(self):
        return self

    def render(self, screen):
        time_now = pygame.time.get_ticks()
        if time_now - self.next_question_timeout > 2000 and self.next_question_timeout != 0:
            self.set_question()

        screen.fill(BLACK)
        screen.blit(self.background_image, (0, 0))

        self.title.render(screen)

        self.question_text.render(screen)

        for quiz_answer_button in self.quiz_answer_buttons:
            quiz_answer_button.render(screen)


class QuizFinishedScreen:
    def __init__(self, num_of_correct_ans, number_of_quiz_questions):

        pygame.mixer.music.stop()
        percent_correct = num_of_correct_ans / number_of_quiz_questions
        poketer.add_health(int(percent_correct * (number_of_quiz_questions * 10)))

        info_text = f"Good job! You got {int(percent_correct*(number_of_quiz_questions * 10))} extra healthpoints!"
        background_image_raw = pygame.image.load("images/Background_forest.jpg").convert()
        self.background_image = pygame.transform.scale(background_image_raw, screen_size)

        self.title = TextBox(rel_pos=(0.5, 0.1), font_name=FONT_ROBOTO,
                             font_size=30, font_bold=False, color=WHITE,
                             text=f"You answered {num_of_correct_ans} out of {number_of_quiz_questions} questions correctly.")

        self.info_text = TextBox(rel_pos=(0.5, 0.25), font_name=FONT_ROBOTO,
                                     font_size=25, font_bold=False, color=WHITE, text=info_text, line_width=55)

        self.poketer_image = pygame.image.load("images/Green_monster_resized.png").convert_alpha()
        self.poketer_image = pygame.transform.smoothscale(self.poketer_image, (207, 207))

        self.quiz_finished_button = Button(rel_pos=(0.5, 0.85), rel_size=(0.3, 0.15),
                                           color=QUIZ_TRANSP_GREEN, highlight=QUIZ_TRANSP_GREEN_HIGHL,
                                           font_size=22, font_color=WHITE, text="CONTINUE")

    def handle_keydown(self, key):
        if key == pygame.K_ESCAPE:
            return QuizScreen()
        return self

    def handle_mouse_button(self, mouse_button):
        if self.quiz_finished_button.handle_mouse_button(mouse_button):
            #common.next_screen = QuizStartScreen(5, quiz_categories)
            global_stuff.next_screen = return_screen
            music("music/battle_time_1.mp3")

    def handle_timer(self):
        return self

    def render(self, screen):
        screen.fill(BLACK)
        screen.blit(self.background_image, (0, 0))
        self.title.render(screen)
        self.info_text.render(screen)

        time = pygame.time.get_ticks()
        y_off = 5 * math.sin(time*3.14/1000)

        pixel_pos = rel_to_pix((0.5, 0.55))
        poketer_image_rect = self.poketer_image.get_rect()
        poketer_image_rect.center = pixel_pos[0], pixel_pos[1] + y_off
        screen.blit(self.poketer_image, poketer_image_rect)

        self.quiz_finished_button.render(screen)


def mainloop(screen, font):
    # Initial state
    current_screen = QuizStartScreen(5, quiz_categories, None, None)

    clock = pygame.time.Clock()
    while True:

        # Event handling
        ev = pygame.event.poll()

        if ev.type == pygame.KEYDOWN:
            current_screen = current_screen.handle_keydown(ev.key)

        elif ev.type == pygame.MOUSEBUTTONDOWN:
            current_screen.handle_mouse_button(ev.button)

        elif ev.type == pygame.QUIT:
            break

        if global_stuff.next_screen is not None:
            current_screen = global_stuff.next_screen
            global_stuff.next_screen = None

        current_screen.handle_timer()

        # Render
        current_screen.render(screen)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    global_stuff.common_init()
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("PokeMood")
    font = FONT_ROBOTO
    mainloop(screen, font)
    pygame.quit()
