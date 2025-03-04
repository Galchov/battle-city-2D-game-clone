import pygame, sys, time
import settings as gs


class Game:
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

        self.prev_time = time.time()

        self.run = True

    def run_game(self) -> None:
        """Main Game While Loop"""
        while self.run:
            dt = time.time() - self.prev_time
            self.prev_time = time.time()

            self.input()
            self.update()
            self.draw()


    def input(self) -> None:
        """Handles all inputs in the game"""

        # Main game controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self, dt) -> None:
        """Update the game and all objects"""

        self.clock.tick(gs.FPS)

    def draw(self) -> None:
        """Handles all game drawings on the screen"""

        self.screen.fill(gs.DARK_GREY)

        pygame.display.update()


if __name__ == "__main__":
    battle_city = Game()
    battle_city.run_game()
    pygame.quit()
    sys.exit()
