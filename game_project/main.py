import pygame, sys, time
import settings as gs

from game_assets import GameAssets
from game import Game
from level_editor import LevelEditor
from levels import LevelData
from start_screen import StartScreen


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
        self.levels = LevelData()

        # Game start screen object
        self.start_screen = StartScreen(self, self.assets)
        self.start_screen_active = True

        # Game object loading and check
        self.game_on = False
        self.game = None

        # Level editor loading and check
        self.level_editor_on = False
        self.level_editor = None

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
        
        # Input controls for the start screen
        if self.start_screen_active:
            self.start_screen_active = self.start_screen.input()

        # Input controls for when level editor is runnig
        if self.level_editor_on:
            self.level_editor.input()

        # Main game controls
        if not self.game_on and not self.level_editor_on and self.start_screen_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    def update(self) -> None:
        """Update the game and all objects"""

        self.clock.tick(gs.FPS)

        # Start screen updating
        if self.start_screen_active:
            self.start_screen.update()

        # If game is on, update game
        if self.game_on:
            self.game.update()

        if self.game:
            if self.game.end_game == True:
                self.start_screen = StartScreen(self, self.assets)
                self.start_screen_active = True

                self.game_on = False
                self.game = None
        
        # If level editor is on, update level editor
        if self.level_editor_on:
            self.level_editor.update()

        if self.level_editor:
            if self.level_editor.active == False:
                self.start_screen = StartScreen(self, self.assets)
                self.start_screen_active = True

                self.level_editor_on = False
                self.level_editor = None

    def draw(self) -> None:
        """Handles all game drawings on the screen"""

        self.screen.fill(gs.BLACK)

        # If the start screen is active, draw the start screen
        if self.start_screen_active:
            self.start_screen.draw(self.screen)

        # If game is runnig, draw the screen
        if self.game_on:
            self.game.draw(self.screen)
        
        # If level editor is running, draw to screen
        if self.level_editor_on:
            self.level_editor.draw(self.screen)

        pygame.display.update()

    def start_new_game(self, player_1, player_2):
        self.game_on = True
        self.game = Game(self, self.assets, player_1, player_2)
        self.start_screen_active = False
        return

    def start_level_creator(self):
        self.level_editor_on = True
        self.level_editor = LevelEditor(self, self.assets)
        self.start_screen_active = False


if __name__ == "__main__":
    battle_city = Main()
    battle_city.run_game()
    pygame.quit()
    sys.exit()
