import pygame

from .types import Color
from .cell import cell_width
from .config import GRID_SIZE

def initialize_game_window(width, height):
    GAME_WINDOW = pygame.display.set_mode(size=(width, height))
    GAME_WINDOW.fill(Color.WHITE)

    # Put 1/3 cell worth of space in between the two boards
    third_cell = (cell_width(height/2, GRID_SIZE) / 3)

    pygame.draw.rect(GAME_WINDOW, Color.ATTACK_BOARD_COLOR, (0, 0, width, height / 2))
    pygame.draw.rect(GAME_WINDOW, Color.DEFENSE_BOARD_COLOR, (0, (height / 2) + third_cell, width, (height / 2) + third_cell))

    pygame.display.set_caption("Battleship")
    return GAME_WINDOW
