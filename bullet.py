import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for controlling projectiles launched by a ship."""

    def __init__(self, game):
        """Creates a projectile object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Creating a projectile at position (0,0) and assigning the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Moves the projectile up the screen."""
        # Updating the exact position of the projectile.
        self.y -= self.settings.bullet_speed
        # Updating the position of the rectangle.
        self.rect.y = self.y

    def draw(self):
        """Displays the projectile on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)