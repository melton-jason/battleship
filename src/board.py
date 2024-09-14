import pygame
from typing import Optional

from pygame import Surface

from .types import Coordinate
from .cell import Cell, px_to_cell_index

from .ship import Ship

class Board:
    def __init__(self, y_offset, width, height, board_size, ship_size) -> None:
        self.cells = [Cell(x, y + px_to_cell_index(y_offset, height, board_size), board_size, width, height) for x in range(board_size)
                      for y in range(board_size)]
        self.ship_size = ship_size
        self.ships = []

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
    
    def SpawnShip(self):
        count = 0
        while count < self.ship_size:
            self.placeShip()
            count += 1

    def placeShip(self, ):
        events = pygame.event.get()
        coordinate = [] # Random coordinates
        # Create a ship and spawn it randomly on the board
        ship = Ship()
        # Check if it is in bounds
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    location -= 1
                if event.key == pygame.K_RIGHT:
                    location += 1
                if event.key == pygame.K_UP:
                    location += 1
                if event.key == pygame.K_DOWN:
                    location += 1

        self.ships.append(ship)
        pass
