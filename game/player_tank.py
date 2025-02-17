import pygame


class PlayerTank(pygame.sprite.Sprite):

    def __init__(self, color: str, width: int, height: int) -> None:
        super().__init__()

        # Create an image of the object
        self.image = pygame.Surface([width, height])

        # Fill it with a color
        self.image.fill(color)

        # Draw the rectangle object
        pygame.draw.rect(self.image, 
                         color, 
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
