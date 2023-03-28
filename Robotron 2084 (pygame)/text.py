import pygame
from config import *


class Text(pygame.sprite.Sprite):
    def __init__(self, text, pos, size):
        super().__init__()
        self.font = pygame.font.Font(UI_FONT, size)
        self.text = text
        self.image = self.font.render(self.text, True, COLORS[0])
        self.color = 0
        self.rect = self.image.get_rect(topleft=pos)

    def set_text(self, text):
        self.text = text

    def update(self):
        self.color += 0.2
        if self.color >= 9:
            self.color = 0
        self.image = self.font.render(self.text, True, COLORS[int(self.color)])
