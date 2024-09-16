import sys
import pygame

from .config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

from .board import Board
from .cell import cell_width
from .types import State, Player

from .screens.menu import MenuScreen
from .screens.playing import PlayingScreen
from .screens.finish import FinishScreen
from .screens.selection import SelectionScreen

HALF_HEIGHT = SCREEN_HEIGHT / 2

class Game:
    def __init__(self, clock, surface: pygame.Surface, grid_size: int) -> None:
        self._running = True
        self.clock = clock
        self.num_ships = 1

        self.current_player = Player.ONE

        self.surface = surface
        self.player_1_board = None
        self.player_2_board = None

        self.winner = None
        self.game_over = False

        self.message = None

        self.state = State.START
        self.screens = {
            State.START: MenuScreen(self),
            State.SELECTION: SelectionScreen(self),
            State.PLAYING: PlayingScreen(self),
            State.END: FinishScreen(self, self.winner),
        }

        # self.hit_sound = pygame.mixer.Sound("sound/hit.mp3")
        # self.miss_sound = pygame.mixer.Sound("sound/miss.mp3")
        # self.sink_sound = pygame.mixer.Sound("sound/sink.mp3")

    def set_state(self, new_state):
        # paint over the screen
        self.state = new_state

    def set_num_ships(self, num_ships):
        print("set num ships: ", num_ships)
        self.num_ships = num_ships
        print(self.num_ships)

        third_cell = (cell_width(HALF_HEIGHT, GRID_SIZE) / 3)

        self.player_1_board = Board(y_offset=HALF_HEIGHT + third_cell, width=SCREEN_WIDTH, height=HALF_HEIGHT - third_cell, board_size=GRID_SIZE, ship_size=self.num_ships)
        self.player_2_board = Board(y_offset=0, width=SCREEN_WIDTH, height=HALF_HEIGHT, board_size=GRID_SIZE, ship_size=self.num_ships)

    def run(self):
        while self._running:
            if self.game_over:
                self.state = State.END
                while self.game_over:
                    print("game over")
                    events = pygame.event.get()
                    print(events)
                    self.screens[self.state].render(self.surface)
                    self.screens[self.state].handle_events(events)
                    self.screens[self.state].update()
                    pygame.display.update()
                    self.clock.tick(FPS)

                    result = self.screens[self.state].handle_events(events)
                    if result == 'restart':
                        self.reset_game()
                        break
                    elif result is None:
                        continue

            events = pygame.event.get()
            self.screens[self.state].render(self.surface)
            self.screens[self.state].handle_events(events)
            self.screens[self.state].update()

            self.handle_global_events(events)
            self.handle_global_update()

            if self.player_1_board != None and self.player_2_board != None:
                self.check_end_game()


    def handle_global_events(self, events):
        """
        Handles catching and processing events which happen each frame: i.e., game logic
        """
        for event in events:
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                sys.exit()

    def handle_global_update(self):
        """
        Handles advancing the game state
        """
        pygame.display.update()
        self.clock.tick(FPS)

    def check_end_game(self):
        """
        Check if the game has ended and set the winner.
        """
        if self.player_1_board.all_ships_sunk():
            self.game_over = True
            self.winner = Player.TWO
            # Update the FinishScreen instance in self.screens
            self.screens[State.END] = FinishScreen(self, 2)
        elif self.player_2_board.all_ships_sunk():
            self.game_over = True
            self.winner = Player.ONE
            # Update the FinishScreen instance in self.screens
            self.screens[State.END] = FinishScreen(self, 1)

    def reset_game(self):
        self.game_over = False
        self.winner = None
        self.set_state(State.START)  # Reset to the starting state
        self.set_num_ships(self.num_ships)  # Reinitialize ship count and other game components