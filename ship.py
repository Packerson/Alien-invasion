import pygame


class Ship:
    """in this class will be everthing about ship"""

    def __init__(self, ai_game):
        """initial spaceship and his base position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # upload space image
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # every new spaceship shows on the bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # spaceship postions is in float
        self.x = float(self.rect.x)

        # moving x
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """changing spaceship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # actualization object rect base on self.x
        self.rect.x = self.x

    def blitime(self):
        # showing spaceship in his actual position
        self.screen.blit(self.image, self.rect)
