from settings import TANK_IMAGE
import pygame


class PlayerTank:

    def __init__(self, x: int, y: int, speed: int) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 'UP'
        self.original_image = pygame.image.load(TANK_IMAGE)
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = 'UP'
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = 'DOWN'
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = 'LEFT'
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = 'RIGHT'

        self.rect.center = (self.x, self.y)

    def rotate(self):
        if self.direction == 'UP':
            self.image = pygame.transform.rotate(self.original_image, 0)
        elif self.direction == 'DOWN':
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif self.direction == 'LEFT':
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif self.direction == 'RIGHT':
            self.image = pygame.transform.rotate(self.original_image, 270)

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

print(TANK_IMAGE)