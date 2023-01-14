import pygame

pygame.init()

COLOR_RED = (147, 45, 11)
COLOR_YELLOW = (219, 184, 79)
COLOR_GREEN = (147, 194, 81)
COLOR_PURPLE = (87, 88, 210)
COLOR_WHITE = (225, 225, 225)

# screen
size = (1050, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Combat - PyGame Edition - 2023-13-01")

# score text player 1
score_1_font = pygame.font.Font('assets/PressStart2P.ttf', 80)
score_1_text = score_1_font.render('0', True, COLOR_GREEN, COLOR_RED)
score_1_text_rect = score_1_text.get_rect()
score_1_text_rect.center = (275, 48)

# score text player 2
score_2_font = pygame.font.Font('assets/PressStart2P.ttf', 80)
score_2_text = score_2_font.render('0', True, COLOR_PURPLE, COLOR_RED)
score_2_text_rect = score_2_text.get_rect()
score_2_text_rect.center = (775, 48)

# sound effects
#bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
#scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1 (green)
player_1 = pygame.image.load("assets/player_1.png")
player_1_size = (60, 60)
player_1 = pygame.transform.scale(player_1, player_1_size)
player_1_x = 55
player_1_y = 395
player_1_move_up = False
player_1_move_down = False

# player 2 (purple)
player_2 = pygame.image.load("assets/player_2.png")
player_2_size = (60, 60)
player_2 = pygame.transform.scale(player_2, player_2_size)
player_2 = pygame.transform.rotate(player_2, 180)
player_2_x = 935
player_2_y = 395
player_2_move_up = False
player_2_move_down = False

# ball 1
ball_1 = pygame.image.load("assets/ball_green.png")
ball_size = (6, 6)
ball_1 = pygame.transform.scale(ball_1, ball_size)
ball_1_x = 60
ball_1_y = 180
ball_1_dx = 1
ball_1_dy = 1

# ball 2
ball_2 = pygame.image.load("assets/ball_purple.png")
ball_size = (6, 6)
ball_2 = pygame.transform.scale(ball_2, ball_size)
ball_2_x = 1000
ball_2_y = 180
ball_2_dx = 1
ball_2_dy = 1


# barrier
def obstacle(pos, size):
    obstacle = pygame.image.load("assets/obstacle.png")
    obstacle_pos = pos
    obstacle_size = size
    obstacle = pygame.transform.scale(obstacle, obstacle_size)

    return obstacle


# border up
border_up_pos = (0, 95)
border_up_size = (1060, 30)
border_up = obstacle(border_up_pos, border_up_size)

# border down
border_down_pos = (0, 725)
border_down_size = (1060, 25)
border_down = obstacle(border_down_pos, border_down_size)

# border right
border_right_pos = (1025, 95)
border_right_size = (25, 700)
border_right = obstacle(border_right_pos, border_right_size)

# border left
border_left_pos = (0, 95)
border_left_size = (25, 700)
border_left = obstacle(border_left_pos, border_left_size)

# obstacle up
obstacle_up_pos = (500, 205)
obstacle_up_size = (50, 105)
obstacle_up = obstacle(obstacle_up_pos, obstacle_up_size)

# obstacle down
obstacle_down_pos = (500, 540)
obstacle_down_size = (50, 105)
obstacle_down = obstacle(obstacle_down_pos, obstacle_down_size)

# obstacle right
obstacle_right_pos = (660, 400)
obstacle_right_size = (105, 50)
obstacle_right = obstacle(obstacle_right_pos, obstacle_right_size)

# obstacle left
obstacle_left_pos = (285, 400)
obstacle_left_size = (105, 50)
obstacle_left = obstacle(obstacle_left_pos, obstacle_left_size)

# wall right
wall_right = pygame.image.load("assets/wall.png")
wall_right_pos = (815, 325)
wall_right_size = (200, 200)
wall_right = pygame.transform.scale(wall_right, wall_right_size)
wall_right = pygame.transform.rotate(wall_right, 180)

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # screen
    screen.fill(COLOR_RED)

    # draw initial obstacle
    pygame.draw.rect(screen, COLOR_YELLOW, (140, 350, 25, 150))
    pygame.draw.rect(screen, COLOR_YELLOW, (115, 350, 25, 25))
    pygame.draw.rect(screen, COLOR_YELLOW, (115, 475, 25, 25))

    # mostrar na tela
    screen.blit(ball_1, (ball_1_x, ball_1_y))
    screen.blit(ball_2, (ball_2_x, ball_2_y))

    screen.blit(player_1, (player_1_x, player_1_y))
    screen.blit(player_2, (player_2_x, player_2_y))

    screen.blit(score_1_text, score_1_text_rect)
    screen.blit(score_2_text, score_2_text_rect)

    screen.blit(border_up, border_up_pos)
    screen.blit(border_down, border_down_pos)
    screen.blit(border_left, border_left_pos)
    screen.blit(border_right, border_right_pos)

    screen.blit(obstacle_up, obstacle_up_pos)
    screen.blit(obstacle_down, obstacle_down_pos)
    screen.blit(obstacle_left, obstacle_left_pos)
    screen.blit(obstacle_right, obstacle_right_pos)

    screen.blit(wall_right, wall_right_pos)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
