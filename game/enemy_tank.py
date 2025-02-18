import pygame


class EnemyTank(pygame.sprite.Sprite):

    def __init__(self, color: str, width: int, height: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
