from dataclasses import dataclass

DIRECTION_RIGHT = 1 # move to the right
DIRECTION_LEFT = -1 # move to the left

@dataclass
class Settings:
    fullscreen: bool = False
    screen_width: int = 1200
    screen_height: int = 800
    fps: int = 60
    background_color: tuple[int, int, int] = (117, 176, 254)
    ship_speed: float = 1.5
    ships_limit: int = 3

    # Bullet
    bullet_speed: int = 6.0
    bullet_width:int = 3
    bullet_height: int = 15
    bullet_color: tuple[int, int, int] = (60, 60, 60)
    bullets_allowed: int = 6

    # Alien
    alien_speed: float = 1.0
    fleet_drop_speed: int = 10
    fleet_direction: int = DIRECTION_RIGHT