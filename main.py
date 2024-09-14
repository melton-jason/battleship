import pygame
from pygame.locals import *
import src.display

from src.display import initialize_game_window, FPS

pygame.init()
GAME_WINDOW = initialize_game_window()

FramePerSec = pygame.time.Clock()

def handle_update():
    pygame.display.update()
    FramePerSec.tick(FPS)


def game_loop():
    handle_update()
    src.display.game_over_display(GAME_WINDOW, 1000) #function to display game over screen
    src.display.game_over_display(GAME_WINDOW, 2) #function to display game over screen
if __name__ == "__main__":
    while True: 
        game_loop()
