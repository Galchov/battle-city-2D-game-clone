import pygame
import sys


from player_tank import PlayerTank


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle City")
clock = pygame.time.Clock()

tank = PlayerTank(WIDTH // 2, HEIGHT // 2, 5)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    tank.move(keys)
    tank.rotate()

    screen.fill("dark grey")

    tank.draw(screen)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()
