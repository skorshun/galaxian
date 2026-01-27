import pygame

class Ship:
    def __init__(self, game):
        """Init spaceship and setup start position"""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load starship image and get rectangle
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()

        # Show spaceship at the bottom edge of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw spaceship at the current position"""
        self.screen.blit(self.image, self.rect)