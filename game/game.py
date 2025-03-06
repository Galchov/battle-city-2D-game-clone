import pygame
import settings as gs

from characters import Tank
from player_tank import PlayerTank


class Game:

    def __init__(self, main, assets) -> None:
        """The main Game Object"""
        self.main = main
        self.assets = assets

        # Objects groups
        self.groups = {"All_Tanks": pygame.sprite.Group()}

        # Player objects
        self.player_1 = PlayerTank(self, self.assets, self.groups, (400, 400), "Up", "Gold", 0)
        self.player_2 = PlayerTank(self, self.assets, self.groups, (600, 400), "Up", "Green", 1)

    def input(self) -> None:
        """Handle the game inputs while running"""

        keypressed = pygame.key.get_pressed()
        self.player_1.input(keypressed)
        self.player_2.input(keypressed)

        # pygame event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False

            # Keyboard shortcut to quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False
    
    def update(self) -> None:

        self.player_1.update()
        self.player_2.update()

    def draw(self, window) -> None:
        """Drawing to the screen"""
        
        self.player_1.draw(window)
        self.player_2.draw(window)
