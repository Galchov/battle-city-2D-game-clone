import pygame
from abc import ABC, abstractmethod


class Tank(pygame.sprite.Sprite, ABC):
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, position: tuple, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.position = position    # (x, y)
        self.speed = speed
        self.direction = None

        self.original_image = self.load_image()
        self.image = pygame.transform.scale(self.original_image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect(topleft=position)
        self.old_rect = self.rect.copy()

    @abstractmethod
    def load_image(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def rotate(self) -> None:
        pass

    @abstractmethod
    def collision(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass
