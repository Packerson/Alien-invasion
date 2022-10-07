import pygame.draw


class Settings():
    """class for all settings in game"""

    def __init__(self):
        """initialization game settings"""

        """screen settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1.5

        """bullet settings"""
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100, 100, 100)
        """max bullets on screen"""
        self.bullets_allowed = 5


