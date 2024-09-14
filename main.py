import pygame

from src.config import SCREEN_WIDTH ,SCREEN_HEIGHT, GRID_SIZE
from src.game import Game
from src.display import initialize_game_window

pygame.init()
GAME_WINDOW = initialize_game_window(SCREEN_WIDTH, SCREEN_HEIGHT)
Clock = pygame.time.Clock()

if __name__ == "__main__":
    battleship = Game(Clock, GAME_WINDOW, GRID_SIZE)
    battleship.run()
