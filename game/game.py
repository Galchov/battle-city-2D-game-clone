import pygame
import settings as gs


class Game:

    def __init__(self, main, assets) -> None:
        """The main Game Object"""

        self.main = main
        self.assets = assets

    def input(self) -> None:
        """Handle the game inputs while running"""

        # pygame event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False

            # Keyboard shortcut to quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False
    
    def update(self) -> None:
        print("Game running...")

    def draw(self, window) -> None:
        """Drawing to the screen"""
        pass
