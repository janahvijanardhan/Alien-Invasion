class GameStats:
    """"""

    def __init__(self, game_instance):
        """"""

        self.settings = game_instance.settings
        self.reset_stats()

    def reset_stats(self):
        """"""
        self.spaceships_left = self.settings.spaceship_limit