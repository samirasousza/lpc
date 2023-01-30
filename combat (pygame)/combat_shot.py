import pygame



class Shot(pygame.sprite.Sprite):
    def __init__(self, ball1_1_x, ball_1_y):
        super().__init__()
        self.image = pygame.draw.rect(screen, COLOR_GREEN, (ball1_1_x, ball_1_y, 6, 6))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.x = ball_1_x
        self.rect.y = ball_1_y

    def trajectory(self):
        self.rect.x = slef.rect.x - self.speed


    def colocar(self, superficie):
        superficie.blit(self.image, self.rect)