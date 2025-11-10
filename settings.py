class Settings:
    """A class to store all settings for Alien Invasion game."""

    def __init__(self):
        """Initialize the game settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 80)
        self.FPS = 60
        # Spaceship settings
        self.spaceship_speed = 5
        self.spaceship_limit = 3
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        # Alien settings
        self.alien_speed = 0.5
        self.alien_speed_increase_challenge = 2
        self.fleet_drop_speed = 10
        self.fleet_drop_speed_increase_challenge = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
