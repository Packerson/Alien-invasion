import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Main class to manage source and game"""

    def __init__(self):
        """initialization game and create source"""
        pygame.init()
        self.settings = Settings()

        """fullscreen mode"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """version with direct resolution"""
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start main game loop"""

        while True:
            """waiting for press key or mouse click"""
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """reaction for even from mouse or keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """reaction for press key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """reaction for release key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """refresh screen during loop iteration"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitime()

        """display last modify screen"""
        pygame.display.flip()


if __name__ == '__main__':
    """creat example of game and start"""
    ai = AlienInvasion()
    ai.run_game()
