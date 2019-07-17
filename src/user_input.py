from src.game_state import GameState
from src.program_variables import ProgramVariables
from pygame.locals import *

mouse_position = __import__('pygame').mouse.get_pos


def check_for_user_input(events, display_surface):

    for event in events:
        if event.type == QUIT:
            ProgramVariables.game_state = GameState.STOPPING

        if event.type == KEYUP or event.type == KEYDOWN:
            handle_keys()

        if event.type == MOUSEBUTTONDOWN:
            mouse_down()

        if event.type == MOUSEBUTTONUP:
            mouse_up()


def handle_keys():
    print("Does nothing yet")


def mouse_down():
    print("Empty")


def mouse_up():
    print("Empty")
