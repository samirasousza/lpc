import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("assets/obstacle.png")
        self.rect = self.image.get_rect()
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center = (self.rect.x, self.rect.y))
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.pos = pos
        

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("assets/wall.png")
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]