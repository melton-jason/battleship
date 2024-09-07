import pygame

FPS = 60

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Color: 
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)
    GREY = pygame.Color(128, 128, 128)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)

SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

def initialize_game_window():
    GAME_WINDOW = pygame.display.set_mode(size=SCREEN_DIMENSIONS)
    GAME_WINDOW.fill(Color.WHITE)
    pygame.display.set_caption("Battleship")
    return GAME_WINDOW
