import sys
import pygame

from src.game_state import GameState
from src.program_variables import ProgramVariables
from src.pygame_helpers import initialise_pygame, running_loop
from src.timer import timer


def main():
    display_surface = timer('Initialisation', initialise_pygame)

    ProgramVariables.game_state = GameState.RUNNING

    running_loop(display_surface)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()