import pygame

from pygame import Surface

from .config import SCREEN_HEIGHT, SCREEN_WIDTH, COL_SIZE

from .types import Coordinate
from .types import Color
from .audio import Audio

class Cell:
    def __init__(self, x: int, y: int, offset) -> None:
        self.is_hit: bool = False
        self.is_active: bool = False
        self.has_ship: bool = False
        self.visible = True

        self.x = x * COL_SIZE + 3
        self.y = y * COL_SIZE + 3 + offset
        self.width = COL_SIZE - 7
        self.height = COL_SIZE - 7

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_hit(self, surface: Surface):
        # Position the hit marker in the center of the Cell
        center = (self.x + self.width/2, self.y + self.height/2)
        pygame.draw.circle(surface, Color.WHITE, center, 3)


    def draw_normal(self, surface: Surface):
        if self.is_hit:
            if self.has_ship: color = Color.RED
            else: color = Color.BACKGROUND
        elif self.has_ship:
            color = Color.GREEN
        elif self.is_active:
            color = Color.GREEN
        else:
            color = Color.CELL_NEUTRAL

        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))

    def draw_invisible(self, surface: Surface):
        pygame.draw.rect(surface, Color.CELL_NEUTRAL, (self.x, self.y, self.width, self.height))


    def draw(self, surface: Surface, visible: bool = True):
        if not visible and not self.is_hit:
            return self.draw_invisible(surface)

        if self.is_hit:
            self.draw_hit(surface)
        self.draw_normal(surface)

    def hit(self, coordinate: Coordinate, board) -> bool:
        """
        Checks whether the coordiate intersects with the cell and "hits" the cell if so. Returns whether the cell was hit or not

        Args:
            coordinate (Tuple[int, int]): The x and y coordinate of the hit in px
        Returns:
            bool: True if the cell was hit, False otherwise
        """
        hit = self.rect.collidepoint(coordinate)

        if hit and not self.is_hit:  # Check if it's not already hit
            self.is_hit = True
            if self.has_ship:
                Audio.play_hit()
                board.check_ship_sunk(self)
            else:
                Audio.play_miss()
            return True
        return False