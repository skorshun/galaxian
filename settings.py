from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    screen_width: int = 1200
    screen_height: int = 800
    fps: int = 60
    background_color: tuple[int, int, int] = (230, 230, 230)