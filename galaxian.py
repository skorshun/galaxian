import sys
import pygame

class Galaxian:
    """Class for managing game resources and behavior"""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Galaxian")

    def run_game(self):
        """Start main game loop"""

        while True:
            # Listen keyboard & mouse events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Displaying the last screen drawn
            pygame.display.flip()

if __name__ == "__main__":
    ai = Galaxian()
    ai.run_game()