import random
import pygame
from human import HumanMark, HumanStacy, HumanTimmy
from player import Player
from enemies import Red, Hulk
from config import *
from wall import Wall
from text import Text
from electrodes import Electrode

pygame.init()
pygame.joystick.init()
Joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print(Joysticks)

# clock
clock = pygame.time.Clock()

# extra sounds
transition_sound = pygame.mixer.Sound("assets/sounds/transition.mp3")
lost_life_sound = pygame.mixer.Sound("assets/sounds/lost_life.wav")

# screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Robotron 2084")

# players
hero1 = Player("assets/player/", human_spawn)
player_group = pygame.sprite.Group()
player_group.add(hero1)

# hud
points_text = Text(str(hero1.get_points()), POINTS_TEXT_POSITION, UI_FONT_SIZE)
life_image = pygame.transform.scale(pygame.image.load("assets/player/life_icon.png"), (21, 36))
life_image_rect = life_image.get_rect(topleft=(1230, 5))
life_text = Text(str(hero1.get_lives()), (life_image_rect.right, 22), 15)
wave_text = Text(("Wave " + str(hero1.wave)), (590, 5), 15)
text_group = pygame.sprite.Group()
text_group.add(points_text)
text_group.add(life_text)
text_group.add(wave_text)

# game over
game_over_text = Text("GAME OVER", (465, screen_size[1]/2), 40)
game_over_sound = pygame.mixer.Sound("assets/sounds/game_over.wav")
game_over_text_group = pygame.sprite.Group()
game_over_text_group.add(game_over_text)

# layout
wall_group = pygame.sprite.Group()
wall_group.add(Wall((1280, 10), (0, 40)))
wall_group.add(Wall((1280, 10), (0, 710)))
wall_group.add(Wall((10, 680), (0, 40)))
wall_group.add(Wall((10, 680), (1270, 40)))
hero1.set_walls(wall_group)

# background
background = pygame.image.load("assets/background.png")

# humans
humans = pygame.sprite.Group()

# enemies
enemy_red_group = pygame.sprite.Group()
enemy_green_group = pygame.sprite.Group()

# obstacles
obstacle_group = pygame.sprite.Group()

# time between waves
wait_mark = 0


def construct_wave(number):
    # creating humans
    humans_number = random.randint(1, 5) + number
    if humans_number > 10:
        humans_number = 10
    for i in range(humans_number):
        x = random.randint(20, 1250)
        while abs(x - hero1.rect.x) < 23:
            x = random.randint(20, 1250)
        y = random.randint(45, 660)
        while abs(y - hero1.rect.x) < 34:
            y = random.randint(45, 660)
        human_type = random.randint(1, 3)
        if human_type == 1:
            human = HumanMark("assets/cit/", x, y)
        elif human_type == 2:
            human = HumanStacy("assets/cit/", x, y)
        else:
            human = HumanTimmy("assets/cit/", x, y)
        human.set_walls(wall_group)
        humans.add(human)
    hero1.set_humans(humans)

    enemy_green_group.empty()
    for i in range(humans_number + 1):
        x = random.randint(20, 1250)
        while abs(x - hero1.rect.x) < 23:
            x = random.randint(20, 1250)
        y = random.randint(45, 660)
        while abs(y - hero1.rect.x) < 34:
            y = random.randint(45, 660)
        enemy_green = Hulk("assets/inimigos/2/", humans, (x, y))
        enemy_green_group.add(enemy_green)
    hero1.set_enemies_green(enemy_green_group)

    enemy_red_number = 9 + (number*2)
    if enemy_red_number > 30:
        enemy_red_number = 30
    for i in range(enemy_red_number):
        x = random.randint(20, 1250)
        while abs(x - hero1.rect.x) < 40:
            x += 10
        y = random.randint(60, 660)
        while abs(y - hero1.rect.x) < 60:
            y += 10
        enemy = Red("assets/inimigos/", hero1, x, y)
        enemy_red_group.add(enemy)
    hero1.set_enemies_red(enemy_red_group)

    obstacle_group.empty()
    obstacles = random.randint(number, number*2)
    typ = random.choice(["square", "stair", "checker", "spark"])
    if obstacles > 30:
        obstacles = 30
    for i in range(obstacles):
        x = random.randint(20, 1250)
        while abs(x - hero1.rect.x) < 40:
            x += 10
        y = random.randint(60, 660)
        while abs(y - hero1.rect.x) < 60:
            y += 10
        electrode = Electrode("assets/inimigos/9/", (x, y), typ)
        obstacle_group.add(electrode)
    hero1.set_hazards(obstacle_group)


def show_everything():
    # Showing everything
    pygame.display.flip()
    screen.blit(background, (0, 0))
    screen.blit(life_image, life_image_rect)
    wall_group.draw(screen)
    obstacle_group.draw(screen)
    enemy_red_group.draw(screen)
    enemy_green_group.draw(screen)
    player_group.draw(screen)
    humans.draw(screen)
    hero1.get_bullets().draw(screen)
    text_group.draw(screen)


def update_everything():
    # Updating everything
    player_group.update()
    humans.update()
    wall_group.update()
    enemy_red_group.update()
    enemy_green_group.update()
    obstacle_group.update()
    points_text.set_text(str(hero1.get_points()))
    life_text.set_text(str(hero1.get_lives()))
    wave_text.set_text(("Wave " + str(hero1.wave)))
    text_group.update()


loop = True


def game_over():
    pygame.display.flip()
    screen.blit(background, (0, 0))
    game_over_text_group.draw(screen)
    game_over_text_group.update()


def next_wave():
    humans.empty()
    hero1.reset_for_wave()


def do_respawn():
    hero1.reset_position()
    hero1.reset_for_wave()
    for enemy in enemy_red_group:
        enemy.reset_position()
    for enemy in enemy_green_group:
        enemy.reset_position()


run = False
respawn = False
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            # movement
            if event.key == pygame.K_w:
                hero1.set_direction_y(-1)
            if event.key == pygame.K_s:
                hero1.set_direction_y(1)
            if event.key == pygame.K_d:
                hero1.set_direction_x(1)
            if event.key == pygame.K_a:
                hero1.set_direction_x(-1)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero1.set_direction_y(0)
            if event.key == pygame.K_s:
                hero1.set_direction_y(0)
            if event.key == pygame.K_d:
                hero1.set_direction_x(0)
            if event.key == pygame.K_a:
                hero1.set_direction_x(0)

    # Movement Keys
    if len(Joysticks) != 0:
        hero1.set_movement(Joysticks[0])
        hero1.set_fire(Joysticks[0])

    if run and not respawn:
        if len(enemy_red_group) == 0:
            transition_sound.play()
            hero1.next_wave()
            run = False
            wait_mark = pygame.time.get_ticks()
        if hero1.get_lives() <= 0:
            game_over_sound.play()
            game_over()
            run = False
        collide_enemy = pygame.sprite.spritecollide(hero1, enemy_red_group, False)
        collide_obstacle = pygame.sprite.spritecollide(hero1, obstacle_group, False)
        if collide_enemy or collide_obstacle:
            lost_life_sound.play()
            hero1.lost_life()
            wait_mark = pygame.time.get_ticks()
            respawn = True

        # Moving the objects
        for bullet in hero1.get_bullets():
            bullet.move()

        # Showing everything
        show_everything()

        # Updating everything
        update_everything()

    elif len(enemy_red_group) != 0 and respawn:
        if len(enemy_red_group) != 0:
            do_respawn()
            show_everything()
            wait = pygame.time.get_ticks()
            if wait - wait_mark > 4000:
                respawn = False
                hero1.set_can_shoot()

    elif hero1.lives <= 0:
        game_over()

    else:
        if len(enemy_red_group) != 0:
            show_everything()
            wait = pygame.time.get_ticks()
            if wait - wait_mark > 4000:
                text_group.draw(screen)
                run = True
                hero1.set_can_shoot()

        else:
            next_wave()
            construct_wave(hero1.wave)

    clock.tick(60)
