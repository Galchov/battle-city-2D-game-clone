import pygame
import random


from player_tank_sprite import PlayerTank
from enemy_tank_sprite import EnemyTank


pygame.init()

# Frame rate
clock = pygame.time.Clock()
FPS = 60

# Screen size parameters
WIDTH = 800
HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle City")

player_tank_team = pygame.sprite.Group()
enemy_tanks_team = pygame.sprite.Group()

player_tank = PlayerTank(400, 300, 3)
player_tank_team.add(player_tank)

for _ in range(3):
    x_axis = random.randint(100, 700)
    tank_obj = EnemyTank(x_axis, 400, 1)
    enemy_tanks_team.add(tank_obj)

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("dark grey")

    keys = pygame.key.get_pressed()
    player_tank.update(keys)
    player_tank.rotate()
    player_tank.hit_object(enemy_tanks_team)
    player_tank.draw(screen)

    enemy_tanks_team.update()
    enemy_tanks_team.draw(screen)
    for enemy in enemy_tanks_team:
        pygame.draw.rect(screen, (255, 0, 0), enemy.rect, 2)
        enemy.hit_object(player_tank_team)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()