import pygame
from pygame.locals import *

from src.display import initialize_game_window, FPS

pygame.init()
GAME_WINDOW = initialize_game_window()

FramePerSec = pygame.time.Clock()

def handle_update():
    pygame.display.update()
    FramePerSec.tick(FPS)


def game_loop():
    handle_update()

if __name__ == "__main__":
    while True: 
        game_loop()
