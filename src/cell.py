import pygame

from pygame import Surface

from .config import SCREEN_HEIGHT, SCREEN_WIDTH

from .types import Coordinate
from .display import Color


class Cell:
    def __init__(self, x: int, y: int, size: int, container_width=SCREEN_WIDTH, container_height=SCREEN_HEIGHT) -> None:
        self.rect = pygame.Rect(x * container_width / size, y * container_height / (
            size * 2), container_width / size, container_height / (size * 2))
        self.is_hit: bool = False
        self.size = size
        self.visible = True

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def draw_hit(self, surface: Surface):
        pygame.draw.circle(surface, Color.WHITE, (self.x +
                           self.width/2, self.y + self.height/2), self.height / 2.5)

    def draw_normal(self, surface: Surface):
        pygame.draw.rect(
            surface, Color.RED if self.is_hit else Color.WHITE, self.rect, 1)

    def draw(self, surface: Surface):
        if self.is_hit:
            self.draw_hit(surface)
        self.draw_normal(surface)

    def hit(self, coordinate: Coordinate) -> bool:
        hit = self.rect.collidepoint(coordinate)
        if hit:
            self.is_hit = True
            return True
        return False
