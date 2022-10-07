import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """class for manage bullets from spaceship"""

    def __init__(self, ai_game):
        """creating bullet object on actual spaceship positions"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """creating rectangle bullet in (0,0) position, next define positions for it"""
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        """bullet position is define by float"""
        self.y = float(self.rect.y)

    def update(self):
        """moving bullet on screen"""
        """actualization bullet position"""
        self.y -= self.settings.bullet_speed

        """actualization bullet rectangle position"""
        self.rect.y = self.y

    def draw_bullet(self):
        """showing bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
