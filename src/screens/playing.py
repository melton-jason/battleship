import pygame

from ._screen import Screen
from ..types import Color, Player, State
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE
from ..cell import cell_width


class PlayingScreen(Screen):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)

    def render(self, surface):
        surface.fill(Color.WHITE)

        # Add 1/3 cell worth of space in between the two boards for greater visual distinction
        third_cell = (cell_width(SCREEN_HEIGHT/2, GRID_SIZE) / 3)

        pygame.draw.rect(surface, Color.PLAYER_1_BOARD_COLOR,
                         (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT / 2))
        pygame.draw.rect(surface, Color.PLAYER_2_BOARD_COLOR, (0, (SCREEN_HEIGHT / 2) +
                         third_cell, SCREEN_WIDTH, (SCREEN_HEIGHT / 2) + third_cell))

        if self.game.current_player == Player.ONE:
            self.game.player_1_board.draw(surface)
            self.game.player_2_board.draw(surface, False)
        elif self.game.current_player == Player.TWO:
            self.game.player_1_board.draw(surface, False)
            self.game.player_2_board.draw(surface)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if self.game.current_player == Player.ONE:
                    hit = self.game.player_2_board.hit_pos(mouse_pos)
                elif self.game.current_player == Player.TWO:
                    hit = self.game.player_1_board.hit_pos(mouse_pos)

                if hit:
                    self.game.set_state(State.TURN_TRANSITION)
