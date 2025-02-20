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

    def move(self) -> None:
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        if self.direction == 'DOWN':
            self.y += self.speed
            if self.y >= 550:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'UP':
            self.y -= self.speed
            if self.y <= 0:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'LEFT':
            self.x -= self.speed
            if self.x <= 0:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'RIGHT':
            self.x += self.speed
            if self.x >= 750:
                self.direction = random.choice(directions)
                self.rotate(self.direction)


    def rotate(self, direction: str) -> None:
        if direction == 'UP':
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif direction == 'DOWN':
            self.image = pygame.transform.rotate(self.original_image, 0)
        elif direction == 'LEFT':
            self.image = pygame.transform.rotate(self.original_image, 270)
        elif direction == 'RIGHT':
            self.image = pygame.transform.rotate(self.original_image, 90)

        # TODO: This scaling to be refactored, so it becomes more memory efficient
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen) -> None:
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