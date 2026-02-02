import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self) -> None:
        """Start main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._check_fleet_edges()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(self.fps) / 1000.0

    def _check_events(self) -> None:
        """Processes keystrokes and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
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
        self.aliens.draw(self.screen)

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
        #  Limiting the number of projectiles per group.
        #  That is, only a certain number of shells can be on the screen at a time.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates projectile positions and destroys old projectiles."""
        self.bullets.update()
        # remove projectile objects that have left the work surface
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Handles collisions between projectiles and aliens."""
        #Removal of projectiles and aliens involved in collisions.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Updates the positions of all newcomers in the fleet."""
        self.aliens.update()

    def _create_fleet(self):
        """Creates a fleet of aliens."""
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x)
            current_x += 2 * alien_width

    def _check_fleet_edges(self):
        """Reacts when the visitor reaches the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """It lowers the entire fleet and changes its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, x_position):
        """Creates an alien and places it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    @staticmethod
    def _quit() -> None:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    galaxian = Galaxian(Settings())
    galaxian.run_game()