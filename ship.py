import pygame

class Ship:
    def __init__(self, game):
        """Init spaceship and setup start position"""

        self.screen = game
        self.screen_rect = self.screen.get_rect()

        # Load starship image and get rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Show spaceship at the bottom edge of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self) -> None:
        """Draw spaceship at the current position"""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """Update position regarding moving_right flag"""
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1