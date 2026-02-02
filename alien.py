import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class representing a single alien."""
    def __init__(self, game):
        """Initializes the alien and sets its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Loading the alien image and assigning the rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Maintaining the precise horizontal position of the alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
