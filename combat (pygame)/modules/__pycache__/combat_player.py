import pygame
import math
from .combat_bullet import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, n_player):
        super().__init__()
        self.image = n_player
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.rotate = self.image
        self.angle = 0
        self.pos = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2(0, 0).rotate(-self.angle)
        self.rotate_left = False
        self.rotate_right = False
        self.forward = False
        
    def movement(self):
        if self.rotate_right: 
            self.image = pygame.transform.rotate(self.rotate, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
            self.angle += 5
        else:
            self.rect.y += 0
        if self.rotate_left:
            self.image = pygame.transform.rotate(self.rotate, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
            self.angle -= 5
        else:
            self.rect.y += 0
        if self.forward:
            self.pos += 3/2*self.direction
            self.rect.center = round(self.pos[0]), round(self.pos[1])
        else:
            self.rect.x += 0
        
        # player collides with upper and lower wall
        if self.rect.y <= 115:
            self.rect.y = 115
        elif self.rect.y >= 660:
            self.rect.y = 660

        # player collides with side walls
        if self.rect.x <= 15:
            self.rect.x = 15
        elif self.rect.x >= 960:
            self.rect.x = 960
    
    def create_bullet(self, nball):
        return Bullet(self, nball)

    def wall_col(self, obstacle, x_pos, y_pos):
        collide = pygame.Rect.colli(self.rect, obstacle)
        