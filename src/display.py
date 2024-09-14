import pygame
import sys

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
    DARK_BLUE = pygame.Color(0,0,139)

SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

def initialize_game_window():
    GAME_WINDOW = pygame.display.set_mode(size=SCREEN_DIMENSIONS)
    GAME_WINDOW.fill(Color.WHITE)
    pygame.display.set_caption("Battleship")
    return GAME_WINDOW

def game_over_display(window, winner_number):
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 36)
   
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 36)

    text = f"Player {winner_number} Wins!"
    text_surface = font.render(text, True, Color.WHITE)


    instructions = "Press Q to Quit or R to Play Again"
    instructions_surface = small_font.render(instructions, True, Color.WHITE)

    running = True

    #Quitting, restarting functionality
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return

        window.fill(Color.DARK_BLUE)

        window.blit(text_surface, (window.get_width() // 2 - text_surface.get_width() // 2, window.get_height() // 2 - text_surface.get_height() // 2 - 50))
        window.blit(instructions_surface, (window.get_width() // 2 - instructions_surface.get_width() // 2, window.get_height() // 2 - instructions_surface.get_height() // 2 + 50))
        
        pygame.display.flip()

