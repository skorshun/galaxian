import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class Galaxian:
    """Class for managing game resources and behavior"""
    def __init__(self, settings: Settings):
        pygame.init()
        self.settings = settings

        self.clock = pygame.time.Clock()
        if not self.settings.fullscreen:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.fps = self.settings.fps
        self.background_color = self.settings.background_color

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Galaxian")

        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()

    def run_game(self) -> None:
        """Start main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self._update_screen()
            self.clock.tick(self.fps) / 1000.0

    def _check_events(self) -> None:
        """Processes keystrokes and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self) -> None:
        """Updates the images on the screen and displays a new screen."""
        self.screen.fill(self.background_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()

        # Displaying the last screen drawn
        pygame.display.flip()

    def _check_keydown_events(self, event) -> None:
        """Responds to key presses"""
        if event.key == pygame.K_ESCAPE:
            self._quit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        """Responds to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creates a new projectile and adds it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    @staticmethod
    def _quit() -> None:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    galaxian = Galaxian(Settings())
    galaxian.run_game()