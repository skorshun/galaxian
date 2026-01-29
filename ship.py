import pygame

from settings import Settings


class Ship:
    def __init__(self, game):
        """Init spaceship and setup start position"""

        self.screen = game
        self.settings = Settings()
        self.screen_rect = self.screen.get_rect()

        # Load starship image and get rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Show spaceship at the bottom edge of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Save float coordinates center of ship
        self.x: float = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self) -> None:
        """Draw spaceship at the current position"""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """Update position regarding moving_right flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
