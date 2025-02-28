import pygame, sys
from settings import *

from battlefield import Battlefield
from player_tank import PlayerTank
from enemy_tank import EnemyTank


pygame.init()

# Frame rate
clock = pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle City")

battlefield = Battlefield(screen)

player_tank_team = pygame.sprite.Group()
enemy_tanks_team = pygame.sprite.Group()

player_tank = PlayerTank(*PLAYER_SPAWN_POINT, 3)
player_tank_team.add(player_tank)

for i in range(3):
    x, y = ENEMY_SPAWN_POINTS[i]
    tank_obj = EnemyTank(x, y, 1)
    enemy_tanks_team.add(tank_obj)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("dark grey")
    
    battlefield.draw()

    player_tank.update()
    player_tank.rotate()
    player_tank.collision(enemy_tanks_team)
    player_tank.draw(screen)

    for enemy in enemy_tanks_team:
        enemy.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), enemy.rect, 2)
        enemy.update()
        enemy.collision(player_tank_team)

    pygame.display.flip()
    clock.tick(FPS)
