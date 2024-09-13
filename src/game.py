import sys

import pygame

from .config import FPS

from .board import Board


class Game:
    def __init__(self, clock, surface: pygame.Surface, grid_size) -> None:
        self._running = True
        self.clock = clock
        self.surface = surface
        self.ships = Board(y_offset=0, board_size=grid_size)
        self.opponent = Board(y_offset=grid_size, board_size=grid_size)

    def run(self):
        while self._running:
            self.render()
            self.handle_events()
            self.handle_update()

    def render(self):
        self.ships.draw(self.surface)
        self.opponent.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self.ships.hit_pos(mouse_pos)
                self.opponent.hit_pos(mouse_pos)

    def handle_update(self):
        pygame.display.update()
        self.clock.tick(FPS)
