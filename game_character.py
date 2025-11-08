from game_object import GameObject


class GameCharacter(GameObject):
    """A class representing a funky game character."""

    def __init__(self, game_instance):
        """Initialize game character."""
        super().__init__(
            game_instance,
            pos_attr="center",
            pos=game_instance.screen.get_rect().center,
            image_path="images/universe.png"
        )
