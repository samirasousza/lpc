import pygame
from projectile import Projectile
from math import sin
from config import player_speed


class Player(pygame.sprite.Sprite):
    def __init__(self, path, spawn):
        super().__init__()
        self.sprites_front = []
        self.sprites_back = []
        self.sprites_right = []
        self.sprites_left = []

        self.sprites_front.append(pygame.transform.scale(pygame.image.load(path + "front/front1.png"), (21, 33)))
        self.sprites_front.append(pygame.transform.scale(pygame.image.load(path + "front/front2.png"), (21, 33)))
        self.sprites_front.append(pygame.transform.scale(pygame.image.load(path + "front/front3.png"), (21, 33)))

        self.sprites_back.append(pygame.transform.scale(pygame.image.load(path + "back/back1.png"), (21, 33)))
        self.sprites_back.append(pygame.transform.scale(pygame.image.load(path + "back/back2.png"), (21, 33)))
        self.sprites_back.append(pygame.transform.scale(pygame.image.load(path + "back/back3.png"), (21, 33)))

        self.sprites_right.append(pygame.transform.scale(pygame.image.load(path + "right/right1.png"), (21, 33)))
        self.sprites_right.append(pygame.transform.scale(pygame.image.load(path + "right/right2.png"), (21, 33)))
        self.sprites_right.append(pygame.transform.scale(pygame.image.load(path + "right/right3.png"), (21, 33)))

        self.sprites_left.append(pygame.transform.scale(pygame.image.load(path + "left/left1.png"), (21, 33)))
        self.sprites_left.append(pygame.transform.scale(pygame.image.load(path + "left/left2.png"), (21, 33)))
        self.sprites_left.append(pygame.transform.scale(pygame.image.load(path + "left/left3.png"), (21, 33)))

        self.lost_life_image = pygame.transform.scale(pygame.image.load(path + "life_icon.png"), (21, 33))

        self.shot_sound = pygame.mixer.Sound("assets/sounds/laser.wav")
        self.one_up_sound = pygame.mixer.Sound("assets/sounds/one_up.wav")
        self.collect_sound = pygame.mixer.Sound("assets/sounds/collect.wav")
        self.kill_robot_sound = pygame.mixer.Sound("assets/sounds/kill_robot.mp3")

        self.current_sprite = 0
        self.sprite_state = 2
        self.image = self.sprites_right[self.current_sprite]
        self.spawn = spawn
        self.rect = self.image.get_rect(center=self.spawn)
        self.moving_x = False
        self.moving_y = False
        self.direction = pygame.math.Vector2()
        self.speed = player_speed
        self.fire = False
        self.reloading = False
        self.vulnerable = True
        self.vulnerable_cooldown = 3000
        self.vulnerable_time = 0
        self.can_shoot = False
        self.reload_cooldown = 150
        self.reload_time = 0
        self.bullets = pygame.sprite.Group()
        self.lives = 5
        self.lives_gain = 0
        self.gain_lives_check = 0
        self.points = 0
        self.orientation = (0, 0)
        self.reset_check = False
        self.walls = []
        self.humans = []
        self.humans_collected = 0
        self.enemies_red = []
        self.enemies_green = []
        self.hazards = []
        self.wave = 0

    def get_image(self):
        return self.image

    def get_spawn(self):
        return self.spawn

    def get_speed(self):
        return self.direction

    def get_fire(self):
        return self.fire

    def get_reloading(self):
        return self.reloading

    def get_reload_time(self):
        return self.reload_time

    def get_bullets(self):
        return self.bullets

    def get_lives(self):
        return self.lives

    def get_points(self):
        return self.points

    def get_rect(self):
        return self.rect

    def set_image(self, asset):
        self.image = asset

    def set_spawn(self, spawn):
        self.spawn = spawn

    def set_speed(self, speed):
        self.direction = speed

    def reset_speed(self):
        self.direction = pygame.math.Vector2()

    def set_reloading(self, reloading):
        self.reloading = reloading

    def set_reload_time(self, reload_time):
        self.reload_time = reload_time

    def add_bullet(self, projectile):
        self.bullets.add(projectile)

    def remove_bullet(self, projectile):
        self.bullets.remove(projectile)

    def set_lives(self, lives):
        self.lives = lives

    def set_points(self, points):
        self.points = points

    def set_rect(self, rect):
        self.rect = rect

    def set_rect_topleft(self, x, y):
        self.rect.topleft = (x, y)

    def set_direction_x(self, x):
        self.direction.x = x

    def set_direction_y(self, y):
        self.direction.y = y

    def set_orientation(self, orientation):
        self.orientation = orientation

    def set_walls(self, walls):
        self.walls = walls

    def set_humans(self, humans):
        self.humans = humans

    def set_enemies_red(self, enemies):
        self.enemies_red = enemies

    def set_enemies_green(self, enemies):
        self.enemies_green = enemies

    def set_can_shoot(self):
        self.can_shoot = True

    def set_hazards(self, hazards):
        self.hazards = hazards

    def set_movement(self, joy):
        self.direction.y = joy.get_axis(1)
        if abs(joy.get_axis(1)) < 0.3:
            self.direction.y = 0
            self.moving_y = False
        if self.direction.y > 0:
            self.sprite_state = 4
            self.moving_y = True
        elif self.direction.y < 0:
            self.sprite_state = 1
            self.moving_y = True

        self.direction.x = joy.get_axis(0)
        if abs(joy.get_axis(0)) < 0.3:
            self.direction.x = 0
            self.moving_x = False
        if self.direction.x > 0:
            self.sprite_state = 2
            self.moving_x = True
        elif self.direction.x < 0:
            self.sprite_state = 3
            self.moving_x = True

    def reset_position(self):
        self.rect.center = self.spawn

    def lost_life(self):
        self.moving_x = False
        self.moving_y = False
        self.image = self.lost_life_image
        self.lives -= 1

    def next_wave(self):
        self.wave += 1

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x = self.rect.x + self.direction.x * speed
        self.collision(0)
        self.rect.y = self.rect.y + self.direction.y * speed
        self.collision(1)

    def update(self):
        if self.points - self.gain_lives_check > 25000:
            self.lives += 1
            self.one_up_sound.play()
            self.lives_gain += 1
            self.gain_lives_check = 25000*self.lives_gain
        self.move(self.speed)
        if self.moving_x or self.moving_y:
            self.current_sprite += 0.25
            if self.current_sprite >= 3:
                self.current_sprite = 0
            if self.sprite_state == 1:
                self.image = self.sprites_back[int(self.current_sprite)]
            elif self.sprite_state == 2:
                self.image = self.sprites_right[int(self.current_sprite)]
            elif self.sprite_state == 3:
                self.image = self.sprites_left[int(self.current_sprite)]
            elif self.sprite_state == 4:
                self.image = self.sprites_front[int(self.current_sprite)]

    def collision(self, orient):
        if not self.vulnerable and pygame.time.get_ticks() - self.vulnerable_time >= self.vulnerable_cooldown:
            self.vulnerable = True
        if orient == 0:
            for sprite in self.walls:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # Going right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # Going left
                        self.rect.left = sprite.rect.right

        if orient == 1:
            for sprite in self.walls:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # Going down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # Going up
                        self.rect.top = sprite.rect.bottom

        for human in self.humans:
            if human.rect.colliderect(self.rect):
                human.kill()
                self.collect_sound.play()
                if self.humans_collected < 5:
                    self.humans_collected += 1
                self.points += 1000 * self.humans_collected

        for enemy in self.enemies_red:
            collide = pygame.sprite.spritecollide(enemy, self.bullets, True)
            if collide:
                self.kill_robot_sound.play()
                self.points += 100
                enemy.kill()

        for enemy in self.enemies_green:
            collide = pygame.sprite.spritecollide(enemy, self.bullets, True)
            if collide:
                enemy.set_stop()

        for obstacle in self.hazards:
            collide = pygame.sprite.spritecollide(obstacle, self.bullets, True)
            if collide:
                obstacle.kill()

    @staticmethod
    def wave_value():
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

    def shoot(self, joy):
        self.orientation = (round(joy.get_axis(2)), (-1*round(joy.get_axis(3))))
        print(self.orientation)
        if self.lives > 0:
            if self.orientation == (0, 1):
                bullet = Projectile(
                    pygame.transform.rotate(pygame.image.load("assets/projectile.png"), 90),
                    self.orientation, self.rect.midtop[0], self.rect.midtop[1], self.walls)
                self.bullets.add(bullet)
            elif self.orientation == (0, -1):
                bullet = Projectile(
                    pygame.transform.rotate(pygame.image.load("assets/projectile.png"), 90),
                    self.orientation, self.rect.midbottom[0], self.rect.midbottom[1], self.walls)
                self.bullets.add(bullet)
            elif self.orientation == (1, 1):
                bullet = Projectile(
                    pygame.transform.rotate(pygame.image.load("assets/projectile.png"), 45),
                    self.orientation, self.rect.topright[0], self.rect.topright[1], self.walls)
                self.bullets.add(bullet)
            elif self.orientation == (-1, 1):
                bullet = Projectile(
                    pygame.transform.rotate(pygame.image.load("assets/projectile.png"), 135),
                    self.orientation, self.rect.topleft[0], self.rect.topleft[1], self.walls)
                self.bullets.add(bullet)
            elif self.orientation == (1, 0):
                bullet = Projectile(
                    pygame.image.load("assets/projectile.png"),
                    self.orientation, self.rect.midright[0], self.rect.midright[1], self.walls)
                self.bullets.add(bullet)
            elif self.orientation == (-1, 0):
                bullet = Projectile(
                    pygame.image.load("assets/projectile.png"),
                    self.orientation, self.rect.midleft[0], self.rect.midleft[1], self.walls)
                self.bullets.add(bullet)
            elif self.orientation == (1, -1):
                bullet = Projectile(
                    pygame.transform.rotate(pygame.image.load("assets/projectile.png"), 135),
                    self.orientation, self.rect.bottomright[0], self.rect.bottomright[1], self.walls)
                self.bullets.add(bullet)
            elif self.orientation == (-1, -1):
                bullet = Projectile(
                    pygame.transform.rotate(pygame.image.load("assets/projectile.png"), 45),
                    self.orientation, self.rect.bottomleft[0], self.rect.bottomleft[1], self.walls)
                self.bullets.add(bullet)

    def set_fire(self, joy):
        if (abs(joy.get_axis(2)) > 0.2 or abs(joy.get_axis(3)) > 0.2) and not self.reloading and self.can_shoot:
            self.shot_sound.play()
            self.shoot(joy)
            self.reloading = True
            self.reload_time = pygame.time.get_ticks()
        elif self.reloading:
            if pygame.time.get_ticks() - self.reload_time >= self.reload_cooldown:
                self.reloading = False

    def reset_for_wave(self):
        self.bullets.empty()
        self.humans_collected = 0
        self.can_shoot = False
        self.rect.center = self.spawn
