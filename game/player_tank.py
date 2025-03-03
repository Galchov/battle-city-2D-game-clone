import pygame
from settings import BATTLEFIELD_SIZE, PLAYER_TANK_IMAGE

from base_tank import Tank


class PlayerTank(Tank):

    def __init__(self, position: tuple, speed: int) -> None:
        super().__init__(position, speed)
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = 'UP'
        self.old_rect = self.rect.copy()

    def load_image(self) -> pygame.image:
        return pygame.image.load(PLAYER_TANK_IMAGE).convert_alpha()
    
    def move(self, dt) -> None:
        self.old_rect = self.rect.copy()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.position.y -= self.speed * dt
            self.direction = 'UP'
        elif keys[pygame.K_DOWN]:
            self.position.y += self.speed * dt
            self.direction = 'DOWN'
        elif keys[pygame.K_LEFT]:
            self.position.x -= self.speed * dt
            self.direction = 'LEFT'
        elif keys[pygame.K_RIGHT]:
            self.position.x += self.speed * dt
            self.direction = 'RIGHT'

        self.position.x = max(0, min(self.position.x, BATTLEFIELD_SIZE - 50))
        self.position.y = max(0, min(self.position.y, BATTLEFIELD_SIZE - 50))

        self.rect.topleft = round(self.position.x), round(self.position.y)

    def rotate(self) -> None:
        if self.direction == 'UP':
            self.image = pygame.transform.rotate(self.original_image, 0)
        elif self.direction == 'DOWN':
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif self.direction == 'LEFT':
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif self.direction == 'RIGHT':
            self.image = pygame.transform.rotate(self.original_image, 270)

        # TODO: This scaling to be refactored, so it becomes more memory efficient
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(center=self.rect.center)

    def collision(self) -> None:
        pass

    def update(self, dt) -> None:
        self.move(dt)
        self.rotate()
        self.collision()
