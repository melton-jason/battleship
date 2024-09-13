import pygame

from pygame import Surface

from .cell import Cell


class Board:
    def __init__(self, board_size=10) -> None:
        self.cells = [Cell(x, y, board_size) for x in range(board_size)
                      for y in range(board_size)]

    def draw(self, surface: Surface):
        for cell in self.cells:
            cell.draw(surface)
