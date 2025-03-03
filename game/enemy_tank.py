import pygame
import random
from settings import BATTLEFIELD_SIZE, ENEMY_TANK_IMAGE

from base_tank import Tank


class EnemyTank(Tank):

    def __init__(self, position: tuple, speed: int) -> None:
        super().__init__(position, speed)
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = 'DOWN'
        self.old_rect = self.rect.copy()

    def load_image(self) -> pygame.image:
        return pygame.image.load(ENEMY_TANK_IMAGE).convert_alpha()

    def move(self, dt) -> None:
        self.old_rect = self.rect.copy()
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        if self.direction == 'DOWN':
            self.position.y += self.speed * dt
            if self.position.y >= BATTLEFIELD_SIZE - 50:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'UP':
            self.position.y -= self.speed * dt
            if self.position.y <= 0:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'LEFT':
            self.position.x -= self.speed * dt
            if self.position.x <= 0:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        elif self.direction == 'RIGHT':
            self.position.x += self.speed * dt
            if self.position.x >= BATTLEFIELD_SIZE - 50:
                self.direction = random.choice(directions)
                self.rotate(self.direction)
        
        self.rect.topleft = round(self.position.x), round(self.position.y)

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

    def collision(self) -> None:
        pass

    def update(self, dt) -> None:
        self.move(dt)
        