import pygame

from .cell import Cell

from .config import SCREEN_HEIGHT, SCREEN_WIDTH, GRID_SIZE

from .types import Coordinate

class Ship:

    def __init__(self, x: int, y: int, GRID_SIZE: int, container_width=SCREEN_WIDTH, container_height=SCREEN_HEIGHT / 2) -> None:
        self.coordinates = []
        pass

    def updateCoordinates():
        pass

    def createShip(self, coordinate: Coordinate):
        # 
        pass

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def hit(self, coordinate: Coordinate) -> bool:
        pass

    def isSunk(self) -> bool:
        pass

    