from dataclasses import dataclass

@dataclass
class Settings:
    fullscreen: bool = False
    screen_width: int = 1200
    screen_height: int = 800
    fps: int = 60
    background_color: tuple[int, int, int] = (117, 176, 254)
    ship_speed: float = 1.5