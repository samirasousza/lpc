import pygame
from modules.combat_player import *
from modules.combat_bullet import *
from modules.combat_obs import *
from modules.combat_score import *
import random

rnd_x = random.randint(15, 960)
rnd_y = random.randint(115, 660)

pygame.init()

COLOR_RED = (147, 45, 11)
COLOR_YELLOW = (219, 184, 79)
COLOR_GREEN = (147, 194, 81)
COLOR_PURPLE = (87, 88, 210)
COLOR_WHITE = (225, 225, 225)

# screen size
size = (1050, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Combat - PyGame Edition - 2023-13-01")

# score text player 1
score_1_text = Score(screen)

# score text player 2
score_2_text = Score(screen)

# player 1 (green)
player_1_image = pygame.image.load("assets/player_1.png")
player_1_x = 55
player_1_y = 395
player_1 = Player(player_1_x, player_1_y, player_1_image)

# player 2 (purple)
player_2_image = pygame.image.load("assets/player_2.png")
player_2_x = 935
player_2_y = 395
player_2 = Player(player_2_x, player_2_y, player_2_image)

ball_1_image = pygame.image.load("./assets/ball_green.png")
ball_2_image = pygame.image.load("./assets/ball_purple.png")

bullets = pygame.sprite.Group()

obstacles = [
    pygame.Rect(285, 400, 105, 50), pygame.Rect(660, 400, 105, 50),
    pygame.Rect(500, 545, 50, 105), pygame.Rect(500, 200, 50, 105),
    pygame.Rect(0, 95, 1060, 30), pygame.Rect(0, 720, 1060, 30),
    pygame.Rect(0, 95, 25, 700), pygame.Rect(1025, 95, 25, 700)
    ]

wall_right = [
    pygame.Rect(140, 350, 25, 150), pygame.Rect(115, 350, 25, 25),
    pygame.Rect(115, 475, 25, 25)
    ]

wall_left = [
    pygame.Rect(880, 350, 25, 150), pygame.Rect(905, 350, 25, 25),
    pygame.Rect(905, 475, 25, 25)
    ]


# score
score_1, score_2 = 0, 0
count_1, count_2 = 5, 5

bullet_group_1 = pygame.sprite.Group()
bullet_group_2 = pygame.sprite.Group()


# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            # player_1 controls
            if event.key == pygame.K_d:
                player_1.rotate_left = True
            if event.key == pygame.K_a:
                player_1.rotate_right = True
            if event.key == pygame.K_w:
                player_1.forward = True
            if event.key == pygame.K_c:
                if len(bullet_group_2) < 1:
                    bullet_group_2.add(player_1.create_bullet(ball_1_image))
            # player_2 controls
            if event.key == pygame.K_LEFT:
                player_2.rotate_right = True
            if event.key == pygame.K_RIGHT:
                player_2.rotate_left = True
            if event.key == pygame.K_UP:
                player_2.forward = True
            if event.key == pygame.K_SPACE:
                if len(bullet_group_1) < 1:
                    bullet_group_1.add(player_2.create_bullet(ball_2_image))
        if event.type == pygame.KEYUP:
            # player_1 controls
            if event.key == pygame.K_d:
                player_1.rotate_left = False
            if event.key == pygame.K_a:
                player_1.rotate_right = False
            if event.key == pygame.K_w:
                player_1.forward = False
            # player_2 controls
            if event.key == pygame.K_LEFT:
                player_2.rotate_right = False
            if event.key == pygame.K_RIGHT:
                player_2.rotate_left = False
            if event.key == pygame.K_UP:
                player_2.forward = False

    rnd_x, rnd_y = 0, 0
    # player 1 movement

    player_1.movement()
    player_2.movement()
    
    # screen color
    screen.fill(COLOR_RED)
    
    # draw screen
    screen.blit(player_1.image, player_1.rect)
    screen.blit(player_2.image, player_2.rect)

    for obs in obstacles:
        pygame.draw.rect(screen, COLOR_YELLOW, obs)
        if player_2.rect.colliderect(obs):
            if player_2.rect.left > obs.left:
                player_2.rect.left = obs.right
                player_2.pos = pygame.Vector2(player_2.rect.center)
            elif player_2.rect.right > obs.left:
                player_2.rect.right = obs.left
                player_2.pos = pygame.Vector2(player_2.rect.center)
            elif player_2.rect.right > obs.bottom:
                print(obs.top)
                player_2.rect.right = obs.bottom + 50
                player_2.pos = pygame.Vector2(player_2.rect.center)

        if player_1.rect.colliderect(obs):
            if player_1.rect.right > obs.left:
                player_1.rect.right = obs.left
                player_1.pos = pygame.Vector2(player_1.rect.center)
            elif player_1.rect.left > obs.left:
                player_1.rect.left = obs.right
                player_1.pos = pygame.Vector2(player_1.rect.center)

    for walls in wall_left:
        pygame.draw.rect(screen, COLOR_YELLOW, walls)
        if player_2.rect.colliderect(walls):
            if player_2.rect.left > walls.left:
                player_2.rect.left = walls.right
                player_2.pos = pygame.Vector2(player_2.rect.center)
            elif player_2.rect.right > walls.left:
                player_2.rect.right = walls.left
                player_2.pos = pygame.Vector2(player_2.rect.center)
        if player_1.rect.colliderect(walls):
            if player_1.rect.right > walls.left:
                player_1.rect.right = walls.left
                player_1.pos = pygame.Vector2(player_1.rect.center)
            elif player_1.rect.left > walls.left:
                player_1.rect.left = walls.right
                player_1.pos = pygame.Vector2(player_1.rect.center)
    
    for walls in wall_right:
        pygame.draw.rect(screen, COLOR_YELLOW, walls)
        if player_2.rect.colliderect(walls):
            if player_2.rect.left > walls.left:
                player_2.rect.left = walls.right
                player_2.pos = pygame.Vector2(player_2.rect.center)
            elif player_2.rect.right > walls.left:
                player_2.rect.right = walls.left
                player_2.pos = pygame.Vector2(player_2.rect.center)
        if player_1.rect.colliderect(walls):
            if player_1.rect.right > walls.left:
                player_1.rect.right = walls.left
                player_1.pos = pygame.Vector2(player_1.rect.center)
            elif player_1.rect.left > walls.left:
                player_1.rect.left = walls.right
                player_1.pos = pygame.Vector2(player_1.rect.center)

    score_1_text.scoring(score_1, screen, COLOR_GREEN, 150, 15)
    score_1_text.scoring(score_2, screen,  COLOR_PURPLE, 775, 15)
    bullet_group_1.draw(screen)
    bullet_group_1.update()
    bullet_group_2.draw(screen)
    bullet_group_2.update()
    
    for bullet in bullet_group_1:
        for i in obstacles:
            if bullet.border_collision() == 1:
                count_1 -= 1
            if bullet.rect.colliderect(i):
                count_1 -= 1
                bullet.direction.x *= -1
                bullet.direction.y *= 2/3
            if count_1 == 0:
                count_1 = 5
                bullet.kill()
        for i in wall_left:
            if bullet.rect.colliderect(i):
                bullet.direction.x *= -1
                bullet.direction.y *= -2/3
                if bullet.rect.top >= i.bottom + 50:
                    bullet.direction.x *= -1
                    bullet.direction.y *= 2/3
                    bullet.rect.top = i.bottom + 50
                if bullet.rect.bottom == i.top + 50:
                    bullet.direction.x *= -1
                    bullet.direction.y *= 2/3
                    bullet.rect.bottom = i.top + 50
        for i in wall_right:
            if bullet.rect.colliderect(i):
                bullet.direction.x *= -1
                bullet.direction.y *= -2/3
                if bullet.rect.top >= i.bottom + 50:
                    bullet.direction.x *= -1
                    bullet.direction.y *= 2/3
                    bullet.rect.top = i.bottom + 50
                if bullet.rect.bottom == i.top + 100:
                    bullet.direction.x *= -1
                    bullet.direction.y *= 2/3
                    bullet.rect.bottom = i.top + 50
        collide_2 = pygame.Rect.colliderect(player_1.rect, bullet.rect)
        if collide_2:
            score_2 += 1
            bullet.kill()
            player_1.rect.center = round(rnd_x), round(rnd_y)
            player_1.pos = pygame.Vector2(player_1.rect.center)
             
    for bullet in bullet_group_2:
        for i in obstacles:
            if bullet.border_collision() == 1:
                count_2 -= 1
            if bullet.rect.colliderect(i):
                count_2 -= 1
                bullet.direction.x *= -1
                bullet.direction.y *= -2/3
            if count_2 == 0:
                count_2 = 5
                bullet.kill()
        for i in wall_left:
            if bullet.rect.colliderect(i):
                bullet.direction.x *= -1
                bullet.direction.y *= -2/3
                if bullet.rect.top == i.bottom + 50:
                    bullet.direction.x *= -1
                    bullet.direction.y *= 2/3
                    bullet.rect.top = i.bottom
                if bullet.rect.bottom == i.top + 50:
                    bullet.direction.x *= -1
                    bullet.direction.y *= 2/3
                    bullet.rect.bottom = i.top + 50
        for i in wall_right:
            if bullet.rect.colliderect(i):
                bullet.direction.x *= -1
                bullet.direction.y *= -2/3
                if bullet.rect.top == i.bottom + 50:
                    bullet.direction.y *= -1
                    bullet.rect.top = i.bottom + 50
                    bullet.direction.y *= 2/3
                if bullet.rect.bottom == i.top + 75:
                    bullet.direction.x *= -1
                    bullet.direction.y *= 2/3
                    bullet.rect.bottom = i.top + 50
        collide_1 = pygame.Rect.colliderect(player_2.rect, bullet.rect)
        if collide_1:
            score_1 += 1
            bullet.kill()
            player_2.rect.center = round(rnd_x), round(rnd_y)
            player_2.pos = pygame.Vector2(player_2.rect.center)
    
    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()