import pygame
import os

# Asteroids
asteroid_spawn_min = 800
asteroid_spawn_max = 1200
asteroid_max_speed = 10
asteroid_min_speed = 5
a = 1/2
life_1 = 3
life_2 = 6
life_3 = 9
a1_1 = (life_1, (40*a, 33*a), os.path.join('sprites', 'asteroid_s1.png'))
a1_2 = (life_1, (46*a, 39*a), os.path.join('sprites', 'asteroid_s2.png'))
a1_3 = (life_1, (44*a, 46*a), os.path.join('sprites', 'asteroid_s3.png'))
a1_4 = (life_1, (31*a, 30*a), os.path.join('sprites', 'asteroid_s4.png'))
a1_5 = (life_1, (30*a, 39*a), os.path.join('sprites', 'asteroid_s5.png'))
a2_1 = (life_2, (84*a, 80*a), os.path.join('sprites', 'asteroid_m1.png'))
a2_2 = (life_2, (80*a, 64*a), os.path.join('sprites', 'asteroid_m2.png'))
a2_3 = (life_2, (62*a, 53*a), os.path.join('sprites', 'asteroid_m3.png'))
a3_1 = (life_3, (148*a, 103*a), os.path.join('sprites', 'asteroid_l1.png'))
a3_2 = (life_3, (117*a, 121*a), os.path.join('sprites', 'asteroid_l2.png'))
a3_3 = (life_3, (128*a, 120*a), os.path.join('sprites', 'asteroid_l3.png'))
asteroids_list = [a1_1, a1_2, a1_3, a1_4, a1_5, a2_1, a2_2, a2_3, a3_1, a3_2, a3_3]
asteroid_hit_box = (0, 255, 0)
ps = 1/4
planet = ((506*ps, 525*ps), os.path.join('sprites', 'asteroid_l2.png'))

# Aliens
alien_spawn_max = 8000
alien_spawn_min = 4000
alien_max_speed = 3
alien_min_speed = 2
life_4 = 6
life_5 = 7
alien_1 = (life_4, (102*a, 74*a), os.path.join('sprites', 'enemy1.png'))
alien_2 = (life_5, (86*a, 49*a), os.path.join('sprites', 'enemy2.png'))
alien_3 = (life_5, (86*a, 49*a), os.path.join('sprites', 'enemy3.png'))
aliens_list = [alien_1, alien_2, alien_3]
alien_hit_box = (0, 255, 0)
center = (1280 / 2, 720 / 2)
x = (1280)
y = (720)

#humanos