import pygame
from config import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, size, spawn):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(COLORS[0])
        self.rect = self.image.get_rect(topleft=spawn)
        self.change_color = 0

    def update(self):
        self.change_color += 0.2
        if self.change_color >= 9:
            self.change_color = 0
        self.image.fill(COLORS[int(self.change_color)])

