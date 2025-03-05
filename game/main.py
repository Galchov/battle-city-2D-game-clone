import pygame, sys, time
import settings as gs

from game_assets import GameAssets
from game import Game

class Main:

    def __init__(self) -> None:
        """Main Game Object"""

        # Initialize the pygame module
        pygame.init()
        
        # Create the game window
        self.screen = pygame.display.set_mode((gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))

        # Set screen caption
        pygame.display.set_caption("Battle City")

        # Frame rate
        self.clock = pygame.time.Clock()
        self.run = True

        self.assets = GameAssets()

        self.game_on = True
        self.game = Game(self, self.assets)

    def run_game(self) -> None:
        """Main Game While Loop"""
        while self.run:
            self.input()
            self.update()
            self.draw()

    def input(self) -> None:
        """Handles all inputs in the game"""

        # Event handler
        if self.game_on:
            self.game.input()

        # Main game controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self) -> None:
        """Update the game and all objects"""

        self.clock.tick(gs.FPS)

        # If game is on, update game
        if self.game_on:
            self.game.update()

    def draw(self) -> None:
        """Handles all game drawings on the screen"""

        self.screen.fill(gs.BLACK)

        # If game is runnig, draw the screen
        if self.game_on:
            self.game.draw(self.screen)

        pygame.display.update()


if __name__ == "__main__":
    battle_city = Main()
    battle_city.run_game()
    pygame.quit()
    sys.exit()
