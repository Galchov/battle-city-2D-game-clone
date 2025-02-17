import pygame
import random

from player_tank import PlayerTank


pygame.init()

SCREEN_SIZE = WIDTH, HEIGHT = 1024, 786
FPS = 60
YELLOW = (255,255, 0)

# Set screen parameters
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Battle City")

all_tanks_list = pygame.sprite.Group()

# Initialize player's tank object
player_tank = PlayerTank(YELLOW, 50, 50)
# Set its position on the map
player_tank.rect.x = 10
player_tank.rect.y = 10

clock = pygame.time.Clock()
running = True

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("dark grey")

    ### Game functionality ###

    all_tanks_list.add(player_tank)
    # fill the screen with a color to wipe away anything from last frame
    all_tanks_list.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
