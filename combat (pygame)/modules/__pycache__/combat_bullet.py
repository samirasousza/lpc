import pygame
import math

# bullet class


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, nball):
        super().__init__()
        self.image = nball
        self.image = pygame.transform.scale(self.image, (6, 6))
        self.rect = self.image.get_rect()
        self.angle = player.angle
        self.pos = pygame.Vector2(player.rect.center)
        self.rect.center = round(self.pos.x), round(self.pos.y)
        self.direction = pygame.Vector2(10, 1).rotate(-self.angle)
        
    def update(self):
        self.pos += self.direction
        self.rect.center = round(self.pos.x), round(self.pos.y)
            
    def border_collision(self):
        if self.rect.left < 25:
            self.direction.x *= -1
            self.rect.left = 25
            return 1
        if self.rect.right > 1025:
            self.direction.x *= -1
            self.rect.right = 1025
            return 1
        if self.rect.top < 125:
            self.direction.y *= -1
            self.rect.top = 125
            return 1
        if self.rect.bottom > 710:
            self.direction.y *= -1
            self.rect.bottom = 710
            return 1

 