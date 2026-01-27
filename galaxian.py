import sys
import pygame

from settings import Settings

class Galaxian:
    """Class for managing game resources and behavior"""

    def __init__(self, settings):
        pygame.init()
        self.settings = settings

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.fps = self.settings.fps
        self.background_color = self.settings.background_color

        pygame.display.set_caption("Galaxian")

    def run_game(self):
        """Start main game loop"""

        while True:
            self.clock.tick(self.fps) / 1000.0

            # Listen keyboard & mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.background_color)

            # Displaying the last screen drawn
            pygame.display.flip()

if __name__ == "__main__":
    galaxian = Galaxian(Settings())
    galaxian.run_game()