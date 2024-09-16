import pygame

from ._screen import Screen
from ..types import Color, Player, State
from ..config import SCREEN_WIDTH, SCREEN_HEIGHT
from ..audio import Audio

TURN_TRANSITION_EVENT = pygame.USEREVENT + 1

class PlayingScreen(Screen):
    def __init__(self, game: "Game") -> None:
        super().__init__(game)
        self.TURN_TRANSITION_DELAY = 1000  # 1 second delay

    def render(self, surface):
        surface.fill(Color.BACKGROUND)

        # Create overlay if it doesn't exist
        if not hasattr(self, 'overlay'):
            self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT // 2), pygame.SRCALPHA)
            self.overlay.fill((0, 0, 0, 100))  # Semi-transparent red

        if self.game.current_player == Player.ONE:
            self.game.player_1_board.draw(surface)
            self.game.player_2_board.draw(surface, False)
            # Apply overlay to bottom half (Player 2's board)
            surface.blit(self.overlay, (0, SCREEN_HEIGHT // 2))
        elif self.game.current_player == Player.TWO:
            self.game.player_1_board.draw(surface, False)
            self.game.player_2_board.draw(surface)
            # Apply overlay to top half (Player 1's board)
            surface.blit(self.overlay, (0, 0))

        # Draw a line to separate the boards
        # pygame.draw.line(surface, Color.WHITE, (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2), 6)


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if self.game.current_player == Player.ONE:
                    hit = self.game.player_2_board.hit_pos(mouse_pos)
                elif self.game.current_player == Player.TWO:
                    hit = self.game.player_1_board.hit_pos(mouse_pos)

                if hit:
                    # Set a timer for turn transition
                    pygame.time.set_timer(TURN_TRANSITION_EVENT, self.TURN_TRANSITION_DELAY, loops=1)

            elif event.type == TURN_TRANSITION_EVENT:
                # This event will be triggered after the delay
                self.game.set_state(State.TURN_TRANSITION)