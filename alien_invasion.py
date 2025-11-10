import sys
import pygame

from time import sleep
from alien import Alien
from bullet import Bullet
from gamestats import GameStats
from settings import Settings
from spaceship import Spaceship
from game_character import GameCharacter


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.game_active = True
        self.hit_status = False

        self._create_objects()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.spaceship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _create_objects(self):
        """Create game objects."""
        self.stats = GameStats(self)
        self.spaceship = Spaceship(self)
        self.game_character = GameCharacter(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _check_events(self):
        """Helper method to track all input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of the bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Check if the bullet and alien game elements have collided."""
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self._update_challenge()

    def _update_challenge(self):
        """Update game's challenge levels after each fleet of alien is shot."""
        if not self.hit_status:
            self.settings.fleet_drop_speed += self.settings.fleet_drop_speed_increase_challenge
            self.settings.alien_speed += self.settings.alien_speed_increase_challenge

    def _create_fleet(self):
        """Create a fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 5 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # Update x and y positions of the alien for subsequent rows.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x, y):
        """Helper class to create alien fleet."""
        new_alien = Alien(self)
        new_alien.rect.x = x
        new_alien.rect.y = y
        new_alien.x = x
        new_alien.y = y
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien ship collision.
        if pygame.sprite.spritecollideany(self.spaceship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop entire fleet and change its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """"""

        if self.stats.spaceships_left > 0:
            self.stats.spaceships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self.spaceship.center_ship()
            sleep(1)
            self.hit_status = True
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                self.hit_status = True
                break

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.game_character.blitme()
        self.bullets.draw(self.screen)
        self.spaceship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
