import pygame

from src.game import Game
from src.display import initialize_game_window

pygame.init()
GAME_WINDOW = initialize_game_window()
Clock = pygame.time.Clock()

if __name__ == "__main__":
    battleship = Game(Clock, GAME_WINDOW)
    battleship.run()
