import pygame
import random


from player_tank import PlayerTank
from enemy_tank import EnemyTank


pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle City")

tank = PlayerTank(WIDTH // 2, HEIGHT // 2, 4)
enemy_tanks = []

for _ in range(5):
    x = random.randint(1, 800)
    y = random.randint(1, 100)
    enemy_tank = EnemyTank(x, y, 1)
    enemy_tanks.append(enemy_tank)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("dark grey")

    keys = pygame.key.get_pressed()
    tank.move(keys)
    tank.rotate()
    tank.draw(screen)

    for t in enemy_tanks:
        t.move()
        t.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()