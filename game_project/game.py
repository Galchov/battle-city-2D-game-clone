import pygame
import settings as gs

from characters import Tank
from player_tank import PlayerTank
from game_hud import GameHud


class Game:

    def __init__(self, main, assets, player_1=True, player_2=False) -> None:
        """The main Game Object"""
        self.main = main
        self.assets = assets

        # Objects groups
        self.groups = {"All_Tanks": pygame.sprite.Group(),
                       "Bullets": pygame.sprite.Group()}

        # Game HUD
        self.hud = GameHud(self, self.assets)

        # Level information
        self.level_num = 1

        # Player attributes
        self.player_1_active = player_1
        self.player_2_active = player_2

        # Player objects
        if self.player_1_active:
            self.player_1 = PlayerTank(self, self.assets, self.groups, (400, 400), "Up", "Gold", 0)
        if self.player_2_active:
            self.player_2 = PlayerTank(self, self.assets, self.groups, (600, 400), "Up", "Green", 1)

        # Number of Enemy Tanks
        self.enemies = 20

    def input(self) -> None:
        """Handle the game inputs while running"""

        keypressed = pygame.key.get_pressed()
        if self.player_1_active:
            self.player_1.input(keypressed)
        if self.player_2_active:
            self.player_2.input(keypressed)

        # pygame event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False

            # Keyboard shortcut to quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False

                if event.key == pygame.K_SPACE:
                    if self.player_1_active:
                        self.player_1.shoot()
                if event.key == pygame.K_RCTRL:
                    if self.player_2_active:
                        self.player_2.shoot()
                if event.key == pygame.K_RETURN:
                    Tank(self, self.assets, self.groups, (100, 100), "Down")
                    self.enemies -= 1
    
    def update(self) -> None:

        self.hud.update()
        for key in self.groups.keys():
            for item in self.groups[key]:
                item.update()

    def draw(self, window) -> None:
        """Drawing to the screen"""

        # Draw the HUD
        self.hud.draw(window)
        
        # Draw characters
        for key in self.groups.keys():
            for item in self.groups[key]:
                item.draw(window)
