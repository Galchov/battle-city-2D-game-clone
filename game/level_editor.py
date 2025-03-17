import pygame

import settings as gs


class LevelEditor:

    def __init__(self, main, assets):
        self.main = main
        self.assets = assets
        self.active = True

        self.level_data = None
        self.all_levels = []

        self.overlay_screen = self.draw_screen()

    def input(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.main.run = False
            elif event == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.overlay_screen, (0, 0))

    def draw_screen(self):
        """Generate the game screen"""

        overlay_screen = pygame.Surface((gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
        overlay_screen.fill(gs.GREY)
        pygame.draw.rect(overlay_screen, gs.BLACK, (gs.GAME_SCREEN))

        return overlay_screen