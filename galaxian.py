import sys
import pygame

WIDTH, HEIGHT = 1200, 800
FPS = 60

class Galaxian:
    """Class for managing game resources and behavior"""

    def __init__(self, width: int, height: int, fps: int):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.fps = fps

        pygame.display.set_caption("Galaxian")

    def run_game(self):
        """Start main game loop"""

        while True:
            self.clock.tick(self.fps) / 1000.0

            # Listen keyboard & mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Displaying the last screen drawn
            pygame.display.flip()

if __name__ == "__main__":
    ai = Galaxian(WIDTH, HEIGHT, FPS)
    ai.run_game()