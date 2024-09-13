import pygame

from pygame import Surface

from .config import SCREEN_HEIGHT, SCREEN_WIDTH

from .types import Coordinate
from .display import Color


class Cell:
    def __init__(self, x, y, size) -> None:
        self.rect = pygame.Rect(x * SCREEN_WIDTH / size, y * SCREEN_HEIGHT / (size * 2), SCREEN_WIDTH / size, SCREEN_HEIGHT / (size * 2))
        self.is_hit = False
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

    def draw(self, surface: Surface):
        if self.is_hit: 
            pygame.draw.circle(surface,Color.WHITE, (self.x + self.width/2, self.y + self.height/2), self.height / 2.5)
        pygame.draw.rect(surface, Color.RED if self.is_hit else Color.WHITE, self.rect, 1)

    def hit(self): 
        self.is_hit = True

    def check_hit(self, coordinate: Coordinate) -> bool:
        return self.rect.collidepoint(coordinate)
