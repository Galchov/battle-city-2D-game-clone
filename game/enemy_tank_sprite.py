import pygame
import random


from settings import enemy_tank_image


class EnemyTank(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed

        self.direction = 'DOWN'
        self.original_image = pygame.image.load(enemy_tank_image)
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.hitbox = (self.x - 1, self.y - 1, 52, 52)

    def update(self) -> None:
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
        
        self.rect.topleft = (self.x, self.y)


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
