import pygame
import math

# bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("./assets/ball_green.png")
        self.image = pygame.transform.scale(self.image, (6, 6))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
    
    def update(self):
        self.rect.x += 5
        
    def check_collision(self, obstacle):
        obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
        bullet_rect = pygame.Rect(self.x, self.y, 10, 10)
        return obstacle_rect.colliderect(bullet_rect)
