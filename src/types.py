import pygame

from typing import Tuple
from enum import Enum

Coordinate = Tuple[int, int]

class Color:
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)
    GREY = pygame.Color(128, 128, 128)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)
    DARK_BLUE = pygame.Color(0, 0, 139)
    ATTACK_BOARD_COLOR = pygame.Color(30, 93, 156)
    DEFENSE_BOARD_COLOR = pygame.Color(111, 169, 227)

class State(Enum):
    START = 1
    SELECTION = 2
    PLAYING = 3
    END = 4

class Player(Enum):
    ONE = 1
    TWO = 2