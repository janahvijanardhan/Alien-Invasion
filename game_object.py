import pygame.image


class GameObject:
    """A class to represent all the game objects."""

    def __init__(self, game_instance, image_path=None, pos_attr=None, pos=None, rect_size=None):
        """Initialize the game objects and set their position."""
        self.screen = game_instance.screen
        self.settings = game_instance.settings

        if image_path:
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
        elif rect_size:
            self.image = None
            width, height = rect_size
            self.rect = pygame.Rect(0, 0, width, height)
        else:
            self.image = None
            self.rect = None

        if self.rect and pos_attr and pos:
            setattr(self.rect, pos_attr, pos)

    def blitme(self):
        """Draw the game object at the current location."""
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            # Draw shape-based objects (will be overridden in subclass)
            pass
