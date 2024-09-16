import pygame
from typing import Optional
import sys
from pygame import Surface

from .types import Coordinate
from .config import COL_SIZE
from .cell import Cell
from .audio import Audio
from .ship import Ship

class Board:
    def __init__(self, y_offset, board_size, ship_size) -> None:
        self.cells = [[Cell(x, y, y_offset) for x in range(board_size)] for y in range(board_size)]

        self.ship_size = ship_size
        self.ships = []


    def draw(self, surface: Surface, show_ships: bool = True):
        for row in self.cells:
            for cell in row:
                cell.draw(surface, show_ships)
        for ship in self.ships:
            ship.draw(self)

    def hit_pos(self, coord: Coordinate) -> Optional[Cell]:
        """
        Checks whether the given coordinate hits a cell in the board. "Hits" and returns the cell if hit,
        or returns None to indiciate no cells were hit

        Args:
            coord (Tuple[int, int]): The x and y coordinate of the hit in px
        Returns:
            Cell or None: The Cell hit by the coordinate, or None if no cells in the board were hit
        """

        for row in self.cells:
            for cell in row:
                if cell.hit(coord, self):
                    print("Cell hit")
                    return cell

        print("No cell hit")

        return None

    def spawnShip(self):
        """
        Spawns a ship on the board
        """
        count = 0
        ship_size = self.ship_size
        while count < self.ship_size:
            self.placeShip(ship_size)
            count += 1
            ship_size -= 1

    def placeShip(self, ship_size):
        """
        Places a ship on the board and allows the player to move it around
        """
        x = 5
        y = 5
        direction = ["VERTICAL", "HORIZONTAL"]
        direction_counter = 0
        valid_direction_counter = direction_counter

        ship = Ship(x, y, ship_size, direction[valid_direction_counter])

        place_ship = True
        while place_ship:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ship.move("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        ship.move("RIGHT")
                    elif event.key == pygame.K_UP:
                        ship.move("UP")
                    elif event.key == pygame.K_DOWN:
                        ship.move("DOWN")
                    elif event.key == pygame.K_RETURN:
                        if self.isValidShipLocation(ship):
                            self.ships.append(ship)
                            self.mark_ship_cells(ship)
                            place_ship = False
                    elif event.key == pygame.K_r:
                        # cycle through the direction
                        direction_counter = (direction_counter+1) % len(direction)
                        if ship.isValidDirection(direction[valid_direction_counter]):
                            valid_direction_counter = direction_counter
                            ship.changeDirection(direction[valid_direction_counter])
                        else:
                            direction_counter = valid_direction_counter
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.reset_cells()
            ship.draw(self)
            self.draw(pygame.display.get_surface())
            pygame.display.update()

    def isValidShipLocation(self, newShip: Ship):
        """
        Checks if the new ship is in a valid location on the board and does not intersect with any other ships
        """
        coord_newShip = set(newShip.coordinates)
        for ship in self.ships:
            if coord_newShip.intersection(set(ship.coordinates)):
                return False
        return True

    def reset_cells(self):
        """
        Resets the is_active state of all cells to False
        """
        for row in self.cells:
            for cell in row:
                cell.is_active = False

    def mark_ship_cells(self, ship: Ship):
        """
        Marks the cells occupied by the ship as having a ship
        """
        for (x, y) in ship.coordinates:
            self.cells[y][x].has_ship = True

    def all_ships_sunk(self) -> bool:
        if len(self.ships) == self.ship_size:
            for ship in self.ships:
                if not self.is_ship_sunk(ship):
                    return False
            return True
        return False

    def check_ship_sunk(self, hit_cell: Cell) -> bool:
        print("Checking if ship sunk", hit_cell.x // COL_SIZE, hit_cell.y // COL_SIZE)
        print(self.ships)
        for ship in self.ships:
            print(ship.coordinates)
            if (hit_cell.x // COL_SIZE, (hit_cell.y // COL_SIZE)) in ship.coordinates:
                if not self.is_ship_sunk(ship):
                    print("Ship sunk")
                    Audio.play_sink()
                    return True
                else:
                    print("Ship not sunk")
        return False

    def is_ship_sunk(self, ship: Ship) -> bool:
        for (x, y) in ship.coordinates:
            cell = self.cells[y][x]
            if not cell.is_hit:
                return False
        return True