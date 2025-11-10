from pygame.sprite import Sprite

from game_object import GameObject


class Alien(GameObject, Sprite):
    """A class representing Aliens."""

    def __init__(self, game_instance):
        """Initialize and set the alien's position."""
        GameObject.__init__(
            self,
            game_instance,
            image_path="images/alien-ship.png"
        )
        Sprite.__init__(self)

        # Start each new alien near the topleft of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the alien's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at either right or left edge of the screen."""
        return (self.rect.right >= self.screen.get_rect().right) or (self.rect.left <= 0)

    def update(self):
        """Update the alien's position."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)
