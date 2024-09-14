import sys

import pygame

from .config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT

from .board import Board
from .cell import cell_width

HALF_HEIGHT = SCREEN_HEIGHT / 2


class Game:
    def __init__(self, clock, surface: pygame.Surface, grid_size: int) -> None:
        self._running = True
        self.clock = clock
        self.surface = surface
        self.opponent_board = Board(y_offset=0, width=SCREEN_WIDTH,
                           height=HALF_HEIGHT, board_size=grid_size, ship_size=5)

        # Put 1/3 cell worth of space in between the two boards
        third_cell = (cell_width(HALF_HEIGHT, grid_size) / 3)
        self.user_board = Board(y_offset=HALF_HEIGHT + third_cell, width=SCREEN_WIDTH,
                              height=HALF_HEIGHT - third_cell, board_size=grid_size, ship_size=5)

    def run(self):
        """
        Starts the Game and handles the core game loop
        """
        while self._running:
            self.render()
            self.handle_events()
            self.handle_update()

    def render(self):
        """
        Handles drawing and showing all UI
        """
        self.opponent_board.draw(self.surface)
        self.user_board.draw(self.surface)

    def handle_events(self):
        """
        Handles catching and processing events which happen each frame: i.e., game logic
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self.opponent_board.hit_pos(mouse_pos)

    def handle_update(self):
        """
        Handles advancing the game state
        """
        pygame.display.update()
        self.clock.tick(FPS)
