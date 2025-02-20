import pygame
import sys


from player_tank import PlayerTank
from enemy_tank import EnemyTank


pygame.init()
clock = pygame.time.Clock()


WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle City")

tank = PlayerTank(WIDTH // 2, HEIGHT // 2, 4)
enemy_1 = EnemyTank(100, 100, 2)
enemy_2 = EnemyTank(350, 100, 2)
enemy_3 = EnemyTank(650, 100, 2)

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

    enemy_1.draw(screen)
    enemy_2.draw(screen)
    enemy_3.draw(screen)


    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()
