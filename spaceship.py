from game_object import GameObject


class Spaceship(GameObject):
    """A class representing a Spaceship."""

    def __init__(self, game_instance):
        """Initialize Spaceship."""
        super().__init__(
            game_instance,
            pos_attr="midbottom",
            pos=game_instance.screen.get_rect().midbottom,
            image_path="images/space-ship.png"
        )
        # Movement flags specific to spaceship.
        # Start with a ship that is not moving.
        self.moving_right = False
        self.moving_left = False
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.settings.spaceship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed

        # Update rect object from self.x
        self.rect.x = int(self.x)

    def center_ship(self):
        """"""
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.x = float(self.rect.x)
