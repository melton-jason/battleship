import pygame

from pygame import Surface

from .config import SCREEN_HEIGHT, SCREEN_WIDTH

from .types import Coordinate
from .display import Color


def cell_width(container_width: float, grid_size: int) -> float:
    """
    Calculates the width or height in px of an individual cell in an NxN grid of cells

    Args: 
        container_size (float): The width or height of the container for the cell
        grid_size (int): The number of cells in a row/column of the NxN grid

    Returns: 
        float: The width or height of the cell in pixels
    """
    return container_width / grid_size


def cell_index_to_px(cell_index: int, container_width: float, grid_size: int) -> float:
    return cell_index * container_width / grid_size

def px_to_cell_index(pixels: int, container_width: float, grid_size: int) -> int:
    return pixels * grid_size / container_width


class Cell:
    def __init__(self, x: int, y: int, size: int, container_width=SCREEN_WIDTH, container_height=SCREEN_HEIGHT / 2) -> None:
        self.rect = pygame.Rect(cell_index_to_px(x, container_width, size), cell_index_to_px(
            y, container_height, size), cell_width(container_width, size), cell_width(container_height, size))
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
        # Position the hit marker in the center of the Cell
        center = (self.x + self.width/2, self.y + self.height/2)

        # The radius of the circle should be slightly smaller than half the height of the Cell
        # The radius is "slightly smaller" than half because it looks better than exactly half 
        # the height of the Cell
        circle_radius = self.height / 2.3

        pygame.draw.circle(surface, Color.WHITE, center, circle_radius)

    def draw_normal(self, surface: Surface):
        color = Color.RED if self.is_hit else Color.WHITE

        pygame.draw.rect(surface, color, self.rect, 1)

    def draw(self, surface: Surface):
        if self.is_hit:
            self.draw_hit(surface)
        self.draw_normal(surface)

    def _hit(self):
        """
        Any internal logic the class needs to perform whenever it is hit
        """
        self.is_hit = True

    def hit(self, coordinate: Coordinate) -> bool:
        """
        Checks whether the coordiate intersects with the cell and "hits" the cell if so. Returns whether the cell was hit or not

        Args: 
            coordinate (Tuple[int, int]): The x and y coordinate of the hit in px
        Returns: 
            bool: True if the cell was hit, False otherwise
        """
        hit = self.rect.collidepoint(coordinate)
        if hit:
            self._hit()
            return True
        return False
