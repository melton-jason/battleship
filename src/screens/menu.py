import pygame

from ._screen import Screen
from src.types import State
from ..config import SCREEN_WIDTH

class MenuScreen(Screen):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.ship_count = None

        button_text_color = (255, 255, 255)
        button_bg_color = (0, 128, 255)
        button_hover_color = (0, 200, 255)

        self.buttons = [
            Button(str(i), (SCREEN_WIDTH // 6) + (i-1) * 60, 225, self.font_sm, button_text_color, button_bg_color, button_hover_color, True)
            for i in range(1, 6)
        ]

        self.start_game_button = Button('PLAY', SCREEN_WIDTH // 2, 400, self.font_md, button_text_color, button_bg_color, button_hover_color, True, False)
        self.selected_ships = None

    def render(self, surface):
        surface.fill((255, 255, 255))
        # Title text
        self.write('BATTLESHIP', self.font_lg, (0, 0, 0), surface, SCREEN_WIDTH // 2, 75, True)
        self.write('——————————', self.font_sm, (0, 0, 0), surface, SCREEN_WIDTH // 2, 125, True)

        # Ship selection text
        self.write('Select the number of ships:', self.font_sm, (0, 0, 0), surface, SCREEN_WIDTH // 2, 175, True)

        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update(mouse_pos)
            button.draw(surface)

        # start game button
        self.start_game_button.update(mouse_pos)
        self.start_game_button.draw(surface)

        pygame.display.flip()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for i, button in enumerate(self.buttons):
                    if button.is_clicked(mouse_pos):
                        if button.is_checked:
                            print("setting num ships to", i + 1)
                            self.selected_ships = i + 1
                            self.game.set_num_ships(i + 1)
                        else:
                            self.selected_ships = None
                            self.game.set_num_ships(None)

                        # Uncheck all other buttons
                        for other_button in self.buttons:
                            if other_button != button:
                                other_button.is_checked = False
                                other_button.current_color = other_button.bg_color
                        break

                if self.start_game_button.is_clicked(mouse_pos):
                    if self.selected_ships is not None:
                        self.game.set_state(State.SELECTION)

class Button:
    def __init__(self, text, x, y, font, text_color, bg_color, hover_color, center=False, square=True):
        self.square = square
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.center = center
        self.current_color = bg_color
        self.clicked_color = (0, 255, 0)  # Green color for clicked state
        self.rect = None
        self.is_checked = False  # New attribute to track checked state

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.text_color)
        if self.rect is None:
            if self.center:
                self.rect = text_surface.get_rect(center=(self.x, self.y))
            else:
                self.rect = text_surface.get_rect(topleft=(self.x, self.y))

            if self.square:
                self.rect.width = self.rect.height = max(self.rect.width + 10, self.rect.height + 10)
            else: self.rect.inflate_ip(75, 10)  # Add some padding

        pygame.draw.rect(surface, self.current_color, self.rect)
        surface.blit(text_surface, text_surface.get_rect(center=self.rect.center))

    def update(self, mouse_pos):
        if self.rect is None:
            return
        if self.rect.collidepoint(mouse_pos):
            if not self.is_checked:
                self.current_color = self.hover_color
        else:
            if not self.is_checked:
                self.current_color = self.bg_color

    def is_clicked(self, mouse_pos):
        if self.rect is None:
            return False
        if self.rect.collidepoint(mouse_pos):
            self.is_checked = not self.is_checked
            self.current_color = self.clicked_color if self.is_checked else self.bg_color
            return True
        return False