import pygame

from settings import WALL


class Obstacle(pygame.sprite.Sprite):
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, position: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.position = position

        self.original_image = self.load_image()
        self.image = pygame.transform.scale(self.original_image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect(topleft=position)
        self.old_rect = self.rect.copy()

    def load_image(self) -> pygame.image:
        return pygame.image.load(WALL).convert_alpha()
