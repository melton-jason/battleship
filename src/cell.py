import pygame

from pygame import Surface

from .display import Color


class Cell:
    def __init__(self, x, y, size) -> None:
        self.rect = pygame.Rect(x * size, y * size, size, size)
        self.hit = False
        self.visible = True

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, Color.WHITE, self.rect, 1)
