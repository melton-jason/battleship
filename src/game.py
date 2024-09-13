import sys

import pygame
from pygame.event import Event

from .board import Board

FPS = 30


class Game:
    def __init__(self, clock, surface) -> None:
        self._running = True
        self.clock = clock
        self.surface = surface
        self.board = Board()

    def run(self):
        while self._running:
            self.board.draw(self.surface)
            self.handle_events()
            self.handle_update()

    def handle_events(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def handle_event(self, event: Event):
        if event.type == pygame.QUIT:
            self._running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            clicked = [
                cell for cell in self.board.cells if cell.rect.collidepoint(mouse_pos)]
            print(clicked)

    def handle_update(self):
        pygame.display.update()
        self.clock.tick(FPS)
