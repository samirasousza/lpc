import pygame.sprite
import random
from tank import Tank
from config import *


class Game:
    def __init__(self, screen, layout):
        self.screen = screen
        self.layout = layout
        self.background = layout.get_bg_color()
        self.walls = layout.get_group()
        self.tank_sprites = pygame.sprite.Group()
        self.coord = [[400, 275], [40, 120], [730, 120], [730, 400]]
        self.tanks = [Tank(tank_1, 40, 280, 0), Tank(tank_2, 730, 280, 8)]
        self.tank_sprites.add(self.tanks)
        self.hit_timer = 0
        self.victory_can_play = True
        self.score_text_1 = score_font.render(f'{self.tanks[0].score}', True, GREEN)
        self.score_text_2 = score_font.render(f'{self.tanks[1].score}', True, BLUE)
        self.score_text_1_rect = (screen_width / 4, -15)
        self.score_text_2_rect = (screen_width - screen_width / 4, -15)
        self.victory_text1 = victory_font.render('VICTORY PLAYER 1', True, GREEN)
        self.victory_text2 = victory_font.render('VICTORY PLAYER 2', True, BLUE)
        self.victory_text_rect = (screen_width / 9, screen_height / 3)
        pass

    # Check if an event happens
    def check_events(self):
        clk.tick(60)
        if self.hit_timer > 0:
            self.hit_timer -= 1
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.tanks[0].rotate(rot_speed)
                if event.key == pygame.K_d:
                    self.tanks[0].rotate(-rot_speed)
                if event.key == pygame.K_w:
                    self.tanks[0].move_w()
                if event.key == pygame.K_e:
                    self.tanks[0].shoot_()
                if event.key == pygame.K_k:
                    self.tanks[1].shoot_()
                if event.key == pygame.K_LEFT:
                    self.tanks[1].rotate(rot_speed)
                if event.key == pygame.K_RIGHT:
                    self.tanks[1].rotate(-rot_speed)
                if event.key == pygame.K_UP:
                    self.tanks[1].move_w()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.tanks[0].no_rot()
                if event.key == pygame.K_d:
                    self.tanks[0].no_rot()
                if event.key == pygame.K_w:
                    self.tanks[0].no_move_w()
                if event.key == pygame.K_LEFT:
                    self.tanks[1].no_rot()
                if event.key == pygame.K_RIGHT:
                    self.tanks[1].no_rot()
                if event.key == pygame.K_UP:
                    self.tanks[1].no_move_w()

    def game_loop(self):
        self.get_screen()
        while True:
            self.shoot_collision(self.tanks[0], self.tanks[1])
            self.shoot_collision(self.tanks[1], self.tanks[0])
            for tank in self.tanks:
                self.tank_collision(tank)
                for ball in tank.ball_list:
                    self.ball_collision(ball)
                if self.hit_timer <= 0:
                    if tank.stop or tank.hit:
                        choice = random.choice(self.coord)
                        self.coord.remove(choice)
                        tank.reposition(choice)
            self.check_events()
            self.draw_sprites()
            self.check_winner(self.tanks[0], self.tanks[1])
            pygame.display.update()
            clk.tick(fps)

    # Select Layout
    def get_screen(self):
        self.background = self.layout.get_bg_color()
        self.walls = self.layout.get_group()

    # Draws Elements
    def draw_sprites(self):
        self.screen.fill(self.background)
        self.tank_sprites.draw(self.screen)
        self.tank_sprites.update()
        self.walls.draw(self.screen)
        self.tanks[0].ball_sprites.draw(self.screen)
        self.tanks[0].ball_sprites.update()
        self.tanks[1].ball_sprites.draw(self.screen)
        self.tanks[1].ball_sprites.update()

    # tank wall collision
    def tank_collision(self, tank):
        for wall in self.walls:
            if pygame.sprite.collide_mask(tank, wall):
                # collision with top side of the wall
                if abs(tank.rect.top - wall.rect.bottom) < 25:
                    tank.y += tank_speed
                # collision with bottom side of the wall
                elif abs(wall.rect.top - tank.rect.bottom) < 25:
                    tank.y -= tank_speed
                # collision with the left side of the wall
                elif abs(wall.rect.left - tank.rect.right) < 25:
                    tank.x -= tank_speed
                # collision with the right side of the wall
                elif abs(tank.rect.left - wall.rect.right) < 25:
                    tank.x += tank_speed

    # ball and wall collision
    def ball_collision(self, ball):
        for wall in self.walls:
            if pygame.sprite.collide_mask(ball, wall):
                # collision with top side of the wall
                if abs(ball.rect.top - wall.rect.bottom) < 25 and ball.dy < 0:
                    ball.dy *= -1
                # collision with bottom side of the wall
                elif abs(wall.rect.top - ball.rect.bottom) < 25 and ball.dy > 0:
                    ball.dy *= -1
                # collision with the left side of the wall
                elif abs(wall.rect.left - ball.rect.right) < 25 and ball.dx > 0:
                    ball.dx *= -1
                # collision with the right side of the wall
                elif abs(ball.rect.left - wall.rect.right) < 25 and ball.dx < 0:
                    ball.dx *= -1
                ball.cont += 1

    # ball collision with tank
    def shoot_collision(self, tank_one, tank_two):
        if tank_two.stop:
            return
        for ball in tank_two.ball_list:
            if pygame.sprite.collide_mask(ball, tank_one):
                tank_one.ball_list.clear()
                tank_two.ball_list.clear()
                tank_one.ball_sprites.empty()
                tank_two.ball_sprites.empty()
                self.hit_timer = defeat_time
                self.coord = [[400, 275], [40, 120], [730, 120], [730, 400]]
                tank_one.hit = True
                tank_two.stop = True
                tank_two.score += 1
                vine_boom_sound_effect.play()

    def check_winner(self, tank_one, tank_two):
        if tank_one.score < max_score and tank_two.score < max_score:
            self.score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
            self.score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
            self.screen.blit(self.score_text_1, self.score_text_1_rect)
            self.screen.blit(self.score_text_2, self.score_text_2_rect)
        else:
            if self.hit_timer > 0:
                score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
                score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
                self.screen.blit(score_text_1, self.score_text_1_rect)
                self.screen.blit(score_text_2, self.score_text_2_rect)
                return

            if tank_two.score < tank_one.score:
                self.screen.fill(DARKER_GREEN)
                self.score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
                self.screen.blit(self.victory_text1, self.victory_text_rect)
                if self.victory_can_play:
                    yippeee_sound_effect.play(-1)
                self.victory_can_play = False

            elif tank_one.score < tank_two.score:
                self.screen.fill(DARKER_BLUE)
                self.score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
                self.screen.blit(self.victory_text2, self.victory_text_rect)
                if self.victory_can_play:
                    yippeee_sound_effect.play(-1)
                self.victory_can_play = False