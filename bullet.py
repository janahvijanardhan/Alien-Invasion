import pygame
from pygame.sprite import Sprite

from game_object import GameObject


class Bullet(GameObject, Sprite):
    """A class to manage bullets fired from the spaceship."""

    def __init__(self, game_instance):
        """Initialize GameObject without image path and initialize all bullet specific attributes."""
        GameObject.__init__(
            self,
            game_instance,
            pos_attr="midtop",
            pos=game_instance.spaceship.rect.midtop,
            image_path="images/bullet1.png",
            # rect_size=(game_instance.settings.bullet_width,game_instance.settings.bullet_height)
        )
        Sprite.__init__(self)

        # Bullet specific attributes.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

# def blitme(self):
#     """Draw the bullet to the screen."""
#     pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
