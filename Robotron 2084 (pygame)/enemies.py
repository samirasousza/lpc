import pygame
import math
import config_enemies
import random
from config import *


class Red(pygame.sprite.Sprite):
    def __init__(self, path, player, x, y):
        super().__init__()
        self.sprites_red = []

        self.sprites_red.append(pygame.transform.scale(pygame.image.load(path + "1/enemy1.png"), (27, 36)))
        self.sprites_red.append(pygame.transform.scale(pygame.image.load(path + "1/enemy2.png"), (27, 36)))
        self.sprites_red.append(pygame.transform.scale(pygame.image.load(path + "1/enemy3.png"), (27, 36)))

        self.speed = random.randint(1, 2)
        self.player = player
        self.current_sprite = 0
        self.image = self.sprites_red[self.current_sprite]
        self.spawn = (x, y)
        self.rect = self.image.get_rect(center=self.spawn)
        self.current_position = 0
        self.angle = random.randint(-180, 180)
        self.rotation_angle = random.randint(-1, 1)
        self.hits = 0

        # Hit box
        self.hit_box = self.image.get_rect()
        self.hit_box_colour = config_enemies.asteroid_hit_box

    def reset_position(self):
        self.rect.center = self.spawn

    def move(self):

        # calcula a direção para o jogador

        dx = self.player.rect.x - self.rect.centerx
        dy = self.player.rect.y - self.rect.centery
        angle = math.atan2(dy, dx)

        # move o alien em direção ao jogador
        self.rect.centerx += self.speed * math.cos(angle)
        self.rect.centery += self.speed * math.sin(angle)

    def update(self):
        self.move()
        self.current_sprite += 0.1
        if self.current_sprite >= 3:
            self.current_sprite = 0
        self.image = self.sprites_red[int(self.current_sprite)]

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # desenha a imagem do alien na tela

        # Update hit box
        self.hit_box.x = self.rect.x
        self.hit_box.y = self.rect.y
        self.hit_box.width = self.image.get_width()
        self.hit_box.height = self.image.get_height() + 5


class Hulk(pygame.sprite.Sprite):
    def __init__(self, path, targets, spawn):
        super().__init__()
        self.sprites_hulk_front = []
        self.sprites_hulk_back = []
        self.sprites_hulk_right = []
        self.sprites_hulk_left = []

        self.sprites_hulk_front.append(pygame.transform.scale(pygame.image.load(path + "front1.png"), (27, 36)))
        self.sprites_hulk_front.append(pygame.transform.scale(pygame.image.load(path + "front2.png"), (27, 36)))
        self.sprites_hulk_front.append(pygame.transform.scale(pygame.image.load(path + "front3.png"), (27, 36)))
        self.sprites_hulk_front.append(pygame.transform.scale(pygame.image.load(path + "front4.png"), (27, 36)))

        self.sprites_hulk_back.append(pygame.transform.scale(pygame.image.load(path + "front1.png"), (27, 36)))
        self.sprites_hulk_back.append(pygame.transform.scale(pygame.image.load(path + "front2.png"), (27, 36)))
        self.sprites_hulk_back.append(pygame.transform.scale(pygame.image.load(path + "front3.png"), (27, 36)))
        self.sprites_hulk_back.append(pygame.transform.scale(pygame.image.load(path + "front4.png"), (27, 36)))

        self.sprites_hulk_right.append(pygame.transform.scale(pygame.image.load(path + "right1.png"), (27, 36)))
        self.sprites_hulk_right.append(pygame.transform.scale(pygame.image.load(path + "right2.png"), (27, 36)))
        self.sprites_hulk_right.append(pygame.transform.scale(pygame.image.load(path + "right3.png"), (27, 36)))
        self.sprites_hulk_right.append(pygame.transform.scale(pygame.image.load(path + "right4.png"), (27, 36)))

        self.sprites_hulk_left.append(pygame.transform.scale(pygame.image.load(path + "left1.png"), (27, 36)))
        self.sprites_hulk_left.append(pygame.transform.scale(pygame.image.load(path + "left2.png"), (27, 36)))
        self.sprites_hulk_left.append(pygame.transform.scale(pygame.image.load(path + "left3.png"), (27, 36)))
        self.sprites_hulk_left.append(pygame.transform.scale(pygame.image.load(path + "left4.png"), (27, 36)))

        self.speed = hulk_speed
        self.targets = targets
        self.current_sprite = 0
        self.image = self.sprites_hulk_front[self.current_sprite]
        self.spawn = spawn
        self.rect = self.image.get_rect(center=spawn)
        self.angle = random.randint(-180, 180)
        self.rotation_angle = random.randint(-1, 1)
        self.hits = 0
        self.game_area = game_area
        self.walls = []
        self.direction = random.choice(["up", "down", "left", "right"])
        self.direction_time = 0
        self.time_walking = 3000
        self.stop_time = 500
        self.stop = False
        self.stop_instant = 0

        # Hit box
        self.hit_box = self.image.get_rect()
        self.hit_box_colour = config_enemies.asteroid_hit_box

    def reset_position(self):
        self.rect.center = self.spawn

    def set_stop(self):
        self.stop = True
        self.stop_instant = pygame.time.get_ticks()

    def move(self):
        # encontra o npc mais próximo
        distances = [math.hypot(target.rect.x - self.rect.centerx, target.rect.y - self.rect.centery) for target in
                     self.targets.sprites()]
        if len(distances) == 0:
            if pygame.time.get_ticks() - self.direction_time > self.time_walking:
                self.direction_time = pygame.time.get_ticks()
                self.direction = random.choice(["up", "down", "left", "right"])

            if self.direction == "up":
                self.rect.y -= self.speed
            elif self.direction == "down":
                self.rect.y += self.speed
            elif self.direction == "left":
                self.rect.x -= self.speed
            elif self.direction == "right":
                self.rect.x += self.speed

            self.collision(0)
            self.collision(1)

            if self.rect.x > self.game_area[0]:
                self.rect.x = 20
            elif self.rect.x < 0:
                self.rect.x = self.game_area[0] - 10
            elif self.rect.y > self.game_area[1]:
                self.rect.y = self.game_area[1]
            elif self.rect.y < 40:
                self.rect.y = 45

        else:
            closest_target_index = distances.index(min(distances))
            closest_target = self.targets.sprites()[closest_target_index]

            # calcula a direção para o npc mais próximo
            dx = closest_target.rect.x - self.rect.centerx
            dy = closest_target.rect.y - self.rect.centery
            angle = math.atan2(dy, dx)

            # move o alien em direção ao npc mais próximo
            self.rect.centerx += self.speed * math.cos(angle)
            self.rect.centery += self.speed * math.sin(angle)

            self.collision(0)
            self.collision(1)

    def collision(self, orient):
        if orient == 0:
            for sprite in self.walls:
                if sprite.rect.colliderect(self.rect):
                    if self.direction == "right":  # Going right
                        self.rect.right = sprite.rect.left
                    if self.direction == "left":  # Going left
                        self.rect.left = sprite.rect.right

        else:
            if orient == 1:
                for sprite in self.walls:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction == "down":  # Going down
                            self.rect.bottom = sprite.rect.top
                        if self.direction == "up":  # Going up
                            self.rect.top = sprite.rect.bottom

        for human in self.targets:
            if human.rect.colliderect(self.rect):
                human.set_death()

    def update(self):
        # chama o método move
        if not self.stop:
            self.move()
        else:
            if pygame.time.get_ticks() - self.stop_instant > self.stop_time:
                self.stop = False
        self.current_sprite += 0.3
        if self.current_sprite >= 3:
            self.current_sprite = 0

        if self.direction == "up":
            self.image = self.sprites_hulk_front[int(self.current_sprite)]
        elif self.direction == "down":
            self.image = self.sprites_hulk_front[int(self.current_sprite)]
        elif self.direction == "left":
            self.image = self.sprites_hulk_left[int(self.current_sprite)]
        elif self.direction == "right":
            self.image = self.sprites_hulk_right[int(self.current_sprite)]
