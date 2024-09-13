from typing import Optional

from pygame import Surface

from .types import Coordinate
from .cell import Cell, px_to_cell_index

class Board:
    def __init__(self, y_offset, width, height, board_size) -> None:
        self.cells = [Cell(x, y + px_to_cell_index(y_offset, height, board_size), board_size, width, height) for x in range(board_size)
                      for y in range(board_size)]

    def draw(self, surface: Surface):
        for cell in self.cells:
            cell.draw(surface)
    
    def hit_pos(self, coord: Coordinate) -> Optional[Cell]: 
        """
        Checks whether the given coordinate hits a cell in the board. "Hits" and returns the cell if hit, 
        or returns None to indiciate no cells were hit 

        Args: 
            coord (Tuple[int, int]): The x and y coordinate of the hit in px
        Returns: 
            Cell or None: The Cell hit by the coordinate, or None if no cells in the board were hit
        """
        for cell in self.cells: 
            if cell.hit(coord):
                return cell
        return None
    
