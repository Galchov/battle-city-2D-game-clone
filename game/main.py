import pygame, sys, time
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

all_sprites = pygame.sprite.Group()

player_tank = PlayerTank(*PLAYER_SPAWN_POINT, 3)
all_sprites.add(player_tank)

for i in range(3):
    x, y = ENEMY_SPAWN_POINTS[i]
    tank_obj = EnemyTank(x, y, 1)
    all_sprites.add(tank_obj)

prev_time = time.time()

while True:
    dt = time.time() - prev_time
    prev_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("dark grey")
    
    battlefield.draw()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

# TODO 1: Implement deltatime
# TODO 2: Refactor the Player and Enemy tanks classes
# TODO 3: Merge all solid objects into one sprite group
# TODO 4: Implement collision detection and effects
