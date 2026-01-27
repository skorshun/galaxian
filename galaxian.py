import sys
import pygame

from settings import Settings
from ship import Ship

class Galaxian:
    """Class for managing game resources and behavior"""
    def __init__(self, settings):
        pygame.init()
        self.settings = settings

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        self.fps = self.settings.fps
        self.background_color = self.settings.background_color

        pygame.display.set_caption("Galaxian")

        self.ship = Ship(self.screen)

    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.fps) / 1000.0

    @staticmethod
    def _check_events() -> None:
        """Processes keystrokes and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self) -> None:
        """Updates the images on the screen and displays a new screen."""
        self.screen.fill(self.background_color)
        self.ship.blitme()

        # Displaying the last screen drawn
        pygame.display.flip()

if __name__ == "__main__":
    galaxian = Galaxian(Settings())
    galaxian.run_game()