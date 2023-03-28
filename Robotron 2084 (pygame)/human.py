import pygame
import random
from config import *


class HumanMark(pygame.sprite.Sprite):

    def __init__(self, path, x, y):
        super().__init__()
        self.game_area = game_area
        self.sprites_front_mark = []
        self.sprites_back_mark = []
        self.sprites_right_mark = []
        self.sprites_left_mark = []

        self.sprites_front_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_front1.png"), (21, 33)))
        self.sprites_front_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_front2.png"), (21, 33)))
        self.sprites_front_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_front3.png"), (21, 33)))

        self.sprites_back_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_back1.png"), (21, 33)))
        self.sprites_back_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_back2.png"), (21, 33)))
        self.sprites_back_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_back3.png"), (21, 33)))

        self.sprites_right_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_right1.png"), (21, 33)))
        self.sprites_right_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_right2.png"), (21, 33)))
        self.sprites_right_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_right3.png"), (21, 33)))

        self.sprites_left_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_left1.png"), (21, 33)))
        self.sprites_left_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_left2.png"), (21, 33)))
        self.sprites_left_mark.append(pygame.transform.scale(pygame.image.load(path + "1/mark_left3.png"), (21, 33)))

        self.death_pic = pygame.transform.scale(pygame.image.load(path + "death.png"), (21, 33))

        self.speed = human_speed
        self.angle = random.randint(0, 360)
        self.image = self.sprites_front_mark[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.hits = 0
        self.direction = random.choice(["up", "down", "left", "right"])
        self.direction_time = 0
        self.time_walking = 3000
        self.animation_count = 0
        self.walls = []
        self.death = False
        self.time_death = 0
        self.screen_time = 2000

        # Hit box
        self.hit_box = self.image.get_rect()
        self.hit_box_colour = (255, 0, 0)

    def set_walls(self, walls):
        self.walls = walls

    def set_death(self):
        self.death = True

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

    def move(self):
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

    def update(self):
        if not self.death:
            self.time_death = pygame.time.get_ticks()
            self.move()
            self.animation_count += 0.3
            if self.animation_count >= 3:
                self.animation_count = 0

            if self.direction == "up":
                self.image = self.sprites_back_mark[int(self.animation_count)]
            elif self.direction == "down":
                self.image = self.sprites_front_mark[int(self.animation_count)]
            elif self.direction == "left":
                self.image = self.sprites_left_mark[int(self.animation_count)]
            elif self.direction == "right":
                self.image = self.sprites_right_mark[int(self.animation_count)]
        else:
            self.image = self.death_pic
            if pygame.time.get_ticks() - self.time_death > self.screen_time:
                self.kill()


class HumanStacy(pygame.sprite.Sprite):

    def __init__(self, path, x, y):
        super().__init__()
        self.screen_size = screen_size
        self.sprites_front_stacy = []
        self.sprites_back_stacy = []
        self.sprites_right_stacy = []
        self.sprites_left_stacy = []

        self.sprites_front_stacy.append(
            pygame.transform.scale(pygame.image.load(path + "2/stacy_front1.png"), (21, 33)))
        self.sprites_front_stacy.append(
            pygame.transform.scale(pygame.image.load(path + "2/stacy_front2.png"), (21, 33)))
        self.sprites_front_stacy.append(
            pygame.transform.scale(pygame.image.load(path + "2/stacy_front3.png"), (21, 33)))

        self.sprites_back_stacy.append(pygame.transform.scale(pygame.image.load(path + "2/stacy_back1.png"), (21, 33)))
        self.sprites_back_stacy.append(pygame.transform.scale(pygame.image.load(path + "2/stacy_back2.png"), (21, 33)))
        self.sprites_back_stacy.append(pygame.transform.scale(pygame.image.load(path + "2/stacy_back3.png"), (21, 33)))

        self.sprites_right_stacy.append(
            pygame.transform.scale(pygame.image.load(path + "2/stacy_right1.png"), (21, 33)))
        self.sprites_right_stacy.append(
            pygame.transform.scale(pygame.image.load(path + "2/stacy_right2.png"), (21, 33)))
        self.sprites_right_stacy.append(
            pygame.transform.scale(pygame.image.load(path + "2/stacy_right3.png"), (21, 33)))

        self.sprites_left_stacy.append(pygame.transform.scale(pygame.image.load(path + "2/stacy_left1.png"), (21, 33)))
        self.sprites_left_stacy.append(pygame.transform.scale(pygame.image.load(path + "2/stacy_left2.png"), (21, 33)))
        self.sprites_left_stacy.append(pygame.transform.scale(pygame.image.load(path + "2/stacy_left3.png"), (21, 33)))

        self.death_pic = pygame.transform.scale(pygame.image.load(path + "death.png"), (21, 33))

        self.speed = human_speed
        self.angle = random.randint(0, 360)
        self.image = self.sprites_front_stacy[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.hits = 0
        self.direction = random.choice(["up", "down", "left", "right"])
        self.direction_time = 0
        self.time_walking = 3000
        self.animation_count = 0
        self.walls = []
        self.death = False
        self.game_area = game_area
        self.time_death = 0
        self.screen_time = 2000

        # Hit box
        self.hit_box = self.image.get_rect()
        self.hit_box_colour = (255, 0, 0)

    def set_walls(self, walls):
        self.walls = walls

    def set_death(self):
        self.death = True

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

    def move(self):
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

    def update(self):
        if not self.death:
            self.time_death = pygame.time.get_ticks()
            self.move()
            self.animation_count += 0.3
            if self.animation_count >= 3:
                self.animation_count = 0

            if self.direction == "up":
                self.image = self.sprites_back_stacy[int(self.animation_count)]
            elif self.direction == "down":
                self.image = self.sprites_front_stacy[int(self.animation_count)]
            elif self.direction == "left":
                self.image = self.sprites_left_stacy[int(self.animation_count)]
            elif self.direction == "right":
                self.image = self.sprites_right_stacy[int(self.animation_count)]
        else:
            self.image = self.death_pic
            if pygame.time.get_ticks() - self.time_death > self.screen_time:
                self.kill()


class HumanTimmy(pygame.sprite.Sprite):
    def __init__(self, path, x, y):
        super().__init__()
        self.screen_size = screen_size
        self.sprites_front_timmy = []
        self.sprites_back_timmy = []
        self.sprites_right_timmy = []
        self.sprites_left_timmy = []

        self.sprites_front_timmy.append(
            pygame.transform.scale(pygame.image.load(path + "3/timmy_front1.png"), (21, 33)))
        self.sprites_front_timmy.append(
            pygame.transform.scale(pygame.image.load(path + "3/timmy_front2.png"), (21, 33)))
        self.sprites_front_timmy.append(
            pygame.transform.scale(pygame.image.load(path + "3/timmy_front3.png"), (21, 33)))

        self.sprites_back_timmy.append(pygame.transform.scale(pygame.image.load(path + "3/timmy_back1.png"), (21, 33)))
        self.sprites_back_timmy.append(pygame.transform.scale(pygame.image.load(path + "3/timmy_back2.png"), (21, 33)))
        self.sprites_back_timmy.append(pygame.transform.scale(pygame.image.load(path + "3/timmy_back3.png"), (21, 33)))

        self.sprites_right_timmy.append(
            pygame.transform.scale(pygame.image.load(path + "3/timmy_right1.png"), (21, 33)))
        self.sprites_right_timmy.append(
            pygame.transform.scale(pygame.image.load(path + "3/timmy_right2.png"), (21, 33)))
        self.sprites_right_timmy.append(
            pygame.transform.scale(pygame.image.load(path + "3/timmy_right3.png"), (21, 33)))

        self.sprites_left_timmy.append(pygame.transform.scale(pygame.image.load(path + "3/timmy_left1.png"), (21, 33)))
        self.sprites_left_timmy.append(pygame.transform.scale(pygame.image.load(path + "3/timmy_left2.png"), (21, 33)))
        self.sprites_left_timmy.append(pygame.transform.scale(pygame.image.load(path + "3/timmy_left3.png"), (21, 33)))

        self.death_pic = pygame.transform.scale(pygame.image.load(path + "death.png"), (21, 33))

        self.speed = human_speed
        self.angle = random.randint(0, 360)
        self.image = self.sprites_front_timmy[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.hits = 0
        self.direction = random.choice(["up", "down", "left", "right"])
        self.direction_time = 0
        self.time_walking = 3000
        self.animation_count = 0
        self.walls = []
        self.death = False
        self.game_area = game_area
        self.time_death = 0
        self.screen_time = 2000

        # Hit box
        self.hit_box = self.image.get_rect()
        self.hit_box_colour = (255, 0, 0)

    def set_walls(self, walls):
        self.walls = walls

    def set_death(self):
        self.death = True

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

    def move(self):
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

    def update(self):
        if not self.death:
            self.time_death = pygame.time.get_ticks()
            self.move()
            self.animation_count += 0.3
            if self.animation_count >= 3:
                self.animation_count = 0

            if self.direction == "up":
                self.image = self.sprites_back_timmy[int(self.animation_count)]
            elif self.direction == "down":
                self.image = self.sprites_front_timmy[int(self.animation_count)]
            elif self.direction == "left":
                self.image = self.sprites_left_timmy[int(self.animation_count)]
            elif self.direction == "right":
                self.image = self.sprites_right_timmy[int(self.animation_count)]
        else:
            self.image = self.death_pic
            if pygame.time.get_ticks() - self.time_death > self.screen_time:
                self.kill()
