class GameStats:
    """Tracks statistics for the game "Galaxian"."""

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initializes statistics that change during gameplay."""
        self.ships_left = self.settings.ships_limit