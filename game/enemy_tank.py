import pygame
import random


from settings import ENEMY_TANK_IMAGE_3


class EnemyTank:
    hitbox_window = pygame.display.set_mode((50, 50))

    def __init__(self, x: int, y: int, speed: int) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 'DOWN'
        self.original_image = pygame.image.load(ENEMY_TANK_IMAGE_3)
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hitbox = (self.x - 1, self.y - 1, 52, 52)

    def move(self):
        pass

    def draw(self, screen):
        self.hitbox = (self.x - 1, self.y - 1, 52, 52)
        pygame.draw.rect(self.hitbox_window, (255, 0, 0), self.hitbox, 1)

        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= 750:
            self.x = 750
        if self.y >= 550:
            self.y = 550

        screen.blit(self.image, (self.x, self.y))