import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class representing a single alien."""

    def __init__(self, game):
        """Initializes the alien and sets its starting position."""
        super().__init__()
        self.screen = game.screen

        # Loading the alien image and assigning the rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Maintaining the precise horizontal position of the alien.
        self.x = float(self.rect.x)
