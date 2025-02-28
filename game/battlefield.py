
import pygame
from settings import *


class Battlefield:
    
    def __init__(self, screen) -> None:
        self.screen = screen

    def draw(self):
        # Battlefield
        pygame.draw.rect(self.screen, (0, 0, 0), (BATTLEFIELD_X, BATTLEFIELD_Y, BATTLEFIELD_SIZE, BATTLEFIELD_SIZE))
        # Border
        pygame.draw.rect(self.screen, (255, 0, 0), (BATTLEFIELD_X, BATTLEFIELD_Y, BATTLEFIELD_SIZE, BATTLEFIELD_SIZE), 2)
        