from typing import Optional

from pygame import Surface

from .types import Coordinate
from .cell import Cell

class Board:
    def __init__(self, y_offset, board_size=10) -> None:
        self.cells = [Cell(x, y + y_offset, board_size) for x in range(board_size)
                      for y in range(board_size)]

    def draw(self, surface: Surface):
        for cell in self.cells:
            cell.draw(surface)
    
    def hit_pos(self, coord: Coordinate) -> Optional[Cell]: 
        for cell in self.cells: 
            if cell.check_hit(coord): 
                cell.hit()
                return cell
        return None
    
