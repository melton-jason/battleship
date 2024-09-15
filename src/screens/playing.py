import pygame
from ._screen import Screen
from ..types import Color, Player
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE
from ..cell import cell_width

class PlayingScreen(Screen):
    def __init__(self, game) -> None:
        super().__init__(game)


    def render(self, surface):
        third_cell = (cell_width(SCREEN_HEIGHT/2, GRID_SIZE) / 3)

        pygame.draw.rect(surface, Color.ATTACK_BOARD_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT / 2))
        pygame.draw.rect(surface, Color.DEFENSE_BOARD_COLOR, (0, (SCREEN_HEIGHT / 2) + third_cell, SCREEN_WIDTH, (SCREEN_HEIGHT / 2) + third_cell))

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
                    self.game.player_2_board.hit_pos(mouse_pos)
                elif self.game.current_player == Player.TWO:
                    self.game.player_1_board.hit_pos(mouse_pos)