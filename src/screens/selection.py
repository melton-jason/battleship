import pygame

from ._screen import Screen
from ..types  import Color, State, Player
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE
from ..cell import cell_width


class SelectionScreen(Screen):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)

    def render(self, surface):
        # Add 1/3 cell worth of space in between the two boards for greater visual distinction
        third_cell = (cell_width(SCREEN_HEIGHT/2, GRID_SIZE) / 3)

        pygame.draw.rect(surface, Color.PLAYER_1_BOARD_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT / 2))
        pygame.draw.rect(surface, Color.PLAYER_2_BOARD_COLOR, (0, (SCREEN_HEIGHT / 2) + third_cell, SCREEN_WIDTH, (SCREEN_HEIGHT / 2) + third_cell))

        self.place_ship_instructions(surface, self.game.current_player)
        if self.game.current_player == Player.ONE:
            self.game.player_1_board.spawnShip()
            self.game.current_player = Player.TWO
        elif self.game.current_player == Player.TWO:
            self.game.player_2_board.spawnShip()
            self.game.current_player = Player.ONE
            self.game.set_state(State.PLAYING)

    def place_ship_instructions(self, surface: pygame.Surface, player: Player): 
        if player == Player.ONE: 
            half_of_player_screen = SCREEN_HEIGHT / 4
            initial_offset = half_of_player_screen - (half_of_player_screen / 2)
        elif player == Player.TWO: 
            half_of_player_screen =  3 * SCREEN_HEIGHT / 4
            initial_offset = half_of_player_screen - (half_of_player_screen / 6)
        
        middle_of_screen = SCREEN_WIDTH // 2

        self.write('Place Your Ships', self.font_sm, Color.BLACK, surface, middle_of_screen, initial_offset, True)
        self.write('——————————', self.font_sm, Color.BLACK, surface, middle_of_screen, initial_offset + 10, True)
        self.write("Use the arrow keys to move the ship", self.font_sm, Color.BLACK, surface, middle_of_screen, initial_offset + 25, True)
        self.write("Use R to rotate the ship", self.font_sm, Color.BLACK, surface, middle_of_screen, initial_offset + 50, True)
        self.write("Press ENTER to confirm ship location", self.font_sm, Color.BLACK, surface, middle_of_screen, initial_offset + 75, True)
