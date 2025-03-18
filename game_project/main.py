import pygame, sys, time
import settings as gs

from game_assets import GameAssets
from game import Game
from level_editor import LevelEditor


# TODO: Level Editor input to be debugged and completed


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

        # Game object loading and check
        self.game_on = False
        self.game = Game(self, self.assets, True, True)

        # Level editor loading and check
        self.level_editor_on = True
        self.level_editor = LevelEditor(self, self.assets)

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

        # Input controls for when level editor is runnig
        if self.level_editor_on:
            self.level_editor.input()

        # Main game controls
        if not self.game_on and not self.level_editor_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    def update(self) -> None:
        """Update the game and all objects"""

        self.clock.tick(gs.FPS)

        # If game is on, update game
        if self.game_on:
            self.game.update()
        
        # If level editor is on, update level editor
        if self.level_editor_on:
            self.level_editor.update()

    def draw(self) -> None:
        """Handles all game drawings on the screen"""

        self.screen.fill(gs.BLACK)

        # If game is runnig, draw the screen
        if self.game_on:
            self.game.draw(self.screen)
        
        # If level editor is running, draw to screen
        if self.level_editor_on:
            self.level_editor.draw(self.screen)

        pygame.display.update()


if __name__ == "__main__":
    battle_city = Main()
    battle_city.run_game()
    pygame.quit()
    sys.exit()
